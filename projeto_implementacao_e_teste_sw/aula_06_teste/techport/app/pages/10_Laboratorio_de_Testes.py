import subprocess
import sys
from pathlib import Path

import streamlit as st


# ============================================================
# CONFIGURAÇÕES DO PROJETO
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


st.set_page_config(
    page_title="TechPort | Laboratório de Testes",
    page_icon="🧪",
    layout="wide",
)


# ============================================================
# FUNÇÕES
# ============================================================

def executar_comando(comando: list[str]) -> tuple[int, str]:
    """
    Executa um comando usando o mesmo Python que iniciou o Streamlit
    e retorna:
        - código de saída;
        - conteúdo produzido no terminal.
    """

    processo = subprocess.run(
        comando,
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    saida = processo.stdout

    if processo.stderr:
        saida += "\n" + processo.stderr

    return processo.returncode, saida


def localizar_testes() -> list[Path]:
    """
    Procura arquivos compatíveis com a convenção do pytest.
    """

    testes = []

    for padrao in ("test_*.py", "*_test.py"):
        testes.extend(ROOT_DIR.rglob(padrao))

    # Evita arquivos internos da própria .venv
    testes = [
        arquivo
        for arquivo in testes
        if ".venv" not in arquivo.parts
        and "__pycache__" not in arquivo.parts
    ]

    return sorted(set(testes))


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🧪 Laboratório de Testes — TechPort")

st.caption(
    "Projeto, Implementação e Teste de Software • "
    "Professor Rodolfo Terra"
)

st.info(
    "Nesta página vamos executar o pytest pelo próprio Streamlit "
    "e visualizar exatamente o que apareceria no terminal."
)


# ============================================================
# ETAPA 1 - AMBIENTE
# ============================================================

st.subheader("1️⃣ Ambiente utilizado")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Python utilizado pelo Streamlit**")
    st.code(sys.executable, language="text")

with col2:
    st.markdown("**Raiz do projeto**")
    st.code(str(ROOT_DIR), language="text")


if ".venv" in sys.executable:
    st.success("✅ O Streamlit está utilizando o Python da .venv.")
else:
    st.warning(
        "⚠️ O Streamlit não parece estar utilizando o Python da .venv."
    )


# ============================================================
# ETAPA 2 - DESCOBERTA DOS TESTES
# ============================================================

st.subheader("2️⃣ O pytest consegue encontrar testes?")

testes_encontrados = localizar_testes()

if testes_encontrados:

    st.success(
        f"✅ Foram encontrados {len(testes_encontrados)} "
        "arquivo(s) de teste."
    )

    with st.expander("📁 Ver arquivos encontrados"):
        for arquivo in testes_encontrados:
            st.code(
                str(arquivo.relative_to(ROOT_DIR)),
                language="text",
            )

else:

    st.error("❌ Nenhum arquivo de teste foi encontrado.")

    st.markdown(
        """
O pytest procura, por padrão, arquivos como:

```text
test_usuario.py
test_service.py
test_api.py
usuario_test.py
```

E funções como:

```python
def test_criar_usuario():
    ...
```

Se aparecer **collected 0 items**, significa que o pytest iniciou
corretamente, mas não encontrou testes para executar.
"""
    )


# ============================================================
# ETAPA 3 - COMANDO
# ============================================================

st.subheader("3️⃣ Comando que será executado")

comando_pytest = [
    sys.executable,
    "-m",
    "pytest",
    "-vv",
]

st.code(
    "python -m pytest -vv",
    language="powershell",
)


# ============================================================
# ETAPA 4 - EXECUÇÃO
# ============================================================

st.subheader("4️⃣ Executar os testes")

executar = st.button(
    "▶ Executar pytest",
    type="primary",
    use_container_width=True,
)


if executar:

    st.markdown("### 🖥️ Saída do terminal")

    with st.spinner("Executando pytest..."):

        codigo, saida = executar_comando(comando_pytest)

    st.code(
        saida if saida.strip() else "Nenhuma saída produzida.",
        language="text",
    )


    # ========================================================
    # INTERPRETAÇÃO
    # ========================================================

    st.markdown("### 📊 Interpretação do resultado")

    texto = saida.lower()

    if "collected 0 items" in texto or "no tests ran" in texto:

        st.warning(
            "⚠️ O pytest foi executado, mas nenhum teste foi encontrado."
        )

        st.markdown(
            """
**O que isso significa?**

```text
PYTEST
   ↓
INICIOU CORRETAMENTE
   ↓
PROCUROU TESTES
   ↓
NÃO ENCONTROU
   ↓
0 TESTES EXECUTADOS
```

Isso não é um `FAILED` de uma regra do sistema.

É um problema de **descoberta/organização dos testes**.
"""
        )

    elif "error" in texto and codigo != 0:

        st.error(
            "🚨 ERROR — O pytest encontrou um problema antes "
            "ou durante a execução dos testes."
        )

    elif "failed" in texto:

        st.error(
            "❌ FAILED — Pelo menos um teste executou, "
            "mas o resultado obtido foi diferente do esperado."
        )

    elif "passed" in texto and codigo == 0:

        st.success(
            "✅ PASSED — Os testes executados produziram "
            "os resultados esperados."
        )

    elif codigo == 0:

        st.success(
            "✅ O comando terminou sem erro."
        )

    else:

        st.error(
            f"❌ O comando terminou com código de saída {codigo}."
        )


# ============================================================
# EXPLICAÇÃO DIDÁTICA
# ============================================================

st.divider()

st.subheader("5️⃣ Como interpretar durante a aula")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success(
        "✅ PASSED\n\n"
        "O teste executou e o resultado foi o esperado."
    )

with c2:
    st.error(
        "❌ FAILED\n\n"
        "O teste executou, mas esperado e obtido foram diferentes."
    )

with c3:
    st.warning(
        "🚨 ERROR\n\n"
        "O teste não conseguiu ser preparado ou executado corretamente."
    )

with c4:
    st.info(
        "🔎 0 TESTS\n\n"
        "O pytest iniciou, mas não encontrou testes."
    )


st.divider()

st.subheader("6️⃣ Próximo passo")

st.markdown(
    """
Para começar a prática, crie a estrutura:

```text
tests/
└── unit/
    └── test_primeiro_teste.py
```

E dentro dela:

```python
def somar(a, b):
    return a + b


def test_somar():
    resultado = somar(2, 3)
    assert resultado == 5
```

Depois volte nesta página e clique novamente em:

**▶ Executar pytest**

O resultado deve mudar de:

```text
0 tests
```

para:

```text
PASSED
```
"""
)