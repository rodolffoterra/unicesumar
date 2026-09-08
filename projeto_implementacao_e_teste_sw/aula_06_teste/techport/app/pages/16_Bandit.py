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
    show_command_result,
)


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="TechPort | Bandit",
    page_icon="🛡️",
    layout="wide",
)


# ============================================================
# FUNÇÕES AUXILIARES
# Compatíveis com Python 3.9
# ============================================================

def extrair_achados_bandit(output):
    """
    Extrai os achados principais do Bandit.

    Formato esperado:
    >> Issue: [BXXX:nome] descrição
       Severity: MEDIUM   Confidence: HIGH
       CWE: ...
       More Info: ...
       Location: app/arquivo.py:linha:coluna
    """

    achados = []

    blocos = re.split(
        r"\n>> Issue:\s*",
        output,
    )

    for bloco in blocos[1:]:
        linhas = bloco.splitlines()

        if not linhas:
            continue

        cabecalho = linhas[0].strip()

        codigo = "não informado"
        titulo = cabecalho

        match_codigo = re.match(
            r"\[([^\]]+)\]\s*(.*)",
            cabecalho,
        )

        if match_codigo:
            codigo = match_codigo.group(1).strip()
            titulo = match_codigo.group(2).strip()

        severidade = "não informada"
        confianca = "não informada"
        localizacao = "não informada"
        cwe = "não informado"
        mais_info = ""

        texto_bloco = "\n".join(linhas)

        match_sev = re.search(
            r"Severity:\s*([A-Z]+)",
            texto_bloco,
            flags=re.IGNORECASE,
        )
        if match_sev:
            severidade = match_sev.group(1).upper()

        match_conf = re.search(
            r"Confidence:\s*([A-Z]+)",
            texto_bloco,
            flags=re.IGNORECASE,
        )
        if match_conf:
            confianca = match_conf.group(1).upper()

        match_loc = re.search(
            r"Location:\s*(.+)",
            texto_bloco,
            flags=re.IGNORECASE,
        )
        if match_loc:
            localizacao = match_loc.group(1).strip()

        match_cwe = re.search(
            r"CWE:\s*(.+)",
            texto_bloco,
            flags=re.IGNORECASE,
        )
        if match_cwe:
            cwe = match_cwe.group(1).strip()

        match_info = re.search(
            r"More Info:\s*(.+)",
            texto_bloco,
            flags=re.IGNORECASE,
        )
        if match_info:
            mais_info = match_info.group(1).strip()

        achados.append(
            {
                "codigo": codigo,
                "titulo": titulo,
                "severidade": severidade,
                "confianca": confianca,
                "localizacao": localizacao,
                "cwe": cwe,
                "mais_info": mais_info,
                "detalhe": bloco.strip(),
            }
        )

    return achados


