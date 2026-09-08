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
    page_title="TechPort | Ruff",
    page_icon="🧹",
    layout="wide",
)

st.title("🧹 4. Ruff — Qualidade do código")

st.write(
    "Ruff analisa o código sem executar a aplicação e identifica "
    "problemas de estilo, qualidade e boas práticas."
)

st.code(
    "python -m ruff check .",
    language="powershell",
)

st.info(
    "Linting = análise estática do código. "
    "Código → regras de qualidade → Ruff → avisos e violações."
)


# ==========================================================
# EXPLICAÇÃO DIDÁTICA
# ==========================================================

with st.expander("ℹ️ O que o Ruff verifica?"):

    st.markdown(
        """
O **Ruff** é uma ferramenta de análise estática para código Python.

Ele examina os arquivos do projeto **sem executar a aplicação**
e identifica problemas relacionados à qualidade, padronização
e boas práticas de desenvolvimento.

Entre os principais pontos analisados estão:

- imports não utilizados;
- variáveis declaradas e não utilizadas;
- erros simples de sintaxe e organização;
- problemas de estilo;
- nomes inadequados ou inconsistentes;
- código redundante;
- comparações desnecessárias;
- problemas relacionados a boas práticas Python;
- regras inspiradas em ferramentas como Flake8, pycodestyle e Pyflakes.

Esse tipo de análise é conhecido como:

### Linting — Análise Estática de Qualidade

O objetivo é encontrar problemas no código **antes da execução**
e manter o projeto mais limpo, consistente e fácil de manter.

### Fluxo da análise

`Código Python → Ruff → Regras de Qualidade → Avisos e Violações`

### Exemplo 1 — Import não utilizado

```python
import os

print("TechPort")
```

Nesse exemplo, o módulo `os` foi importado,
mas não está sendo utilizado.

O Ruff pode identificar esse problema.

### Exemplo 2 — Variável não utilizada

```python
nome = "TechPort"
idade = 10

print(nome)
```

A variável `idade` foi criada,
mas nunca utilizada.

O Ruff pode apontar essa situação.

### Exemplo 3 — Comparação desnecessária

```python
if ativo == True:
    print("Ativo")
```

Uma forma mais adequada seria:

```python
if ativo:
    print("Ativo")
```

Ferramentas de linting ajudam a identificar padrões
que podem ser simplificados ou melhorados.

### Como interpretar o resultado

Quando encontra um problema, o Ruff normalmente apresenta:

- arquivo;
- linha;
- coluna;
- código da regra;
- descrição do problema.

Exemplo:

```text
app/main.py:10:1: F401 `os` imported but unused
```

Nesse exemplo:

- `app/main.py` → arquivo;
- `10` → linha;
- `1` → coluna;
- `F401` → código da regra;
- `imported but unused` → descrição.

### Alguns códigos comuns

| Código | Significado |
|---|---|
| `F401` | Import não utilizado |
| `F841` | Variável local não utilizada |
| `E501` | Linha muito longa |
| `E722` | Uso de `except` sem especificar exceção |
| `F821` | Nome utilizado sem estar definido |

⚠️ **Importante:** um aviso do Ruff não significa necessariamente
que a aplicação vai parar de funcionar.

Ele indica que existe um problema de qualidade,
organização ou boas práticas que deve ser analisado pelo desenvolvedor.

O Ruff ajuda a tornar o código:

- mais limpo;
- mais legível;
- mais padronizado;
- mais fácil de manter;
- menos propenso a erros simples.
"""
    )


# ==========================================================
# EXECUÇÃO DO RUFF
# ==========================================================

if st.button(
    "▶ Executar Ruff",
    type="primary",
    use_container_width=True,
):

    result = run_command(
        python_command("-m", "ruff", "check", "."),
        "Ruff",
    )

    show_tool_result(
        result,
        "✅ Ruff não encontrou violações bloqueantes.",
        "❌ Ruff encontrou problemas no código. "
        "Analise arquivo, linha, código da regra e descrição.",
    )
