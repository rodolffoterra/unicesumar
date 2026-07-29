import hashlib
import hmac
import os
import time
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Segurança",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONSTANTES
# =========================================================
PAGINA_INICIAL = "app.py"

USUARIO_DEMONSTRACAO = "admin"
SENHA_DEMONSTRACAO = "Admin@123"

MAXIMO_TENTATIVAS = 3
TEMPO_BLOQUEIO_SEGUNDOS = 30
ITERACOES_PBKDF2 = 120_000


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "resultado_login_inseguro" not in st.session_state:
    st.session_state.resultado_login_inseguro = None

if "resultado_login_seguro" not in st.session_state:
    st.session_state.resultado_login_seguro = None

if "tentativas_login_seguro" not in st.session_state:
    st.session_state.tentativas_login_seguro = 0

if "bloqueado_ate" not in st.session_state:
    st.session_state.bloqueado_ate = None

if "logs_seguranca" not in st.session_state:
    st.session_state.logs_seguranca = []

if "salt_usuario" not in st.session_state:
    st.session_state.salt_usuario = os.urandom(16)

if "hash_senha_usuario" not in st.session_state:
    st.session_state.hash_senha_usuario = hashlib.pbkdf2_hmac(
        "sha256",
        SENHA_DEMONSTRACAO.encode("utf-8"),
        st.session_state.salt_usuario,
        ITERACOES_PBKDF2,
    )


# =========================================================
# NAVEGAÇÃO
# =========================================================
def voltar_para_inicio() -> None:
    """
    Retorna para a página inicial.
    """

    st.switch_page(PAGINA_INICIAL)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def registrar_evento(
    evento: str,
    nivel: str,
    usuario: str = "",
) -> None:
    """
    Registra um evento de segurança para fins didáticos.
    """

    st.session_state.logs_seguranca.append(
        {
            "Data e hora": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "Usuário": usuario or "Não informado",
            "Evento": evento,
            "Nível": nivel,
        }
    )


def gerar_hash_senha(
    senha: str,
    salt: bytes,
) -> bytes:
    """
    Gera o hash seguro da senha utilizando PBKDF2-HMAC-SHA256.
    """

    return hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        ITERACOES_PBKDF2,
    )


def verificar_senha_segura(senha: str) -> bool:
    """
    Compara o hash da senha informada com o hash armazenado.
    """

    hash_informado = gerar_hash_senha(
        senha=senha,
        salt=st.session_state.salt_usuario,
    )

    return hmac.compare_digest(
        hash_informado,
        st.session_state.hash_senha_usuario,
    )


def formatar_tempo_restante(segundos: int) -> str:
    """
    Formata o tempo restante do bloqueio.
    """

    if segundos <= 1:
        return "1 segundo"

    return f"{segundos} segundos"


def verificar_bloqueio() -> Tuple[bool, int]:
    """
    Verifica se o login seguro está temporariamente bloqueado.
    """

    bloqueado_ate: Optional[datetime] = (
        st.session_state.bloqueado_ate
    )

    if bloqueado_ate is None:
        return False, 0

    agora = datetime.now()

    if agora >= bloqueado_ate:
        st.session_state.bloqueado_ate = None
        st.session_state.tentativas_login_seguro = 0

        registrar_evento(
            evento="Bloqueio temporário encerrado.",
            nivel="Informação",
        )

        return False, 0

    segundos_restantes = int(
        (bloqueado_ate - agora).total_seconds()
    ) + 1

    return True, segundos_restantes


