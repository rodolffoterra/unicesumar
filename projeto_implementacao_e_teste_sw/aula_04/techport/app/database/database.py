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
    fechamento do cursor
          ↓
    fechamento da conexão
    """


    # ======================================================
    # VARIÁVEIS INICIAIS
    # ======================================================

    # Inicializamos as variáveis com None.
    #
    # Isso é importante porque, caso aconteça um erro
    # antes da conexão ou do cursor serem criados,
    # o bloco finally ainda poderá verificar essas
    # variáveis com segurança.

    conexao = None
    cursor = None


    # ======================================================
    # TRY
    # ======================================================

    # O bloco try contém as operações que podem gerar erros.
    #
    # Exemplos:
    #
    # - MySQL desligado;
    # - usuário incorreto;
    # - senha incorreta;
    # - banco inexistente;
    # - problema de rede;
    # - erro na consulta SQL.

    try:


        # ==================================================
        # 1 - ABRIR CONEXÃO
        # ==================================================

        # Chamamos a função obter_conexao().
        #
        # Internamente ela executará:
        #
        # mysql.connector.connect(...)
        #
        # Se tudo estiver correto, recebemos um objeto
        # representando a conexão aberta com o MySQL.

        conexao = obter_conexao()


        # ==================================================
        # 2 - CRIAR CURSOR
        # ==================================================

        # O cursor é o objeto utilizado para enviar
        # comandos SQL para o banco de dados.
        #
        # Podemos imaginar:
        #
        # conexão
        #    ↓
        # cursor
        #    ↓
        # SQL
        #    ↓
        # MySQL

        cursor = conexao.cursor()


        # ==================================================
        # 3 - CONSULTA SQL DE TESTE
        # ==================================================

        # Executamos uma consulta simples para verificar
        # se realmente conseguimos conversar com o MySQL.
        #
        # DATABASE()
        #     retorna o banco atualmente selecionado.
        #
        # VERSION()
        #     retorna a versão do servidor MySQL.

        cursor.execute(
            """
            SELECT
                DATABASE(),
                VERSION();
            """
        )


        # ==================================================
        # 4 - RECUPERAR O RESULTADO
        # ==================================================

        # fetchone() recupera apenas UMA linha do resultado.
        #
        # Como nossa consulta retorna somente uma linha,
        # fetchone() é suficiente.

        resultado = cursor.fetchone()


        # O resultado será semelhante a:
        #
        # ('techport', '8.0.43')
        #
        # Portanto:
        #
        # resultado[0] -> nome do banco
        # resultado[1] -> versão do MySQL


        # ==================================================
        # 5 - MOSTRAR RESULTADO
        # ==================================================

        print(
            "\nConexão realizada com sucesso!"
        )


        print(
            f"Banco atual: {resultado[0]}"
        )


        print(
            f"Versão MySQL: {resultado[1]}"
        )


    # ======================================================
    # EXCEPT
    # ======================================================

    # Se qualquer erro acontecer dentro do bloco try,
    # o Python interrompe aquela execução e entra aqui.
    #
    # A variável "erro" recebe as informações sobre
    # a exceção ocorrida.

    except Exception as erro:

        print(
            "\nNão foi possível realizar o teste."
        )

        print(
            f"Erro: {erro}"
        )


    # ======================================================
    # FINALLY
    # ======================================================

    # O bloco finally será executado independentemente
    # de ter ocorrido sucesso ou erro.
    #
    # Por isso ele é um bom local para liberar recursos,
    # como cursor e conexão.

    finally:


        # ==================================================
        # 6 - FECHAR CURSOR
        # ==================================================

        # Primeiro verificamos se o cursor realmente
        # chegou a ser criado.
        #
        # Caso exista, fechamos o cursor.

        if cursor:

            cursor.close()


        # ==================================================
        # 7 - FECHAR CONEXÃO
        # ==================================================

        # Verificamos duas condições:
        #
        # 1. se a variável conexao possui uma conexão;
        # 2. se essa conexão ainda está aberta.
        #
        # Somente então executamos close().

        if conexao and conexao.is_connected():

            conexao.close()

            print(
                "Conexão encerrada."
            )


# ==========================================================
# PONTO DE ENTRADA DO PROGRAMA
# ==========================================================

# Esta condição verifica se este arquivo Python está
# sendo executado diretamente.
#
# Quando executamos:
#
# python database.py
#
# __name__ recebe o valor:
#
# "__main__"
#
# Portanto, a função testar_conexao() será executada.
#
#
# Porém, se este arquivo for importado por outro arquivo:
#
# from app.database.database import testar_conexao
#
# a função NÃO será executada automaticamente.

if __name__ == "__main__":

    testar_conexao()