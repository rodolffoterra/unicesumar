import sys
from pathlib import Path

import streamlit as st


# ============================================================
# CAMINHO RAIZ DO PROJETO
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


# ============================================================
# IMPORTS DO PROJETO
# ============================================================

from app.utils.test_runner import (
    python_command,
    run_command,
    show_pytest_summary,
)


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="TechPort | pytest",
    page_icon="🧪",
    layout="wide",
)

st.title("🧪 2. pytest — Testes automatizados")

st.write(
    "Execute os testes de forma individual e acompanhe "
    "exatamente o resultado produzido pelo pytest."
)


# ============================================================
# EXPLICAÇÃO
# ============================================================

st.code(
    "python -m pytest -vv",
    language="powershell",
)

st.info(
    "Use `-vv` para visualizar o nome de cada teste e seu resultado "
    "individual: PASSED, FAILED, ERROR, SKIPPED ou NO TESTS."
)


# ============================================================
# FUNÇÃO AUXILIAR
# ============================================================

def executar_teste(
    titulo: str,
    caminho_teste: str,
    descricao: str,
) -> None:
    """
    Executa um teste específico e mostra a interpretação
    apenas daquele resultado.
    """

    st.markdown(f"### {titulo}")
    st.caption(descricao)

    st.code(
        f"python -m pytest {caminho_teste} -vv -s",
        language="powershell",
    )

    if st.button(
        f"▶ Executar {titulo}",
        key=f"btn_{caminho_teste}",
        use_container_width=True,
    ):
        args = [
            "-m",
            "pytest",
            caminho_teste,
            "-vv",
            "-s",
        ]

        result = run_command(
            python_command(*args),
            titulo,
        )

        st.markdown("#### Interpretação")
        show_pytest_summary(result)


# ============================================================
# TESTES UNITÁRIOS
# ============================================================

st.header("1️⃣ Testes unitários")

st.write(
    "Os testes unitários verificam pequenas partes do código "
    "de maneira isolada."
)

st.markdown(
    """
A ideia é começar por testes simples e depois avançar para
regras reais do TechPort.
"""
)


# ------------------------------------------------------------
# TESTE UNITÁRIO 01
# ------------------------------------------------------------

executar_teste(
    titulo="Teste unitário — soma",
    caminho_teste=(
        "tests/unit/test_primeiro_teste.py::test_somar"
    ),
    descricao=(
        "Exemplo básico de Arrange, Act e Assert. "
        "Serve para mostrar um PASSED ou um FAILED simples."
    ),
)


st.divider()


# ------------------------------------------------------------
# TESTE UNITÁRIO 02
# ------------------------------------------------------------

executar_teste(
    titulo="Teste unitário — usuário service",
    caminho_teste=(
        "tests/unit/test_usuario_service.py"
    ),
    descricao=(
        "Executa os testes unitários relacionados ao serviço "
        "de usuários."
    ),
)


st.divider()


# ------------------------------------------------------------
# TESTE UNITÁRIO 03
# ------------------------------------------------------------

executar_teste(
    titulo="Teste unitário — técnico service",
    caminho_teste=(
        "tests/unit/test_tecnico_service.py"
    ),
    descricao=(
        "Executa os testes unitários relacionados ao serviço "
        "de técnicos."
    ),
)


st.divider()


# ------------------------------------------------------------
# TESTE UNITÁRIO 04
# ------------------------------------------------------------

executar_teste(
    titulo="Teste unitário — chamado service",
    caminho_teste=(
        "tests/unit/test_chamado_service.py"
    ),
    descricao=(
        "Executa os testes unitários relacionados ao serviço "
        "de chamados."
    ),
)


# ============================================================
# TESTES DE INTEGRAÇÃO COM MYSQL
# ============================================================

st.divider()

st.header("2️⃣ Testes de integração com MySQL")

st.write(
    "Aqui o teste deixa de ser isolado e passa a consultar "
    "o banco de dados real."
)


# ------------------------------------------------------------
# MYSQL JOIN
# ------------------------------------------------------------