def executar_login_inseguro(
    usuario: str,
    senha: str,
) -> Dict[str, Any]:
    """
    Simula uma autenticação com várias falhas de segurança.
    """

    inicio = time.perf_counter()

    time.sleep(0.4)

    if usuario != USUARIO_DEMONSTRACAO:
        resultado = {
            "sucesso": False,
            "mensagem": (
                f"O usuário '{usuario}' não existe no sistema."
            ),
            "detalhe": (
                "A mensagem confirma que o nome de usuário "
                "não está cadastrado."
            ),
            "senha_exposta": senha,
        }

    elif senha != SENHA_DEMONSTRACAO:
        resultado = {
            "sucesso": False,
            "mensagem": (
                "O usuário existe, mas a senha está incorreta."
            ),
            "detalhe": (
                "A mensagem permite descobrir quais usuários "
                "são válidos."
            ),
            "senha_exposta": senha,
        }

    else:
        resultado = {
            "sucesso": True,
            "mensagem": "Login realizado com sucesso.",
            "detalhe": (
                "A autenticação funcionou, mas a senha foi "
                "comparada e armazenada em texto puro."
            ),
            "senha_exposta": senha,
        }

    resultado["tempo"] = time.perf_counter() - inicio

    return resultado


def executar_login_seguro(
    usuario: str,
    senha: str,
) -> Dict[str, Any]:
    """
    Executa uma autenticação com controles básicos de segurança.
    """

    bloqueado, segundos_restantes = verificar_bloqueio()

    if bloqueado:
        registrar_evento(
            evento="Tentativa de acesso durante bloqueio.",
            nivel="Alerta",
            usuario=usuario,
        )

        return {
            "sucesso": False,
            "bloqueado": True,
            "mensagem": (
                "Acesso temporariamente bloqueado. "
                f"Tente novamente em "
                f"{formatar_tempo_restante(segundos_restantes)}."
            ),
            "tentativas_restantes": 0,
        }

    inicio = time.perf_counter()

    # Pequeno atraso uniforme para reduzir diferenças perceptíveis
    # entre usuário inexistente e senha incorreta.
    time.sleep(0.5)

    usuario_valido = hmac.compare_digest(
        usuario.strip(),
        USUARIO_DEMONSTRACAO,
    )

    senha_valida = verificar_senha_segura(senha)

    if usuario_valido and senha_valida:
        st.session_state.tentativas_login_seguro = 0
        st.session_state.bloqueado_ate = None

        registrar_evento(
            evento="Autenticação realizada com sucesso.",
            nivel="Sucesso",
            usuario=usuario,
        )

        return {
            "sucesso": True,
            "bloqueado": False,
            "mensagem": "Autenticação realizada com sucesso.",
            "tentativas_restantes": MAXIMO_TENTATIVAS,
            "tempo": time.perf_counter() - inicio,
        }

    st.session_state.tentativas_login_seguro += 1

    tentativas = st.session_state.tentativas_login_seguro

    registrar_evento(
        evento="Falha de autenticação.",
        nivel="Alerta",
        usuario=usuario,
    )

    if tentativas >= MAXIMO_TENTATIVAS:
        st.session_state.bloqueado_ate = (
            datetime.now()
            + timedelta(seconds=TEMPO_BLOQUEIO_SEGUNDOS)
        )

        registrar_evento(
            evento=(
                "Acesso bloqueado após múltiplas tentativas "
                "inválidas."
            ),
            nivel="Crítico",
            usuario=usuario,
        )

        return {
            "sucesso": False,
            "bloqueado": True,
            "mensagem": (
                "Muitas tentativas inválidas. O acesso foi "
                f"bloqueado por {TEMPO_BLOQUEIO_SEGUNDOS} segundos."
            ),
            "tentativas_restantes": 0,
            "tempo": time.perf_counter() - inicio,
        }

    tentativas_restantes = MAXIMO_TENTATIVAS - tentativas

    return {
        "sucesso": False,
        "bloqueado": False,
        "mensagem": "Usuário ou senha inválidos.",
        "tentativas_restantes": tentativas_restantes,
        "tempo": time.perf_counter() - inicio,
    }


