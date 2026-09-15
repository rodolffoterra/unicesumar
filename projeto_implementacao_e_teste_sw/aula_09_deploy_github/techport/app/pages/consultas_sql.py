# ==========================================================
# IMPORTAÇÕES PADRÃO DO PYTHON
# ==========================================================

import sys
from pathlib import Path

import streamlit as st


# ==========================================================
# CONFIGURAÇÃO DO CAMINHO DO PROJETO
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT_DIR)
    )


# ==========================================================
# IMPORTAÇÃO DA CONEXÃO COM O BANCO
# ==========================================================

from app.database.connection import obter_conexao


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="TechPort - Consultas SQL",
    page_icon="🔎",
    layout="wide"
)


# ==========================================================
# CONSULTAS DIDÁTICAS
# ==========================================================

CONSULTAS = {

    "01 - Listar bancos disponíveis": """
SHOW DATABASES;
""",

    "02 - Selecionar banco TechPort": """
USE techport;
""",

    "03 - Mostrar banco em uso": """
SELECT DATABASE() AS banco_em_uso;
""",

    "04 - Listar tabelas": """
SHOW TABLES;
""",

    "05 - Estrutura da tabela usuários": """
DESCRIBE usuarios;
""",

    "06 - Estrutura da tabela chamados": """
DESCRIBE chamados;
""",

    "07 - Mostrar CREATE TABLE de chamados": """
SHOW CREATE TABLE chamados;
""",

    "08 - Volumetria de todas as tabelas": """
SELECT 'usuarios' AS tabela, COUNT(*) AS quantidade
FROM usuarios

UNION ALL

SELECT 'tecnicos', COUNT(*)
FROM tecnicos

UNION ALL

SELECT 'chamados', COUNT(*)
FROM chamados

UNION ALL

SELECT 'comentarios', COUNT(*)
FROM comentarios

UNION ALL

SELECT 'historico_chamados', COUNT(*)
FROM historico_chamados

UNION ALL

SELECT 'anexos', COUNT(*)
FROM anexos;
""",

    "09 - Total geral de registros": """
SELECT
    (SELECT COUNT(*) FROM usuarios)
  + (SELECT COUNT(*) FROM tecnicos)
  + (SELECT COUNT(*) FROM chamados)
  + (SELECT COUNT(*) FROM comentarios)
  + (SELECT COUNT(*) FROM historico_chamados)
  + (SELECT COUNT(*) FROM anexos)
    AS total_geral_registros;
""",

    "10 - Mostrar 10 usuários": """
SELECT *
FROM usuarios
LIMIT 10;
""",

    "11 - Colunas principais de usuários": """
SELECT
    id,
    nome,
    email,
    perfil,
    ativo,
    data_cadastro
FROM usuarios
LIMIT 20;
""",

    "12 - Mostrar 10 técnicos": """
SELECT
    id,
    nome,
    email,
    especialidade,
    nivel,
    disponivel,
    ativo
FROM tecnicos
LIMIT 10;
""",

    "13 - Mostrar 20 chamados": """
SELECT *
FROM chamados
LIMIT 20;
""",

    "14 - Usuários ativos": """
SELECT
    id,
    nome,
    email,
    perfil
FROM usuarios
WHERE ativo = TRUE
LIMIT 20;
""",

    "15 - Técnicos disponíveis": """
SELECT
    id,
    nome,
    especialidade,
    nivel
FROM tecnicos
WHERE disponivel = TRUE
  AND ativo = TRUE
LIMIT 20;
""",

    "16 - Chamados críticos": """
SELECT
    id,
    titulo,
    categoria,
    prioridade,
    status,
    data_abertura
FROM chamados
WHERE prioridade = 'critica'
LIMIT 20;
""",

    "17 - Chamados fechados": """
SELECT
    id,
    titulo,
    status,
    data_abertura,
    data_fechamento
FROM chamados
WHERE status = 'fechado'
LIMIT 20;
""",

    "18 - Chamados sem técnico": """
SELECT
    id,
    titulo,
    status,
    prioridade,
    tecnico_id
FROM chamados
WHERE tecnico_id IS NULL
LIMIT 20;
""",

    "19 - Prioridade alta ou crítica": """
SELECT
    id,
    titulo,
    prioridade,
    status
FROM chamados
WHERE prioridade IN ('alta', 'critica')
LIMIT 20;
""",

    "20 - Chamados mais recentes": """
SELECT
    id,
    titulo,
    status,
    prioridade,
    data_abertura
FROM chamados
ORDER BY data_abertura DESC
LIMIT 20;
""",

    "21 - Chamados mais antigos": """
SELECT
    id,
    titulo,
    status,
    prioridade,
    data_abertura
FROM chamados
ORDER BY data_abertura ASC
LIMIT 20;
""",

    "22 - Histórico mais recente": """
SELECT
    id,
    chamado_id,
    evento,
    status_anterior,
    status_novo,
    observacao,
    data_evento
FROM historico_chamados
ORDER BY data_evento DESC
LIMIT 20;
""",

    "23 - Categorias existentes": """
SELECT DISTINCT categoria
FROM chamados
ORDER BY categoria;
""",

    "24 - Status existentes": """
SELECT DISTINCT status
FROM chamados
ORDER BY status;
""",

    "25 - Prioridades existentes": """
SELECT DISTINCT prioridade
FROM chamados
ORDER BY prioridade;
""",

    "26 - Canais de abertura": """
SELECT DISTINCT canal_abertura
FROM chamados
ORDER BY canal_abertura;
""",

    "27 - Chamados por status": """
SELECT
    status,
    COUNT(*) AS quantidade_chamados
FROM chamados
GROUP BY status
ORDER BY quantidade_chamados DESC;
""",

    "28 - Chamados por prioridade": """
SELECT
    prioridade,
    COUNT(*) AS quantidade_chamados
FROM chamados
GROUP BY prioridade
ORDER BY quantidade_chamados DESC;
""",

    "29 - Chamados por categoria": """
SELECT
    categoria,
    COUNT(*) AS quantidade_chamados
FROM chamados
GROUP BY categoria
ORDER BY quantidade_chamados DESC;
""",

    "30 - Chamados por canal": """
SELECT
    canal_abertura,
    COUNT(*) AS quantidade_chamados
FROM chamados
GROUP BY canal_abertura
ORDER BY quantidade_chamados DESC;
""",

    "31 - Usuários por perfil": """
SELECT
    perfil,
    COUNT(*) AS quantidade_usuarios
FROM usuarios
GROUP BY perfil
ORDER BY quantidade_usuarios DESC;
""",

    "32 - Técnicos por especialidade": """
SELECT
    especialidade,
    COUNT(*) AS quantidade_tecnicos
FROM tecnicos
GROUP BY especialidade
ORDER BY quantidade_tecnicos DESC;
""",

    "33 - Intervalo de abertura dos chamados": """
SELECT
    MIN(data_abertura) AS primeira_abertura,
    MAX(data_abertura) AS ultima_abertura
FROM chamados;
""",

    "34 - Intervalo do histórico": """
SELECT
    MIN(data_evento) AS primeiro_evento,
    MAX(data_evento) AS ultimo_evento
FROM historico_chamados;
""",

    "35 - Chamados por mês": """
SELECT
    DATE_FORMAT(data_abertura, '%Y-%m') AS mes,
    COUNT(*) AS quantidade_chamados
FROM chamados
GROUP BY DATE_FORMAT(data_abertura, '%Y-%m')
ORDER BY mes;
""",

    "36 - Eventos do histórico por mês": """
SELECT
    DATE_FORMAT(data_evento, '%Y-%m') AS mes,
    COUNT(*) AS quantidade_eventos
FROM historico_chamados
GROUP BY DATE_FORMAT(data_evento, '%Y-%m')
ORDER BY mes;
""",

    "37 - Chamados dos últimos 30 dias": """
SELECT
    id,
    titulo,
    status,
    prioridade,
    data_abertura
FROM chamados
WHERE data_abertura >= DATE_SUB(NOW(), INTERVAL 30 DAY)
ORDER BY data_abertura DESC
LIMIT 20;
""",

    "38 - Chamados com usuários - INNER JOIN": """
SELECT
    c.id AS chamado_id,
    c.titulo,
    c.status,
    u.id AS usuario_id,
    u.nome AS usuario
FROM chamados AS c
INNER JOIN usuarios AS u
    ON u.id = c.usuario_id
LIMIT 20;
""",

    "39 - Chamados, usuários e técnicos": """
SELECT
    c.id AS chamado_id,
    c.titulo,
    c.status,
    c.prioridade,
    u.nome AS usuario,
    t.nome AS tecnico,
    c.data_abertura
FROM chamados AS c
INNER JOIN usuarios AS u
    ON u.id = c.usuario_id
LEFT JOIN tecnicos AS t
    ON t.id = c.tecnico_id
ORDER BY c.data_abertura DESC
LIMIT 20;
""",

    "40 - Técnico com COALESCE": """
SELECT
    c.id AS chamado_id,
    c.titulo,
    u.nome AS usuario,
    COALESCE(t.nome, 'Sem técnico atribuído') AS tecnico,
    c.status,
    c.prioridade
FROM chamados AS c
INNER JOIN usuarios AS u
    ON u.id = c.usuario_id
LEFT JOIN tecnicos AS t
    ON t.id = c.tecnico_id
LIMIT 20;
""",

    "41 - Usuários com mais chamados": """
SELECT
    u.id AS usuario_id,
    u.nome AS usuario,
    COUNT(c.id) AS total_chamados
FROM usuarios AS u
LEFT JOIN chamados AS c
    ON c.usuario_id = u.id
GROUP BY
    u.id,
    u.nome
ORDER BY total_chamados DESC
LIMIT 20;
""",

    "42 - Técnicos com mais chamados": """
SELECT
    t.id AS tecnico_id,
    t.nome AS tecnico,
    t.especialidade,
    COUNT(c.id) AS total_chamados
FROM tecnicos AS t
LEFT JOIN chamados AS c
    ON c.tecnico_id = t.id
GROUP BY
    t.id,
    t.nome,
    t.especialidade
ORDER BY total_chamados DESC
LIMIT 20;
""",

    "43 - Técnicos com mais de 30 chamados": """
SELECT
    t.id AS tecnico_id,
    t.nome AS tecnico,
    COUNT(c.id) AS total_chamados
FROM tecnicos AS t
INNER JOIN chamados AS c
    ON c.tecnico_id = t.id
GROUP BY
    t.id,
    t.nome
HAVING COUNT(c.id) > 30
ORDER BY total_chamados DESC;
""",

    "44 - Comentários e autores": """
SELECT
    co.id AS comentario_id,
    co.chamado_id,
    co.autor_tipo,
    COALESCE(u.nome, t.nome, 'Autor não identificado') AS autor,
    co.comentario,
    co.visibilidade,
    co.data_comentario
FROM comentarios AS co
LEFT JOIN usuarios AS u
    ON u.id = co.usuario_id
LEFT JOIN tecnicos AS t
    ON t.id = co.tecnico_id
ORDER BY co.data_comentario DESC
LIMIT 20;
""",

    "45 - Comentários por autor": """
SELECT
    autor_tipo,
    COUNT(*) AS quantidade_comentarios
FROM comentarios
GROUP BY autor_tipo
ORDER BY quantidade_comentarios DESC;
""",

    "46 - Comentários por visibilidade": """
SELECT
    visibilidade,
    COUNT(*) AS quantidade_comentarios
FROM comentarios
GROUP BY visibilidade
ORDER BY quantidade_comentarios DESC;
""",

    "47 - Histórico com técnico": """
SELECT
    h.id AS historico_id,
    h.chamado_id,
    h.evento,
    h.status_anterior,
    h.status_novo,
    h.prioridade_anterior,
    h.prioridade_nova,
    COALESCE(t.nome, 'Evento sem técnico') AS tecnico,
    h.data_evento
FROM historico_chamados AS h
LEFT JOIN tecnicos AS t
    ON t.id = h.tecnico_id
ORDER BY h.data_evento DESC
LIMIT 20;
""",

    "48 - Tipos de eventos": """
SELECT
    evento,
    COUNT(*) AS quantidade_eventos
FROM historico_chamados
GROUP BY evento
ORDER BY quantidade_eventos DESC;
""",

    "49 - Histórico de um chamado": """
SELECT
    h.id,
    h.evento,
    h.status_anterior,
    h.status_novo,
    h.prioridade_anterior,
    h.prioridade_nova,
    h.observacao,
    h.data_evento
FROM historico_chamados AS h
WHERE h.chamado_id = 1
ORDER BY h.data_evento;
""",

    "50 - Anexos com chamado": """
SELECT
    a.id AS anexo_id,
    a.nome_arquivo,
    a.tipo_mime,
    a.tamanho_bytes,
    c.id AS chamado_id,
    c.titulo,
    a.data_upload
FROM anexos AS a
INNER JOIN chamados AS c
    ON c.id = a.chamado_id
ORDER BY a.data_upload DESC
LIMIT 20;
""",

    "51 - Tamanho dos anexos em MB": """
SELECT
    id AS anexo_id,
    nome_arquivo,
    tipo_mime,
    ROUND(tamanho_bytes / 1024 / 1024, 2) AS tamanho_mb,
    data_upload
FROM anexos
ORDER BY tamanho_bytes DESC
LIMIT 20;
""",

    "52 - Anexos por tipo": """
SELECT
    tipo_mime,
    COUNT(*) AS quantidade_anexos
FROM anexos
GROUP BY tipo_mime
ORDER BY quantidade_anexos DESC;
""",

    "53 - Validar usuários inexistentes": """
SELECT c.*
FROM chamados AS c
LEFT JOIN usuarios AS u
    ON u.id = c.usuario_id
WHERE u.id IS NULL;
""",

    "54 - Validar chamados dos comentários": """
SELECT co.*
FROM comentarios AS co
LEFT JOIN chamados AS c
    ON c.id = co.chamado_id
WHERE c.id IS NULL;
""",

    "55 - Validar chamados dos anexos": """
SELECT a.*
FROM anexos AS a
LEFT JOIN chamados AS c
    ON c.id = a.chamado_id
WHERE c.id IS NULL;
""",

    "56 - Consulta completa para relatório": """
SELECT
    c.id AS chamado_id,
    c.titulo,
    c.categoria,
    c.status,
    c.prioridade,
    c.canal_abertura,
    u.nome AS usuario,
    u.email AS email_usuario,
    COALESCE(t.nome, 'Sem técnico atribuído') AS tecnico,
    t.especialidade,
    c.data_abertura,
    c.data_atualizacao,
    c.data_fechamento
FROM chamados AS c
INNER JOIN usuarios AS u
    ON u.id = c.usuario_id
LEFT JOIN tecnicos AS t
    ON t.id = c.tecnico_id
ORDER BY c.data_abertura DESC
LIMIT 30;
""",

    "57 - Resumo executivo": """
SELECT
    (SELECT COUNT(*) FROM usuarios) AS total_usuarios,
    (SELECT COUNT(*) FROM tecnicos) AS total_tecnicos,
    (SELECT COUNT(*) FROM chamados) AS total_chamados,
    (SELECT COUNT(*) FROM chamados WHERE status = 'aberto')
        AS chamados_abertos,
    (SELECT COUNT(*) FROM chamados WHERE prioridade = 'critica')
        AS chamados_criticos,
    (SELECT COUNT(*) FROM chamados WHERE tecnico_id IS NULL)
        AS chamados_sem_tecnico,
    (SELECT COUNT(*) FROM comentarios) AS total_comentarios,
    (SELECT COUNT(*) FROM historico_chamados) AS total_historicos,
    (SELECT COUNT(*) FROM anexos) AS total_anexos;
""",
}


