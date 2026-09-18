# ==========================================================
# IMPORTAÇÃO DA CONEXÃO
# ==========================================================

# Importamos a função responsável por abrir
# uma conexão com o banco de dados TechPort.

from app.database.connection import obter_conexao


# ==========================================================
# GET - LISTAR TODOS OS TÉCNICOS
# ==========================================================

def listar_tecnicos():
    """
    Retorna todos os técnicos cadastrados
    na tabela tecnicos.
    """

    conexao = None
    cursor = None

    try:

        # --------------------------------------------------
        # 1 - ABRIR CONEXÃO
        # --------------------------------------------------

        conexao = obter_conexao()


        # --------------------------------------------------
        # 2 - CRIAR CURSOR
        # --------------------------------------------------

        # dictionary=True faz com que cada registro
        # seja retornado como um dicionário Python.
        #
        # Exemplo:
        #
        # {
        #     "id": 1,
        #     "nome": "Carlos",
        #     "email": "carlos@email.com"
        # }

        cursor = conexao.cursor(
            dictionary=True
        )


        # --------------------------------------------------
        # 3 - EXECUTAR CONSULTA
        # --------------------------------------------------

        sql = """
            SELECT
                id,
                nome,
                email,
                especialidade,
                nivel,
                disponivel,
                ativo,
                data_cadastro
            FROM tecnicos
            ORDER BY id;
        """

        cursor.execute(sql)


        # --------------------------------------------------
        # 4 - RECUPERAR TODOS OS REGISTROS
        # --------------------------------------------------

        tecnicos = cursor.fetchall()

        return tecnicos


    finally:

        # --------------------------------------------------
        # 5 - FECHAR CURSOR
        # --------------------------------------------------

        if cursor:
            cursor.close()


        # --------------------------------------------------
        # 6 - FECHAR CONEXÃO
        # --------------------------------------------------

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# GET - BUSCAR TÉCNICO POR ID
# ==========================================================

def buscar_tecnico_por_id(tecnico_id: int):
    """
    Busca um técnico específico através do ID.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor(
            dictionary=True
        )


        sql = """
            SELECT
                id,
                nome,
                email,
                especialidade,
                nivel,
                disponivel,
                ativo,
                data_cadastro
            FROM tecnicos
            WHERE id = %s;
        """


        # %s representa o parâmetro que será
        # enviado separadamente para o MySQL.

        cursor.execute(
            sql,
            (tecnico_id,)
        )


        # fetchone() recupera apenas um registro.

        tecnico = cursor.fetchone()

        return tecnico


    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# POST - CADASTRAR TÉCNICO
# ==========================================================

def criar_tecnico(tecnico):
    """
    Cadastra um novo técnico no banco de dados.

    Retorna o ID criado pelo AUTO_INCREMENT.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        sql = """
            INSERT INTO tecnicos
            (
                nome,
                email,
                especialidade,
                nivel,
                disponivel,
                ativo
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
        """


        valores = (
            tecnico.nome,
            tecnico.email,
            tecnico.especialidade,
            tecnico.nivel,
            tecnico.disponivel,
            tecnico.ativo
        )


        cursor.execute(
            sql,
            valores
        )


        # --------------------------------------------------
        # COMMIT
        # --------------------------------------------------

        # INSERT altera dados.
        #
        # Por isso precisamos confirmar a transação.

        conexao.commit()


        # --------------------------------------------------
        # ID GERADO
        # --------------------------------------------------

        tecnico_id = cursor.lastrowid

        return tecnico_id


    except Exception:

        # Se ocorrer qualquer problema durante o INSERT,
        # desfazemos a transação.

        if conexao:
            conexao.rollback()

        raise


    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# PUT - ATUALIZAR TÉCNICO
# ==========================================================

def atualizar_tecnico(
    tecnico_id: int,
    tecnico
):
    """
    Atualiza somente os campos enviados pela API.

    Exemplo:

    Se o usuário enviar apenas:

    {
        "disponivel": false
    }

    somente a coluna disponivel será alterada.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        # --------------------------------------------------
        # TRANSFORMAR SCHEMA EM DICIONÁRIO
        # --------------------------------------------------

        # exclude_unset=True:
        #
        # considera somente os campos efetivamente
        # enviados pelo usuário através da API.

        dados = tecnico.model_dump(
            exclude_unset=True
        )


        # --------------------------------------------------
        # VERIFICAR SE EXISTEM CAMPOS
        # --------------------------------------------------

        if not dados:

            return 0


        # --------------------------------------------------
        # CONSTRUIR UPDATE DINAMICAMENTE
        # --------------------------------------------------

        campos = []

        valores = []


        for campo, valor in dados.items():

            campos.append(
                f"{campo} = %s"
            )

            valores.append(
                valor
            )


        # O ID será utilizado no WHERE.

        valores.append(
            tecnico_id
        )


        # --------------------------------------------------
        # MONTAR SQL
        # --------------------------------------------------

        sql = f"""
            UPDATE tecnicos
            SET {", ".join(campos)}
            WHERE id = %s;
        """


        # --------------------------------------------------
        # EXECUTAR UPDATE
        # --------------------------------------------------

        cursor.execute(
            sql,
            tuple(valores)
        )


        conexao.commit()


        # rowcount informa quantas linhas foram alteradas.

        return cursor.rowcount


    except Exception:

        if conexao:
            conexao.rollback()

        raise


    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# DELETE - EXCLUIR TÉCNICO
# ==========================================================

def excluir_tecnico(tecnico_id: int):
    """
    Exclui um técnico através do ID.

    Atenção:

    A exclusão poderá ser impedida pelo MySQL
    caso existam registros relacionados através
    de chaves estrangeiras.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        sql = """
            DELETE FROM tecnicos
            WHERE id = %s;
        """


        cursor.execute(
            sql,
            (tecnico_id,)
        )


        conexao.commit()


        return cursor.rowcount


    except Exception:

        if conexao:
            conexao.rollback()

        raise


    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()