def calcular_forca_senha(senha: str) -> Tuple[int, List[str]]:
    """
    Avalia a força da senha para fins educacionais.
    """

    pontos = 0
    recomendacoes = []

    if len(senha) >= 8:
        pontos += 20
    else:
        recomendacoes.append(
            "Use pelo menos 8 caracteres."
        )

    if len(senha) >= 12:
        pontos += 20
    else:
        recomendacoes.append(
            "Prefira senhas com 12 ou mais caracteres."
        )

    if any(caractere.isupper() for caractere in senha):
        pontos += 15
    else:
        recomendacoes.append(
            "Inclua uma letra maiúscula."
        )

    if any(caractere.islower() for caractere in senha):
        pontos += 15
    else:
        recomendacoes.append(
            "Inclua uma letra minúscula."
        )

    if any(caractere.isdigit() for caractere in senha):
        pontos += 15
    else:
        recomendacoes.append(
            "Inclua um número."
        )

    if any(
        not caractere.isalnum()
        for caractere in senha
    ):
        pontos += 15
    else:
        recomendacoes.append(
            "Inclua um caractere especial."
        )

    return min(pontos, 100), recomendacoes


def reiniciar_demonstracao() -> None:
    """
    Limpa os resultados e controles da demonstração.
    """

    st.session_state.resultado_login_inseguro = None
    st.session_state.resultado_login_seguro = None
    st.session_state.tentativas_login_seguro = 0
    st.session_state.bloqueado_ate = None
    st.session_state.logs_seguranca = []

    st.rerun()


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("🔐 Segurança")

    st.write(
        """
        Esta página compara duas formas de autenticação:
        uma insegura e outra com controles básicos de proteção.
        """
    )

    st.divider()

    if st.button(
        "🏠 Voltar para a página inicial",
        key="voltar_inicio_sidebar",
        use_container_width=True,
    ):
        voltar_para_inicio()

    st.divider()

    st.subheader("Credenciais da demonstração")

    st.code(
        f"""
Usuário: {USUARIO_DEMONSTRACAO}
Senha: {SENHA_DEMONSTRACAO}
        """.strip(),
        language="text",
    )

    st.warning(
        """
        Estas credenciais são apenas fictícias e foram criadas
        para a demonstração.
        """
    )

    st.subheader("Aspectos avaliados")

    st.markdown(
        """
        - confidencialidade;
        - integridade;
        - autenticação;
        - controle de acesso;
        - rastreabilidade;
        - prevenção de ataques;
        - proteção de credenciais.
        """
    )

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("🔐 Falha de Segurança")

st.write(
    """
    Nesta demonstração, dois sistemas realizam a mesma função:
    autenticar um usuário.

    O primeiro expõe informações sensíveis e não controla tentativas.
    O segundo protege as credenciais e limita acessos inválidos.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Segurança?

    Segurança avalia a capacidade do sistema de proteger informações
    e impedir acessos, alterações ou divulgações não autorizadas.

    Um sistema seguro deve proteger a confidencialidade, a integridade,
    a autenticidade e a rastreabilidade das operações.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Uma aplicação administrativa possui uma tela de login.

    Somente usuários autorizados devem conseguir acessar o sistema.
    As credenciais não podem ser expostas nem armazenadas em texto puro.
    """
)

st.success(
    """
    ### Requisito de segurança

    O sistema deve:

    - ocultar a senha durante a digitação;
    - armazenar somente o hash da senha;
    - não confirmar se um usuário específico existe;
    - limitar tentativas inválidas;
    - registrar eventos relevantes;
    - impedir acesso após múltiplas falhas.
    """
)


st.divider()


# =========================================================
# DEMONSTRAÇÕES
# =========================================================
st.header("Execute as demonstrações")

coluna_insegura, coluna_segura = st.columns(2)


# =========================================================
# LOGIN INSEGURO
# =========================================================
with coluna_insegura:
    with st.container(border=True):
        st.subheader("❌ Sistema inseguro")

        st.write(
            """
            Esta implementação apresenta os seguintes problemas:

            - senha visível;
            - comparação em texto puro;
            - mensagens detalhadas;
            - tentativas ilimitadas;
            - ausência de logs;
            - exposição de informações sensíveis.
            """
        )

        with st.form(
            key="formulario_login_inseguro",
            clear_on_submit=False,
        ):
            usuario_inseguro = st.text_input(
                "Usuário",
                key="usuario_inseguro",
                placeholder="Digite o usuário",
            )

            senha_insegura = st.text_input(
                "Senha visível",
                key="senha_insegura",
                placeholder="Digite a senha",
            )

            enviar_inseguro = st.form_submit_button(
                "Entrar no sistema inseguro",
                type="primary",
                use_container_width=True,
            )

        if enviar_inseguro:
            st.session_state.resultado_login_seguro = None

            st.session_state.resultado_login_inseguro = (
                executar_login_inseguro(
                    usuario=usuario_inseguro,
                    senha=senha_insegura,
                )
            )

            st.rerun()


