# ==========================================================
# IMPORTAÇÕES PADRÃO
# ==========================================================

import sys
from pathlib import Path

import streamlit as st


# ==========================================================
# CONFIGURAÇÃO DO CAMINHO DO PROJETO
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


# ==========================================================
# IMPORTAÇÕES DO PROJETO
# ==========================================================

from app.core.config import (
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
    DB_USER,
    DB_PASSWORD,
    DB_ENCRYPTION_KEY,
)

from app.core.security import descriptografar_senha

from app.database.connection import (
    obter_conexao
)

from app.database.inicializar_banco import (
    inicializar_banco
)


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="TechPort - MySQL",
    page_icon="🗄️",
    layout="wide"
)


# ==========================================================
# CABEÇALHO
# ==========================================================

st.title("🗄️ TechPort")

st.subheader(
    "Projeto, Implementação e Teste de Software"
)

st.write(
    """
    Nesta aplicação vamos acompanhar todo o processo,
    desde a configuração da conexão até a criação,
    população e consulta do banco MySQL.
    """
)

st.divider()


# ==========================================================
# FLUXO GERAL
# ==========================================================

st.subheader("🔄 Fluxo da aplicação")

st.code(
    """
.env
   ↓
config.py
   ↓
security.py
   ↓
descriptografia da senha
   ↓
MySQL
   ↓
techport_mysql_volumetria.sql
   ↓
Banco TechPort
   ↓
connection.py
   ↓
Consultas SQL
   ↓
Streamlit
    """,
    language="text"
)

st.divider()


# ==========================================================
# 1 - CONFIGURAÇÕES
# ==========================================================

st.subheader(
    "1️⃣ Configurações carregadas do .env"
)


col1, col2 = st.columns(2)


# ----------------------------------------------------------
# BANCO
# ----------------------------------------------------------

with col1:

    st.write(
        "### 🗄️ Banco de Dados"
    )

    st.write("Host")

    st.code(
        DB_HOST or "Não configurado"
    )

    st.write("Porta")

    st.code(
        str(DB_PORT)
    )

    st.write("Banco")

    st.code(
        DB_DATABASE or "Não configurado"
    )

    st.write("Usuário")

    st.code(
        DB_USER or "Não configurado"
    )


# ----------------------------------------------------------
# SEGURANÇA
# ----------------------------------------------------------

with col2:

    st.write(
        "### 🔐 Segurança"
    )

    st.write(
        "Senha criptografada:"
    )

    if DB_PASSWORD:

        st.code(
            DB_PASSWORD,
            language="text"
        )

    else:

        st.error(
            "DB_PASSWORD não encontrada."
        )


    st.write(
        "Chave Fernet:"
    )

    if DB_ENCRYPTION_KEY:

        chave_oculta = (
            DB_ENCRYPTION_KEY[:8]
            + "********************"
            + DB_ENCRYPTION_KEY[-5:]
        )

        st.code(
            chave_oculta,
            language="text"
        )

    else:

        st.error(
            "DB_ENCRYPTION_KEY não encontrada."
        )


st.divider()


# ==========================================================
# 2 - DESCRIPTOGRAFIA
# ==========================================================

st.subheader(
    "2️⃣ Descriptografia da senha"
)


try:

    senha_mysql = descriptografar_senha(
        DB_PASSWORD
    )

    st.success(
        "✅ Senha descriptografada com sucesso."
    )

    st.write(
        "Senha disponível apenas em memória:"
    )

    st.code(
        "*" * len(senha_mysql)
    )


except Exception as erro:

    st.error(
        "❌ Erro ao descriptografar a senha."
    )

    st.exception(
        erro
    )


st.divider()

# ==========================================================
# 3 - PRIMEIRO TESTE DE CONEXÃO
# ==========================================================

st.subheader(
    "3️⃣ Primeiro teste de conexão com MySQL"
)

st.write(
    """
    Neste primeiro teste, vamos verificar se o banco TechPort
    já existe e se a aplicação consegue conectar a ele.
    """
)

if st.button(
    "🔌 Testar conexão antes da criação",
    use_container_width=True
):

    conexao = None
    cursor = None

    try:

        with st.spinner(
            "Tentando conectar ao banco TechPort..."
        ):

            conexao = obter_conexao()

        if conexao.is_connected():

            st.success(
                "✅ O banco TechPort já existe e a conexão foi realizada!"
            )

            cursor = conexao.cursor()

            cursor.execute(
                """
                SELECT
                    DATABASE(),
                    VERSION(),
                    USER();
                """
            )

            resultado = cursor.fetchone()

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Banco",
                    resultado[0]
                )

            with col2:

                st.metric(
                    "Versão MySQL",
                    resultado[1]
                )

            with col3:

                st.metric(
                    "Usuário",
                    resultado[2]
                )

    except Exception as erro:

        mensagem_erro = str(erro)

        if "1049" in mensagem_erro:

            st.error(
                "❌ O banco TechPort ainda não existe."
            )

            st.info(
                """
                Esse erro é esperado nesta etapa.

                No próximo passo vamos criar o banco
                executando o arquivo SQL.
                """
            )

        else:

            st.error(
                "❌ Ocorreu um erro ao conectar ao MySQL."
            )

            st.exception(
                erro
            )

    finally:

        if cursor:

            try:
                cursor.close()
            except Exception:
                pass

        if conexao and conexao.is_connected():

            conexao.close()

            st.info(
                "🔒 Conexão encerrada."
            )


