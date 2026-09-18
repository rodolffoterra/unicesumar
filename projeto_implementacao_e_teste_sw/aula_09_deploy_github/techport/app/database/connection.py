# ==========================================================
# IMPORTAÇÃO DA BIBLIOTECA MYSQL
# ==========================================================

# mysql.connector é a biblioteca responsável por permitir
# que uma aplicação Python se comunique com um servidor MySQL.
#
# Ela fornece recursos para:
# - abrir conexões;
# - executar comandos SQL;
# - realizar consultas;
# - controlar transações;
# - fechar conexões.

import mysql.connector


# ==========================================================
# IMPORTAÇÃO DAS CONFIGURAÇÕES DO BANCO
# ==========================================================

# As informações abaixo não estão escritas diretamente
# neste arquivo.
#
# Elas são carregadas pelo arquivo:
#
# app/core/config.py
#
# O config.py, por sua vez, lê essas informações do
# arquivo .env.
#
# Fluxo:
#
# .env
#   ↓
# config.py
#   ↓
# connection.py

from app.core.config import (
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
    DB_USER,
    DB_PASSWORD,
)


# ==========================================================
# IMPORTAÇÃO DA FUNÇÃO DE SEGURANÇA
# ==========================================================

# A senha armazenada no arquivo .env está criptografada.
#
# Portanto, não podemos enviar diretamente DB_PASSWORD
# para o MySQL.
#
# A função descriptografar_senha() utiliza a chave Fernet
# para recuperar a senha original antes da conexão.

from app.core.security import descriptografar_senha


# ==========================================================
# FUNÇÃO RESPONSÁVEL PELA CONEXÃO
# ==========================================================

def obter_conexao():
    """
    Cria e retorna uma conexão com o banco de dados TechPort.

    Etapas realizadas:

    1. Recebe a senha criptografada carregada do .env.
    2. Descriptografa a senha.
    3. Utiliza host, porta, banco, usuário e senha
       para abrir a conexão.
    4. Retorna a conexão para a aplicação.
    """


    # ======================================================
    # 1 - DESCRIPTOGRAFAR A SENHA
    # ======================================================

    # DB_PASSWORD contém a senha criptografada.
    #
    # Exemplo:
    #
    # gAAAAABqe39faSWGLvyqfZMG_crtWe11g2f9...
    #
    # Essa informação não pode ser utilizada diretamente
    # pelo MySQL.
    #
    # Por isso, enviamos DB_PASSWORD para a função
    # descriptografar_senha().

    senha_mysql = descriptografar_senha(
        DB_PASSWORD
    )


    # Neste momento, a variável senha_mysql contém
    # temporariamente a senha original.
    #
    # Exemplo conceitual:
    #
    # DB_PASSWORD
    #     ↓
    # senha criptografada
    #     ↓
    # descriptografar_senha()
    #     ↓
    # senha_mysql
    #     ↓
    # senha original
    #
    # IMPORTANTE:
    #
    # Não devemos utilizar:
    #
    # print(senha_mysql)
    #
    # pois isso poderia expor a senha no terminal ou
    # nos logs da aplicação.


    # ======================================================
    # 2 - ABRIR A CONEXÃO COM O MYSQL
    # ======================================================

    # A função mysql.connector.connect() recebe os dados
    # necessários para localizar o servidor MySQL e
    # autenticar o usuário.

    conexao = mysql.connector.connect(

        # --------------------------------------------------
        # HOST
        # --------------------------------------------------

        # Endereço onde o servidor MySQL está executando.
        #
        # Em ambiente local normalmente:
        #
        # localhost

        host=DB_HOST,


        # --------------------------------------------------
        # PORTA
        # --------------------------------------------------

        # Porta utilizada pelo servidor MySQL.
        #
        # A porta padrão do MySQL é:
        #
        # 3306

        port=DB_PORT,


        # --------------------------------------------------
        # DATABASE
        # --------------------------------------------------

        # Nome do banco que queremos utilizar.
        #
        # Neste projeto:
        #
        # techport

        database=DB_DATABASE,


        # --------------------------------------------------
        # USUÁRIO
        # --------------------------------------------------

        # Usuário utilizado para autenticação no MySQL.
        #
        # Exemplo:
        #
        # root

        user=DB_USER,


        # --------------------------------------------------
        # SENHA
        # --------------------------------------------------

        # Aqui utilizamos a senha que foi descriptografada
        # anteriormente.
        #
        # Observe que NÃO utilizamos DB_PASSWORD diretamente,
        # pois DB_PASSWORD contém a versão criptografada.

        password=senha_mysql
    )


    # ======================================================
    # 3 - RETORNAR A CONEXÃO
    # ======================================================

    # Se mysql.connector.connect() conseguir estabelecer
    # a comunicação com o MySQL, teremos um objeto de
    # conexão armazenado na variável "conexao".
    #
    # Retornamos esse objeto para que outras partes da
    # aplicação possam executar consultas SQL.

    return conexao