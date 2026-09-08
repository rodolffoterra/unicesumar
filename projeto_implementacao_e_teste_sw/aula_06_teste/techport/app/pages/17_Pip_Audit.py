import os
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
    page_title="TechPort | pip-audit",
    page_icon="📦",
    layout="wide",
)


# ============================================================
# FUNÇÕES AUXILIARES
# Compatíveis com Python 3.9
# ============================================================

def extrair_vulnerabilidades_pip_audit(output):
    """
    Extrai linhas tabulares comuns do pip-audit.

    Formato típico:
    Name      Version   ID              Fix Versions
    package   1.2.3     CVE-XXXX-XXXX   1.2.4
    """

    vulnerabilidades = []

    for linha in output.splitlines():
        linha_limpa = linha.strip()

        if not linha_limpa:
            continue

        if linha_limpa.lower().startswith("name "):
            continue

        if set(linha_limpa) <= set("- "):
            continue

        if not re.search(
            r"\b(CVE-\d{4}-\d+|GHSA-[A-Za-z0-9-]+|PYSEC-\d{4}-\d+)\b",
            linha_limpa,
            flags=re.IGNORECASE,
        ):
            continue

        partes = re.split(
            r"\s{2,}|\t+",
            linha_limpa,
        )

        if len(partes) < 3:
            partes = linha_limpa.split()

        nome = partes[0] if len(partes) > 0 else "não informado"
        versao = partes[1] if len(partes) > 1 else "não informada"
        identificador = partes[2] if len(partes) > 2 else "não informado"
        correcao = " ".join(partes[3:]) if len(partes) > 3 else "não informada"

        vulnerabilidades.append(
            {
                "pacote": nome,
                "versao": versao,
                "id": identificador,
                "correcao": correcao,
                "linha": linha_limpa,
            }
        )

    return vulnerabilidades


def extrair_resumo_pip_audit(output):
    """
    Extrai informações gerais do resultado do pip-audit.
    """

    resultado = {
        "vulnerabilidades": 0,
        "pacotes_afetados": 0,
        "sem_vulnerabilidades": False,
    }

    if re.search(
        r"No known vulnerabilities found",
        output,
        flags=re.IGNORECASE,
    ):
        resultado["sem_vulnerabilidades"] = True

    vulnerabilidades = extrair_vulnerabilidades_pip_audit(output)

    resultado["vulnerabilidades"] = len(vulnerabilidades)

    if vulnerabilidades:
        resultado["pacotes_afetados"] = len(
            set(
                item["pacote"]
                for item in vulnerabilidades
            )
        )

    return resultado



# ============================================================
# EXECUÇÃO SEGURA DO PIP-AUDIT NO WINDOWS
# ============================================================

def executar_pip_audit_utf8():
    """
    Executa o pip-audit forçando UTF-8 no subprocesso.

    Isso evita um problema comum no Windows quando o caminho do projeto
    contém caracteres como ç, ã, á etc. Algumas dependências internas
    do pip-audit podem tentar interpretar a saída do pip como UTF-8 e
    falhar quando o Windows utiliza outra codificação.
    """

    comando = python_command(
        "-m",
        "pip_audit",
    )

    ambiente = os.environ.copy()

    # Força o Python filho a trabalhar em UTF-8.
    ambiente["PYTHONUTF8"] = "1"
    ambiente["PYTHONIOENCODING"] = "utf-8"

    st.markdown("### 🖥️ pip-audit")

    st.code(
        "python -m pip_audit",
        language="powershell",
    )

    st.caption(
        "O Streamlit também força PYTHONUTF8=1 e "
        "PYTHONIOENCODING=utf-8 para reduzir problemas de codificação no Windows."
    )

    import subprocess

    try:
        with st.spinner("Executando pip-audit..."):
            processo = subprocess.run(
                comando,
                cwd=str(ROOT_DIR),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=ambiente,
                timeout=300,
            )

        stdout = processo.stdout or ""
        stderr = processo.stderr or ""

        partes = []

        if stdout.strip():
            partes.append(stdout.rstrip())

        if stderr.strip():
            partes.append(stderr.rstrip())

        output = "\n".join(partes)

        class ResultadoPipAudit:
            pass

        result = ResultadoPipAudit()
        result.command = comando
        result.returncode = processo.returncode
        result.stdout = stdout
        result.stderr = stderr
        result.output = output

        st.markdown("#### Saída do terminal")

        if output.strip():
            st.code(
                output,
                language="text",
            )
        else:
            st.info(
                "O comando não produziu saída no terminal."
            )

        return result

    except subprocess.TimeoutExpired:
        class ResultadoPipAudit:
            pass

        result = ResultadoPipAudit()
        result.command = comando
        result.returncode = -1
        result.stdout = ""
        result.stderr = "Timeout"
        result.output = (
            "O pip-audit excedeu o tempo máximo de execução."
        )

        st.error(
            "⏱️ O pip-audit excedeu o tempo máximo de execução."
        )

        return result