# =========================================================
# LOGIN SEGURO
# =========================================================
with coluna_segura:
    with st.container(border=True):
        st.subheader("✅ Sistema seguro")

        st.write(
            """
            Esta implementação utiliza:

            - campo protegido;
            - hash com salt;
            - comparação segura;
            - erro genérico;
            - limite de tentativas;
            - bloqueio temporário;
            - registro de eventos.
            """
        )

        bloqueado, segundos_restantes = verificar_bloqueio()

        if bloqueado:
            st.error(
                f"""
                Acesso temporariamente bloqueado.

                Aguarde aproximadamente
                **{formatar_tempo_restante(segundos_restantes)}**.
                """
            )

        with st.form(
            key="formulario_login_seguro",
            clear_on_submit=False,
        ):
            usuario_seguro = st.text_input(
                "Usuário",
                key="usuario_seguro",
                placeholder="Digite o usuário",
                disabled=bloqueado,
            )

            senha_segura = st.text_input(
                "Senha",
                key="senha_segura",
                type="password",
                placeholder="Digite a senha",
                disabled=bloqueado,
            )

            enviar_seguro = st.form_submit_button(
                "Entrar com segurança",
                use_container_width=True,
                disabled=bloqueado,
            )

        if enviar_seguro:
            st.session_state.resultado_login_inseguro = None

            st.session_state.resultado_login_seguro = (
                executar_login_seguro(
                    usuario=usuario_seguro,
                    senha=senha_segura,
                )
            )

            st.rerun()


# =========================================================
# RESULTADO DO SISTEMA INSEGURO
# =========================================================
resultado_inseguro = (
    st.session_state.resultado_login_inseguro
)

if resultado_inseguro is not None:
    st.divider()

    st.header("Resultado do sistema inseguro")

    if resultado_inseguro["sucesso"]:
        st.success(resultado_inseguro["mensagem"])
    else:
        st.error(resultado_inseguro["mensagem"])

    st.warning(resultado_inseguro["detalhe"])

    coluna_senha, coluna_tentativas = st.columns(2)

    with coluna_senha:
        st.metric(
            label="Senha capturada pela aplicação",
            value=(
                resultado_inseguro["senha_exposta"]
                or "Senha vazia"
            ),
        )

    with coluna_tentativas:
        st.metric(
            label="Limite de tentativas",
            value="Ilimitado",
        )

    st.error(
        """
        ### Informação sensível exposta

        A senha digitada foi mantida em texto legível.

        Em um sistema real, isso permitiria que pessoas com acesso
        ao código, aos logs ou ao banco visualizassem as credenciais.
        """
    )

    st.code(
        f"""
usuario_recebido = "{st.session_state.get('usuario_inseguro', '')}"
senha_recebida = "{resultado_inseguro['senha_exposta']}"

if usuario_recebido == "admin":
    if senha_recebida == "Admin@123":
        permitir_acesso()
        """.strip(),
        language="python",
    )


# =========================================================
# RESULTADO DO SISTEMA SEGURO
# =========================================================
resultado_seguro = (
    st.session_state.resultado_login_seguro
)

