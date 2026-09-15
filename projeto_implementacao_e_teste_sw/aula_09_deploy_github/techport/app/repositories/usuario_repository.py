from app.database.connection import obter_conexao


# ==========================================================
# GET - LISTAR TODOS OS USUÁRIOS
# ==========================================================

def listar_usuarios():
    """
    Retorna todos os usuários cadastrados.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor(
            dictionary=True
        )

        cursor.execute(
            """
            SELECT
                id,
                nome,
                email,
                perfil,
                ativo,
                data_cadastro
            FROM usuarios
            ORDER BY id;
            """
        )

        usuarios = cursor.fetchall()

        print(
            f"[GET USUÁRIOS] "
            f"{len(usuarios)} registro(s) encontrado(s)."
        )

        return usuarios

    except Exception as erro:

        print(
            f"[ERRO GET USUÁRIOS] {erro}"
        )

        raise

    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# GET - BUSCAR USUÁRIO POR ID
# ==========================================================

def buscar_usuario_por_id(
    usuario_id: int
):
    """
    Busca um usuário específico pelo ID.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor(
            dictionary=True
        )

        cursor.execute(
            """
            SELECT
                id,
                nome,
                email,
                perfil,
                ativo,
                data_cadastro
            FROM usuarios
            WHERE id = %s;
            """,
            (usuario_id,)
        )

        usuario = cursor.fetchone()

        if usuario:

            print(
                f"[GET USUÁRIO] "
                f"Usuário ID {usuario_id} encontrado."
            )

        else:

            print(
                f"[GET USUÁRIO] "
                f"Usuário ID {usuario_id} não encontrado."
            )

        return usuario

    except Exception as erro:

        print(
            f"[ERRO GET USUÁRIO] "
            f"ID {usuario_id}: {erro}"
        )

        raise

    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# POST - CRIAR USUÁRIO
# ==========================================================

def criar_usuario(usuario):

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()

        print("\n====================================")
        print("POST - CADASTRANDO USUÁRIO")
        print("====================================")

        print(f"Nome: {usuario.nome}")
        print(f"Email: {usuario.email}")
        print(f"Perfil: {usuario.perfil}")
        print(f"Ativo: {usuario.ativo}")

        cursor.execute(
            """
            INSERT INTO usuarios
            (
                nome,
                email,
                senha_hash,
                perfil,
                ativo,
                data_cadastro
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                NOW()
            );
            """,
            (
                usuario.nome,
                usuario.email,
                usuario.senha_hash,
                usuario.perfil,
                usuario.ativo
            )
        )

        usuario_id = cursor.lastrowid

        conexao.commit()

        print("------------------------------------")
        print("Usuário cadastrado com sucesso!")
        print(f"ID criado: {usuario_id}")
        print("COMMIT realizado.")
        print("====================================")

        return usuario_id

    except Exception as erro:

        if conexao:
            conexao.rollback()

        print("\n====================================")
        print("ERRO AO CADASTRAR USUÁRIO")
        print("====================================")
        print(f"Tipo: {type(erro).__name__}")
        print(f"Erro: {erro}")
        print("ROLLBACK realizado.")
        print("====================================")

        raise

    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()

# ==========================================================
# PUT - ATUALIZAR USUÁRIO
# ==========================================================

def atualizar_usuario(
    usuario_id: int,
    usuario
):
    """
    Atualiza somente os campos enviados pela API.

    Exemplo:

    {
        "nome": "Novo Nome",
        "ativo": false
    }

    Somente esses campos serão modificados.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        # ==================================================
        # RECUPERAR SOMENTE CAMPOS ENVIADOS
        # ==================================================

        dados = usuario.model_dump(
            exclude_unset=True
        )


        if not dados:

            print(
                f"[PUT USUÁRIO] "
                f"Nenhum campo informado para ID {usuario_id}."
            )

            return 0


        # ==================================================
        # MONTAR UPDATE DINÂMICO
        # ==================================================

        campos = []

        valores = []


        for campo, valor in dados.items():

            campos.append(
                f"{campo} = %s"
            )

            valores.append(
                valor
            )


        valores.append(
            usuario_id
        )


        sql = f"""
            UPDATE usuarios
            SET {", ".join(campos)}
            WHERE id = %s;
        """


        print(
            f"[PUT USUÁRIO] "
            f"Atualizando usuário ID {usuario_id}."
        )

        print(
            f"[PUT USUÁRIO] "
            f"Campos recebidos: {list(dados.keys())}"
        )


        cursor.execute(
            sql,
            tuple(valores)
        )


        registros_afetados = cursor.rowcount


        # ==================================================
        # CONFIRMAR ALTERAÇÃO
        # ==================================================

        conexao.commit()


        print(
            f"[PUT USUÁRIO] "
            f"Registros afetados: {registros_afetados}"
        )

        print(
            "[PUT USUÁRIO] COMMIT realizado."
        )


        return registros_afetados

    except Exception as erro:

        if conexao:
            conexao.rollback()

        print(
            f"[ERRO PUT USUÁRIO] "
            f"ID {usuario_id}: {erro}"
        )

        print(
            "[PUT USUÁRIO] ROLLBACK realizado."
        )

        raise

    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


# ==========================================================
# DELETE - EXCLUIR USUÁRIO
# ==========================================================

def excluir_usuario(
    usuario_id: int
):
    """
    Exclui um usuário pelo ID.

    Retorna:
        1 -> usuário excluído;
        0 -> usuário não encontrado.

    A exclusão poderá ser bloqueada pelo MySQL
    caso existam registros relacionados por
    chave estrangeira.
    """

    conexao = None
    cursor = None

    try:

        conexao = obter_conexao()

        cursor = conexao.cursor()


        print(
            f"[DELETE USUÁRIO] "
            f"Tentando excluir usuário ID {usuario_id}."
        )


        cursor.execute(
            """
            DELETE FROM usuarios
            WHERE id = %s;
            """,
            (usuario_id,)
        )


        registros_afetados = cursor.rowcount


        # ==================================================
        # CONFIRMAR EXCLUSÃO
        # ==================================================

        conexao.commit()


        print(
            f"[DELETE USUÁRIO] "
            f"Registros excluídos: {registros_afetados}"
        )

        print(
            "[DELETE USUÁRIO] COMMIT realizado."
        )


        if registros_afetados == 0:

            print(
                f"[DELETE USUÁRIO] "
                f"ID {usuario_id} não encontrado."
            )

        else:

            print(
                f"[DELETE USUÁRIO] "
                f"Usuário ID {usuario_id} "
                f"excluído definitivamente do MySQL."
            )


        return registros_afetados

    except Exception as erro:

        if conexao:
            conexao.rollback()

        print(
            f"[ERRO DELETE USUÁRIO] "
            f"ID {usuario_id}: {erro}"
        )

        print(
            "[DELETE USUÁRIO] ROLLBACK realizado."
        )

        raise

    finally:

        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():

            conexao.close()

            print(
                "[USUÁRIO REPOSITORY] "
                "Conexão com MySQL encerrada."
            )