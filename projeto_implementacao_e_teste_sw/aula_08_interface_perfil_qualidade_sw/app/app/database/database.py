# ==========================================================
# IMPORTAÇÃO DA FUNÇÃO DE CONEXÃO
# ==========================================================

# Importamos a função obter_conexao() que foi criada no
# arquivo:
#
# app/database/connection.py
#
# Essa função já é responsável por:
#
# 1. carregar as configurações;
# 2. descriptografar a senha;
# 3. conectar ao servidor MySQL;
# 4. selecionar o banco TechPort;
# 5. retornar o objeto de conexão.

from app.database.connection import obter_conexao


# ==========================================================
# FUNÇÃO PARA TESTAR A CONEXÃO
# ==========================================================

def testar_conexao():
    """
    Testa a conexão com o MySQL executando
    uma consulta SQL simples.

    Essa função pode ser utilizada de duas maneiras:

    1. Diretamente pelo terminal:

       python -m app.database.database

    2. Importada pela API FastAPI:

       from app.database.database import testar_conexao


    Fluxo:

    obter_conexao()
          ↓
    conexão com MySQL
          ↓
    criação do cursor
          ↓
    execução do SELECT
          ↓
    leitura do resultado
          ↓
    retorno das informações
          ↓
    fechamento do cursor
          ↓
    fechamento da conexão
    """


    # ======================================================
    # VARIÁVEIS INICIAIS
    # ======================================================

    conexao = None
    cursor = None


    # ======================================================
    # TRY
    # ======================================================

    try:


        # ==================================================
        # 1 - ABRIR CONEXÃO
        # ==================================================

        conexao = obter_conexao()


        # ==================================================
        # 2 - CRIAR CURSOR
        # ==================================================

        cursor = conexao.cursor()


        # ==================================================
        # 3 - CONSULTA SQL DE TESTE
        # ==================================================

        cursor.execute(
            """
            SELECT
                DATABASE(),
                VERSION();
            """
        )


        # ==================================================
        # 4 - RECUPERAR RESULTADO
        # ==================================================

        resultado = cursor.fetchone()


        # ==================================================
        # 5 - RECUPERAR BANCO E VERSÃO
        # ==================================================

        banco_atual = resultado[0]

        versao_mysql = resultado[1]


        # ==================================================
        # 6 - MOSTRAR NO TERMINAL
        # ==================================================

        print(
            "\nConexão realizada com sucesso!"
        )

        print(
            f"Banco atual: {banco_atual}"
        )

        print(
            f"Versão MySQL: {versao_mysql}"
        )


        # ==================================================
        # 7 - RETORNAR RESULTADO
        # ==================================================

        # Esse retorno é importante porque agora outros
        # arquivos poderão utilizar o resultado da função.
        #
        # Por exemplo, o FastAPI poderá transformar este
        # dicionário automaticamente em JSON.

        return {
            "status": True,
            "mensagem": "Conexão com MySQL realizada com sucesso.",
            "banco": banco_atual,
            "versao_mysql": versao_mysql
        }


    # ======================================================
    # EXCEPT
    # ======================================================

    except Exception as erro:


        print(
            "\nNão foi possível realizar o teste."
        )

        print(
            f"Erro: {erro}"
        )


        # Também retornamos informações quando ocorrer erro.
        #
        # Assim a API poderá mostrar o problema no Swagger.

        return {
            "status": False,
            "mensagem": "Não foi possível conectar ao MySQL.",
            "erro": str(erro)
        }


    # ======================================================
    # FINALLY
    # ======================================================

    finally:


        # ==================================================
        # 8 - FECHAR CURSOR
        # ==================================================

        if cursor:

            cursor.close()


        # ==================================================
        # 9 - FECHAR CONEXÃO
        # ==================================================

        if conexao and conexao.is_connected():

            conexao.close()

            print(
                "Conexão encerrada."
            )


# ==========================================================
# PONTO DE ENTRADA DO PROGRAMA
# ==========================================================

if __name__ == "__main__":

    testar_conexao()