def classificar_resultado_pip_audit(result):
    """
    Distingue:
    - auditoria concluída sem vulnerabilidades;
    - auditoria concluída com vulnerabilidades;
    - erro técnico/ambiente;
    """

    output = (result.output or "").lower()

    if (
        "unicodedecodeerror" in output
        or "can't decode byte" in output
        or "invalid continuation byte" in output
    ):
        return "ERRO_CODIFICACAO"

    if (
        "traceback (most recent call last)" in output
        or "modulenotfounderror" in output
        or "importerror" in output
    ):
        return "ERRO_TECNICO"

    if result.returncode == 0:
        return "SEM_VULNERABILIDADES"

    return "COM_VULNERABILIDADES_OU_ERRO"


# ============================================================
# CABEÇALHO
# ============================================================

st.title("📦 7. pip-audit — Dependências vulneráveis")

st.write(
    "O pip-audit analisa as bibliotecas instaladas no ambiente Python "
    "e compara suas versões com bases públicas de vulnerabilidades conhecidas."
)

st.code(
    "python -m pip_audit",
    language="powershell",
)

st.info(
    "SCA = Software Composition Analysis. "
    "Dependências → versões instaladas → vulnerabilidades conhecidas."
)


# ============================================================
# O QUE É UMA DEPENDÊNCIA?
# ============================================================

st.subheader("🧠 Primeiro: o que é uma dependência?")

st.markdown(
    """
Uma dependência é uma biblioteca externa utilizada pelo projeto.

No TechPort, por exemplo:

```text
FastAPI
pytest
Streamlit
mysql-connector-python
cryptography
httpx
Bandit
mypy
Ruff
```

Essas bibliotecas ajudam a construir funcionalidades sem precisar
implementar tudo do zero.

Porém, elas também possuem versões e podem conter vulnerabilidades conhecidas.
"""
)


# ============================================================
# REQUIREMENTS
# ============================================================

st.subheader("📄 Onde essas dependências aparecem?")

st.markdown(
    """
Normalmente em arquivos como:

```text
requirements.txt
```

ou:

```text
pyproject.toml
```

Exemplo:

```text
fastapi
streamlit
pytest
httpx
cryptography
```

Quando instalamos:

```powershell
python -m pip install -r requirements.txt
```

essas bibliotecas passam a fazer parte do ambiente da aplicação.
"""
)


# ============================================================
# O QUE É SCA?
# ============================================================

st.subheader("🔎 O que é SCA?")

st.markdown(
    """
SCA significa **Software Composition Analysis**.

A ideia é verificar componentes de terceiros utilizados pelo software.

```text
PROJETO
   ↓
DEPENDÊNCIAS
   ↓
VERSÕES INSTALADAS
   ↓
PIP-AUDIT
   ↓
BASE DE VULNERABILIDADES
   ↓
COMPARAÇÃO
   ↓
ACHADOS
```

O foco aqui não é o nosso código diretamente.

O foco são as **bibliotecas das quais nosso código depende**.
"""
)


