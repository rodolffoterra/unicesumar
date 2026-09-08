import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.utils.test_runner import (
    python_command,
    run_command,
)


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="TechPort | Cobertura",
    page_icon="📊",
    layout="wide",
)

st.title("📊 3. Cobertura de testes")

st.write(
    "Cobertura mostra quais partes do código foram exercitadas "
    "durante a execução dos testes."
)

st.code(
    "python -m pytest --cov=app --cov-report=term-missing",
    language="powershell",
)

st.info(
    "Coverage = medição de cobertura. "
    "Testes → execução do código → medição → linhas cobertas e não cobertas."
)

st.warning(
    "100% de cobertura não significa 100% de qualidade. "
    "Cobertura apenas mostra quais partes do código foram executadas pelos testes."
)


# ==========================================================
# EXPLICAÇÃO DIDÁTICA
# ==========================================================

with st.expander("ℹ️ O que a cobertura de testes verifica?"):

    st.markdown(
        """
A **cobertura de testes** mede quais partes do código da aplicação
foram executadas enquanto os testes estavam sendo realizados.

Neste projeto utilizamos:

- **pytest** para executar os testes;
- **pytest-cov** para medir a cobertura;
- **coverage.py** como mecanismo de medição utilizado pelo plugin.

O comando executado é:

```powershell
python -m pytest --cov=app --cov-report=term-missing
```

### O que esse comando significa?

| Parte do comando | Função |
|---|---|
| `python -m pytest` | Executa os testes com pytest |
| `--cov=app` | Mede a cobertura do pacote `app` |
| `--cov-report=term-missing` | Mostra no terminal as linhas que não foram executadas |

### O que a cobertura consegue mostrar?

A ferramenta pode indicar:

- quantidade de linhas existentes;
- quantidade de linhas executadas;
- linhas que não foram exercitadas;
- percentual de cobertura;
- arquivos com maior ou menor cobertura;
- trechos do sistema que precisam de novos testes.

### Fluxo da análise

`Testes → pytest → aplicação → pytest-cov → relatório de cobertura`

### Exemplo

Imagine o seguinte código:

```python
def calcular_desconto(valor, cliente_vip):
    if cliente_vip:
        return valor * 0.90

    return valor
```

E temos somente este teste:

```python
def test_cliente_vip():
    assert calcular_desconto(100, True) == 90
```

O teste executou o caminho:

```text
cliente_vip = True
```

Porém, o caminho:

```text
cliente_vip = False
```

não foi testado.

A cobertura ajuda a identificar que existe uma parte da função
que ainda não foi exercitada pelos testes.

### Como interpretar o relatório

Um resultado pode aparecer assim:

```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
app/services/usuario.py     40      5    88%   32-35, 48
app/main.py                 80     20    75%   50-60, 90-99
------------------------------------------------------
TOTAL                      120     25    79%
```

### Significado das colunas

| Coluna | Significado |
|---|---|
| `Name` | Arquivo analisado |
| `Stmts` | Quantidade de instruções |
| `Miss` | Instruções que não foram executadas |
| `Cover` | Percentual de cobertura |
| `Missing` | Linhas que não foram cobertas |

Nesse exemplo:

```text
app/services/usuario.py → 88% de cobertura
```

Isso significa que **88% das instruções medidas nesse arquivo
foram executadas durante os testes**.

### Cobertura alta significa software sem erros?

Não.

Um projeto pode apresentar:

```text
100% de cobertura
```

e ainda possuir:

- testes mal escritos;
- regras de negócio incorretas;
- asserts fracos;
- casos extremos não avaliados;
- problemas de segurança;
- problemas de desempenho;
- comportamentos incorretos.

### O objetivo da cobertura

A cobertura deve ser utilizada como **indicador** para ajudar
a equipe a encontrar regiões do sistema que estão pouco testadas.

Ela ajuda a responder:

> Quais partes do meu código ainda não foram exercitadas pelos testes?

⚠️ **Importante:** cobertura mede execução, não mede diretamente qualidade.
"""
    )