st.divider()


# ==========================================================
# 4 - CRIAR / RECRIAR BANCO
# ==========================================================

st.subheader(
    "4️⃣ Criar ou recriar Banco TechPort"
)

st.write(
    """
    Agora vamos executar o arquivo:

    `app/database/techport_mysql_volumetria.sql`

    O script cria toda a estrutura do banco
    e insere os dados fictícios.
    """
)

st.warning(
    """
    ⚠️ O script pode executar DROP DATABASE.

    Caso o banco TechPort já exista,
    seus dados atuais poderão ser removidos.
    """
)


if st.button(
    "🚀 Criar / Recriar Banco TechPort",
    type="primary",
    use_container_width=True
):

    st.write(
        "### ⚙️ Execução do script SQL"
    )

    area_status = st.empty()

    progresso = st.progress(0)

    mensagens = []

    def atualizar_status(mensagem):

        mensagens.append(
            mensagem
        )

        area_status.code(
            "\n".join(
                mensagens[-12:]
            ),
            language="text"
        )

    try:

        atualizar_status(
            "🚀 Iniciando criação do banco..."
        )

        progresso.progress(10)

        inicializar_banco(
            callback=atualizar_status
        )

        progresso.progress(100)

        st.success(
            "🎉 Banco TechPort criado e populado com sucesso!"
        )

        st.info(
            """
            Agora execute o próximo teste de conexão
            para validar se o banco foi criado corretamente.
            """
        )

    except Exception as erro:

        progresso.empty()

        st.error(
            "❌ Erro durante a criação do banco."
        )

        st.exception(
            erro
        )


st.divider()


# ==========================================================
# 5 - SEGUNDO TESTE DE CONEXÃO
# ==========================================================

st.subheader(
    "5️⃣ Segundo teste de conexão com MySQL"
)

st.write(
    """
    Agora que o script de criação foi executado,
    vamos testar novamente a conexão com o banco TechPort.
    """
)


if st.button(
    "🔌 Testar conexão após a criação",
    use_container_width=True
):

    conexao = None
    cursor = None

    try:

        with st.spinner(
            "Conectando ao banco TechPort..."
        ):

            conexao = obter_conexao()

        if conexao.is_connected():

            st.success(
                "✅ Conexão realizada com sucesso!"
            )

            cursor = conexao.cursor()


            # ==================================================
            # INFORMAÇÕES DA CONEXÃO
            # ==================================================

            consulta_info = """
SELECT
    DATABASE(),
    VERSION(),
    USER();
"""

            st.write(
                "### Consulta executada"
            )

            st.code(
                consulta_info,
                language="sql"
            )

            cursor.execute(
                consulta_info
            )

            resultado = cursor.fetchone()


            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Banco",
                    resultado[0]
                )

            with col2:

                st.metric(
                    "Versão MySQL",
                    resultado[1]
                )

            with col3:

                st.metric(
                    "Usuário",
                    resultado[2]
                )


            # ==================================================
            # DETALHES DA CONEXÃO
            # ==================================================

            st.write(
                "### 🔧 Detalhes técnicos"
            )

            st.write(
                f"**Host:** `{DB_HOST}`"
            )

            st.write(
                f"**Porta:** `{DB_PORT}`"
            )

            st.write(
                f"**Banco:** `{DB_DATABASE}`"
            )

            st.write(
                f"**Usuário:** `{DB_USER}`"
            )

            st.write(
                "**Senha:** `********`"
            )

            st.write(
                "**Status:** 🟢 CONECTADO"
            )




    except Exception as erro:

        mensagem_erro = str(
            erro
        )

        if "1049" in mensagem_erro:

            st.error(
                "❌ O banco TechPort ainda não existe."
            )

            st.warning(
                """
                Volte para a etapa 4 e execute:

                **🚀 Criar / Recriar Banco TechPort**
                """
            )

        else:

            st.error(
                "❌ Não foi possível conectar ao MySQL."
            )

            st.exception(
                erro
            )

    finally:

        if cursor:

            try:
                cursor.close()
            except Exception:
                pass

        if conexao and conexao.is_connected():

            conexao.close()

            st.info(
                "🔒 Conexão com MySQL encerrada."
            )