def extrair_resumo_bandit(output):
    """
    Extrai números do bloco 'Run metrics' do Bandit.
    """

    resultado = {
        "issues_low": 0,
        "issues_medium": 0,
        "issues_high": 0,
        "confidence_low": 0,
        "confidence_medium": 0,
        "confidence_high": 0,
        "lines_scanned": 0,
    }

    padroes = {
        "issues_low": r"Low:\s*(\d+)",
        "issues_medium": r"Medium:\s*(\d+)",
        "issues_high": r"High:\s*(\d+)",
    }

    # Tenta capturar apenas a seção "Total issues"
    match_total_issues = re.search(
        r"Total issues.*?(?=\n\s*Code scanned|\Z)",
        output,
        flags=re.IGNORECASE | re.DOTALL,
    )

    bloco_issues = match_total_issues.group(0) if match_total_issues else output

    for chave, padrao in padroes.items():
        match = re.search(
            padrao,
            bloco_issues,
            flags=re.IGNORECASE,
        )
        if match:
            resultado[chave] = int(match.group(1))

    # Linhas analisadas
    match_lines = re.search(
        r"Total lines of code:\s*(\d+)",
        output,
        flags=re.IGNORECASE,
    )
    if match_lines:
        resultado["lines_scanned"] = int(match_lines.group(1))

    # Confiança: tenta capturar na seção específica, quando presente
    match_conf_section = re.search(
        r"Total issues by confidence:.*?(?=\n\s*Files skipped|\Z)",
        output,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if match_conf_section:
        bloco_conf = match_conf_section.group(0)

        for chave, nivel in [
            ("confidence_low", "Low"),
            ("confidence_medium", "Medium"),
            ("confidence_high", "High"),
        ]:
            match = re.search(
                r"{}:\s*(\d+)".format(nivel),
                bloco_conf,
                flags=re.IGNORECASE,
            )
            if match:
                resultado[chave] = int(match.group(1))

    return resultado


def cor_severidade(severidade):
    nivel = severidade.upper()

    if nivel == "HIGH":
        return "high"

    if nivel == "MEDIUM":
        return "medium"

    return "low"


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🛡️ 6. Bandit — Segurança SAST")

st.write(
    "O Bandit examina o código Python sem executar a aplicação "
    "e procura padrões que podem representar riscos de segurança."
)

st.code(
    "python -m bandit -r app",
    language="powershell",
)

st.info(
    "SAST = Static Application Security Testing. "
    "Código → análise estática → possíveis problemas de segurança."
)


# ============================================================
# O QUE É SAST?
# ============================================================

st.subheader("🧠 O que é SAST?")

st.markdown(
    """
SAST significa **Static Application Security Testing**.

A ideia é analisar o código-fonte antes da aplicação precisar estar em execução.

```text
CÓDIGO-FONTE
     ↓
   BANDIT
     ↓
ANÁLISE ESTÁTICA
     ↓
PADRÕES DE RISCO
     ↓
ACHADOS DE SEGURANÇA
```

Isso ajuda a antecipar problemas durante o desenvolvimento.
"""
)


# ============================================================
# BANDIT NÃO É PENTEST
# ============================================================

st.subheader("⚖️ Bandit × Pentest")

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
### 🛡️ Bandit

Analisa o código.

Não precisa executar a aplicação.

Procura padrões potencialmente inseguros.

```text
CÓDIGO
  ↓
BANDIT
  ↓
ACHADO
```
"""
    )

with col2:
    st.info(
        """
### 🎯 Pentest

Avalia a aplicação em execução.

Simula tentativas de exploração.

```text
APLICAÇÃO
   ↓
ATAQUE CONTROLADO
   ↓
COMPORTAMENTO
```
"""
    )


# ============================================================
# O QUE O BANDIT PODE ENCONTRAR?
# ============================================================

st.subheader("🔎 O que o Bandit pode encontrar?")

st.markdown(
    """
Entre os padrões que podem gerar alertas estão:

- uso inseguro de `subprocess`;
- comandos de sistema com `shell=True`;
- senhas ou segredos escritos diretamente no código;
- uso de funções criptográficas fracas;
- geração insegura de números aleatórios;
- uso de `eval()` ou construções semelhantes;
- permissões inseguras;
- práticas que podem facilitar injeção ou execução indevida;
- configurações potencialmente perigosas.
"""
)


# ============================================================
# IMPORTANTE: ACHADO ≠ VULNERABILIDADE CONFIRMADA
# ============================================================

st.warning(
    "⚠️ Um achado do Bandit não significa automaticamente que existe "
    "uma vulnerabilidade explorável. O resultado precisa ser analisado "
    "no contexto do código."
)

st.code(
    """ACHADO
  ↓
POSSÍVEL RISCO
  ↓
ANÁLISE HUMANA
  ↓
CONFIRMAR OU DESCARTAR
""",
    language="text",
)


# ============================================================
# EXEMPLO DIDÁTICO
# ============================================================

st.subheader("📌 Exemplo — execução de comando")

st.code(
    """import subprocess

subprocess.run(
    comando,
    shell=True
)
""",
    language="python",
)

st.markdown(
    """
Dependendo do contexto, o Bandit pode sinalizar esse padrão porque
`Shell=True` pode aumentar o risco de injeção de comandos.

A ferramenta não sabe automaticamente se o valor de `comando`
é confiável ou controlado pelo usuário.

Por isso ela gera um **achado** para investigação.
"""
)


# ============================================================
# COMO LER UM ACHADO
# ============================================================

st.subheader("📖 Como ler um resultado do Bandit")

st.code(
    """>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified
   Severity: High   Confidence: High
   CWE: CWE-78
   Location: app/utils/exemplo.py:20:4
""",
    language="text",
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info(
        """
### Código

`B602`

Identifica a regra de segurança acionada.
"""
    )

with c2:
    st.info(
        """
### Severidade

`HIGH`

Representa o impacto potencial do problema.
"""
    )

with c3:
    st.info(
        """
### Confiança

`HIGH`

Indica o quanto a ferramenta está confiante naquele achado.
"""
    )

with c4:
    st.info(
        """
### Localização

`arquivo:linha`

Mostra onde investigar o problema.
"""
    )


# ============================================================
# SEVERIDADE
# ============================================================

st.subheader("🚦 O que significa Severidade?")

st.markdown(
    """
A **severidade** representa o impacto potencial do problema.

| Nível | Interpretação didática |
|---|---|
| `LOW` | impacto potencial baixo |
| `MEDIUM` | impacto potencial intermediário |
| `HIGH` | impacto potencial elevado |

Importante: severidade não substitui análise humana.
"""
)


# ============================================================
# CONFIANÇA
# ============================================================

st.subheader("🎯 O que significa Confidence?")

st.markdown(
    """
A **confiança** representa o quanto o Bandit acredita que o padrão encontrado
realmente corresponde ao problema descrito.

| Nível | Interpretação didática |
|---|---|
| `LOW` | pouca confiança |
| `MEDIUM` | confiança intermediária |
| `HIGH` | alta confiança |

Podemos ter, por exemplo:

```text
Severity: HIGH
Confidence: LOW
```

Isso significa:

> O impacto seria alto se o problema for real, mas a ferramenta possui
> baixa confiança de que aquele trecho realmente representa a vulnerabilidade.
"""
)


# ============================================================
# CWE
# ============================================================

st.subheader("🏷️ O que é CWE?")

st.markdown(
    """
CWE significa **Common Weakness Enumeration**.

É uma classificação padronizada de tipos de fraquezas de software.

Exemplo:

```text
CWE-78
```

pode estar associado a problemas relacionados à injeção de comandos.

O Bandit pode usar essa referência para ajudar o desenvolvedor a entender
qual categoria de fraqueza está relacionada ao achado.
"""
)


# ============================================================
# EXECUÇÃO
# ============================================================

st.divider()

st.subheader("💻 Executando no TechPort")

st.code(
    "python -m bandit -r app",
    language="powershell",
)

st.markdown(
    """
O comando significa:

```text
python
   ↓
executa o módulo

bandit
   ↓
ferramenta de análise

-r
   ↓
análise recursiva

app
   ↓
pasta analisada
```

O `-r` faz o Bandit percorrer as subpastas do projeto.
"""
)


# ============================================================
# FLUXO
# ============================================================

st.subheader("🔄 Fluxo da análise")

st.code(
    """PASTA app/
    ↓
BANDIT
    ↓
PERCORRE OS .PY
    ↓
APLICA REGRAS DE SEGURANÇA
    ↓
ENCONTROU PADRÃO DE RISCO?
      ↙               ↘
    NÃO                SIM
     ↓                  ↓
  SUCESSO            ACHADO
""",
    language="text",
)


# ============================================================
# EXECUTAR BANDIT
# ============================================================

st.divider()

st.subheader("▶ Executar análise de segurança")

if st.button(
    "▶ Executar Bandit",
    type="primary",
    use_container_width=True,
):

    result = run_command(
        python_command(
            "-m",
            "bandit",
            "-r",
            "app",
        ),
        "Bandit",
    )

    output = result.output

    achados = extrair_achados_bandit(output)
    resumo = extrair_resumo_bandit(output)

    st.subheader("🖥️ Resultado da análise")

    show_command_result(
        result,
        success_message=(
            "Bandit concluiu sem achados que alterem o código de saída."
        ),
        error_message=(
            "Bandit encontrou achados de segurança. "
            "Analise severidade, confiança, arquivo e linha."
        ),
    )

    # ========================================================
    # INDICADORES
    # ========================================================

    st.divider()
    st.subheader("📊 Resumo dos achados")

    total_achados = len(achados)

    high = sum(
        1 for item in achados
        if item["severidade"] == "HIGH"
    )

    medium = sum(
        1 for item in achados
        if item["severidade"] == "MEDIUM"
    )

    low = sum(
        1 for item in achados
        if item["severidade"] == "LOW"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🛡️ Total de achados",
        total_achados,
    )

    c2.metric(
        "🔴 High",
        high,
    )

    c3.metric(
        "🟡 Medium",
        medium,
    )

    c4.metric(
        "🟢 Low",
        low,
    )

    if total_achados == 0 and result.returncode == 0:
        st.success(
            "✅ Nenhum achado de segurança foi identificado "
            "pelas regras executadas pelo Bandit."
        )

    elif total_achados > 0:
        st.warning(
            "⚠️ O Bandit encontrou {} achado(s). "
            "Cada item deve ser analisado antes de concluir "
            "que existe uma vulnerabilidade real.".format(total_achados)
        )

    # ========================================================
    # ACHADOS INDIVIDUAIS
    # ========================================================

    if achados:
        st.divider()
        st.subheader("🔎 Achados encontrados")

        for indice, item in enumerate(achados, start=1):

            st.markdown(
                "### {}. `{}`".format(
                    indice,
                    item["codigo"],
                )
            )

            st.write(
                item["titulo"]
            )

            c1, c2, c3 = st.columns(3)

            with c1:
                if item["severidade"] == "HIGH":
                    st.error(
                        "**Severidade**\n\n{}".format(
                            item["severidade"]
                        )
                    )
                elif item["severidade"] == "MEDIUM":
                    st.warning(
                        "**Severidade**\n\n{}".format(
                            item["severidade"]
                        )
                    )
                else:
                    st.info(
                        "**Severidade**\n\n{}".format(
                            item["severidade"]
                        )
                    )

            with c2:
                st.info(
                    "**Confiança**\n\n{}".format(
                        item["confianca"]
                    )
                )

            with c3:
                st.info(
                    "**CWE**\n\n{}".format(
                        item["cwe"]
                    )
                )

            st.markdown(
                "**Localização:** `{}`".format(
                    item["localizacao"]
                )
            )

            st.markdown(
                """
**Como interpretar:**

```text
CÓDIGO
  ↓
qual regra foi acionada

SEVERIDADE
  ↓
impacto potencial

CONFIANÇA
  ↓
certeza da ferramenta

LOCALIZAÇÃO
  ↓
onde investigar no código
```
"""
            )

            with st.expander(
                "🔎 Ver detalhe completo do Bandit"
            ):
                st.code(
                    item["detalhe"],
                    language="text",
                )

            st.divider()


# ============================================================
# RESULTADO SEM ACHADOS
# ============================================================

st.divider()

st.subheader("✅ E se o Bandit não encontrar achados?")

st.code(
    """CÓDIGO
  ↓
BANDIT
  ↓
REGRAS EXECUTADAS
  ↓
0 ACHADOS RELEVANTES
  ↓
SUCESSO
""",
    language="text",
)

st.success(
    "Isso significa que nenhuma das regras executadas pelo Bandit "
    "identificou padrões que gerassem achados naquele momento."
)

st.warning(
    "Isso não prova que a aplicação é 100% segura. "
    "SAST é apenas uma das camadas de análise de segurança."
)


# ============================================================
# RESULTADO COM ACHADOS
# ============================================================

st.subheader("❌ E se o Bandit encontrar achados?")

st.code(
    """ACHADO
  ↓
VERIFICAR REGRA
  ↓
VER SEVERIDADE
  ↓
VER CONFIANÇA
  ↓
LOCALIZAR CÓDIGO
  ↓
ANALISAR CONTEXTO
  ↓
CORRIGIR OU JUSTIFICAR
""",
    language="text",
)


# ============================================================
# BANDIT E SHIFT LEFT
# ============================================================

st.divider()

st.subheader("⬅️ Bandit e Shift Left")

st.markdown(
    """
O Bandit ajuda a antecipar segurança para a fase de desenvolvimento.

```text
ESCREVER CÓDIGO
      ↓
    BANDIT
      ↓
ANÁLISE DE SEGURANÇA
      ↓
ACHADO
      ↓
INVESTIGAÇÃO
      ↓
CORREÇÃO
```

Isso é um exemplo direto de **Shift Left Security**.
"""
)


# ============================================================
# BANDIT X PIP-AUDIT X ZAP
# ============================================================

st.subheader("🧰 Bandit × pip-audit × OWASP ZAP")

st.markdown(
    """
As três ferramentas olham para problemas diferentes:

```text
BANDIT
   ↓
código Python
   ↓
SAST

PIP-AUDIT
   ↓
bibliotecas instaladas
   ↓
SCA

OWASP ZAP
   ↓
aplicação executando
   ↓
DAST
```

### Bandit
Procura padrões inseguros no código.

### pip-audit
Procura vulnerabilidades conhecidas nas dependências.

### OWASP ZAP
Analisa a aplicação enquanto ela está em execução.
"""
)


# ============================================================
# BANDIT NO TECHPORT
# ============================================================

st.divider()

st.subheader("🏗️ Onde o Bandit atua no TechPort?")

st.code(
    """TECHPORT
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
└── Bandit
      ↓
ANÁLISE RECURSIVA
      ↓
POSSÍVEIS PADRÕES INSEGUROS
""",
    language="text",
)


# ============================================================
# KIT DE QUALIDADE
# ============================================================

st.subheader("🧩 Onde o Bandit entra no nosso kit?")

st.code(
    """pytest
   ↓
comportamento

pytest-cov
   ↓
cobertura

Ruff
   ↓
qualidade do código

mypy
   ↓
tipagem

Bandit
   ↓
segurança do código

pip-audit
   ↓
segurança das dependências
""",
    language="text",
)


# ============================================================
# RESUMO
# ============================================================

st.divider()

st.subheader("📘 Resumo para memorizar")

st.code(
    """BANDIT
   ↓
SAST
   ↓
ANÁLISE ESTÁTICA
   ↓
NÃO PRECISA EXECUTAR A APLICAÇÃO
   ↓
PROCURA PADRÕES DE RISCO
   ↓
ACHADO
   ↓
SEVERIDADE + CONFIANÇA + LOCALIZAÇÃO
""",
    language="text",
)

st.markdown(
    """
**Bandit**  
Ferramenta de análise estática de segurança para código Python.

**SAST**  
Static Application Security Testing.

**Severidade**  
Impacto potencial do problema.

**Confiança**  
Quanto a ferramenta acredita que o achado corresponde ao problema descrito.

**CWE**  
Classificação padronizada de fraquezas de software.

**Achado**  
Um padrão que merece investigação. Não é automaticamente uma vulnerabilidade confirmada.

**Shift Left Security**  
Trazer atividades de segurança para fases mais iniciais do desenvolvimento.
"""
)

st.success(
    "🛡️ O objetivo do Bandit é ajudar a identificar riscos de segurança "
    "o mais cedo possível no ciclo de desenvolvimento."
)