# ==========================================================
# EXECUÇÃO DA COBERTURA
# ==========================================================

if st.button(
    "▶ Executar cobertura",
    type="primary",
    use_container_width=True,
):

    result = run_command(
        python_command(
            "-m",
            "pytest",
            "--cov=app",
            "--cov-report=term-missing",
        ),
        "coverage",
    )

    # ======================================================
    # INTERPRETAÇÃO DO RESULTADO
    # ======================================================

    output = result.output or ""
    lower_output = output.lower()

    # O pytest pode retornar 1 porque um teste falhou e,
    # ainda assim, o pytest-cov produzir normalmente
    # o relatório de cobertura.
    coverage_ok = (
        "tests coverage" in lower_output
        or (
            "name" in lower_output
            and "stmts" in lower_output
            and "miss" in lower_output
            and "cover" in lower_output
            and "total" in lower_output
        )
    )

    if coverage_ok:

        st.success(
            "📊 Relatório de cobertura produzido com sucesso."
        )

        st.markdown("### 🧪 Situação dos testes")

        if result.returncode == 0:

            st.success(
                "✅ Todos os testes executados passaram."
            )

            st.info(
                """
O `pytest` terminou com **Exit Code 0**.

Isso significa que os testes executados produziram
os resultados esperados.

A cobertura apresentada no terminal indica quais partes
do código foram exercitadas durante esses testes.
"""
            )

        elif result.returncode == 1:

            st.warning(
                "⚠️ A cobertura foi calculada, porém existem "
                "testes que falharam."
            )

            st.info(
                """
O código de saída `1` pertence ao **pytest** e indica que
um ou mais testes apresentaram resultado diferente do esperado.

Isso **não significa que a cobertura falhou**.

```text
PYTEST
   ↓
EXECUTA OS TESTES
   ↓
ALGUM TESTE FALHA
   ↓
EXIT CODE 1

        +

PYTEST-COV
   ↓
OBSERVA O CÓDIGO EXECUTADO
   ↓
CALCULA A COBERTURA
   ↓
RELATÓRIO GERADO
```

Portanto, podemos ter ao mesmo tempo:

```text
TESTES FAILED
      +
COBERTURA CALCULADA
```
"""
            )

        elif result.returncode == 5:

            st.warning(
                "⚠️ O pytest não encontrou testes para executar."
            )

            st.info(
                """
No pytest, o **Exit Code 5** significa:

```text
Nenhum teste foi coletado.
```

Verifique se os arquivos estão dentro da pasta `tests`
e seguem nomes como:

```text
test_usuario.py
test_service.py
test_api.py
```

As funções de teste também devem começar com `test_`.
"""
            )

        else:

            st.error(
                "🚨 O pytest encontrou um problema durante "
                "a execução. Analise a saída do terminal acima."
            )

        st.divider()

        st.subheader("🎓 Interpretação didática")

        st.markdown(
            """
A cobertura e o resultado dos testes representam
**informações diferentes**.

```text
RESULTADO DOS TESTES
        ↓
O comportamento obtido
foi o esperado?

PASSED / FAILED
```

```text
COBERTURA
        ↓
Quanto do código foi
executado pelos testes?

0% ─────────────── 100%
```

Por isso:

> **Passar nos testes não significa possuir cobertura alta.**

E também:

> **Ter cobertura alta não significa que o software está correto.**

A cobertura deve ser utilizada como um **indicador**
para identificar regiões do sistema que ainda precisam
ser exercitadas por testes.
"""
        )

    else:

        st.error(
            "❌ Não foi possível identificar um relatório "
            "de cobertura na saída do comando."
        )

        st.info(
            """
Verifique principalmente se o `pytest-cov` está instalado.

Execute:

```powershell
python -m pip install pytest-cov
```

Depois confirme:

```powershell
python -m pytest --cov=app --cov-report=term-missing
```
"""
        )