# ============================================================
# PIP-AUDIT X BANDIT
# ============================================================

st.subheader("⚖️ pip-audit × Bandit")

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
### 🛡️ Bandit

Analisa o **nosso código Python**.

```text
app/
 ↓
Bandit
 ↓
SAST
```

Pergunta:

> Existem padrões potencialmente inseguros no código?
"""
    )

with col2:
    st.info(
        """
### 📦 pip-audit

Analisa as **dependências instaladas**.

```text
bibliotecas
    ↓
pip-audit
    ↓
SCA
```

Pergunta:

> Alguma biblioteca possui vulnerabilidade conhecida?
"""
    )


# ============================================================
# EXEMPLO CONCEITUAL
# ============================================================

st.subheader("📌 Exemplo conceitual")

st.markdown(
    """
Imagine que o projeto utiliza:

```text
biblioteca-x==1.2.0
```

E existe uma vulnerabilidade conhecida nessa versão.

O pip-audit pode apresentar:

```text
Name          Version    ID               Fix Versions
biblioteca-x  1.2.0      CVE-2026-12345   1.2.1
```

A leitura seria:

```text
PACOTE
biblioteca-x

VERSÃO INSTALADA
1.2.0

VULNERABILIDADE
CVE-2026-12345

VERSÃO COM CORREÇÃO
1.2.1
```
"""
)


# ============================================================
# O QUE É CVE?
# ============================================================

st.subheader("🏷️ O que é CVE?")

st.markdown(
    """
CVE significa **Common Vulnerabilities and Exposures**.

É um identificador utilizado para catalogar vulnerabilidades publicamente conhecidas.

Exemplo:

```text
CVE-2026-12345
```

Esse identificador permite pesquisar informações como:

- descrição da vulnerabilidade;
- impacto;
- versões afetadas;
- versões corrigidas;
- referências técnicas.
"""
)


# ============================================================
# OUTROS IDENTIFICADORES
# ============================================================

st.subheader("🧾 Outros identificadores que podem aparecer")

st.markdown(
    """
Além de CVE, podem aparecer identificadores como:

```text
GHSA-xxxx-xxxx-xxxx
```

ou:

```text
PYSEC-2026-123
```

A ideia é a mesma:

> identificar publicamente um problema de segurança conhecido.
"""
)


# ============================================================
# VERSÃO INSTALADA X CORRIGIDA
# ============================================================

st.subheader("🎯 Versão instalada × versão corrigida")

col1, col2 = st.columns(2)

with col1:
    st.error(
        """
### Versão instalada

```text
1.2.0
```

É a versão que está atualmente no ambiente.

Se ela estiver listada como vulnerável, precisa ser analisada.
"""
    )

with col2:
    st.success(
        """
### Fix Versions

```text
1.2.1
```

É uma versão indicada como contendo correção para aquela vulnerabilidade.
"""
    )

st.warning(
    "Atualizar uma dependência deve ser feito com cuidado, porque uma nova versão "
    "também pode introduzir incompatibilidades. Segurança e compatibilidade precisam "
    "ser avaliadas juntas."
)


# ============================================================
# EXECUÇÃO
# ============================================================

st.divider()

st.subheader("💻 Executando no TechPort")

st.code(
    "python -m pip_audit",
    language="powershell",
)

st.markdown(
    """
Podemos ler esse comando assim:

```text
python
   ↓
executa o módulo

pip_audit
   ↓
ferramenta SCA

ambiente atual
   ↓
dependências instaladas
```

O pip-audit analisa as bibliotecas do mesmo ambiente Python
que está executando a página.
"""
)


# ============================================================
# FLUXO
# ============================================================

st.subheader("🔄 O que acontecerá?")

st.code(
    """AMBIENTE PYTHON
      ↓
PACOTES INSTALADOS
      ↓
VERSÕES
      ↓
PIP-AUDIT
      ↓
BASE DE VULNERABILIDADES
      ↓