# ==========================================================
# FUNÇÃO PARA RESTAURAR QUERY
# ==========================================================

def restaurar_query():
    """
    Restaura no editor SQL a consulta original
    atualmente selecionada.
    """

    consulta_atual = (
        st.session_state.consulta_selecionada
    )

    st.session_state.sql_editor = (
        CONSULTAS[
            consulta_atual
        ].strip()
    )


# ==========================================================
# CABEÇALHO
# ==========================================================

st.title(
    "🔎 Laboratório de Consultas SQL"
)

st.write(
    """
    Escolha uma consulta didática, analise o SQL,
    altere o código se desejar e execute diretamente
    no banco de dados TechPort.
    """
)

st.divider()


# ==========================================================
# 1 - SELEÇÃO DA CONSULTA
# ==========================================================

st.subheader(
    "1️⃣ Escolha uma pergunta"
)


consulta_selecionada = st.selectbox(
    "Consulta didática:",
    list(CONSULTAS.keys()),
    key="consulta_selecionada"
)


# ==========================================================
# ATUALIZAR EDITOR QUANDO TROCAR A CONSULTA
# ==========================================================

if (
    "consulta_anterior" not in st.session_state
    or st.session_state.consulta_anterior
    != consulta_selecionada
):

    st.session_state.sql_editor = (
        CONSULTAS[
            consulta_selecionada
        ].strip()
    )

    st.session_state.consulta_anterior = (
        consulta_selecionada
    )