if resultado_seguro is not None:
    st.divider()

    st.header("Resultado do sistema seguro")

    if resultado_seguro["sucesso"]:
        st.success(
            """
            ### Acesso autorizado

            O usuário e a senha foram validados corretamente.
            """
        )

        st.metric(
            label="Tentativas inválidas acumuladas",
            value="0",
        )

    else:
        if resultado_seguro["bloqueado"]:
            st.error(resultado_seguro["mensagem"])
        else:
            st.warning(resultado_seguro["mensagem"])

            st.metric(
                label="Tentativas restantes",
                value=str(
                    resultado_seguro["tentativas_restantes"]
                ),
            )

        st.info(
            """
            A mensagem não revela se o usuário existe nem se somente
            a senha está incorreta.
            """
        )

    st.subheader("Representação da senha armazenada")

    hash_hexadecimal = (
        st.session_state.hash_senha_usuario.hex()
    )

    salt_hexadecimal = (
        st.session_state.salt_usuario.hex()
    )

    st.code(
        f"""
Salt:
{salt_hexadecimal}

Hash PBKDF2-HMAC-SHA256:
{hash_hexadecimal}
        """.strip(),
        language="text",
    )

    st.success(
        """
        A senha original não é armazenada.

        Durante o login, o sistema calcula o hash da senha informada
        e compara o resultado com o hash previamente armazenado.
        """
    )


st.divider()


# =========================================================
# TESTE DE FORÇA DA SENHA
# =========================================================
st.header("Teste educacional de força da senha")

st.write(
    """
    Digite uma senha fictícia para verificar alguns critérios básicos.

    Não utilize uma senha real nesta demonstração.
    """
)

senha_teste = st.text_input(
    "Senha fictícia para avaliação",
    type="password",
    key="senha_teste_forca",
    placeholder="Digite uma senha de teste",
)

if senha_teste:
    pontuacao, recomendacoes = calcular_forca_senha(
        senha_teste
    )

    st.progress(
        pontuacao,
        text=f"Força estimada: {pontuacao}%",
    )

    if pontuacao >= 80:
        st.success("Senha considerada forte para esta demonstração.")

    elif pontuacao >= 50:
        st.warning(
            "A senha possui proteção intermediária."
        )

    else:
        st.error(
            "A senha apresenta critérios fracos."
        )

    if recomendacoes:
        st.subheader("Recomendações")

        for recomendacao in recomendacoes:
            st.write(f"• {recomendacao}")


st.divider()


# =========================================================
# LOGS DE SEGURANÇA
# =========================================================
st.header("Registro de eventos de segurança")

if st.session_state.logs_seguranca:
    st.dataframe(
        list(reversed(st.session_state.logs_seguranca)),
        use_container_width=True,
        hide_index=True,
    )

else:
    st.info(
        """
        Nenhum evento foi registrado.

        Execute o sistema seguro para gerar eventos de autenticação.
        """
    )

st.caption(
    """
    Em uma aplicação real, logs não devem armazenar senhas, tokens,
    chaves de acesso ou outras informações sensíveis.
    """
)


st.divider()


# =========================================================
# COMPARAÇÃO
# =========================================================
st.header("Comparação dos sistemas")

comparacao = [
    {
        "Critério": "Campo de senha",
        "Sistema inseguro": "Senha visível",
        "Sistema seguro": "Senha ocultada",
    },
    {
        "Critério": "Armazenamento",
        "Sistema inseguro": "Texto puro",
        "Sistema seguro": "Hash com salt",
    },
    {
        "Critério": "Mensagem de erro",
        "Sistema inseguro": "Revela o motivo exato",
        "Sistema seguro": "Mensagem genérica",
    },
    {
        "Critério": "Tentativas inválidas",
        "Sistema inseguro": "Ilimitadas",
        "Sistema seguro": "Máximo de 3",
    },
    {
        "Critério": "Bloqueio",
        "Sistema inseguro": "Não existe",
        "Sistema seguro": "Bloqueio temporário",
    },
    {
        "Critério": "Rastreabilidade",
        "Sistema inseguro": "Sem registros",
        "Sistema seguro": "Eventos registrados",
    },
    {
        "Critério": "Comparação",
        "Sistema inseguro": "Comparação direta",
        "Sistema seguro": "Comparação resistente a timing",
    },
]