COMPARAÇÃO
      ↓
VULNERABILIDADES CONHECIDAS?
      ↙                  ↘
    NÃO                   SIM
     ↓                     ↓
  SUCESSO               RELATÓRIO
""",
    language="text",
)


# ============================================================
# EXECUTAR PIP-AUDIT
# ============================================================

st.divider()

st.subheader("▶ Executar auditoria")

if st.button(
    "▶ Executar pip-audit",
    type="primary",
    use_container_width=True,
):

    result = executar_pip_audit_utf8()

    output = result.output

    vulnerabilidades = extrair_vulnerabilidades_pip_audit(output)
    resumo = extrair_resumo_pip_audit(output)
    classificacao = classificar_resultado_pip_audit(result)

    st.subheader("🖥️ Interpretação do resultado")

    if classificacao == "ERRO_CODIFICACAO":
        st.error(
            "🚨 ERRO DE CODIFICAÇÃO — O pip-audit não chegou a concluir "
            "a auditoria das dependências."
        )

        st.markdown(
            """
O erro indica um problema de **encoding no ambiente Windows**.

```text
pip-audit
   ↓
pip_api
   ↓
pip --version
   ↓
texto retornado pelo Windows
   ↓
tentativa de decodificar como UTF-8
   ↓
UnicodeDecodeError
```

### Importante

Neste caso:

```text
NÃO houve auditoria concluída
NÃO houve análise completa de CVEs
NÃO significa que vulnerabilidades foram encontradas
```

O problema é técnico, relacionado à forma como uma dependência
interna do `pip-audit` interpretou caracteres do ambiente.
"""
        )

        st.warning(
            "A página já está executando o comando com "
            "`PYTHONUTF8=1` e `PYTHONIOENCODING=utf-8`. "
            "Se o erro persistir, mova temporariamente o projeto "
            "para um caminho sem acentos, por exemplo `C:\\techport`."
        )

    elif classificacao == "ERRO_TECNICO":
        st.error(
            "🚨 ERRO TÉCNICO — O pip-audit não conseguiu concluir "
            "a auditoria."
        )

        st.info(
            "Analise o traceback acima. Esse resultado não deve ser "
            "interpretado como vulnerabilidade encontrada."
        )

    elif classificacao == "SEM_VULNERABILIDADES":
        st.success(
            "✅ A auditoria foi concluída e nenhuma vulnerabilidade "
            "conhecida foi reportada."
        )

    else:
        if vulnerabilidades:
            st.error(
                "❌ A auditoria foi concluída e encontrou "
                "dependências com vulnerabilidades conhecidas."
            )
        else:
            st.warning(
                "⚠️ O pip-audit terminou com código diferente de zero, "
                "mas a saída não pôde ser classificada apenas como "
                "vulnerabilidade conhecida. Analise o terminal."
            )

    # ========================================================
    # INDICADORES
    # ========================================================

    st.divider()
    st.subheader("📊 Resumo da auditoria")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🚨 Vulnerabilidades",
        resumo["vulnerabilidades"],
    )

    c2.metric(
        "📦 Pacotes afetados",
        resumo["pacotes_afetados"],
    )

    if classificacao == "ERRO_CODIFICACAO":
        c3.metric(
            "🚨 Resultado",
            "ERRO DE ENCODING",
        )
    elif classificacao == "ERRO_TECNICO":
        c3.metric(
            "🚨 Resultado",
            "ERRO TÉCNICO",
        )
    elif classificacao == "SEM_VULNERABILIDADES":
        c3.metric(
            "✅ Resultado",
            "SEM ACHADOS",
        )
    elif vulnerabilidades:
        c3.metric(
            "❌ Resultado",
            "VULNERÁVEL",
        )
    else:
        c3.metric(
            "⚠️ Resultado",
            "REVISAR",
        )

    # ========================================================
    # SEM VULNERABILIDADES
    # ========================================================

    if classificacao == "SEM_VULNERABILIDADES" and not vulnerabilidades:
        st.success(
            "✅ O pip-audit não reportou vulnerabilidades conhecidas "
            "nas dependências analisadas."
        )

        st.warning(
            "Isso não significa que as bibliotecas são absolutamente seguras. "
            "Significa apenas que nenhuma vulnerabilidade conhecida foi encontrada "
            "pelas fontes consultadas pelo pip-audit naquele momento."
        )

    # ========================================================
    # COM VULNERABILIDADES
    # ========================================================

    if vulnerabilidades:
        st.divider()
        st.subheader("🚨 Vulnerabilidades encontradas")

        st.write(
            "Cada bloco abaixo representa uma vulnerabilidade conhecida "
            "associada a uma dependência instalada."
        )

        for indice, item in enumerate(
            vulnerabilidades,
            start=1,
        ):

            st.markdown(
                "### {}. `{}`".format(
                    indice,
                    item["pacote"],
                )
            )

            c1, c2, c3 = st.columns(3)

            with c1:
                st.info(
                    "**Versão instalada**\n\n`{}`".format(
                        item["versao"]
                    )
                )

            with c2:
                st.error(
                    "**Vulnerabilidade**\n\n`{}`".format(
                        item["id"]
                    )
                )

            with c3:
                st.success(
                    "**Fix Versions**\n\n`{}`".format(
                        item["correcao"]
                    )
                )

            st.markdown(
                """