executar_teste(
    titulo="MySQL — JOIN chamados da semana",
    caminho_teste=(
        "tests/integration/"
        "test_chamados_mysql.py::"
        "test_chamados_abertos_na_semana_com_usuario_e_tecnico"
    ),
    descricao=(
        "Executa JOIN entre chamados, usuários e técnicos "
        "para consultar registros da semana."
    ),
)


st.divider()


# ------------------------------------------------------------
# REGRA QUE DEVE PASSAR
# ------------------------------------------------------------

executar_teste(
    titulo="Regra de negócio — usuário válido",
    caminho_teste=(
        "tests/integration/"
        "test_chamados_mysql.py::"
        "test_todo_chamado_deve_possuir_usuario_valido"
    ),
    descricao=(
        "Valida a regra de que todo chamado deve possuir "
        "um usuário válido."
    ),
)


st.divider()


# ------------------------------------------------------------
# REGRA QUE PODE FALHAR
# ------------------------------------------------------------

executar_teste(
    titulo="Regra de negócio — chamado deve ter técnico",
    caminho_teste=(
        "tests/integration/"
        "test_chamados_mysql.py::"
        "test_todo_chamado_da_semana_deve_ter_tecnico"
    ),
    descricao=(
        "Regra proposital para demonstrar um FAILED quando "
        "existirem chamados da semana sem técnico."
    ),
)


st.divider()


# ------------------------------------------------------------
# LISTAGEM DOS REGISTROS QUE QUEBRAM A REGRA
# ------------------------------------------------------------

executar_teste(
    titulo="Diagnóstico — listar chamados sem técnico",
    caminho_teste=(
        "tests/integration/"
        "test_chamados_mysql.py::"
        "test_listar_chamados_da_semana_sem_tecnico"
    ),
    descricao=(
        "Lista exatamente quais chamados estão quebrando "
        "a regra de negócio."
    ),
)


st.divider()


# ------------------------------------------------------------
# PRIORIDADE
# ------------------------------------------------------------

executar_teste(
    titulo="Regra de negócio — prioridade válida",
    caminho_teste=(
        "tests/integration/"
        "test_chamados_mysql.py::"
        "test_prioridade_dos_chamados_deve_ser_valida"
    ),
    descricao=(
        "Verifica se os chamados possuem somente prioridades "
        "permitidas pela regra de negócio."
    ),
)


# ============================================================
# TESTE E2E
# ============================================================

st.divider()

st.header("3️⃣ Teste E2E")

st.write(
    "O E2E testa o fluxo de ponta a ponta, com a aplicação "
    "realmente em execução."
)

st.warning(
    "Antes de executar o E2E, confirme que a FastAPI está ativa "
    "em outro terminal."
)

st.code(
    "python -m uvicorn app.api.fastapi_app:app --reload",
    language="powershell",
)

st.code(
    '$env:TECHPORT_E2E_URL="http://127.0.0.1:8000"',
    language="powershell",
)

executar_teste(
    titulo="E2E — API em execução",
    caminho_teste=(
        "tests/e2e/test_api_em_execucao.py"
    ),
    descricao=(
        "Executa um teste real contra a API em execução."
    ),
)


# ============================================================
# EXECUTAR TODOS
# ============================================================

st.divider()

st.header("4️⃣ Executar todos os testes")

st.write(
    "Depois de analisar cada teste separadamente, "
    "execute a suíte completa."
)

st.code(
    "python -m pytest -vv -s",
    language="powershell",
)

if st.button(
    "▶ Executar todos os testes",
    type="primary",
    use_container_width=True,
):
    result = run_command(
        python_command(
            "-m",
            "pytest",
            "-vv",
            "-s",
        ),
        "Todos os testes",
    )

    st.subheader("Resumo geral")
    show_pytest_summary(result)


# ============================================================
# LEITURA DIDÁTICA
# ============================================================

st.divider()

st.subheader("📘 Leitura didática")

st.code(
    """NO TESTS → procurei testes, mas não encontrei

ERROR    → não consegui preparar/executar o teste

FAILED   → executei e encontrei diferença

PASSED   → executei e obtive o esperado

SKIPPED  → o teste existe, mas não foi executado""",
    language="text",
)
