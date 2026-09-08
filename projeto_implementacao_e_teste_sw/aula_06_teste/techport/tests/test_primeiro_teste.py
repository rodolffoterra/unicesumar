import pytest

from app.database.connection import obter_conexao


# ============================================================
# TESTE UNITÁRIO SIMPLES
# ============================================================

@pytest.mark.unit
def test_somar():
    # Arrange
    a = 2
    b = 3

    # Act
    resultado = a + b

    # Assert
    assert resultado == 5


# ============================================================
# FUNÇÃO AUXILIAR PARA CONSULTAS MYSQL
# ============================================================

def executar_query(sql: str):
    """
    Executa uma consulta SELECT no MySQL
    e retorna os registros como dicionários.
    """

    conexao = obter_conexao()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute(sql)
        resultados = cursor.fetchall()

        return resultados

    finally:
        cursor.close()

        if conexao.is_connected():
            conexao.close()


# ============================================================
# TESTE 01
# JOIN - CHAMADOS ABERTOS NA SEMANA
# ============================================================

@pytest.mark.integration
def test_chamados_abertos_na_semana_com_usuario_e_tecnico():
    """
    Verifica se conseguimos consultar os chamados da semana
    relacionando chamados, usuários e técnicos.
    """

    # Arrange
    sql = """
        SELECT
            c.id AS chamado_id,
            c.titulo,
            c.status,
            c.prioridade,
            c.data_abertura,

            u.id AS usuario_id,
            u.nome AS usuario_nome,

            t.id AS tecnico_id,
            t.nome AS tecnico_nome

        FROM chamados c

        INNER JOIN usuarios u
            ON u.id = c.usuario_id

        LEFT JOIN tecnicos t
            ON t.id = c.tecnico_id

        WHERE
            YEARWEEK(c.data_abertura, 1)
            =
            YEARWEEK(CURDATE(), 1)

        ORDER BY c.data_abertura DESC;
    """

    # Act
    resultados = executar_query(sql)

    print("\n")
    print("Chamados encontrados na semana:")
    print("--------------------------------")

    for chamado in resultados:
        print(
            chamado["chamado_id"],
            chamado["titulo"],
            chamado["usuario_nome"],
            chamado["tecnico_nome"],
        )

    # Assert
    assert isinstance(resultados, list)


# ============================================================
# TESTE 02
# REGRA DE NEGÓCIO CORRETA
# TODO CHAMADO DEVE POSSUIR USUÁRIO VÁLIDO
# ============================================================

@pytest.mark.integration
def test_todo_chamado_deve_possuir_usuario_valido():
    """
    Regra esperada:
    todo chamado deve possuir um usuário válido.
    """

    # Arrange
    sql = """
        SELECT
            COUNT(*) AS quantidade

        FROM chamados c

        LEFT JOIN usuarios u
            ON u.id = c.usuario_id

        WHERE u.id IS NULL;
    """

    # Act
    resultado = executar_query(sql)

    quantidade_invalidos = resultado[0]["quantidade"]

    print("\n")
    print(
        "Chamados com usuário inválido:",
        quantidade_invalidos,
    )

    # Assert
    assert quantidade_invalidos == 0, (
        f"Foram encontrados {quantidade_invalidos} "
        "chamado(s) sem usuário válido."
    )


# ============================================================
# TESTE 03
# REGRA PROPOSITAL PARA DEMONSTRAR FAIL
# TODO CHAMADO DA SEMANA DEVE TER TÉCNICO
# ============================================================

@pytest.mark.integration
def test_todo_chamado_da_semana_deve_ter_tecnico():
    """
    Regra utilizada para demonstração:

    todo chamado aberto nesta semana deveria possuir técnico.

    Se existirem chamados sem técnico, o teste falhará.
    """

    # Arrange
    sql = """
        SELECT
            COUNT(*) AS quantidade

        FROM chamados c

        WHERE
            YEARWEEK(c.data_abertura, 1)
            =
            YEARWEEK(CURDATE(), 1)

            AND c.tecnico_id IS NULL;
    """

    # Act
    resultado = executar_query(sql)

    chamados_sem_tecnico = resultado[0]["quantidade"]

    print("\n")
    print(
        "Chamados da semana sem técnico:",
        chamados_sem_tecnico,
    )

    # Assert
    assert chamados_sem_tecnico == 0, (
        f"Foram encontrados {chamados_sem_tecnico} "
        "chamado(s) sem técnico."
    )


# ============================================================
# TESTE 04
# LISTAR REGISTROS QUE QUEBRAM A REGRA
# ============================================================

@pytest.mark.integration
def test_listar_chamados_da_semana_sem_tecnico():
    """
    Lista os chamados da semana que não possuem técnico.

    Esse teste é útil para mostrar exatamente
    quais registros estão quebrando a regra.
    """

    # Arrange
    sql = """
        SELECT
            c.id,
            c.titulo,
            c.prioridade,
            c.status,
            c.data_abertura,

            u.nome AS usuario

        FROM chamados c

        INNER JOIN usuarios u
            ON u.id = c.usuario_id

        LEFT JOIN tecnicos t
            ON t.id = c.tecnico_id

        WHERE
            YEARWEEK(c.data_abertura, 1)
            =
            YEARWEEK(CURDATE(), 1)

            AND t.id IS NULL

        ORDER BY c.data_abertura DESC;
    """

    # Act
    resultados = executar_query(sql)

    print("\n")
    print("Chamados encontrados sem técnico:")
    print("--------------------------------")

    if not resultados:
        print("Nenhum chamado sem técnico encontrado.")

    for chamado in resultados:
        print(
            f"ID: {chamado['id']} | "
            f"Título: {chamado['titulo']} | "
            f"Usuário: {chamado['usuario']} | "
            f"Prioridade: {chamado['prioridade']} | "
            f"Status: {chamado['status']}"
        )

    # Assert
    assert len(resultados) == 0, (
        f"Foram encontrados {len(resultados)} "
        "chamado(s) da semana sem técnico."
    )


# ============================================================
# TESTE 05
# REGRA DE PRIORIDADE
# ============================================================

@pytest.mark.integration
def test_prioridade_dos_chamados_deve_ser_valida():
    """
    Verifica se todos os chamados possuem
    prioridades permitidas pela regra de negócio.
    """

    # Arrange
    sql = """
        SELECT
            COUNT(*) AS quantidade

        FROM chamados

        WHERE LOWER(prioridade) NOT IN (
            'baixa',
            'media',
            'alta',
            'critica'
        );
    """

    # Act
    resultado = executar_query(sql)

    invalidos = resultado[0]["quantidade"]

    print("\n")
    print(
        "Chamados com prioridade inválida:",
        invalidos,
    )

    # Assert
    assert invalidos == 0, (
        f"Foram encontrados {invalidos} "
        "chamado(s) com prioridade inválida."
    )