**Como interpretar:**

```text
PACOTE
   ↓
biblioteca afetada

VERSÃO
   ↓
versão instalada no ambiente

ID
   ↓
vulnerabilidade conhecida

FIX VERSIONS
   ↓
versões indicadas com correção
```
"""
            )

            with st.expander(
                "🔎 Ver linha original do pip-audit"
            ):
                st.code(
                    item["linha"],
                    language="text",
                )

            st.divider()


# ============================================================
# COMO LER O RESULTADO
# ============================================================

st.divider()

st.subheader("📖 Como ler uma linha do pip-audit")

st.code(
    "package-x    1.2.0    CVE-2026-12345    1.2.1",
    language="text",
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info(
        """
### Package

`package-x`

Biblioteca afetada.
"""
    )

with col2:
    st.info(
        """
### Version

`1.2.0`

Versão instalada.
"""
    )

with col3:
    st.error(
        """
### ID

`CVE-2026-12345`

Vulnerabilidade conhecida.
"""
    )

with col4:
    st.success(
        """
### Fix Version

`1.2.1`

Versão indicada como corrigida.
"""
    )


# ============================================================
# RESULTADO SEM ACHADOS
# ============================================================

st.subheader("✅ E se nenhuma vulnerabilidade for encontrada?")

st.code(
    """DEPENDÊNCIAS
      ↓
PIP-AUDIT
      ↓
COMPARAÇÃO
      ↓
0 VULNERABILIDADES CONHECIDAS
      ↓
SUCESSO
""",
    language="text",
)

st.success(
    "Esse é um bom resultado, mas não deve ser interpretado como "
    "prova de segurança total."
)


# ============================================================
# RESULTADO COM ACHADOS
# ============================================================

st.subheader("❌ E se vulnerabilidades forem encontradas?")

st.code(
    """VULNERABILIDADE
      ↓
IDENTIFICAR PACOTE
      ↓
VER VERSÃO INSTALADA
      ↓
VER ID
      ↓
VER FIX VERSION
      ↓
AVALIAR COMPATIBILIDADE
      ↓
ATUALIZAR / MITIGAR
""",
    language="text",
)

st.markdown(
    """
O próximo passo pode ser:

```powershell
python -m pip install --upgrade nome-do-pacote
```

Mas a atualização deve ser validada com testes, porque uma nova versão
pode alterar comportamentos da aplicação.
"""
)


# ============================================================
# RELAÇÃO COM REQUIREMENTS
# ============================================================

st.divider()

st.subheader("📄 pip-audit e requirements.txt")

st.markdown(
    """