st.divider()


# ==========================================================
# 2 - EDITOR SQL
# ==========================================================

st.subheader(
    "2️⃣ Consulta SQL"
)

st.write(
    """
    O campo abaixo é editável.

    Você pode utilizar a consulta sugerida
    ou escrever qualquer outra query SQL.
    """
)


query = st.text_area(
    "SQL:",
    key="sql_editor",
    height=300
)


# ==========================================================
# BOTÕES
# ==========================================================

col1, col2 = st.columns(2)


with col1:

    executar = st.button(
        "▶️ Executar Query",
        key="btn_executar_query",
        type="primary",
        use_container_width=True
    )


with col2:

    st.button(
        "🔄 Restaurar Query Original",
        key="btn_restaurar_query",
        use_container_width=True,
        on_click=restaurar_query
    )


st.divider()


# ==========================================================
# 3 - EXECUTAR QUERY
# ==========================================================

if executar:


    # ======================================================
    # VALIDAR QUERY
    # ======================================================

    if not query.strip():

        st.warning(
            "Digite uma consulta SQL."
        )

        st.stop()


    conexao = None
    cursor = None


    try:


        with st.spinner(
            "Executando consulta..."
        ):


            # ==================================================
            # ABRIR CONEXÃO
            # ==================================================

            conexao = obter_conexao()


            # ==================================================
            # CRIAR CURSOR
            # ==================================================

            cursor = conexao.cursor()


            # ==================================================
            # EXECUTAR QUERY
            # ==================================================

            cursor.execute(
                query
            )


            # ==================================================
            # QUERY COM RESULTADO
            # ==================================================

            if cursor.with_rows:


                registros = cursor.fetchall()


                colunas = [
                    coluna[0]
                    for coluna in cursor.description
                ]


                dados = [
                    dict(
                        zip(
                            colunas,
                            registro
                        )
                    )
                    for registro in registros
                ]


                st.success(
                    f"✅ Consulta executada com sucesso. "
                    f"{len(dados)} registro(s) retornado(s)."
                )


                if dados:

                    st.subheader(
                        "3️⃣ Resultado"
                    )


                    st.dataframe(
                        dados,
                        use_container_width=True,
                        hide_index=True
                    )


                else:

                    st.info(
                        "A consulta foi executada, "
                        "mas não retornou registros."
                    )


            # ==================================================
            # QUERY SEM RESULTADO
            # ==================================================

            else:


                conexao.commit()


                st.success(
                    "✅ Comando SQL executado com sucesso."
                )


                st.info(
                    f"Linhas afetadas: {cursor.rowcount}"
                )


    # ======================================================
    # ERRO
    # ======================================================

    except Exception as erro:

        st.error(
            "❌ Erro ao executar a consulta."
        )

        st.exception(
            erro
        )


    # ======================================================
    # FINALIZAÇÃO
    # ======================================================

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