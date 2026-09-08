# ============================================================
# TECHPORT
# Utilitário para execução e visualização dos testes
# Disciplina: Projeto, Implementação e Teste de Software
# Professor Rodolfo Terra
# ============================================================

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import streamlit as st


# ============================================================
# RAIZ DO PROJETO
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

# Mantém compatibilidade com as páginas do Streamlit
PROJECT_ROOT = ROOT_DIR


# ============================================================
# RESULTADO DE UM COMANDO
# ============================================================

@dataclass
class CommandResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    output: str


# ============================================================
# MONTAR COMANDO USANDO O PYTHON ATUAL
# ============================================================

def python_command(*args: str) -> list[str]:
    """
    Usa exatamente o Python que está executando o Streamlit.
    Assim, as ferramentas são executadas na mesma .venv.
    """
    return [sys.executable, *args]


# ============================================================
# FORMATAR COMANDO PARA EXIBIÇÃO
# ============================================================

def command_to_text(command: Sequence[str]) -> str:
    partes = []

    for item in command:
        item = str(item)

        if " " in item:
            partes.append(f'"{item}"')
        else:
            partes.append(item)

    return " ".join(partes)


# ============================================================
# EXECUTAR COMANDO
# ============================================================

def run_command(
    command: Sequence[str],
    label: str = "Comando",
    cwd: Path | None = None,
    timeout: int = 300,
    show_terminal: bool = True,
) -> CommandResult:
    """
    Executa um comando e captura stdout, stderr e exit code.
    """

    command = [str(item) for item in command]
    diretorio = cwd or ROOT_DIR

    st.markdown(f"### 🖥️ {label}")

    st.code(
        command_to_text(command),
        language="powershell",
    )

    try:
        with st.spinner(f"Executando {label}..."):
            processo = subprocess.run(
                command,
                cwd=str(diretorio),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
            )

        stdout = processo.stdout or ""
        stderr = processo.stderr or ""

        output_partes = []

        if stdout.strip():
            output_partes.append(stdout.rstrip())

        if stderr.strip():
            output_partes.append(stderr.rstrip())

        output = "\n".join(output_partes)

        result = CommandResult(
            command=command,
            returncode=processo.returncode,
            stdout=stdout,
            stderr=stderr,
            output=output,
        )

        if show_terminal:
            st.markdown("#### Saída do terminal")

            if output.strip():
                st.code(output, language="text")
            else:
                st.info("O comando não produziu saída no terminal.")

        return result

    except subprocess.TimeoutExpired as exc:
        output = f"O comando excedeu o tempo máximo de {timeout} segundos."

        st.error(f"⏱️ {output}")

        return CommandResult(
            command=command,
            returncode=-1,
            stdout=exc.stdout if isinstance(exc.stdout, str) else "",
            stderr=exc.stderr if isinstance(exc.stderr, str) else "",
            output=output,
        )

    except FileNotFoundError as exc:
        output = f"O comando ou executável não foi encontrado: {exc}"

        st.error(f"🚨 {output}")

        return CommandResult(
            command=command,
            returncode=-1,
            stdout="",
            stderr=str(exc),
            output=output,
        )

    except Exception as exc:
        output = f"Erro inesperado ao executar o comando: {exc}"

        st.error(f"🚨 {output}")

        return CommandResult(
            command=command,
            returncode=-1,
            stdout="",
            stderr=str(exc),
            output=output,
        )


# ============================================================
# EXTRAIR CONTADORES DO PYTEST
# ============================================================

def _extract_pytest_count(output: str, pattern: str) -> int:
    match = re.search(pattern, output.lower())

    if match:
        return int(match.group(1))

    return 0


# ============================================================
# CLASSIFICAR RESULTADO DO PYTEST
# ============================================================