Depois de atualizar uma dependência, é importante garantir que o arquivo
de dependências represente corretamente o ambiente desejado.

Exemplo:

```text
fastapi==0.x.x
httpx==0.x.x
pytest==8.x.x
```

O controle de versões facilita:

```text
REPRODUZIR AMBIENTE
      ↓
CONTROLAR DEPENDÊNCIAS
      ↓
AUDITAR VERSÕES
      ↓
ATUALIZAR COM SEGURANÇA
```
"""
)


# ============================================================
# SHIFT LEFT
# ============================================================

st.subheader("⬅️ pip-audit e Shift Left Security")

st.code(
    """DESENVOLVIMENTO
      ↓
INSTALA DEPENDÊNCIAS
      ↓
PIP-AUDIT
      ↓
IDENTIFICA VULNERABILIDADE
      ↓
ATUALIZA / MITIGA
      ↓
ANTES DA ENTREGA
""",
    language="text",
)

st.write(
    "Isso permite encontrar riscos em bibliotecas antes que o software "
    "seja disponibilizado em produção."
)


# ============================================================
# SCA X SAST X DAST
# ============================================================

st.divider()

st.subheader("🧰 SCA × SAST × DAST")

st.markdown(
    """
Essas categorias analisam pontos diferentes:

```text
SAST
 ↓
Código-fonte
 ↓
Bandit

SCA
 ↓
Dependências
 ↓
pip-audit

DAST
 ↓
Aplicação executando
 ↓
OWASP ZAP
```

### SAST
Procura problemas no código sem executar a aplicação.

### SCA
Procura vulnerabilidades conhecidas nos componentes utilizados.

### DAST
Testa a aplicação enquanto ela está em execução.
"""
)


# ============================================================
# KIT DE QUALIDADE
# ============================================================

st.subheader("🧩 Onde o pip-audit entra no nosso kit?")

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
# IMPORTANTE SOBRE TEMPO
# ============================================================

st.warning(
    "As bases de vulnerabilidades evoluem com o tempo. "
    "Uma dependência que hoje não possui vulnerabilidade conhecida "
    "pode receber um alerta no futuro. Por isso auditorias de dependências "
    "devem ser repetidas regularmente."
)


# ============================================================
# PIPELINE
# ============================================================

st.divider()

st.subheader("⚙️ pip-audit em integração contínua")

st.markdown(
    """
Esse comando também pode fazer parte de pipelines:

```text
COMMIT
   ↓
RUFF
   ↓
MYPY
   ↓
BANDIT
   ↓
PIP-AUDIT
   ↓
PYTEST
   ↓
BUILD / ENTREGA
```

Assim, uma vulnerabilidade conhecida em uma dependência pode ser detectada
antes que uma nova versão do sistema seja liberada.
"""
)


# ============================================================
# RESUMO
# ============================================================

st.divider()

st.subheader("📘 Resumo para memorizar")

st.code(
    """PIP-AUDIT
      ↓
SCA
      ↓
DEPENDÊNCIAS
      ↓
VERSÕES INSTALADAS
      ↓
BASE DE VULNERABILIDADES
      ↓
COMPARAÇÃO
      ↓
PACOTE + VERSÃO + ID + FIX VERSION
""",
    language="text",
)

st.markdown(
    """
**pip-audit**  
Ferramenta para auditoria de dependências Python.

**SCA**  
Software Composition Analysis.

**Dependência**  
Biblioteca externa utilizada pelo projeto.

**Version**  
Versão atualmente instalada.

**ID**  
Identificador da vulnerabilidade, como CVE, GHSA ou PYSEC.

**Fix Version**  
Versão indicada como contendo a correção.

**Importante**  
Ausência de vulnerabilidades conhecidas não significa segurança absoluta.

**Shift Left Security**  
Identificar riscos nas dependências o mais cedo possível.
"""
)

st.success(
    "📦 O objetivo do pip-audit é ajudar a identificar dependências "
    "com vulnerabilidades conhecidas antes que elas se tornem um problema em produção."
)
