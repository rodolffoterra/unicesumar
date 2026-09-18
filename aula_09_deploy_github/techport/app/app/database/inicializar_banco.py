# ==========================================================
# IMPORTAÇÕES
# ==========================================================

# Path, da biblioteca pathlib, é utilizado para trabalhar
# com caminhos de arquivos e pastas de forma mais segura
# e independente do sistema operacional.

from pathlib import Path


# mysql.connector permite que o Python se conecte
# ao servidor MySQL e execute comandos SQL.

import mysql.connector


# Importamos as configurações do banco carregadas
# pelo arquivo app/core/config.py.
#
# Essas informações normalmente vêm do arquivo .env.

from app.core.config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
)


# Importamos a função responsável por descriptografar
# a senha armazenada no .env.

from app.core.security import descriptografar_senha


# ==========================================================
# CAMINHO DO ARQUIVO SQL
# ==========================================================

# __file__ representa o caminho do arquivo Python atual.
#
# Path(__file__).resolve()
#     obtém o caminho absoluto do arquivo.
#
# .parent
#     retorna a pasta onde este arquivo está localizado.
#
# Depois adicionamos:
#
# techport_mysql_volumetria.sql
#
# Portanto, o Python procura o arquivo SQL na mesma pasta
# deste script.

CAMINHO_SQL = (
    Path(__file__).resolve().parent
    / "techport_mysql_volumetria.sql"
)


# ==========================================================
# CONEXÃO SOMENTE COM O SERVIDOR MYSQL
# ==========================================================

def obter_conexao_servidor():
    """
    Cria uma conexão com o servidor MySQL sem selecionar
    inicialmente um banco de dados específico.

    Isso é necessário porque o banco TechPort pode ainda
    não existir.

    Essa conexão será utilizada para executar comandos como:

    CREATE DATABASE
    DROP DATABASE
    USE
    """


    # ======================================================
    # DESCRIPTOGRAFAR A SENHA
    # ======================================================

    # DB_PASSWORD contém a senha criptografada.
    #
    # Antes de enviar a senha ao MySQL precisamos recuperar
    # temporariamente o valor original.

    senha_mysql = descriptografar_senha(
        DB_PASSWORD
    )


    # ======================================================
    # ABRIR CONEXÃO COM O SERVIDOR MYSQL
    # ======================================================

    # Observe que NÃO informamos:
    #
    # database=...
    #
    # Isso é proposital.
    #
    # Se utilizássemos:
    #
    # database="techport"
    #
    # e o banco não existisse, receberíamos:
    #
    # Error 1049 - Unknown database 'techport'

    conexao = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=senha_mysql
    )


    # Retorna a conexão aberta para quem chamou a função.

    return conexao


# ==========================================================
# LER E SEPARAR COMANDOS SQL
# ==========================================================

