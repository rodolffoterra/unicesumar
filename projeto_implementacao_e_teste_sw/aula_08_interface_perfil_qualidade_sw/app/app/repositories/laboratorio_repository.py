from app.database.connection import obter_conexao


def assumir_chamado(chamado_id: int, tecnico_id: int):
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, status, prioridade FROM chamados WHERE id = %s FOR UPDATE;",
            (chamado_id,),
        )
        chamado = cursor.fetchone()
        if not chamado:
            return None

        status_anterior = chamado["status"]
        cursor.execute(
            """
            UPDATE chamados
               SET tecnico_id = %s,
                   status = 'em_atendimento',
                   data_atualizacao = NOW()
             WHERE id = %s;
            """,
            (tecnico_id, chamado_id),
        )
        cursor.execute(
            """
            INSERT INTO historico_chamados
                (chamado_id, tecnico_id, evento, status_anterior, status_novo,
                 prioridade_anterior, prioridade_nova, observacao, data_evento)
            VALUES (%s, %s, 'CHAMADO_ASSUMIDO', %s, 'em_atendimento', %s, %s,
                    'Chamado assumido pelo técnico.', NOW());
            """,
            (
                chamado_id,
                tecnico_id,
                status_anterior,
                chamado["prioridade"],
                chamado["prioridade"],
            ),
        )
        conexao.commit()
        return {"id": chamado_id, "tecnico_id": tecnico_id, "status": "em_atendimento"}
    except Exception:
        if conexao:
            conexao.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def alterar_status(chamado_id: int, status: str, tecnico_id=None, observacao=""):
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, status, prioridade, tecnico_id FROM chamados WHERE id = %s FOR UPDATE;",
            (chamado_id,),
        )
        chamado = cursor.fetchone()
        if not chamado:
            return None

        tecnico_final = tecnico_id if tecnico_id is not None else chamado["tecnico_id"]
        data_fechamento_sql = "NOW()" if status.lower() in {"finalizado", "resolvido"} else "NULL"
        sql = f"""
            UPDATE chamados
               SET status = %s,
                   tecnico_id = %s,
                   data_atualizacao = NOW(),
                   data_fechamento = {data_fechamento_sql}
             WHERE id = %s;
        """
        cursor.execute(sql, (status, tecnico_final, chamado_id))
        cursor.execute(
            """
            INSERT INTO historico_chamados
                (chamado_id, tecnico_id, evento, status_anterior, status_novo,
                 prioridade_anterior, prioridade_nova, observacao, data_evento)
            VALUES (%s, %s, 'STATUS_ALTERADO', %s, %s, %s, %s, %s, NOW());
            """,
            (
                chamado_id,
                tecnico_final,
                chamado["status"],
                status,
                chamado["prioridade"],
                chamado["prioridade"],
                observacao or "Status atualizado pela interface do TechPort.",
            ),
        )
        conexao.commit()
        return {"id": chamado_id, "status": status, "tecnico_id": tecnico_final}
    except Exception:
        if conexao:
            conexao.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def criar_comentario(chamado_id: int, dados):
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id FROM chamados WHERE id = %s;",
            (chamado_id,),
        )
        if not cursor.fetchone():
            return None

        cursor.execute(
            """
            INSERT INTO comentarios
                (chamado_id, usuario_id, tecnico_id, autor_tipo, comentario,
                 visibilidade, data_comentario)
            VALUES (%s, %s, %s, %s, %s, %s, NOW());
            """,
            (
                chamado_id,
                dados.usuario_id,
                dados.tecnico_id,
                dados.autor_tipo,
                dados.comentario,
                dados.visibilidade,
            ),
        )
        comentario_id = cursor.lastrowid
        conexao.commit()
        return comentario_id
    except Exception:
        if conexao:
            conexao.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_comentarios(chamado_id: int):
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id, chamado_id, usuario_id, tecnico_id, autor_tipo,
                   comentario, visibilidade, data_comentario
              FROM comentarios
             WHERE chamado_id = %s
             ORDER BY data_comentario, id;
            """,
            (chamado_id,),
        )
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_historico(chamado_id: int):
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id, chamado_id, tecnico_id, evento, status_anterior, status_novo,
                   prioridade_anterior, prioridade_nova, observacao, data_evento
              FROM historico_chamados
             WHERE chamado_id = %s
             ORDER BY data_evento, id;
            """,
            (chamado_id,),
        )
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def obter_resumo_dashboard():
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) AS total FROM usuarios WHERE ativo = 1;")
        usuarios = cursor.fetchone()["total"]
        cursor.execute("SELECT COUNT(*) AS total FROM tecnicos WHERE ativo = 1;")
        tecnicos = cursor.fetchone()["total"]
        cursor.execute("SELECT COUNT(*) AS total FROM chamados;")
        chamados = cursor.fetchone()["total"]
        cursor.execute(
            """
            SELECT LOWER(status) AS status, COUNT(*) AS total
              FROM chamados
             GROUP BY LOWER(status);
            """
        )
        por_status = {r["status"]: r["total"] for r in cursor.fetchall()}
        cursor.execute(
            """
            SELECT categoria, COUNT(*) AS total
              FROM chamados
             GROUP BY categoria
             ORDER BY total DESC
             LIMIT 10;
            """
        )
        por_categoria = cursor.fetchall()
        return {
            "usuarios": usuarios,
            "tecnicos": tecnicos,
            "chamados": chamados,
            "por_status": por_status,
            "por_categoria": por_categoria,
        }
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
