import re
import time
from typing import Dict, List, Tuple

import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Usabilidade",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONSTANTES
# =========================================================
PAGINA_INICIAL = "app.py"


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "resultado_formulario_ruim" not in st.session_state:
    st.session_state.resultado_formulario_ruim = None

if "resultado_formulario_bom" not in st.session_state:
    st.session_state.resultado_formulario_bom = None

if "inicio_formulario_ruim" not in st.session_state:
    st.session_state.inicio_formulario_ruim = time.perf_counter()

if "inicio_formulario_bom" not in st.session_state:
    st.session_state.inicio_formulario_bom = time.perf_counter()


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
def validar_email(email: str) -> bool:
    """
    Verifica se o e-mail possui um formato básico válido.
    """

    padrao = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return bool(re.match(padrao, email.strip()))


def validar_telefone(telefone: str) -> bool:
    """
    Verifica se o telefone possui entre 10 e 11 dígitos.
    """

    somente_numeros = re.sub(r"\D", "", telefone)

    return len(somente_numeros) in (10, 11)


def validar_senha(senha: str) -> Tuple[bool, List[str]]:
    """
    Valida os requisitos mínimos da senha.
    """

    erros = []

    if len(senha) < 8:
        erros.append("A senha deve possuir pelo menos 8 caracteres.")

    if not any(caractere.isupper() for caractere in senha):
        erros.append("A senha deve possuir pelo menos uma letra maiúscula.")

    if not any(caractere.islower() for caractere in senha):
        erros.append("A senha deve possuir pelo menos uma letra minúscula.")

    if not any(caractere.isdigit() for caractere in senha):
        erros.append("A senha deve possuir pelo menos um número.")

    return len(erros) == 0, erros