def classify_pytest(
    output: str,
    returncode: int,
) -> dict[str, str | int]:
    """
    Interpreta a saída do pytest.

    Estados:
    - PASSED
    - FAILED
    - ERROR
    - SKIPPED
    - NO TESTS
    - ATENÇÃO
    """

    output = output or ""
    lower = output.lower()

    passed = _extract_pytest_count(output, r"(\d+)\s+passed")
    failed = _extract_pytest_count(output, r"(\d+)\s+failed")
    errors = _extract_pytest_count(output, r"(\d+)\s+errors?")
    skipped = _extract_pytest_count(output, r"(\d+)\s+skipped")
    xfailed = _extract_pytest_count(output, r"(\d+)\s+xfailed")
    xpassed = _extract_pytest_count(output, r"(\d+)\s+xpassed")
    deselected = _extract_pytest_count(output, r"(\d+)\s+deselected")

    total = (
        passed
        + failed
        + errors
        + skipped
        + xfailed
        + xpassed
    )

    # Exit code 5 = nenhum teste coletado.
    if (
        returncode == 5
        or "collected 0 items" in lower
        or "no tests ran" in lower
        or "no tests collected" in lower
    ):
        state = "NO TESTS"
        explanation = (
            "O pytest iniciou corretamente, mas não encontrou "
            "nenhum teste para executar."
        )

    elif (
        errors > 0
        or "error collecting" in lower
        or "modulenotfounderror" in lower
        or "no module named" in lower
        or "importerror" in lower
        or "internalerror" in lower
        or returncode in {2, 3, 4}
    ):
        state = "ERROR"
        explanation = (
            "O pytest não conseguiu preparar, coletar "
            "ou executar corretamente os testes."
        )

    elif failed > 0 or returncode == 1:
        state = "FAILED"
        explanation = (
            "Um ou mais testes foram executados, mas o resultado "
            "obtido foi diferente do resultado esperado."
        )

    elif (
        returncode == 0
        and passed > 0
        and failed == 0
        and errors == 0
    ):
        state = "PASSED"
        explanation = (
            "Os testes executados produziram os resultados esperados."
        )

    elif (
        returncode == 0
        and skipped > 0
        and passed == 0
        and failed == 0
        and errors == 0
    ):
        state = "SKIPPED"
        explanation = (
            "Os testes existem, porém foram ignorados nesta execução."
        )

    else:
        state = "ATENÇÃO"
        explanation = (
            "O pytest terminou em uma situação que precisa ser analisada."
        )

    return {
        "state": state,
        "explanation": explanation,
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "skipped": skipped,
        "xfailed": xfailed,
        "xpassed": xpassed,
        "deselected": deselected,
        "total": total,
        "returncode": returncode,
    }


# ============================================================
# MOSTRAR RESUMO VISUAL DO PYTEST
# ============================================================

def show_pytest_summary(result: CommandResult) -> None:
    """
    Exibe no Streamlit uma interpretação didática
    do resultado produzido pelo pytest.
    """

    data = classify_pytest(
        result.output,
        result.returncode,
    )

    passed = int(data["passed"])
    failed = int(data["failed"])
    errors = int(data["errors"])
    skipped = int(data["skipped"])
    total = int(data["total"])
    returncode = int(data["returncode"])
    state = str(data["state"])
    explanation = str(data["explanation"])

    # --------------------------------------------------------
    # MÉTRICAS
    # --------------------------------------------------------

    cols = st.columns(5)

    cols[0].metric("✅ PASSED", passed)
    cols[1].metric("❌ FAILED", failed)
    cols[2].metric("🚨 ERROR", errors)
    cols[3].metric("⏭️ SKIPPED", skipped)
    cols[4].metric("🧪 TESTES", total)

    # --------------------------------------------------------
    # NO TESTS
    # --------------------------------------------------------

    if state == "NO TESTS":
        st.warning("🔎 **NO TESTS — Nenhum teste foi encontrado.**")

        st.markdown(
            """
O pytest foi iniciado corretamente, porém não encontrou
nenhum teste para executar.

```text
PYTEST
   ↓
INICIOU
   ↓
PROCUROU TESTES
   ↓
NÃO ENCONTROU
   ↓
0 TESTES EXECUTADOS
```
"""
        )

        st.info(
            """
**Importante:** o código de saída `5` não significa
que cinco testes passaram.

No pytest:

```text
Exit Code 5
=
Nenhum teste foi coletado
```
"""
        )

        st.markdown("#### O pytest procura arquivos como:")

        st.code(
            """tests/
├── test_usuario.py
├── test_service.py
├── test_api.py
└── unit/
    └── test_primeiro_teste.py""",
            language="text",
        )

        st.markdown("E funções começando com `test_`:")

        st.code(
            """def test_somar():
    resultado = 2 + 3
    assert resultado == 5""",
            language="python",
        )

    # --------------------------------------------------------
    # ERROR
    # --------------------------------------------------------

    elif state == "ERROR":
        st.error(f"🚨 **ERROR — {explanation}**")

        st.markdown(
            """
```text
PYTEST
   ↓
TENTOU PREPARAR
   ↓
ENCONTROU UM PROBLEMA
   ↓
TESTE NÃO EXECUTADO CORRETAMENTE
```

Possíveis causas:

- biblioteca não instalada;
- erro de importação;
- módulo não encontrado;
- erro no `conftest.py`;
- configuração incorreta;
- erro durante a coleta;
- problema interno do pytest.
"""
        )

    # --------------------------------------------------------
    # FAILED
    # --------------------------------------------------------

    elif state == "FAILED":
        st.error(f"❌ **FAILED — {failed} teste(s) falharam.**")

        st.markdown(
            """
```text
TESTE
   ↓
EXECUTOU
   ↓
COMPAROU

ESPERADO
   ≠
OBTIDO

   ↓

FAILED
```
"""
        )

        st.info(
            "O teste foi executado, porém o resultado obtido "
            "foi diferente do resultado esperado."
        )

        if passed > 0:
            st.success(
                f"✅ Apesar das falhas, {passed} teste(s) "
                "passaram corretamente."
            )

    # --------------------------------------------------------
    # PASSED
    # --------------------------------------------------------

    elif state == "PASSED":
        st.success(
            f"✅ **PASSED — {passed} teste(s) executados com sucesso.**"
        )

        st.markdown(
            """
```text
TESTE
   ↓
EXECUTOU
   ↓
COMPAROU

ESPERADO
   =
OBTIDO

   ↓

PASSED
```
"""
        )

        st.info(
            "Os resultados produzidos foram os resultados esperados. "
            "Isso aumenta nossa confiança no comportamento do software."
        )

        if skipped > 0:
            st.warning(
                f"⏭️ {skipped} teste(s) foram ignorados nesta execução."
            )

    # --------------------------------------------------------
    # SKIPPED
    # --------------------------------------------------------

    elif state == "SKIPPED":
        st.warning(
            f"⏭️ **SKIPPED — {skipped} teste(s) foram ignorados.**"
        )

        st.markdown(
            """
O teste existe, porém não foi executado.

Isso pode acontecer quando:

- depende do banco;
- depende de uma API externa;
- depende de variável de ambiente;
- está marcado com `pytest.mark.skip`;
- não atende às condições desta execução.
"""
        )

    # --------------------------------------------------------
    # ATENÇÃO
    # --------------------------------------------------------

    else:
        st.warning(f"⚠️ **ATENÇÃO — {explanation}**")

    # --------------------------------------------------------
    # RESULTADOS ADICIONAIS
    # --------------------------------------------------------

    xfailed = int(data["xfailed"])
    xpassed = int(data["xpassed"])
    deselected = int(data["deselected"])

    if xfailed > 0 or xpassed > 0 or deselected > 0:
        st.markdown("### Outros resultados")

        extras = st.columns(3)

        extras[0].metric("XFAILED", xfailed)
        extras[1].metric("XPASSED", xpassed)
        extras[2].metric("DESELECTED", deselected)

    # --------------------------------------------------------
    # EXIT CODE
    # --------------------------------------------------------

    with st.expander("🔎 Entender o código de saída do pytest"):
        st.code(
            f"Exit Code: {returncode}",
            language="text",
        )

        st.markdown(
            """
| Código | Significado |
|---:|---|
| `0` | Todos os testes passaram |
| `1` | Um ou mais testes falharam |
| `2` | Execução interrompida |
| `3` | Erro interno do pytest |
| `4` | Uso incorreto do pytest |
| `5` | Nenhum teste foi coletado |
"""
        )


