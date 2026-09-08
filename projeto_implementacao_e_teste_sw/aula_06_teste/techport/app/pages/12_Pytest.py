import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.utils.test_runner import (
    python_command,
    run_command,
    show_pytest_summary,
)


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="TechPort | pytest",
    page_icon="🧪",
    layout="wide",
)

st.title("🧪 2. pytest — Testes automatizados")

st.write(
    "Executa os testes automatizados do projeto e apresenta "
    "individualmente os resultados encontrados."
)

st.code(
    "python -m pytest -vv",
    language="powershell",
)

st.info(
    "Use `-vv` para enxergar o nome de cada teste e seu resultado "
    "individual: PASSED, FAILED, ERROR ou SKIPPED."
)


# ==========================================================
# EXPLICAÇÃO DIDÁTICA
# ==========================================================

with st.expander("ℹ️ O que o pytest verifica?"):

    st.markdown(
        """
O **pytest** é uma ferramenta utilizada para criar e executar
testes automatizados em aplicações Python.

Enquanto ferramentas como Ruff, mypy e Bandit analisam o código
estaticamente, o pytest **executa os testes** para verificar se
o comportamento da aplicação corresponde ao resultado esperado.

Ele pode ser utilizado para diferentes níveis de teste, como:

- testes unitários;
- testes de integração;
- testes funcionais;
- testes de API;
- testes de banco de dados;
- testes de regressão;
- testes End-to-End (E2E).

### Fluxo da execução

`Código → Caso de Teste → pytest → Execução → Resultado`

O pytest ajuda a responder:

> O sistema está se comportando da forma que esperamos?

### Exemplo 1 — Teste simples

Imagine a seguinte função:

```python
def somar(a, b):
    return a + b
```

Podemos criar o teste:

```python
def test_somar():
    assert somar(2, 3) == 5
```

Ao executar o pytest, ele compara:

```text
Resultado obtido → 5
Resultado esperado → 5
```

Se forem iguais:

```text
PASSED
```

### Exemplo 2 — Teste que falha

Considere:

```python
def multiplicar(a, b):
    return a + b
```

E o teste:

```python
def test_multiplicar():
    assert multiplicar(2, 3) == 6
```

A função retorna:

```text
5
```

mas o teste esperava:

```text
6
```

O resultado será:

```text
FAILED
```

Isso significa:

> O teste foi executado, mas o comportamento encontrado
> foi diferente do comportamento esperado.

### Exemplo 3 — Testando exceções

Também é possível verificar se uma operação gera corretamente
uma exceção.

```python
import pytest

def dividir(a, b):
    return a / b

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
```

Nesse caso, o teste passa se a exceção esperada ocorrer.

### Como interpretar os resultados

O pytest pode apresentar diferentes estados:

| Resultado | Significado |
|---|---|
| `PASSED` | O teste executou e obteve o resultado esperado |
| `FAILED` | O teste executou, mas encontrou um resultado diferente |
| `ERROR` | O teste não conseguiu ser executado corretamente |
| `SKIPPED` | O teste foi ignorado intencionalmente |

### Diferença entre FAILED e ERROR

Essa diferença é muito importante.

#### FAILED

```text
Testei
↓
O código executou
↓
O resultado foi diferente do esperado
```

Exemplo:

```python
assert 2 + 2 == 5
```

#### ERROR

```text
Tentei testar
↓
Algo impediu a execução do teste
↓
O teste não conseguiu chegar à validação
```

Pode ocorrer por:

- erro de importação;
- biblioteca ausente;
- banco indisponível;
- fixture quebrada;
- configuração incorreta;
- exceção inesperada durante a preparação.

### O que significa `assert`?

O `assert` representa uma expectativa do teste.

Por exemplo:

```python
assert usuario.nome == "Rodolfo"
```

Estamos dizendo:

> Eu espero que `usuario.nome` seja igual a `"Rodolfo"`.

Se a condição for verdadeira:

```text
PASSED
```

Se for falsa:

```text
FAILED
```

### Testes unitários

Testes unitários verificam pequenas unidades do sistema
de forma isolada.

Exemplo:

```python
def calcular_desconto(valor):
    return valor * 0.10

def test_calcular_desconto():
    assert calcular_desconto(100) == 10
```

O objetivo é testar uma função, método ou regra específica.

### Testes E2E

E2E significa:

### End-to-End

Nesse tipo de teste verificamos um fluxo mais completo
da aplicação.

Exemplo:

```text
Usuário
↓
Interface
↓
API
↓
Service
↓
Repository
↓
Banco de Dados
↓
Resposta
```

O teste procura validar o comportamento do sistema
de ponta a ponta.

### Marcadores do pytest

Neste laboratório você pode selecionar:

- **Todos os testes**
- **Somente unitários**
- **Somente E2E**

Isso utiliza os marcadores do pytest.

Por exemplo:

```python
import pytest

@pytest.mark.unit
def test_somar():
    assert 2 + 2 == 4
```

Para executar somente testes marcados como `unit`:

```powershell
python -m pytest -vv -m unit
```

Para executar somente os testes `e2e`:

```powershell
python -m pytest -vv -m e2e
```

### Por que utilizar testes automatizados?

Testes automatizados ajudam a:

- detectar regressões;
- validar regras de negócio;
- reduzir testes manuais repetitivos;
- identificar problemas mais rapidamente;
- dar segurança durante refatorações;
- apoiar integração contínua;
- melhorar a confiabilidade do software.

⚠️ **Importante:** um teste que passa comprova apenas
que o cenário definido naquele teste produziu o resultado esperado.

Por isso, qualidade não depende apenas da quantidade de testes,
mas também da qualidade dos cenários escolhidos.
"""
    )


# ==========================================================
# SELEÇÃO DOS TESTES
# ==========================================================

st.subheader("🎯 Selecione o conjunto de testes")

mode = st.radio(
    "O que executar?",
    [
        "Todos os testes",
        "Somente unitários",
        "Somente E2E",
    ],
    horizontal=True,
)

args = [
    "-m",
    "pytest",
    "-vv",
]

if mode == "Somente unitários":
    args += [
        "-m",
        "unit",
    ]

elif mode == "Somente E2E":
    args += [
        "-m",
        "e2e",
    ]


# ==========================================================
# EXECUÇÃO DO PYTEST
# ==========================================================

if st.button(
    "▶ Executar pytest",
    type="primary",
    use_container_width=True,
):

    result = run_command(
        python_command(*args),
        "pytest",
    )

    st.subheader("📋 Interpretação do resultado")

    show_pytest_summary(result)


# ==========================================================
# LEITURA DIDÁTICA
# ==========================================================

st.divider()

st.subheader("📚 Leitura didática")

st.code(
    """PASSED  → testei e obtive o resultado esperado
FAILED  → testei e encontrei diferença
ERROR   → não consegui concluir o teste
SKIPPED → o teste foi ignorado intencionalmente""",
    language="text",
)

st.caption(
    "FAILED e ERROR representam situações diferentes: "
    "em FAILED o teste foi executado; em ERROR algo impediu "
    "que a validação fosse concluída."
)