st.dataframe(
    comparacao,
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# ASPECTOS DE SEGURANÇA
# =========================================================
st.header("Aspectos de Segurança demonstrados")

coluna_1, coluna_2, coluna_3 = st.columns(3)

with coluna_1:
    with st.container(border=True):
        st.subheader("Confidencialidade")

        st.write(
            """
            Garante que informações sejam acessadas somente por
            pessoas e sistemas autorizados.
            """
        )

    with st.container(border=True):
        st.subheader("Integridade")

        st.write(
            """
            Protege informações contra alterações indevidas ou
            não autorizadas.
            """
        )

with coluna_2:
    with st.container(border=True):
        st.subheader("Não repúdio")

        st.write(
            """
            Permite comprovar que uma determinada ação ou operação
            foi realizada.
            """
        )

    with st.container(border=True):
        st.subheader("Responsabilização")

        st.write(
            """
            Permite identificar quem realizou cada ação relevante
            dentro do sistema.
            """
        )

with coluna_3:
    with st.container(border=True):
        st.subheader("Autenticidade")

        st.write(
            """
            Verifica se a identidade apresentada por um usuário ou
            sistema é verdadeira.
            """
        )

    with st.container(border=True):
        st.subheader("Resistência a ataques")

        st.write(
            """
            Reduz a possibilidade de exploração por tentativas
            repetidas, exposição de dados ou manipulação indevida.
            """
        )


st.divider()


# =========================================================
# CÓDIGO INSEGURO
# =========================================================
st.header("Código com falhas de segurança")

with st.expander(
    "Visualizar implementação insegura",
    expanded=True,
):
    st.code(
        """
USUARIO = "admin"
SENHA = "Admin@123"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario != USUARIO:
    print("Esse usuário não existe.")

elif senha != SENHA:
    print("O usuário existe, mas a senha está incorreta.")

else:
    print("Acesso autorizado.")
        """.strip(),
        language="python",
    )

st.error(
    """
    Problemas da implementação:

    - credencial escrita diretamente no código;
    - senha armazenada em texto puro;
    - mensagens que revelam informações;
    - ausência de limite de tentativas;
    - ausência de logs;
    - ausência de segundo fator de autenticação.
    """
)


# =========================================================
# CÓDIGO SEGURO
# =========================================================
st.header("Código com proteção de senha")

with st.expander(
    "Visualizar implementação com hash",
    expanded=True,
):
    st.code(
        """
import hashlib
import hmac
import os


ITERACOES = 120_000


def criar_hash(senha: str) -> tuple[bytes, bytes]:
    salt = os.urandom(16)

    hash_senha = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        ITERACOES,
    )

    return salt, hash_senha


def verificar_senha(
    senha_informada: str,
    salt: bytes,
    hash_armazenado: bytes,
) -> bool:
    hash_informado = hashlib.pbkdf2_hmac(
        "sha256",
        senha_informada.encode("utf-8"),
        salt,
        ITERACOES,
    )

    return hmac.compare_digest(
        hash_informado,
        hash_armazenado,
    )
        """.strip(),
        language="python",
    )

st.info(
    """
    Para sistemas reais, prefira bibliotecas especializadas e
    algoritmos próprios para armazenamento de senhas, como Argon2,
    bcrypt ou scrypt.

    O PBKDF2 desta demonstração utiliza apenas recursos da biblioteca
    padrão do Python para facilitar a execução do projeto.
    """
)


st.divider()


# =========================================================
# OUTROS EXEMPLOS
# =========================================================
st.header("Outros exemplos de falhas de segurança")

exemplo_1, exemplo_2, exemplo_3 = st.columns(3)

with exemplo_1:
    with st.container(border=True):
        st.subheader("Controle de acesso")

        st.write(
            """
            Um usuário comum consegue acessar páginas administrativas
            apenas alterando a URL.
            """
        )

with exemplo_2:
    with st.container(border=True):
        st.subheader("Dados sensíveis")

        st.write(
            """
            Senhas, documentos pessoais ou cartões são registrados
            em arquivos de log.
            """
        )

with exemplo_3:
    with st.container(border=True):
        st.subheader("Entrada não validada")

        st.write(
            """
            Dados recebidos do usuário são utilizados diretamente
            em consultas ou comandos sem validação adequada.
            """
        )


st.divider()


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir a Segurança?")

metrica_1, metrica_2, metrica_3, metrica_4 = st.columns(4)

with metrica_1:
    st.metric(
        label="Tentativas inválidas",
        value=str(
            st.session_state.tentativas_login_seguro
        ),
    )

with metrica_2:
    st.metric(
        label="Eventos registrados",
        value=str(
            len(st.session_state.logs_seguranca)
        ),
    )

with metrica_3:
    bloqueado_atual, _ = verificar_bloqueio()

    st.metric(
        label="Estado do acesso",
        value=(
            "Bloqueado"
            if bloqueado_atual
            else "Disponível"
        ),
    )

with metrica_4:
    st.metric(
        label="Limite de tentativas",
        value=str(MAXIMO_TENTATIVAS),
    )

st.info(
    """
    Algumas métricas utilizadas na avaliação de segurança:

    - quantidade de tentativas de acesso inválidas;
    - quantidade de vulnerabilidades identificadas;
    - percentual de senhas protegidas;
    - número de acessos não autorizados;
    - quantidade de incidentes por período;
    - tempo para detectar um incidente;
    - tempo para responder a um incidente;
    - cobertura de logs e auditoria;
    - percentual de usuários com autenticação multifator;
    - percentual de dependências atualizadas.
    """
)


st.divider()


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos de uma falha de segurança")

coluna_usuario, coluna_empresa = st.columns(2)

with coluna_usuario:
    with st.container(border=True):
        st.subheader("Impactos para o usuário")

        st.markdown(
            """
            - exposição de dados pessoais;
            - roubo de credenciais;
            - invasão de contas;
            - alterações não autorizadas;
            - fraude;
            - perda de privacidade;
            - perda de confiança no sistema.
            """
        )

with coluna_empresa:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - vazamento de informações;
            - interrupção dos serviços;
            - prejuízo financeiro;
            - danos à reputação;
            - sanções e problemas jurídicos;
            - perda de clientes;
            - custos de investigação e recuperação.
            """
        )


st.divider()


# =========================================================
# BOAS PRÁTICAS
# =========================================================
st.header("Boas práticas de segurança")

st.markdown(
    """
    - nunca armazenar senhas em texto puro;
    - utilizar hash seguro com salt;
    - utilizar autenticação multifator;
    - aplicar o princípio do menor privilégio;
    - proteger segredos em variáveis de ambiente ou cofres;
    - limitar tentativas de autenticação;
    - registrar eventos sem expor informações sensíveis;
    - validar dados recebidos;
    - utilizar consultas parametrizadas;
    - manter dependências atualizadas;
    - utilizar HTTPS;
    - expirar sessões inativas;
    - realizar testes de segurança;
    - manter plano de resposta a incidentes.
    """
)

st.warning(
    """
    Não registre senhas, tokens, chaves de API ou credenciais em logs.

    Também não mantenha segredos diretamente no código-fonte.
    """
)


st.divider()


# =========================================================
# REINICIAR
# =========================================================
st.header("Reiniciar a demonstração")

if st.button(
    "🗑️ Limpar resultados",
    key="limpar_resultados_seguranca",
    use_container_width=True,
):
    reiniciar_demonstracao()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um sistema não é seguro apenas porque possui uma tela de login.

    A segurança depende da proteção das credenciais, do controle de
    acesso, da limitação de tentativas, da rastreabilidade e do
    tratamento adequado das informações sensíveis.

    Nesta demonstração, o sistema inseguro expôs a senha e revelou
    informações sobre o usuário. O sistema seguro armazenou somente
    o hash, limitou tentativas e registrou eventos relevantes.
    """
)


# =========================================================
# BOTÃO FINAL
# =========================================================
if st.button(
    "🏠 Voltar para a página inicial",
    key="voltar_inicio_final",
    use_container_width=True,
):
    voltar_para_inicio()