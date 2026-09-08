# ==========================================================
# IMPORTAÇÃO DA CONEXÃO
# ==========================================================

from app.database.connection import obter_conexao


# ==========================================================
# GET - LISTAR TODOS OS CHAMADOS
# ==========================================================

def listar_chamados():
    """
    Retorna todos os chamados cadastrados.
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
                usuario_id,
                tecnico_id,
                titulo,
                descricao,
                categoria,
                prioridade,
                status,
                canal_abertura,
                data_abertura,
                data_atualizacao,
                data_fechamento
            FROM chamados
            ORDER BY id;
        """


        cursor.execute(sql)


        chamados = cursor.fetchall()


        return chamados


    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# GET - BUSCAR CHAMADO POR ID
# ==========================================================

def buscar_chamado_por_id(
    chamado_id: int
):
    """
    Busca um chamado específico pelo ID.
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
                usuario_id,
                tecnico_id,
                titulo,
                descricao,
                categoria,
                prioridade,
                status,
                canal_abertura,
                data_abertura,
                data_atualizacao,
                data_fechamento
            FROM chamados
            WHERE id = %s;
        """


        cursor.execute(
            sql,
            (chamado_id,)
        )


        chamado = cursor.fetchone()


        return chamado


    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# POST - CADASTRAR CHAMADO
# ==========================================================

def criar_chamado(
    chamado
):
    """
    Cadastra um novo chamado.

    Retorna o ID criado pelo AUTO_INCREMENT.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        sql = """
            INSERT INTO chamados
            (
                usuario_id,
                tecnico_id,
                titulo,
                descricao,
                categoria,
                prioridade,
                status,
                canal_abertura,
                data_abertura,
                data_atualizacao
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                NOW(),
                NOW()
            );
        """


        valores = (
            chamado.usuario_id,
            chamado.tecnico_id,
            chamado.titulo,
            chamado.descricao,
            chamado.categoria,
            chamado.prioridade,
            chamado.status,
            chamado.canal_abertura
        )


        cursor.execute(
            sql,
            valores
        )


        conexao.commit()


        chamado_id = cursor.lastrowid


        return chamado_id


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
# PUT - ATUALIZAR CHAMADO
# ==========================================================

def atualizar_chamado(
    chamado_id: int,
    chamado
):
    """
    Atualiza somente os campos enviados
    através da API.

    Exemplo:

    {
        "status": "em_atendimento",
        "tecnico_id": 15
    }

    Somente esses campos serão alterados.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        # --------------------------------------------------
        # TRANSFORMAR O SCHEMA EM DICIONÁRIO
        # --------------------------------------------------

        dados = chamado.model_dump(
            exclude_unset=True
        )


        if not dados:
            return 0


        # --------------------------------------------------
        # CONSTRUIR UPDATE DINÂMICO
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


        # Sempre que houver alteração,
        # atualizamos também data_atualizacao.

        campos.append(
            "data_atualizacao = NOW()"
        )


        valores.append(
            chamado_id
        )


        sql = f"""
            UPDATE chamados
            SET {", ".join(campos)}
            WHERE id = %s;
        """


        cursor.execute(
            sql,
            tuple(valores)
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


# ==========================================================
# DELETE - EXCLUIR CHAMADO
# ==========================================================

def excluir_chamado(
    chamado_id: int
):
    """
    Exclui um chamado pelo ID.

    A exclusão pode ser bloqueada caso
    existam registros relacionados em:

    - comentarios;
    - historico_chamados;
    - anexos.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        sql = """
            DELETE FROM chamados
            WHERE id = %s;
        """


        cursor.execute(
            sql,
            (chamado_id,)
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