def formatar_tempo(segundos: float) -> str:
    """
    Formata o tempo de preenchimento.
    """

    if segundos < 60:
        return f"{segundos:.1f} segundos"

    minutos = int(segundos // 60)
    segundos_restantes = int(segundos % 60)

    return f"{minutos} min e {segundos_restantes} s"


def validar_formulario_adequado(
    nome: str,
    email: str,
    telefone: str,
    senha: str,
    confirmar_senha: str,
    aceitar_termos: bool,
) -> List[str]:
    """
    Retorna mensagens específicas para cada problema encontrado.
    """

    erros = []

    if len(nome.strip()) < 3:
        erros.append(
            "Informe o nome completo com pelo menos 3 caracteres."
        )

    if not validar_email(email):
        erros.append(
            "Informe um e-mail válido, como nome@empresa.com.br."
        )

    if not validar_telefone(telefone):
        erros.append(
            "Informe um telefone com DDD e 10 ou 11 dígitos."
        )

    senha_valida, erros_senha = validar_senha(senha)

    if not senha_valida:
        erros.extend(erros_senha)

    if senha != confirmar_senha:
        erros.append("A confirmação da senha não corresponde à senha.")

    if not aceitar_termos:
        erros.append(
            "É necessário aceitar os termos para concluir o cadastro."
        )

    return erros


def reiniciar_demonstracao() -> None:
    """
    Limpa todos os resultados e reinicia os cronômetros.
    """

    st.session_state.resultado_formulario_ruim = None
    st.session_state.resultado_formulario_bom = None
    st.session_state.inicio_formulario_ruim = time.perf_counter()
    st.session_state.inicio_formulario_bom = time.perf_counter()

    st.rerun()


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("🧭 Usabilidade")

    st.write(
        """
        Esta página compara duas interfaces que executam a mesma
        funcionalidade: cadastrar um cliente.
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

    st.subheader("Aspectos avaliados")

    st.markdown(
        """
        - clareza das informações;
        - facilidade de aprendizado;
        - facilidade de operação;
        - prevenção de erros;
        - mensagens de validação;
        - acessibilidade;
        - proteção de informações.
        """
    )

    st.warning(
        """
        O formulário com falha foi criado propositalmente para
        demonstrar problemas de usabilidade.
        """
    )

    st.caption("Medição e Avaliação da Qualidade de Software")


# =========================================================
# CABEÇALHO
# =========================================================
st.title("🧭 Falha de Usabilidade")

st.write(
    """
    Nesta demonstração, dois formulários realizam o cadastro de um
    cliente.

    Os dois possuem a mesma finalidade, mas oferecem experiências
    completamente diferentes ao usuário.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Usabilidade?

    Usabilidade avalia o quanto um sistema pode ser compreendido,
    aprendido e operado pelos usuários de maneira eficiente,
    segura e satisfatória.

    Uma funcionalidade pode estar tecnicamente correta e ainda
    apresentar baixa qualidade quando sua interface é confusa,
    difícil de aprender ou propensa a erros.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Uma loja precisa cadastrar novos clientes.

    O usuário deve informar nome, e-mail, telefone e senha para criar
    uma conta.
    """
)

st.success(
    """
    ### Requisito de usabilidade

    O cadastro deve apresentar campos claros, orientar o usuário,
    prevenir erros e informar exatamente como corrigir dados inválidos.
    """
)


st.divider()


# =========================================================
# FORMULÁRIO COM FALHA
# =========================================================
st.header("❌ Demonstração 1 — Interface com falha")

st.error(
    """
    Este formulário apresenta nomes de campos pouco claros, não informa
    os formatos esperados, exibe a senha e apresenta apenas uma mensagem
    genérica quando ocorre um erro.
    """
)

with st.container(border=True):
    st.subheader("Cadastro XP-01")

    st.caption(
        "Preencha os dados abaixo. Os campos obrigatórios não estão "
        "identificados."
    )

    with st.form(
        key="formulario_usabilidade_ruim",
        clear_on_submit=True,
    ):
        coluna_1, coluna_2 = st.columns(2)

        with coluna_1:
            campo_1 = st.text_input(
                "Campo 1",
                help="Digite a informação solicitada.",
            )

            campo_2 = st.text_input(
                "Campo 2",
            )

        with coluna_2:
            campo_3 = st.text_input(
                "Campo 3",
            )

            campo_4 = st.text_input(
                "Código",
                help="Digite o código de acesso.",
            )

        opcao = st.selectbox(
            "Tipo",
            options=[
                "",
                "1",
                "2",
                "3",
            ],
        )

        enviar_ruim = st.form_submit_button(
            "OK",
            type="primary",
            use_container_width=True,
        )

    if enviar_ruim:
        tempo_decorrido = (
            time.perf_counter()
            - st.session_state.inicio_formulario_ruim
        )

        # Validação propositalmente ruim.
        if (
            not campo_1
            or not campo_2
            or not campo_3
            or not campo_4
            or not opcao
        ):
            st.session_state.resultado_formulario_ruim = {
                "sucesso": False,
                "tempo": tempo_decorrido,
                "mensagem": "Erro 400. Dados inválidos.",
            }

        elif "@" not in campo_2:
            st.session_state.resultado_formulario_ruim = {
                "sucesso": False,
                "tempo": tempo_decorrido,
                "mensagem": "Erro 400. Dados inválidos.",
            }

        else:
            st.session_state.resultado_formulario_ruim = {
                "sucesso": True,
                "tempo": tempo_decorrido,
                "mensagem": "Operação finalizada.",
            }

        st.session_state.inicio_formulario_ruim = time.perf_counter()


resultado_ruim = st.session_state.resultado_formulario_ruim

if resultado_ruim is not None:
    if resultado_ruim["sucesso"]:
        st.success(resultado_ruim["mensagem"])
    else:
        st.error(resultado_ruim["mensagem"])

        st.warning(
            """
            A mensagem não informa qual campo está incorreto, qual formato
            era esperado ou como o usuário pode resolver o problema.

            Como o formulário foi limpo após o envio, todos os dados
            precisam ser digitados novamente.
            """
        )

    st.metric(
        label="Tempo até o envio",
        value=formatar_tempo(resultado_ruim["tempo"]),
    )


# =========================================================
# ANÁLISE DA FALHA
# =========================================================
with st.expander(
    "Analisar problemas da interface com falha",
    expanded=True,
):
    problemas = [
        {
            "Problema": "Rótulos genéricos",
            "Exemplo": "Campo 1, Campo 2 e Campo 3",
            "Impacto": "O usuário não sabe qual informação deve fornecer.",
        },
        {
            "Problema": "Senha exposta",
            "Exemplo": "Campo Código usa entrada de texto normal",
            "Impacto": "Outras pessoas podem visualizar a senha.",
        },
        {
            "Problema": "Opções sem significado",
            "Exemplo": "Tipo 1, 2 ou 3",
            "Impacto": "O usuário não consegue tomar uma decisão segura.",
        },
        {
            "Problema": "Erro genérico",
            "Exemplo": "Erro 400. Dados inválidos.",
            "Impacto": "Não existe orientação para corrigir o cadastro.",
        },
        {
            "Problema": "Perda dos dados",
            "Exemplo": "O formulário é limpo mesmo quando ocorre erro",
            "Impacto": "O usuário precisa preencher tudo novamente.",
        },
    ]

    st.dataframe(
        problemas,
        use_container_width=True,
        hide_index=True,
    )


st.divider()


# =========================================================
# FORMULÁRIO ADEQUADO
# =========================================================
st.header("✅ Demonstração 2 — Interface com boa usabilidade")

st.success(
    """
    Este formulário utiliza rótulos claros, exemplos, ajuda contextual,
    proteção da senha e mensagens específicas para cada erro.
    """
)

with st.container(border=True):
    st.subheader("Cadastro de cliente")

    st.write(
        """
        Preencha os campos obrigatórios identificados com `*`.
        Seus dados serão utilizados para criar uma conta de cliente.
        """
    )

    with st.form(
        key="formulario_usabilidade_bom",
        clear_on_submit=False,
    ):
        nome = st.text_input(
            "Nome completo *",
            placeholder="Exemplo: Maria da Silva",
            help="Informe o nome e o sobrenome do cliente.",
        )

        coluna_email, coluna_telefone = st.columns(2)

        with coluna_email:
            email = st.text_input(
                "E-mail *",
                placeholder="nome@empresa.com.br",
                help=(
                    "O e-mail será utilizado para identificação "
                    "e recuperação da conta."
                ),
            )

        with coluna_telefone:
            telefone = st.text_input(
                "Telefone com DDD *",
                placeholder="(44) 99999-9999",
                help="Informe um telefone com 10 ou 11 dígitos.",
            )

        coluna_senha, coluna_confirmacao = st.columns(2)

        with coluna_senha:
            senha = st.text_input(
                "Senha *",
                type="password",
                help=(
                    "Use pelo menos 8 caracteres, uma letra maiúscula, "
                    "uma letra minúscula e um número."
                ),
            )

        with coluna_confirmacao:
            confirmar_senha = st.text_input(
                "Confirme a senha *",
                type="password",
                help="Digite novamente a senha informada.",
            )

        tipo_cliente = st.radio(
            "Tipo de cliente *",
            options=[
                "Pessoa física",
                "Pessoa jurídica",
            ],
            horizontal=True,
            help="Selecione a categoria correspondente ao cliente.",
        )

        receber_comunicacoes = st.checkbox(
            "Desejo receber novidades e ofertas por e-mail.",
        )

        aceitar_termos = st.checkbox(
            "Li e aceito os termos de uso e a política de privacidade. *"
        )

        st.caption("* Campos obrigatórios.")

        enviar_bom = st.form_submit_button(
            "Criar conta",
            type="primary",
            use_container_width=True,
        )

    if enviar_bom:
        tempo_decorrido = (
            time.perf_counter()
            - st.session_state.inicio_formulario_bom
        )

        erros = validar_formulario_adequado(
            nome=nome,
            email=email,
            telefone=telefone,
            senha=senha,
            confirmar_senha=confirmar_senha,
            aceitar_termos=aceitar_termos,
        )

        if erros:
            st.session_state.resultado_formulario_bom = {
                "sucesso": False,
                "tempo": tempo_decorrido,
                "erros": erros,
            }

        else:
            st.session_state.resultado_formulario_bom = {
                "sucesso": True,
                "tempo": tempo_decorrido,
                "cliente": {
                    "Nome": nome.strip(),
                    "E-mail": email.strip(),
                    "Telefone": telefone.strip(),
                    "Tipo": tipo_cliente,
                    "Comunicações": (
                        "Autorizadas"
                        if receber_comunicacoes
                        else "Não autorizadas"
                    ),
                },
            }

        st.session_state.inicio_formulario_bom = time.perf_counter()


resultado_bom = st.session_state.resultado_formulario_bom

if resultado_bom is not None:
    if resultado_bom["sucesso"]:
        st.success(
            """
            ### Cadastro concluído

            A conta foi criada com sucesso.
            """
        )

        st.json(resultado_bom["cliente"])

    else:
        st.error(
            """
            Não foi possível concluir o cadastro. Corrija os itens
            apresentados abaixo.
            """
        )

        for erro in resultado_bom["erros"]:
            st.write(f"❌ {erro}")

        st.info(
            """
            Os dados digitados permaneceram no formulário para que o
            usuário altere somente os campos necessários.
            """
        )

    st.metric(
        label="Tempo até o envio",
        value=formatar_tempo(resultado_bom["tempo"]),
    )


st.divider()


# =========================================================
# COMPARAÇÃO
# =========================================================
st.header("Comparação das interfaces")

comparacao = [
    {
        "Critério": "Identificação dos campos",
        "Interface com falha": "Campos genéricos",
        "Interface adequada": "Rótulos claros e objetivos",
    },
    {
        "Critério": "Orientação",
        "Interface com falha": "Sem exemplos de preenchimento",
        "Interface adequada": "Exemplos e textos de ajuda",
    },
    {
        "Critério": "Tratamento de erros",
        "Interface com falha": "Mensagem genérica",
        "Interface adequada": "Mensagem específica para cada problema",
    },
    {
        "Critério": "Proteção da senha",
        "Interface com falha": "Senha visível",
        "Interface adequada": "Senha ocultada",
    },
    {
        "Critério": "Recuperação de erro",
        "Interface com falha": "Dados apagados",
        "Interface adequada": "Dados preservados",
    },
    {
        "Critério": "Ação principal",
        "Interface com falha": "Botão chamado OK",
        "Interface adequada": "Botão chamado Criar conta",
    },
]

st.dataframe(
    comparacao,
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# SUBCARACTERÍSTICAS
# =========================================================
st.header("Aspectos de Usabilidade demonstrados")

coluna_1, coluna_2, coluna_3 = st.columns(3)

with coluna_1:
    with st.container(border=True):
        st.subheader("Compreensibilidade")

        st.write(
            """
            O usuário precisa entender a finalidade da tela, dos campos
            e das ações disponíveis.
            """
        )

    with st.container(border=True):
        st.subheader("Aprendizado")

        st.write(
            """
            A interface deve ser fácil de aprender, mesmo para pessoas
            que estão utilizando o sistema pela primeira vez.
            """
        )

with coluna_2:
    with st.container(border=True):
        st.subheader("Operabilidade")

        st.write(
            """
            O usuário deve conseguir controlar e executar as operações
            com facilidade.
            """
        )

    with st.container(border=True):
        st.subheader("Proteção contra erros")

        st.write(
            """
            O sistema deve prevenir erros e orientar claramente sua
            correção.
            """
        )

with coluna_3:
    with st.container(border=True):
        st.subheader("Interface do usuário")

        st.write(
            """
            A organização visual deve facilitar a leitura e destacar
            informações importantes.
            """
        )

    with st.container(border=True):
        st.subheader("Acessibilidade")

        st.write(
            """
            A interface deve considerar usuários com diferentes
            capacidades e necessidades.
            """
        )


st.divider()


# =========================================================
# EXEMPLO DE CÓDIGO
# =========================================================
st.header("Comparação do código")

coluna_codigo_ruim, coluna_codigo_bom = st.columns(2)

with coluna_codigo_ruim:
    with st.container(border=True):
        st.subheader("❌ Código com baixa usabilidade")

        st.code(
            """
campo_1 = st.text_input("Campo 1")
campo_2 = st.text_input("Campo 2")
campo_3 = st.text_input("Campo 3")
senha = st.text_input("Código")

if st.button("OK"):
    if algum_dado_invalido:
        st.error("Erro 400")
            """.strip(),
            language="python",
        )

with coluna_codigo_bom:
    with st.container(border=True):
        st.subheader("✅ Código com boa usabilidade")

        st.code(
            """
nome = st.text_input(
    "Nome completo *",
    placeholder="Exemplo: Maria da Silva"
)

email = st.text_input(
    "E-mail *",
    placeholder="nome@empresa.com.br"
)

senha = st.text_input(
    "Senha *",
    type="password",
    help="Use pelo menos 8 caracteres."
)

if email_invalido:
    st.error("Informe um e-mail válido.")
            """.strip(),
            language="python",
        )


st.divider()


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir a Usabilidade?")

metrica_1, metrica_2, metrica_3, metrica_4 = st.columns(4)

with metrica_1:
    st.metric(
        label="Taxa de conclusão",
        value="Usuários que concluem",
    )

with metrica_2:
    st.metric(
        label="Tempo da tarefa",
        value="Minutos ou segundos",
    )

with metrica_3:
    st.metric(
        label="Taxa de erros",
        value="Erros por tentativa",
    )

with metrica_4:
    st.metric(
        label="Satisfação",
        value="Pesquisa com usuários",
    )

st.info(
    """
    Métricas que podem ser utilizadas:

    - percentual de usuários que concluem a tarefa;
    - tempo médio para concluir o cadastro;
    - quantidade de erros por tentativa;
    - número de campos preenchidos incorretamente;
    - quantidade de solicitações de ajuda;
    - taxa de abandono;
    - nível de satisfação dos usuários;
    - tempo necessário para aprender a utilizar o sistema.
    """
)


st.divider()


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos de uma interface difícil de utilizar")

coluna_usuario, coluna_empresa = st.columns(2)

with coluna_usuario:
    with st.container(border=True):
        st.subheader("Impactos para o usuário")

        st.markdown(
            """
            - dificuldade para entender o sistema;
            - aumento da quantidade de erros;
            - perda de tempo;
            - frustração;
            - abandono da tarefa;
            - necessidade de treinamento;
            - falta de confiança.
            """
        )

with coluna_empresa:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - aumento dos chamados de suporte;
            - maior custo de treinamento;
            - redução das conversões;
            - perda de clientes;
            - retrabalho;
            - baixa produtividade;
            - prejuízo à imagem da organização.
            """
        )


st.divider()


# =========================================================
# REINICIAR
# =========================================================
st.header("Reiniciar a demonstração")

if st.button(
    "🗑️ Limpar resultados",
    key="limpar_resultados_usabilidade",
    use_container_width=True,
):
    reiniciar_demonstracao()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um sistema não possui boa usabilidade apenas porque sua
    funcionalidade pode ser executada.

    A interface deve ajudar o usuário a compreender a tarefa, preencher
    os dados corretamente, evitar erros e recuperar-se facilmente quando
    algum problema ocorrer.

    Os dois formulários realizam o cadastro de clientes, mas somente o
    segundo oferece informações claras, proteção contra erros e uma
    experiência adequada.
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