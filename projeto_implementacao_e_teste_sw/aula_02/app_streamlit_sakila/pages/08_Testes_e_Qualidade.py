import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import streamlit as st

from services.database import get_config, test_connection


# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Testes e Qualidade",
    page_icon="🧪",
    layout="wide",
)

# A página está dentro de /pages. O diretório pai é a raiz do projeto.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = PROJECT_ROOT / "tests"


# -----------------------------------------------------------------------------
# FUNÇÕES AUXILIARES
# -----------------------------------------------------------------------------
def executar_pytest() -> Tuple[int, str, List[str]]:
    """
    Executa os testes automatizados do projeto usando o mesmo interpretador
    Python que iniciou o Streamlit.

    O plugin de cache é desabilitado para evitar o PytestCacheWarning causado
    por falta de permissão para criar a pasta .pytest_cache no Windows.
    """
    comando = [
        sys.executable,
        "-m",
        "pytest",
        "-v",
        "-p",
        "no:cacheprovider",
    ]

    ambiente = os.environ.copy()
    ambiente["PYTHONIOENCODING"] = "utf-8"

    try:
        processo = subprocess.run(
            comando,
            cwd=str(PROJECT_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            env=ambiente,
            check=False,
        )

        return processo.returncode, processo.stdout, comando

    except subprocess.TimeoutExpired as erro:
        saida = erro.stdout or ""
        if isinstance(saida, bytes):
            saida = saida.decode("utf-8", errors="replace")

        mensagem = (
            f"{saida}\n\n"
            "ERRO: a execução ultrapassou o limite de 120 segundos."
        )
        return 124, mensagem, comando

    except FileNotFoundError:
        return (
            127,
            "ERRO: não foi possível localizar o interpretador Python.",
            comando,
        )

    except Exception as erro:
        return (
            1,
            f"ERRO inesperado ao executar o pytest: {erro}",
            comando,
        )


def analisar_resultado_pytest(saida: str, codigo_retorno: int) -> Dict[str, int]:
    """Extrai os principais totais apresentados no resumo do pytest."""
    resultado = {
        "coletados": 0,
        "aprovados": 0,
        "falharam": 0,
        "erros": 0,
        "ignorados": 0,
        "avisos": 0,
        "codigo_retorno": codigo_retorno,
    }

    padroes = {
        "coletados": r"collected\s+(\d+)\s+items?",
        "aprovados": r"(\d+)\s+passed",
        "falharam": r"(\d+)\s+failed",
        "erros": r"(\d+)\s+errors?",
        "ignorados": r"(\d+)\s+skipped",
        "avisos": r"(\d+)\s+warnings?",
    }

    for chave, padrao in padroes.items():
        correspondencia = re.search(padrao, saida, flags=re.IGNORECASE)
        if correspondencia:
            resultado[chave] = int(correspondencia.group(1))

    # Em algumas saídas aparece "collected 1 item" e não "items".
    if resultado["coletados"] == 0:
        correspondencia = re.search(
            r"collected\s+(\d+)\s+item",
            saida,
            flags=re.IGNORECASE,
        )
        if correspondencia:
            resultado["coletados"] = int(correspondencia.group(1))

    return resultado


def explicar_codigo_retorno(codigo: int) -> str:
    """Retorna uma explicação didática do código de saída do pytest."""
    explicacoes = {
        0: "Todos os testes executados foram aprovados.",
        1: "Um ou mais testes falharam.",
        2: "A execução foi interrompida pelo usuário ou pelo sistema.",
        3: "O pytest encontrou um erro interno.",
        4: "O comando ou os argumentos do pytest são inválidos.",
        5: "Nenhum teste foi encontrado.",
        124: "A execução ultrapassou o tempo máximo configurado.",
        127: "O interpretador Python não foi localizado.",
    }
    return explicacoes.get(
        codigo,
        "A execução terminou com um código não previsto.",
    )


# -----------------------------------------------------------------------------
# CABEÇALHO
# -----------------------------------------------------------------------------
st.title("8️⃣ Testes e Qualidade")
st.caption(
    "Validação da integração entre o aplicativo Streamlit, o Python "
    "e o banco MySQL Sakila."
)


# -----------------------------------------------------------------------------
# TESTE MANUAL DE CONEXÃO
# -----------------------------------------------------------------------------
st.subheader("🔌 Teste manual de integração")

config = get_config()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Servidor", str(config["host"]))
col2.metric("Porta", str(config["port"]))
col3.metric("Usuário", str(config["user"]))
col4.metric("Banco", str(config["database"]))

st.info(
    "A senha é carregada pelo arquivo `.env`. Caso ele não exista, "
    "o projeto utiliza a configuração local definida em "
    "`services/database.py`."
)

if st.button(
    "🔌 Testar conexão com MySQL",
    type="primary",
    use_container_width=True,
):
    with st.spinner("Testando a conexão com o MySQL..."):
        ok, message = test_connection()

    if ok:
        st.success(message)
        st.balloons()
    else:
        st.error(message)
        st.warning(
            "Confirme se o serviço MySQL está iniciado, se o banco "
            "`sakila` existe e se os dados `MYSQL_USER` e "
            "`MYSQL_PASSWORD` estão corretos no arquivo `.env`."
        )


# -----------------------------------------------------------------------------
# PIRÂMIDE DE TESTES
# -----------------------------------------------------------------------------
st.divider()
st.subheader("🔺 Pirâmide de testes")

st.code(
    """
          Testes de interface
        Testes de integração
      Testes unitários
""",
    language="text",
)

st.markdown(
    """
- **Testes unitários:** validam pequenas partes do código de forma isolada.
- **Testes de integração:** verificam a comunicação entre Python, serviços e MySQL.
- **Testes de interface:** validam páginas, botões, formulários, filtros e mensagens do Streamlit.
"""
)


# -----------------------------------------------------------------------------
# CASOS DE TESTE
# -----------------------------------------------------------------------------
st.subheader("📋 Exemplos de casos de teste")

st.dataframe(
    {
        "Caso": [
            "Configuração",
            "Conexão",
            "Consulta",
            "Cadastro",
            "Validação",
            "Integridade",
        ],
        "Tipo": [
            "Unitário",
            "Integração",
            "Integração",
            "Integração",
            "Unitário/Interface",
            "Integração",
        ],
        "Resultado esperado": [
            "Carregar host, porta, usuário e banco corretamente",
            "Conectar ao banco sakila",
            "Retornar colunas e registros esperados",
            "Inserir ator com nome e sobrenome",
            "Bloquear formulário incompleto",
            "Impedir exclusão quando existir chave estrangeira",
        ],
    },
    use_container_width=True,
    hide_index=True,
)


# -----------------------------------------------------------------------------
# EXECUÇÃO DO PYTEST PELO STREAMLIT
# -----------------------------------------------------------------------------
st.divider()
st.subheader("🧪 Executar testes automatizados pelo aplicativo")

st.markdown(
    """
Ao clicar no botão abaixo, o Streamlit executa internamente:

```bash
python -m pytest -v -p no:cacheprovider
```

O parâmetro `-p no:cacheprovider` desativa somente o cache do pytest.  
Ele evita o aviso de permissão relacionado à pasta `.pytest_cache` e **não
interfere na execução ou no resultado dos testes**.
"""
)

st.caption(f"Diretório do projeto: {PROJECT_ROOT}")
st.caption(f"Diretório de testes: {TESTS_DIR}")

if not TESTS_DIR.exists():
    st.error(
        "A pasta `tests` não foi encontrada na raiz do projeto. "
        "Crie a pasta e adicione arquivos com nomes iniciados por `test_`."
    )

if st.button(
    "▶️ Executar pytest agora",
    type="primary",
    use_container_width=True,
    disabled=not TESTS_DIR.exists(),
):
    with st.spinner("Executando os testes automatizados..."):
        codigo, saida, comando = executar_pytest()

    st.session_state["pytest_resultado"] = {
        "codigo": codigo,
        "saida": saida,
        "comando": comando,
    }


# -----------------------------------------------------------------------------
# RESULTADO E EXPLICAÇÃO
# -----------------------------------------------------------------------------
if "pytest_resultado" in st.session_state:
    resultado_execucao = st.session_state["pytest_resultado"]

    codigo = resultado_execucao["codigo"]
    saida = resultado_execucao["saida"]
    comando = resultado_execucao["comando"]

    resumo = analisar_resultado_pytest(saida, codigo)

    st.divider()
    st.subheader("📊 Resultado da execução")

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Coletados", resumo["coletados"])
    c2.metric("Aprovados", resumo["aprovados"])
    c3.metric("Falharam", resumo["falharam"])
    c4.metric("Erros", resumo["erros"])
    c5.metric("Avisos", resumo["avisos"])

    if codigo == 0:
        st.success(
            "✅ Execução concluída com sucesso: todos os testes "
            "encontrados foram aprovados."
        )
    elif codigo == 5:
        st.warning(
            "⚠️ O pytest foi executado, mas nenhum teste foi encontrado."
        )
    else:
        st.error(
            "❌ A execução terminou com falha. Analise o relatório abaixo."
        )

    st.markdown("#### Comando executado")
    st.code(" ".join(comando), language="bash")

    st.markdown("#### Saída completa do pytest")
    st.code(saida, language="text")

    st.markdown("#### Explicação do resultado")
    st.markdown(
        f"""
**Código de retorno:** `{codigo}`  
**Significado:** {explicar_codigo_retorno(codigo)}

O pytest procurou arquivos e funções que seguem sua convenção de nomes:

- arquivos como `test_config.py`;
- funções como `test_config_database_padrao`;
- classes de teste com nomes iniciados por `Test`.

No seu resultado anterior, o pytest coletou **1 teste** e apresentou:

```text
tests/test_config.py::test_config_database_padrao PASSED
```

Isso significa que:

1. o arquivo `tests/test_config.py` foi encontrado;
2. a função `test_config_database_padrao` foi executada;
3. todas as afirmações (`assert`) desse teste foram atendidas;
4. o teste recebeu o status `PASSED`;
5. o projeto terminou com código de retorno `0`.

O aviso antigo sobre `.pytest_cache` não representava falha no teste.
Ele ocorreu porque o Windows negou permissão para criar ou renomear a pasta
de cache. Nesta página, o cache foi desabilitado com
`-p no:cacheprovider`, eliminando esse aviso.
"""
    )

    if resumo["coletados"] == 1 and resumo["aprovados"] == 1:
        st.info(
            "Atualmente existe somente um teste automatizado no projeto. "
            "O resultado confirma a configuração padrão do banco, mas ainda "
            "não testa consultas, CRUD, integração real com MySQL ou interface."
        )

    with st.expander("Como interpretar os principais status do pytest"):
        st.markdown(
            """
| Status | Significado |
|---|---|
| `PASSED` | O comportamento obtido correspondeu ao comportamento esperado. |
| `FAILED` | O teste foi executado, mas alguma afirmação não foi atendida. |
| `ERROR` | O teste não conseguiu ser preparado ou executado corretamente. |
| `SKIPPED` | O teste foi ignorado intencionalmente. |
| `XFAIL` | A falha já era esperada e foi documentada. |
| `XPASS` | Um teste que deveria falhar acabou sendo aprovado. |
"""
        )

    with st.expander("Diferença entre o teste de conexão e o pytest"):
        st.markdown(
            """
- O botão **Testar conexão com MySQL** chama diretamente a função
  `test_connection()` e verifica se o banco está acessível naquele momento.
- O botão **Executar pytest agora** inicia o framework pytest e executa todos
  os testes existentes na pasta `tests`.
- Um teste de configuração pode ser aprovado mesmo com o MySQL desligado,
  porque ele pode validar apenas os valores configurados.
- Para verificar realmente o banco dentro do pytest, é necessário criar um
  teste de integração que abra uma conexão e execute uma consulta controlada.
"""
        )

    if st.button("🗑️ Limpar resultado", use_container_width=True):
        del st.session_state["pytest_resultado"]
        st.rerun()