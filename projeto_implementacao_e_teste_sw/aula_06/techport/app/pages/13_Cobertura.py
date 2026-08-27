import re
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
)


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="TechPort | Cobertura",
    page_icon="📊",
    layout="wide",
)


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def extrair_resumo_pytest(output: str):
    """
    Extrai o resumo final do pytest sem contar ocorrências repetidas
    de PASSED/FAILED ao longo do terminal.
    """

    linhas = output.lower().splitlines()
    trecho_final = "\n".join(linhas[-30:])

    def contar(padrao: str) -> int:
        match = re.search(padrao, trecho_final)
        return int(match.group(1)) if match else 0

    passed = contar(r"(\d+)\s+passed")
    failed = contar(r"(\d+)\s+failed")
    errors = contar(r"(\d+)\s+errors?")
    skipped = contar(r"(\d+)\s+skipped")

    total = passed + failed + errors + skipped

    return {
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "skipped": skipped,
        "total": total,
    }


def extrair_tabela_cobertura(output: str):
    """
    Extrai as linhas do relatório de cobertura produzido pelo pytest-cov.

    Espera linhas como:
    app\\core\\config.py     13      0   100%
    """

    registros = []

    for linha in output.splitlines():
        linha = linha.rstrip()

        if not linha.startswith("app"):
            continue

        match = re.match(
            r"^(app[\\/].*?)\s+(\d+)\s+(\d+)\s+(\d+)%\s*(.*)$",
            linha,
        )

        if not match:
            continue

        arquivo = match.group(1)
        stmts = int(match.group(2))
        miss = int(match.group(3))
        cover = int(match.group(4))
        missing = match.group(5).strip()

        registros.append(
            {
                "arquivo": arquivo,
                "stmts": stmts,
                "miss": miss,
                "cover": cover,
                "missing": missing,
            }
        )

    return registros


def extrair_total_cobertura(output: str):
    """
    Extrai a linha TOTAL do relatório.

    Exemplo:
    TOTAL 1012 958 5%
    """

    match = re.search(
        r"^TOTAL\s+(\d+)\s+(\d+)\s+(\d+)%",
        output,
        flags=re.MULTILINE,
    )

    if not match:
        return {
            "stmts": 0,
            "miss": 0,
            "cover": 0,
        }

    return {
        "stmts": int(match.group(1)),
        "miss": int(match.group(2)),
        "cover": int(match.group(3)),
    }


