import time
from typing import Any, Dict, List, Optional

import streamlit as st

try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    mysql = None
    Error = Exception


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Falha de Compatibilidade",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONFIGURAÇÕES DO MYSQL
# =========================================================
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "1234556"

# Banco propositalmente inexistente ou incompatível.
BANCO_INCOMPATIVEL = "sistema_legado_incompativel"

# Banco existente informado para a demonstração de sucesso.
BANCO_CORRETO = "cliente"

# Tabela existente dentro do banco cliente.
TABELA_CLIENTES = "clientes"


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "resultado_falha_compatibilidade" not in st.session_state:
    st.session_state.resultado_falha_compatibilidade = None

if "resultado_sucesso_compatibilidade" not in st.session_state:
    st.session_state.resultado_sucesso_compatibilidade = None


# =========================================================
# FUNÇÕES DE NAVEGAÇÃO
# =========================================================
def voltar_para_inicio() -> None:
    """
    Retorna para a página principal da aplicação.
    """

    st.switch_page("app.py")


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def biblioteca_mysql_disponivel() -> bool:
    """
    Verifica se o mysql-connector-python está instalado.
    """

    return mysql is not None


def formatar_tempo(segundos: float) -> str:
    """
    Formata o tempo de execução.
    """

    if segundos >= 1:
        return f"{segundos:.2f} segundos"

    milissegundos = segundos * 1000

    return f"{milissegundos:.2f} ms"


def criar_configuracao_mysql(
    database: str,
) -> Dict[str, Any]:
    """
    Cria a configuração utilizada na conexão com o MySQL.
    """

    return {
        "host": MYSQL_HOST,
        "port": MYSQL_PORT,
        "user": MYSQL_USER,
        "password": MYSQL_PASSWORD,
        "database": database,
        "connection_timeout": 5,
    }