def separar_comandos_sql(script_sql):
    """
    Recebe todo o conteúdo de um arquivo SQL como texto
    e separa os comandos individuais.

    Exemplo:

    CREATE DATABASE techport;

    USE techport;

    CREATE TABLE usuarios (...);

    Cada comando será colocado em uma posição da lista.

    A função também trata alterações de DELIMITER.

    Isso é necessário porque procedimentos armazenados
    podem possuir vários ";" dentro de BEGIN ... END.
    """


    # ======================================================
    # LISTA DE COMANDOS
    # ======================================================

    # Esta lista armazenará cada comando SQL completo.

    comandos = []


    # ======================================================
    # DELIMITADOR PADRÃO
    # ======================================================

    # Normalmente comandos SQL terminam com:
    #
    # ;
    #
    # Exemplo:
    #
    # SELECT * FROM usuarios;

    delimitador = ";"


    # ======================================================
    # COMANDO EM CONSTRUÇÃO
    # ======================================================

    # Algumas instruções SQL possuem várias linhas.
    #
    # Por isso, precisamos guardar as linhas até encontrar
    # o delimitador que representa o final do comando.

    comando_atual = []


    # ======================================================
    # PERCORRER O SCRIPT LINHA POR LINHA
    # ======================================================

    # splitlines() divide o conteúdo do arquivo SQL
    # em várias linhas.

    for linha in script_sql.splitlines():


        # --------------------------------------------------
        # REMOVER ESPAÇOS DAS EXTREMIDADES
        # --------------------------------------------------

        # strip() remove espaços e quebras de linha
        # no início e no final.

        linha_limpa = linha.strip()


        # --------------------------------------------------
        # IGNORAR LINHAS VAZIAS
        # --------------------------------------------------

        # Se a linha estiver vazia, não precisamos
        # adicioná-la ao comando SQL.

        if not linha_limpa:
            continue


        # --------------------------------------------------
        # IGNORAR COMENTÁRIOS SQL
        # --------------------------------------------------

        # Comentários iniciados com:
        #
        # --
        #
        # não precisam ser enviados ao servidor.

        if linha_limpa.startswith("--"):
            continue


        # --------------------------------------------------
        # IDENTIFICAR ALTERAÇÃO DE DELIMITER
        # --------------------------------------------------

        # Procedimentos podem utilizar:
        #
        # DELIMITER $$
        #
        # CREATE PROCEDURE ...
        #
        # BEGIN
        #
        #     SELECT ...;
        #     INSERT ...;
        #
        # END $$
        #
        # DELIMITER ;
        #
        # Portanto precisamos atualizar o delimitador
        # utilizado para identificar o final do comando.

        if linha_limpa.upper().startswith("DELIMITER"):

            partes = linha_limpa.split()


            # Exemplo:
            #
            # "DELIMITER $$"
            #
            # depois do split:
            #
            # partes[0] = DELIMITER
            # partes[1] = $$

            if len(partes) >= 2:
                delimitador = partes[1]


            # A linha DELIMITER não é enviada ao MySQL
            # através do cursor.
            #
            # Ela é uma instrução utilizada pelo cliente
            # MySQL para interpretar o arquivo.

            continue


        # --------------------------------------------------
        # ADICIONAR LINHA AO COMANDO ATUAL
        # --------------------------------------------------

        comando_atual.append(
            linha
        )


        # --------------------------------------------------
        # MONTAR O TEXTO ATUAL
        # --------------------------------------------------

        # As linhas acumuladas são novamente unidas
        # formando um comando SQL.

        texto_atual = "\n".join(
            comando_atual
        ).rstrip()


        # --------------------------------------------------
        # VERIFICAR SE O COMANDO TERMINOU
        # --------------------------------------------------

        # Verificamos se o texto termina com o delimitador
        # atual.
        #
        # Pode ser:
        #
        # ;
        #
        # ou:
        #
        # $$

        if texto_atual.endswith(
            delimitador
        ):


            # ------------------------------------------------
            # REMOVER DELIMITADOR
            # ------------------------------------------------

            # O delimitador não precisa ser enviado
            # junto com o comando para cursor.execute().

            comando = texto_atual[
                :-len(delimitador)
            ].strip()


            # ------------------------------------------------
            # ADICIONAR À LISTA
            # ------------------------------------------------

            if comando:

                comandos.append(
                    comando
                )


            # ------------------------------------------------
            # LIMPAR PARA O PRÓXIMO COMANDO
            # ------------------------------------------------

            comando_atual = []


    # ======================================================
    # TRATAR EVENTUAL COMANDO RESTANTE
    # ======================================================

    # Caso exista alguma instrução que não tenha sido
    # adicionada anteriormente, fazemos a última verificação.

    if comando_atual:

        comando = "\n".join(
            comando_atual
        ).strip()


        if comando:

            comandos.append(
                comando
            )


    # ======================================================
    # RETORNAR COMANDOS
    # ======================================================

    # Exemplo conceitual:
    #
    # [
    #   "DROP DATABASE IF EXISTS techport",
    #   "CREATE DATABASE techport",
    #   "USE techport",
    #   "CREATE TABLE usuarios (...)",
    #   ...
    # ]

    return comandos


# ==========================================================
# CRIAR / RECRIAR BANCO
# ==========================================================