def extrair_falhas_pytest(output: str):
    """
    Extrai somente os testes FAILED do short test summary info.
    """

    falhas = []

    match_summary = re.search(
        r"=+\s*short test summary info\s*=+(.*?)(?=={3,}|$)",
        output,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if not match_summary:
        return falhas

    bloco = match_summary.group(1)

    for linha in bloco.splitlines():
        linha = linha.strip()

        if not linha.startswith("FAILED "):
            continue

        conteudo = linha[len("FAILED "):]

        if " - " in conteudo:
            nodeid, mensagem = conteudo.split(" - ", 1)
        else:
            nodeid = conteudo
            mensagem = "Falha identificada pelo pytest."

        falhas.append(
            {
                "teste": nodeid.strip(),
                "mensagem": mensagem.strip(),
            }
        )

    return falhas


def explicar_faixa_cobertura(percentual: int):
    """
    Retorna um rótulo didático e uma explicação para a cobertura.
    """

    if percentual == 100:
        return (
            "Cobertura total",
            "Todas as linhas consideradas pelo coverage foram executadas pelos testes.",
        )

    if percentual >= 80:
        return (
            "Cobertura alta",
            "Grande parte do arquivo foi exercitada pelos testes, mas ainda existem linhas sem cobertura.",
        )

    if percentual >= 50:
        return (
            "Cobertura intermediária",
            "Uma parte relevante do arquivo foi testada, porém ainda existem vários caminhos sem execução.",
        )

    if percentual > 0:
        return (
            "Cobertura baixa",
            "Poucas linhas foram exercitadas pelos testes. O arquivo ainda precisa de mais cenários de teste.",
        )

    return (
        "Sem cobertura",
        "Nenhuma linha executável desse arquivo foi alcançada pela suíte de testes atual.",
    )


# ============================================================
# CABEÇALHO
# ============================================================

st.title("📊 3. Cobertura de testes")

st.write(
    "Esta página executa a suíte de testes com o `pytest-cov` e explica "
    "quanto do código do TechPort realmente foi exercitado pelos testes."
)

st.code(
    "python -m pytest --cov=app --cov-report=term-missing",
    language="powershell",
)

st.warning(
    "⚠️ Cobertura não mede se o teste está correto. "
    "Ela mede apenas se determinada linha do código foi executada durante os testes."
)


# ============================================================
# EXPLICAÇÃO CONCEITUAL
# ============================================================

st.subheader("🧠 O que significa cobertura?")

c1, c2 = st.columns(2)

with c1:
    st.markdown(
        """
**Cobertura responde à pergunta:**

> Quais partes do meu código foram executadas enquanto os testes rodavam?

Exemplo:

```text
100 linhas no arquivo
80 linhas executadas pelos testes
20 linhas não executadas

Cobertura = 80%
```
"""
    )

with c2:
    st.markdown(
        """
**Cobertura não responde:**

- se a regra de negócio está correta;
- se todos os cenários possíveis foram testados;
- se o sistema está livre de defeitos;
- se o teste possui boa qualidade.

Por isso:

```text
100% cobertura ≠ 100% qualidade
```
"""
    )


# ============================================================
# EXPLICAÇÃO DAS COLUNAS
# ============================================================

st.subheader("📚 Como ler o relatório")

st.markdown(
    """
O `pytest-cov` apresenta uma tabela parecida com:

```text
Name                         Stmts   Miss   Cover   Missing
app/core/config.py              13      0    100%
app/core/security.py            10      2     80%   12, 17
app/api/routes.py               93     93      0%   1-513
```
"""
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.info(
        "**Name**\n\n"
        "Arquivo Python que está sendo analisado."
    )

with col2:
    st.info(
        "**Stmts**\n\n"
        "Quantidade de instruções executáveis existentes no arquivo."
    )

with col3:
    st.info(
        "**Miss**\n\n"
        "Quantidade de instruções que os testes não executaram."
    )

with col4:
    st.info(
        "**Cover**\n\n"
        "Percentual das instruções que foram executadas."
    )

with col5:
    st.info(
        "**Missing**\n\n"
        "Linhas específicas do arquivo que não foram alcançadas pelos testes."
    )


# ============================================================
# EXECUÇÃO
# ============================================================

st.divider()

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
        "Coverage",
    )

    output = result.output

    resumo_testes = extrair_resumo_pytest(output)
    cobertura_total = extrair_total_cobertura(output)
    arquivos = extrair_tabela_cobertura(output)
    falhas = extrair_falhas_pytest(output)

    # ========================================================
    # RESULTADO DOS TESTES
    # ========================================================

    st.subheader("🧪 Resultado da execução dos testes")

    total_testes = resumo_testes["total"]
    passed = resumo_testes["passed"]
    failed = resumo_testes["failed"]
    errors = resumo_testes["errors"]

    taxa_sucesso = (
        (passed / total_testes) * 100
        if total_testes > 0
        else 0
    )

    t1, t2, t3, t4 = st.columns(4)

    t1.metric(
        "🧪 Total executado",
        total_testes,
    )

    t2.metric(
        "✅ Passaram",
        passed,
    )

    t3.metric(
        "❌ Falharam",
        failed,
    )

    t4.metric(
        "📈 Taxa de sucesso",
        f"{taxa_sucesso:.1f}%",
    )

    if failed > 0:
        st.error(
            f"❌ A suíte possui {failed} teste(s) com falha. "
            "Isso não impede o coverage de mostrar quais linhas foram executadas."
        )
    elif errors > 0:
        st.error(
            f"🚨 Foram encontrados {errors} erro(s) durante a execução/coleta."
        )
    elif total_testes > 0:
        st.success(
            "✅ Todos os testes executados passaram."
        )

    # ========================================================
    # RESUMO DA COBERTURA
    # ========================================================

    st.divider()
    st.subheader("📊 Cobertura geral do projeto")

    percentual_total = cobertura_total["cover"]
    stmts_total = cobertura_total["stmts"]
    miss_total = cobertura_total["miss"]
    executadas = max(stmts_total - miss_total, 0)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Instruções",
        stmts_total,
    )

    c2.metric(
        "✅ Executadas",
        executadas,
    )

    c3.metric(
        "❌ Não executadas",
        miss_total,
    )

    c4.metric(
        "📈 Cobertura",
        f"{percentual_total}%",
    )

    titulo_faixa, explicacao_faixa = explicar_faixa_cobertura(
        percentual_total
    )

    if percentual_total >= 80:
        st.success(
            f"**{titulo_faixa}: {percentual_total}%** — {explicacao_faixa}"
        )
    elif percentual_total >= 50:
        st.warning(
            f"**{titulo_faixa}: {percentual_total}%** — {explicacao_faixa}"
        )
    else:
        st.error(
            f"**{titulo_faixa}: {percentual_total}%** — {explicacao_faixa}"
        )

    st.markdown(
        f"""
### Como interpretar este total

```text
Instruções existentes:     {stmts_total}
Executadas pelos testes:   {executadas}
Não executadas:             {miss_total}
Cobertura geral:            {percentual_total}%
```

Isso significa que a suíte atual executou apenas parte do código existente
na pasta `app/`.
"""
    )

    # ========================================================
    # ARQUIVOS POR FAIXA
    # ========================================================

    st.divider()
    st.subheader("🗂️ Cobertura por arquivo")

    sem_cobertura = [
        item for item in arquivos
        if item["cover"] == 0
    ]

    parcial = [
        item for item in arquivos
        if 0 < item["cover"] < 100
    ]

    completa = [
        item for item in arquivos
        if item["cover"] == 100
    ]

    a1, a2, a3 = st.columns(3)

    a1.metric(
        "🔴 Arquivos com 0%",
        len(sem_cobertura),
    )

    a2.metric(
        "🟡 Cobertura parcial",
        len(parcial),
    )

    a3.metric(
        "🟢 Cobertura 100%",
        len(completa),
    )

    # --------------------------------------------------------
    # SEM COBERTURA
    # --------------------------------------------------------

    if sem_cobertura:
        with st.expander(
            f"🔴 Arquivos sem cobertura ({len(sem_cobertura)})",
            expanded=True,
        ):
            st.write(
                "Esses arquivos não tiveram nenhuma linha executável "
                "alcançada pelos testes atuais."
            )

            for item in sem_cobertura:
                st.markdown(
                    f"**`{item['arquivo']}`** — "
                    f"{item['stmts']} instruções, "
                    f"{item['miss']} não executadas."
                )

                if item["missing"]:
                    st.caption(
                        f"Linhas não cobertas: {item['missing']}"
                    )

    # --------------------------------------------------------
    # COBERTURA PARCIAL
    # --------------------------------------------------------

    if parcial:
        with st.expander(
            f"🟡 Arquivos com cobertura parcial ({len(parcial)})"
        ):
            st.write(
                "Esses arquivos foram parcialmente exercitados. "
                "Algumas funções ou caminhos ainda não foram testados."
            )

            for item in sorted(
                parcial,
                key=lambda x: int(x["cover"]),
            ):
                percentual = int(item["cover"])

                st.markdown(
                    f"**`{item['arquivo']}` — {percentual}%**"
                )

                st.progress(
                    percentual / 100
                )

                st.caption(
                    f"Stmts: {item['stmts']} | "
                    f"Miss: {item['miss']} | "
                    f"Missing: {item['missing'] or 'nenhuma linha informada'}"
                )

    # --------------------------------------------------------
    # COBERTURA COMPLETA
    # --------------------------------------------------------

    if completa:
        with st.expander(
            f"🟢 Arquivos com 100% de cobertura ({len(completa)})"
        ):
            st.write(
                "Todas as linhas executáveis desses arquivos foram "
                "alcançadas pelos testes."
            )

            for item in completa:
                st.success(
                    f"{item['arquivo']} — 100%"
                )

    # ========================================================
    # EXEMPLOS DIDÁTICOS DO RESULTADO
    # ========================================================

    st.divider()
    st.subheader("🎓 O que este relatório está ensinando?")

    st.markdown(
        """
### 1. Um arquivo com 100%

Exemplo:

```text
app/core/config.py     13     0     100%
```

Significa:

```text
13 instruções existentes
0 instruções perdidas
13 executadas
100% alcançadas pelos testes
```

Isso **não significa** que `config.py` está livre de defeitos.
Significa apenas que todas as instruções consideradas pelo coverage
foram executadas.

---

### 2. Um arquivo com cobertura parcial

Exemplo:

```text
app/core/security.py     10     2     80%     12, 17
```

Significa:

```text
10 instruções
8 executadas
2 não executadas
80% cobertura

linhas sem cobertura:
12 e 17
```

Agora o desenvolvedor sabe exatamente onde criar novos testes.

---

### 3. Um arquivo com 0%

Exemplo:

```text
app/api/routes.py     93     93     0%
```

Significa:

```text
93 instruções existentes
93 não executadas
0% cobertura
```

A suíte atual não entrou nas rotas da API.

Isso indica uma oportunidade para criar testes com:

```python
TestClient(app)
```

e testar os endpoints do FastAPI.
"""
    )

    # ========================================================
    # FALHAS DOS TESTES
    # ========================================================

    if falhas:
        st.divider()
        st.subheader("❌ Testes que falharam")

        st.write(
            "Essas falhas pertencem ao pytest. "
            "Elas representam regras ou resultados que não atenderam "
            "ao valor esperado."
        )

        for indice, falha in enumerate(
            falhas,
            start=1,
        ):
            st.markdown(
                f"### {indice}. `{falha['teste']}`"
            )

            st.error(
                falha["mensagem"]
            )

    # ========================================================
    # DIFERENÇA ENTRE FALHA E COBERTURA
    # ========================================================

    st.divider()
    st.subheader("⚖️ Falha de teste × Cobertura")

    d1, d2 = st.columns(2)

    with d1:
        st.error(
            """
**FAILED**

O teste executou uma regra e encontrou:

```text
resultado obtido
≠
resultado esperado
```

Exemplo:

```text
Esperado: 0 chamados sem técnico
Obtido:   9 chamados sem técnico
```
"""
        )

    with d2:
        st.info(
            """
**COVERAGE**

Responde apenas:

```text
Esta linha do código
foi executada pelo teste?
```

Exemplo:

```text
routes.py
0% coverage
```

Não significa necessariamente erro.
Significa que os testes atuais não passaram por esse arquivo.
"""
        )

    # ========================================================
    # PRÓXIMOS PASSOS
    # ========================================================

    st.divider()
    st.subheader("🚀 Como aumentar a cobertura do TechPort?")

    st.markdown(
        """
Com o relatório atual, o próximo passo é criar testes por camada:

```text
services/
    ↓
testes unitários + mocks

repositories/
    ↓
testes de integração com MySQL

api/routes.py
    ↓
TestClient do FastAPI

schemas/
    ↓
validação Pydantic

main.py / pages/
    ↓
testes funcionais ou E2E
```

A ideia não é simplesmente perseguir **100%**.

A ideia é aumentar a cobertura principalmente nas partes que representam:

- regras de negócio;
- validações;
- acesso a dados;
- endpoints;
- fluxos críticos;
- tratamento de erros.
"""
    )


# ============================================================
# RODAPÉ DIDÁTICO
# ============================================================

st.divider()

st.subheader("📘 Resumo para memorizar")

st.code(
    """Stmts   → quantas instruções o arquivo possui

Miss    → quantas instruções não foram executadas

Cover   → percentual executado pelos testes

Missing → quais linhas ainda não foram alcançadas

FAILED  → o teste executou, mas encontrou resultado diferente

PASSED  → o teste executou e obteve o resultado esperado

Coverage → mede alcance dos testes, não garante qualidade""",
    language="text",
)