def ocultar_senha(
    configuracao: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Retorna uma cópia da configuração sem expor a senha.
    """

    configuracao_segura = configuracao.copy()
    configuracao_segura["password"] = "********"

    return configuracao_segura


def testar_banco_incompativel() -> Dict[str, Any]:
    """
    Tenta estabelecer uma conexão com um banco propositalmente
    inexistente ou incompatível.

    O erro é esperado e faz parte da demonstração.
    """

    conexao = None
    inicio = time.perf_counter()

    configuracao = criar_configuracao_mysql(
        database=BANCO_INCOMPATIVEL
    )

    try:
        conexao = mysql.connector.connect(**configuracao)

        tempo_execucao = time.perf_counter() - inicio

        return {
            "sucesso": True,
            "tempo": tempo_execucao,
            "mensagem": (
                "A conexão foi realizada. O banco utilizado na "
                "demonstração existe no seu ambiente."
            ),
            "codigo_erro": None,
            "banco": BANCO_INCOMPATIVEL,
        }

    except Error as erro:
        tempo_execucao = time.perf_counter() - inicio

        return {
            "sucesso": False,
            "tempo": tempo_execucao,
            "mensagem": str(erro),
            "codigo_erro": getattr(erro, "errno", None),
            "banco": BANCO_INCOMPATIVEL,
        }

    finally:
        if conexao is not None and conexao.is_connected():
            conexao.close()


def consultar_clientes() -> Dict[str, Any]:
    """
    Conecta ao banco cliente e consulta a tabela cliente.clientes.

    A consulta utiliza SELECT * porque os nomes das colunas não foram
    informados. São retornados no máximo 10 registros.
    """

    conexao = None
    cursor = None
    inicio = time.perf_counter()

    configuracao = criar_configuracao_mysql(
        database=BANCO_CORRETO
    )

    try:
        conexao = mysql.connector.connect(**configuracao)

        if not conexao.is_connected():
            raise RuntimeError(
                "A conexão foi criada, mas não está ativa."
            )

        cursor = conexao.cursor(dictionary=True)

        consulta = f"""
            SELECT *
            FROM `{BANCO_CORRETO}`.`{TABELA_CLIENTES}`
            LIMIT 10
        """

        cursor.execute(consulta)

        registros: List[Dict[str, Any]] = cursor.fetchall()

        tempo_execucao = time.perf_counter() - inicio

        informacoes_servidor = conexao.get_server_info()

        return {
            "sucesso": True,
            "tempo": tempo_execucao,
            "mensagem": "Conexão e consulta realizadas com sucesso.",
            "codigo_erro": None,
            "banco": BANCO_CORRETO,
            "tabela": TABELA_CLIENTES,
            "registros": registros,
            "quantidade_registros": len(registros),
            "versao_mysql": informacoes_servidor,
        }

    except Error as erro:
        tempo_execucao = time.perf_counter() - inicio

        return {
            "sucesso": False,
            "tempo": tempo_execucao,
            "mensagem": str(erro),
            "codigo_erro": getattr(erro, "errno", None),
            "banco": BANCO_CORRETO,
            "tabela": TABELA_CLIENTES,
            "registros": [],
            "quantidade_registros": 0,
            "versao_mysql": None,
        }

    except Exception as erro:
        tempo_execucao = time.perf_counter() - inicio

        return {
            "sucesso": False,
            "tempo": tempo_execucao,
            "mensagem": str(erro),
            "codigo_erro": None,
            "banco": BANCO_CORRETO,
            "tabela": TABELA_CLIENTES,
            "registros": [],
            "quantidade_registros": 0,
            "versao_mysql": None,
        }

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


def identificar_tipo_erro(
    codigo_erro: Optional[int],
    mensagem: str,
) -> str:
    """
    Retorna uma explicação didática para erros comuns do MySQL.
    """

    mensagem_minuscula = mensagem.lower()

    if codigo_erro == 1049 or "unknown database" in mensagem_minuscula:
        return (
            "O servidor MySQL foi encontrado, mas o banco solicitado "
            "não existe. A aplicação espera uma estrutura diferente "
            "daquela disponível no ambiente."
        )

    if codigo_erro == 1045 or "access denied" in mensagem_minuscula:
        return (
            "O MySQL recusou o usuário ou a senha. Nesse caso, o "
            "problema é de autenticação ou permissão."
        )

    if codigo_erro == 1146 or "doesn't exist" in mensagem_minuscula:
        return (
            "A conexão com o banco funcionou, mas a tabela solicitada "
            "não foi encontrada."
        )

    if (
        codigo_erro == 2003
        or "can't connect" in mensagem_minuscula
        or "cannot connect" in mensagem_minuscula
    ):
        return (
            "A aplicação não conseguiu acessar o servidor MySQL. "
            "Verifique se o serviço está iniciado, se a porta está "
            "correta e se o host está acessível."
        )

    return (
        "O ambiente não conseguiu atender ao formato de integração "
        "esperado pela aplicação."
    )


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("🔌 Compatibilidade")

    st.markdown(
        """
        Esta página demonstra uma aplicação que precisa interagir
        com um banco de dados MySQL.
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

    st.subheader("Cenários")

    st.markdown(
        f"""
        **❌ Ambiente incompatível**

        Banco solicitado:

        `{BANCO_INCOMPATIVEL}`

        **✅ Ambiente compatível**

        Banco e tabela:

        `{BANCO_CORRETO}.{TABELA_CLIENTES}`
        """
    )

    st.warning(
        """
        A primeira conexão foi configurada incorretamente de forma
        proposital para fins didáticos.
        """
    )

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("🔌 Falha de Compatibilidade")

st.markdown(
    """
    Nesta demonstração, uma aplicação tenta se comunicar com dois
    ambientes MySQL.

    O primeiro ambiente não possui o banco esperado. O segundo possui
    o banco e a tabela compatíveis com a aplicação.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Compatibilidade?

    Compatibilidade avalia a capacidade de um software funcionar
    adequadamente com outros sistemas, componentes ou ambientes.

    Duas subcaracterísticas importantes são:

    - **Coexistência:** capacidade de compartilhar o mesmo ambiente
      e os mesmos recursos com outros sistemas.

    - **Interoperabilidade:** capacidade de trocar informações e
      utilizar corretamente as informações recebidas de outro sistema.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Uma aplicação foi desenvolvida para consultar clientes armazenados
    em um banco MySQL.

    Para funcionar corretamente, o ambiente deve possuir:

    - servidor MySQL disponível em `localhost:3306`;
    - usuário autorizado;
    - banco chamado `cliente`;
    - tabela chamada `clientes`;
    - estrutura de dados que possa ser consultada pela aplicação.
    """
)

st.success(
    """
    ### Requisito de compatibilidade

    A aplicação deve conectar-se ao MySQL e conseguir consultar os
    registros existentes em `cliente.clientes`.
    """
)


# =========================================================
# VERIFICAÇÃO DA BIBLIOTECA
# =========================================================
if not biblioteca_mysql_disponivel():
    st.error(
        """
        A biblioteca `mysql-connector-python` não está instalada.

        Instale-a antes de executar esta página:
        """
    )

    st.code(
        "python -m pip install mysql-connector-python",
        language="bash",
    )

    st.stop()


st.divider()


# =========================================================
# CONFIGURAÇÃO UTILIZADA
# =========================================================
st.header("Configuração utilizada")

configuracao_falha = ocultar_senha(
    criar_configuracao_mysql(BANCO_INCOMPATIVEL)
)

configuracao_sucesso = ocultar_senha(
    criar_configuracao_mysql(BANCO_CORRETO)
)

coluna_configuracao_falha, coluna_configuracao_sucesso = st.columns(2)

with coluna_configuracao_falha:
    with st.container(border=True):
        st.subheader("❌ Configuração incompatível")

        st.json(configuracao_falha)

        st.caption(
            "O banco foi configurado com um nome inexistente."
        )

with coluna_configuracao_sucesso:
    with st.container(border=True):
        st.subheader("✅ Configuração compatível")

        st.json(configuracao_sucesso)

        st.caption(
            f"A aplicação consultará "
            f"`{BANCO_CORRETO}.{TABELA_CLIENTES}`."
        )


st.divider()


# =========================================================
# EXECUÇÃO DAS DEMONSTRAÇÕES
# =========================================================
st.header("Execute as demonstrações")

coluna_falha, coluna_sucesso = st.columns(2)


# =========================================================
# CONEXÃO COM FALHA
# =========================================================
with coluna_falha:
    with st.container(border=True):
        st.subheader("❌ Ambiente incompatível")

        st.write(
            f"""
            A aplicação tentará conectar-se ao banco
            `{BANCO_INCOMPATIVEL}`.

            Como esse banco não deveria existir, espera-se que o MySQL
            rejeite a conexão.
            """
        )

        executar_falha = st.button(
            "Testar ambiente incompatível",
            key="testar_ambiente_incompativel",
            type="primary",
            use_container_width=True,
        )

        if executar_falha:
            # Limpa o resultado da conexão correta.
            st.session_state.resultado_sucesso_compatibilidade = None

            with st.spinner(
                "Tentando conectar ao ambiente incompatível..."
            ):
                st.session_state.resultado_falha_compatibilidade = (
                    testar_banco_incompativel()
                )

            st.rerun()


# =========================================================
# CONEXÃO COM SUCESSO
# =========================================================
with coluna_sucesso:
    with st.container(border=True):
        st.subheader("✅ Ambiente compatível")

        st.write(
            f"""
            A aplicação tentará conectar-se ao banco `{BANCO_CORRETO}`
            e executar:

            `SELECT * FROM cliente.clientes LIMIT 10`
            """
        )

        executar_sucesso = st.button(
            "Conectar e consultar clientes",
            key="testar_ambiente_compativel",
            use_container_width=True,
        )

        if executar_sucesso:
            # Limpa o resultado da conexão com falha.
            st.session_state.resultado_falha_compatibilidade = None

            with st.spinner(
                "Conectando ao MySQL e consultando clientes..."
            ):
                st.session_state.resultado_sucesso_compatibilidade = (
                    consultar_clientes()
                )

            st.rerun()

# =========================================================
# RESULTADO DA CONEXÃO COM FALHA
# =========================================================
resultado_falha = (
    st.session_state.resultado_falha_compatibilidade
)

if resultado_falha is not None:
    st.divider()

    st.header("Resultado do ambiente incompatível")

    if resultado_falha["sucesso"]:
        st.warning(
            f"""
            A conexão com `{BANCO_INCOMPATIVEL}` foi realizada.

            Isso significa que esse banco existe no seu computador.
            Para manter a demonstração de falha, altere a constante
            `BANCO_INCOMPATIVEL` para outro nome inexistente.
            """
        )

    else:
        st.error(
            """
            ### Falha de integração identificada

            A aplicação não conseguiu utilizar o banco solicitado pelo
            sistema.
            """
        )

        coluna_codigo, coluna_tempo = st.columns(2)

        with coluna_codigo:
            st.metric(
                label="Código do erro MySQL",
                value=(
                    str(resultado_falha["codigo_erro"])
                    if resultado_falha["codigo_erro"] is not None
                    else "Não informado"
                ),
            )

        with coluna_tempo:
            st.metric(
                label="Tempo da tentativa",
                value=formatar_tempo(
                    resultado_falha["tempo"]
                ),
            )

        st.code(
            resultado_falha["mensagem"],
            language="text",
        )

        st.warning(
            identificar_tipo_erro(
                codigo_erro=resultado_falha["codigo_erro"],
                mensagem=resultado_falha["mensagem"],
            )
        )


# =========================================================
# RESULTADO DA CONEXÃO CORRETA
# =========================================================
resultado_sucesso = (
    st.session_state.resultado_sucesso_compatibilidade
)

if resultado_sucesso is not None:
    st.divider()

    st.header("Resultado do ambiente compatível")

    if resultado_sucesso["sucesso"]:
        st.success(
            """
            ### Integração realizada com sucesso

            A aplicação conectou-se ao MySQL, acessou o banco correto
            e conseguiu consultar a tabela de clientes.
            """
        )

        coluna_banco, coluna_tabela, coluna_registros, coluna_tempo = (
            st.columns(4)
        )

        with coluna_banco:
            st.metric(
                label="Banco conectado",
                value=resultado_sucesso["banco"],
            )

        with coluna_tabela:
            st.metric(
                label="Tabela consultada",
                value=resultado_sucesso["tabela"],
            )

        with coluna_registros:
            st.metric(
                label="Registros retornados",
                value=str(
                    resultado_sucesso["quantidade_registros"]
                ),
            )

        with coluna_tempo:
            st.metric(
                label="Tempo da operação",
                value=formatar_tempo(
                    resultado_sucesso["tempo"]
                ),
            )

        st.caption(
            f"Versão do servidor MySQL: "
            f"{resultado_sucesso['versao_mysql']}"
        )

        if resultado_sucesso["registros"]:
            st.subheader("Registros de cliente")

            st.dataframe(
                resultado_sucesso["registros"],
                use_container_width=True,
                hide_index=True,
            )

        else:
            st.info(
                """
                A conexão e a consulta funcionaram, mas a tabela
                `cliente.clientes` não possui registros.
                """
            )

    else:
        st.error(
            """
            ### Não foi possível concluir a consulta

            Verifique o servidor, as credenciais, o banco e a tabela.
            """
        )

        coluna_codigo, coluna_tempo = st.columns(2)

        with coluna_codigo:
            st.metric(
                label="Código do erro MySQL",
                value=(
                    str(resultado_sucesso["codigo_erro"])
                    if resultado_sucesso["codigo_erro"] is not None
                    else "Não informado"
                ),
            )

        with coluna_tempo:
            st.metric(
                label="Tempo da tentativa",
                value=formatar_tempo(
                    resultado_sucesso["tempo"]
                ),
            )

        st.code(
            resultado_sucesso["mensagem"],
            language="text",
        )

        st.warning(
            identificar_tipo_erro(
                codigo_erro=resultado_sucesso["codigo_erro"],
                mensagem=resultado_sucesso["mensagem"],
            )
        )


# =========================================================
# COMPARAÇÃO DOS RESULTADOS
# =========================================================
if (
    resultado_falha is not None
    and resultado_sucesso is not None
):
    st.divider()

    st.header("Comparação dos ambientes")

    comparacao = [
        {
            "Ambiente": "Incompatível",
            "Banco solicitado": BANCO_INCOMPATIVEL,
            "Conexão": (
                "Conectado"
                if resultado_falha["sucesso"]
                else "Falhou"
            ),
            "Consulta realizada": "Não",
            "Compatibilidade": "❌ Não atende",
        },
        {
            "Ambiente": "Compatível",
            "Banco solicitado": BANCO_CORRETO,
            "Conexão": (
                "Conectado"
                if resultado_sucesso["sucesso"]
                else "Falhou"
            ),
            "Consulta realizada": (
                "Sim"
                if resultado_sucesso["sucesso"]
                else "Não"
            ),
            "Compatibilidade": (
                "✅ Atende"
                if resultado_sucesso["sucesso"]
                else "❌ Não atende"
            ),
        },
    ]

    st.dataframe(
        comparacao,
        use_container_width=True,
        hide_index=True,
    )

    if (
        not resultado_falha["sucesso"]
        and resultado_sucesso["sucesso"]
    ):
        st.success(
            """
            A demonstração foi concluída como esperado.

            O primeiro ambiente não possui o banco exigido pela
            aplicação. O segundo ambiente disponibiliza o banco e a
            tabela no formato esperado, permitindo a interoperabilidade.
            """
        )


st.divider()


# =========================================================
# CÓDIGO COM FALHA
# =========================================================
st.header("Código da conexão incompatível")

with st.expander(
    "Visualizar conexão com falha",
    expanded=True,
):
    st.code(
        f"""
import mysql.connector

conexao = mysql.connector.connect(
    host="{MYSQL_HOST}",
    port={MYSQL_PORT},
    user="{MYSQL_USER}",
    password="********",
    database="{BANCO_INCOMPATIVEL}"
)

print("Conectado com sucesso!")
        """.strip(),
        language="python",
    )

st.error(
    f"""
    O código espera encontrar o banco `{BANCO_INCOMPATIVEL}`,
    mas o ambiente disponibiliza o banco `{BANCO_CORRETO}`.
    """
)


# =========================================================
# CÓDIGO CORRETO
# =========================================================
st.header("Código da conexão compatível")

with st.expander(
    "Visualizar conexão e consulta corretas",
    expanded=True,
):
    st.code(
        f"""
import mysql.connector

conexao = None
cursor = None

try:
    conexao = mysql.connector.connect(
        host="{MYSQL_HOST}",
        port={MYSQL_PORT},
        user="{MYSQL_USER}",
        password="********",
        database="{BANCO_CORRETO}"
    )

    cursor = conexao.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM {BANCO_CORRETO}.{TABELA_CLIENTES} LIMIT 10"
    )

    clientes = cursor.fetchall()

    print("Conectado com sucesso!")
    print(clientes)

finally:
    if cursor is not None:
        cursor.close()

    if conexao is not None and conexao.is_connected():
        conexao.close()
        """.strip(),
        language="python",
    )


st.divider()


# =========================================================
# OUTROS EXEMPLOS DE INCOMPATIBILIDADE
# =========================================================
st.header("Outros exemplos de falhas de compatibilidade")

exemplo_1, exemplo_2, exemplo_3 = st.columns(3)

with exemplo_1:
    with st.container(border=True):
        st.subheader("Versão incompatível")

        st.write(
            """
            A aplicação utiliza um comando ou recurso disponível em
            uma versão mais recente do MySQL, mas o servidor executa
            uma versão antiga.
            """
        )

with exemplo_2:
    with st.container(border=True):
        st.subheader("Estrutura incompatível")

        st.write(
            """
            A aplicação espera uma coluna chamada `email`, mas o banco
            possui a coluna chamada `email_cliente`.
            """
        )

with exemplo_3:
    with st.container(border=True):
        st.subheader("Formato incompatível")

        st.write(
            """
            Um sistema envia datas no formato `DD/MM/AAAA`, enquanto
            outro sistema espera o formato `AAAA-MM-DD`.
            """
        )


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos da falha")

impactos_usuario, impactos_empresa = st.columns(2)

with impactos_usuario:
    with st.container(border=True):
        st.subheader("Impactos para o usuário")

        st.markdown(
            """
            - impossibilidade de consultar clientes;
            - mensagens de erro;
            - interrupção da operação;
            - necessidade de repetir tarefas;
            - perda de produtividade;
            - falta de confiança no sistema.
            """
        )

with impactos_empresa:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - sistemas que não conseguem trocar dados;
            - falhas em integrações;
            - retrabalho;
            - indisponibilidade de funcionalidades;
            - aumento dos chamados de suporte;
            - risco de inconsistência de dados;
            - atraso em processos do negócio.
            """
        )


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir a Compatibilidade?")

metrica_1, metrica_2, metrica_3 = st.columns(3)

with metrica_1:
    st.metric(
        label="Integrações testadas",
        value="2",
    )

with metrica_2:
    st.metric(
        label="Integrações bem-sucedidas",
        value=(
            "1"
            if (
                resultado_sucesso is not None
                and resultado_sucesso["sucesso"]
            )
            else "0"
        ),
    )

with metrica_3:
    st.metric(
        label="Taxa esperada de sucesso",
        value="50%",
    )

st.info(
    """
    Algumas métricas possíveis:

    - percentual de integrações concluídas com sucesso;
    - quantidade de ambientes suportados;
    - percentual de dados interpretados corretamente;
    - número de erros de integração;
    - número de versões compatíveis;
    - quantidade de falhas causadas por diferenças de formato;
    - tempo necessário para adaptar o sistema a outro ambiente.
    """
)


st.divider()


# =========================================================
# SEGURANÇA DAS CREDENCIAIS
# =========================================================
st.warning(
    """
    ### Atenção às credenciais

    A senha foi mantida no código porque faz parte da demonstração
    solicitada.

    Em um projeto real, não armazene senhas diretamente no arquivo
    Python. Utilize variáveis de ambiente ou o arquivo
    `.streamlit/secrets.toml`.
    """
)

with st.expander("Exemplo com st.secrets"):
    st.code(
        """
conexao = mysql.connector.connect(
    host=st.secrets["mysql"]["host"],
    port=st.secrets["mysql"]["port"],
    user=st.secrets["mysql"]["user"],
    password=st.secrets["mysql"]["password"],
    database=st.secrets["mysql"]["database"]
)
        """.strip(),
        language="python",
    )


# =========================================================
# LIMPAR RESULTADOS
# =========================================================
st.header("Reiniciar demonstração")

if st.button(
    "🗑️ Limpar resultados",
    key="limpar_resultados_compatibilidade",
    use_container_width=True,
):
    st.session_state.resultado_falha_compatibilidade = None
    st.session_state.resultado_sucesso_compatibilidade = None
    st.rerun()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um sistema compatível precisa conseguir funcionar no ambiente
    esperado e trocar informações corretamente com outros componentes.

    Nesta demonstração, a aplicação que procura um banco inexistente
    não consegue realizar a integração.

    Quando o banco `cliente` e a tabela `clientes` são utilizados, a
    aplicação consegue acessar e interpretar os dados disponíveis.
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