def inicializar_banco(callback=None):
    """
    Executa todo o arquivo techport_mysql_volumetria.sql.

    A função realiza:

    1. Localização do arquivo SQL
    2. Leitura do arquivo
    3. Separação dos comandos
    4. Conexão com o MySQL
    5. Execução dos comandos
    6. Commit
    7. Fechamento da conexão

    O parâmetro callback é opcional.

    Ele permite enviar mensagens de progresso para outra
    parte da aplicação, como uma página Streamlit.
    """


    # ======================================================
    # VARIÁVEIS INICIAIS
    # ======================================================

    # Inicializamos com None para que o bloco finally
    # consiga verificar com segurança se os objetos
    # chegaram a ser criados.

    conexao = None
    cursor = None


    # ======================================================
    # TRY
    # ======================================================

    try:


        # ==================================================
        # 1 - VERIFICAR SE O ARQUIVO SQL EXISTE
        # ==================================================

        # Antes de tentar abrir o arquivo, verificamos
        # se ele realmente existe.

        if not CAMINHO_SQL.exists():

            raise FileNotFoundError(
                f"Arquivo SQL não encontrado: {CAMINHO_SQL}"
            )


        # ==================================================
        # CALLBACK - LEITURA
        # ==================================================

        # Se uma função callback foi enviada,
        # informamos o andamento.

        if callback:

            callback(
                "📄 Lendo arquivo SQL..."
            )


        # ==================================================
        # 2 - LER O ARQUIVO SQL
        # ==================================================

        # read_text() carrega todo o conteúdo do arquivo
        # como uma string Python.

        script_sql = CAMINHO_SQL.read_text(
            encoding="utf-8"
        )


        # ==================================================
        # 3 - SEPARAR OS COMANDOS SQL
        # ==================================================

        # O conteúdo inteiro do arquivo é enviado para
        # separar_comandos_sql().
        #
        # O resultado será uma lista de comandos.

        comandos = separar_comandos_sql(
            script_sql
        )


        # ==================================================
        # CALLBACK - QUANTIDADE DE COMANDOS
        # ==================================================

        if callback:

            callback(
                f"📋 {len(comandos)} comandos SQL identificados."
            )


        # ==================================================
        # 4 - CONECTAR AO SERVIDOR MYSQL
        # ==================================================

        # A conexão é aberta SEM selecionar inicialmente
        # o banco TechPort.
        #
        # Isso permite executar CREATE DATABASE.

        if callback:

            callback(
                "🔌 Conectando ao servidor MySQL..."
            )


        conexao = obter_conexao_servidor()


        # ==================================================
        # 5 - CRIAR CURSOR
        # ==================================================

        # O cursor será utilizado para enviar os comandos
        # SQL para o servidor MySQL.

        cursor = conexao.cursor()


        # ==================================================
        # QUANTIDADE TOTAL DE COMANDOS
        # ==================================================

        total = len(
            comandos
        )


        # ==================================================
        # 6 - EXECUTAR COMANDOS SQL
        # ==================================================

        # enumerate() permite percorrer a lista e,
        # ao mesmo tempo, saber qual número do comando
        # está sendo executado.
        #
        # start=1 faz a contagem iniciar em 1.

        for indice, comando in enumerate(
            comandos,
            start=1
        ):


            # ------------------------------------------------
            # PEGAR PRIMEIRA LINHA DO COMANDO
            # ------------------------------------------------

            # Utilizamos apenas para mostrar no Streamlit
            # qual comando está sendo executado.

            inicio = comando.strip().split(
                "\n"
            )[0]


            # ------------------------------------------------
            # CALLBACK - PROGRESSO
            # ------------------------------------------------

            if callback:

                callback(
                    f"⚙️ Executando {indice}/{total}: "
                    f"{inicio[:70]}"
                )


            # ------------------------------------------------
            # EXECUTAR SQL
            # ------------------------------------------------

            # Aqui ocorre efetivamente a execução
            # do comando no servidor MySQL.

            cursor.execute(
                comando
            )


            # ------------------------------------------------
            # CONSULTAS QUE RETORNAM LINHAS
            # ------------------------------------------------

            # Alguns comandos podem retornar resultados.
            #
            # Exemplo:
            #
            # SELECT ...
            #
            # cursor.with_rows indica se existem linhas
            # disponíveis para leitura.

            if cursor.with_rows:

                cursor.fetchall()


            # ------------------------------------------------
            # RESULTADOS ADICIONAIS
            # ------------------------------------------------

            # Alguns comandos, especialmente procedures,
            # podem produzir mais de um conjunto de
            # resultados.
            #
            # nextset() avança para o próximo resultado.

            while cursor.nextset():

                if cursor.with_rows:

                    cursor.fetchall()


        # ==================================================
        # 7 - COMMIT
        # ==================================================

        # commit() confirma as alterações realizadas.
        #
        # É especialmente importante para:
        #
        # INSERT
        # UPDATE
        # DELETE
        #
        # Sem o commit, algumas alterações poderiam
        # permanecer apenas dentro da transação atual.

        conexao.commit()


        # ==================================================
        # CALLBACK - SUCESSO
        # ==================================================

        if callback:

            callback(
                "✅ Banco TechPort criado e populado com sucesso!"
            )


        # Indica para quem chamou a função que
        # a execução foi concluída corretamente.

        return True


    # ======================================================
    # EXCEPT
    # ======================================================

    # Se qualquer erro ocorrer durante a execução,
    # entramos neste bloco.

    except Exception:


        # ==================================================
        # ROLLBACK
        # ==================================================

        # Se a conexão já tiver sido criada,
        # tentamos desfazer alterações ainda não confirmadas.

        if conexao:

            try:

                conexao.rollback()

            except Exception:

                # Se o rollback também falhar,
                # não interrompemos o tratamento principal.

                pass


        # ==================================================
        # PROPAGAR O ERRO
        # ==================================================

        # raise sem parâmetros relança o mesmo erro.
        #
        # Isso permite que o Streamlit, por exemplo,
        # capture e mostre a mensagem para o usuário.

        raise


    # ======================================================
    # FINALLY
    # ======================================================

    # O bloco finally será executado com sucesso ou erro.
    #
    # Ele é responsável por liberar os recursos abertos.

    finally:


        # ==================================================
        # FECHAR CURSOR
        # ==================================================

        if cursor:

            try:

                cursor.close()

            except Exception:

                pass


        # ==================================================
        # FECHAR CONEXÃO
        # ==================================================

        # Verificamos se:
        #
        # 1. a conexão existe;
        # 2. ela ainda está aberta.
        #
        # Depois fechamos corretamente.

        if conexao and conexao.is_connected():

            conexao.close()