# ============================================================
# MOSTRAR RESULTADO GENÉRICO
# ============================================================

def show_command_result(
    result: CommandResult,
    success_message: str = "Comando executado com sucesso.",
    error_message: str = "O comando encontrou problemas.",
) -> None:
    """
    Exibe o resultado de comandos que não são pytest.
    Pode ser usado com Ruff, mypy, Bandit, pip-audit etc.
    """

    st.markdown("### Resultado")

    if result.returncode == 0:
        st.success(f"✅ {success_message}")
    else:
        st.error(f"❌ {error_message}")

    with st.expander("🔎 Código de saída"):
        st.code(
            str(result.returncode),
            language="text",
        )


# ============================================================
# VERIFICAR SE UM MÓDULO ESTÁ INSTALADO
# ============================================================

def module_is_installed(module_name: str) -> bool:
    """
    Verifica se um módulo Python pode ser importado
    no ambiente atual.
    """
    return importlib.util.find_spec(module_name) is not None


# ============================================================
# MOSTRAR INFORMAÇÕES DO AMBIENTE
# ============================================================

def show_environment_info() -> None:
    """
    Exibe informações importantes sobre o ambiente Python atual.
    """

    st.subheader("🐍 Ambiente Python")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Python utilizado**")
        st.code(
            sys.executable,
            language="text",
        )

    with col2:
        st.markdown("**Raiz do projeto**")
        st.code(
            str(ROOT_DIR),
            language="text",
        )

    if ".venv" in sys.executable.lower():
        st.success("✅ O Python da `.venv` está sendo utilizado.")
    else:
        st.warning(
            "⚠️ O Python atual não parece pertencer à `.venv`."
        )


# ============================================================
# COMPATIBILIDADE COM AS PÁGINAS DO STREAMLIT
# ============================================================

def show_tool_result(
    result: CommandResult,
    success_message: str = "Comando executado com sucesso.",
    error_message: str = "O comando encontrou problemas.",
) -> None:
    """
    Alias didático para exibir o resultado das ferramentas
    utilizadas no ambiente de testes.
    """
    show_command_result(
        result,
        success_message,
        error_message,
    )