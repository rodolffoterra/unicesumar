import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.utils.test_runner import (
    python_command,
    run_command,
    show_tool_result,
)


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="TechPort | mypy",
    page_icon="🔤",
    layout="wide",
)

st.title("🔤 5. mypy — Validação de tipos")

st.write(
    "mypy verifica se as anotações e os usos de tipos "
    "são coerentes antes da execução."
)

st.code(
    "python -m mypy app",
    language="powershell",
)

st.info(
    "Type Checking = verificação estática dos tipos. "
    "Código → anotações de tipo → análise → inconsistências."
)


# ==========================================================
# EXPLICAÇÃO DIDÁTICA
# ==========================================================

with st.expander("ℹ️ O que o mypy verifica?"):

    st.markdown(
        """
O **mypy** realiza uma análise estática dos tipos utilizados
no código Python.

Ele verifica se as **anotações de tipo** declaradas pelo
desenvolvedor estão sendo respeitadas durante o desenvolvimento.

Entre os principais pontos analisados estão:

- tipos dos parâmetros das funções;
- tipos dos valores retornados;
- atribuições entre variáveis de tipos incompatíveis;
- uso incorreto de `Optional`;
- passagem de argumentos incompatíveis;
- acesso a atributos inexistentes;
- incompatibilidades entre listas, dicionários e outros objetos;
- inconsistências entre classes e métodos.

Esse tipo de verificação é conhecido como:

### Static Type Checking — Verificação Estática de Tipos

O objetivo é identificar possíveis inconsistências **antes mesmo
da execução da aplicação**.

### Exemplo 1 — Argumento incompatível

Imagine a seguinte função:

```python
def calcular_total(valor: float) -> float:
    return valor
```

A função informa que espera receber um `float`.

Porém, se utilizarmos:

```python
calcular_total("100")
```

estamos enviando uma `str`.

O **mypy** pode identificar essa incompatibilidade durante
a análise do código.

### Exemplo 2 — Retorno incompatível

```python
def quantidade() -> int:
    return "dez"
```

A função declara retornar:

`int`

mas está retornando:

`str`

O mypy pode detectar essa inconsistência antes da execução.

### Fluxo da análise

`Código Python → Anotações de Tipo → mypy → Inconsistências`

### Tipos comuns em Python

| Tipo | Significado |
|---|---|
| `str` | Texto |
| `int` | Número inteiro |
| `float` | Número decimal |
| `bool` | Verdadeiro ou falso |
| `list[str]` | Lista de textos |
| `dict` | Dicionário |
| `Optional[str]` | Pode ser `str` ou `None` |

### Um erro importante — Optional

Por exemplo:

```python
senha: Optional[str]
```

significa que `senha` pode conter:

```text
str
OU
None
```

Se uma função aceitar somente:

```python
def descriptografar_senha(senha: str):
    ...
```

o mypy poderá alertar caso tentemos passar um `Optional[str]`.

### Como interpretar o resultado

Quando o mypy encontra uma inconsistência, normalmente apresenta:

- arquivo onde o problema foi encontrado;
- número da linha;
- descrição do problema;
- categoria do erro.

Exemplo:

```text
app/main.py:225: error: Argument 1 to "descriptografar_senha"
has incompatible type "Optional[str]"; expected "str" [arg-type]
```

Nesse caso, uma função esperava receber uma `str`, mas existe
a possibilidade de receber `None`.

⚠️ **Importante:** o mypy não executa o programa.

Ele analisa o código e suas anotações de tipo para encontrar
possíveis inconsistências antes que elas se transformem em
problemas durante a execução.
"""
    )


# ==========================================================
# EXECUÇÃO DO MYPY
# ==========================================================

if st.button(
    "▶ Executar mypy",
    type="primary",
    use_container_width=True,
):

    result = run_command(
        python_command("-m", "mypy", "app"),
        "mypy",
    )

    show_tool_result(
        result,
        "✅ mypy concluiu sem erros de tipagem.",
        "❌ mypy encontrou inconsistências de tipos.",
    )
