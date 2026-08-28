import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.utils.test_runner import (
    PROJECT_ROOT,
    python_command,
    run_command,
    show_tool_result,
)


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="TechPort | Ambiente",
    page_icon="🧰",
    layout="wide",
)

st.title("🧰 1. Ambiente de testes")

st.write(
    "Antes de executar qualquer teste, verificamos se o projeto está "
    "utilizando o Python correto, a virtual environment esperada e "
    "as dependências necessárias."
)

st.info(
    "Ambiente de testes = Python correto + .venv ativa + dependências instaladas "
    "+ projeto preparado para executar as ferramentas de qualidade."
)


# ==========================================================
# INFORMAÇÕES DO AMBIENTE
# ==========================================================

c1, c2 = st.columns(2)

with c1:

    st.subheader("🐍 Python em uso")

    st.metric(
        "Executável Python",
        Path(sys.executable).name,
    )

    st.code(
        sys.executable,
        language="text",
    )


with c2:

    st.subheader("📁 Projeto")

    venv_ok = ".venv" in str(sys.executable).lower()

    if venv_ok:

        st.success(
            "✅ O Streamlit está usando a .venv do projeto."
        )

    else:

        st.error(
            "❌ O Streamlit NÃO parece estar usando a .venv."
        )

    st.code(
        str(PROJECT_ROOT),
        language="text",
    )


# ==========================================================
# EXPLICAÇÃO DIDÁTICA
# ==========================================================

with st.expander("ℹ️ O que verificamos no ambiente de testes?"):

    st.markdown(
        r"""
Antes de executar testes automatizados, análise estática,
segurança ou cobertura, precisamos garantir que o ambiente
esteja configurado corretamente.

Um problema de ambiente pode fazer um teste falhar mesmo quando
o código da aplicação está correto.

Por isso, verificamos principalmente:

- qual versão do Python está sendo utilizada;
- qual executável Python está rodando o Streamlit;
- se a `.venv` do projeto está ativa;
- se as bibliotecas necessárias estão instaladas;
- se o arquivo `requirements.txt` está disponível;
- se as versões das dependências estão corretas;
- se as ferramentas de teste estão instaladas.

### O que é uma `.venv`?

A `.venv` é uma **Virtual Environment** do Python.

Ela cria um ambiente isolado para o projeto.

Isso permite que cada aplicação tenha suas próprias versões
de bibliotecas sem interferir em outros projetos instalados
no computador.

### Exemplo

Imagine dois projetos:

```text
Projeto A
Python
FastAPI 0.100
pytest 7.x
```

e:

```text
Projeto B
Python
FastAPI 0.115
pytest 8.x
```

Sem ambientes virtuais, essas versões poderiam entrar
em conflito.

Com `.venv`:

```text
Projeto A
└── .venv
    └── dependências do Projeto A
```

```text
Projeto B
└── .venv
    └── dependências do Projeto B
```

Cada projeto fica isolado.

### Como saber qual Python está sendo usado?

O Python disponibiliza:

```python
sys.executable
```

Esse comando mostra o caminho completo do executável
que está rodando a aplicação.

Exemplo esperado:

```text
C:\projeto\techport\.venv\Scripts\python.exe
```

Se aparecer algo semelhante a:

```text
C:\Users\usuario\AppData\Local\Programs\Python\Python39\python.exe
```

é possível que o projeto esteja utilizando o Python global
em vez da `.venv`.

### Por que isso é importante?

Se o Streamlit estiver usando um Python diferente daquele
em que as bibliotecas foram instaladas, podem surgir erros como:

```text
ModuleNotFoundError
```

Por exemplo:

```text
No module named pytest
No module named mypy
No module named bandit
No module named pip_audit
```

Nesse caso, o problema pode não estar no código.

O problema pode estar no **ambiente**.

### O que é o requirements.txt?

O arquivo:

```text
requirements.txt
```

registra as dependências necessárias para executar o projeto.

Exemplo:

```text
streamlit
fastapi
uvicorn
pytest
pytest-cov
mypy
ruff
bandit
pip-audit
```

Isso permite reconstruir o ambiente em outro computador.

### Instalação das dependências

O comando:

```powershell
python -m pip install -r requirements.txt
```

significa:

```text
Python
↓
pip
↓
requirements.txt
↓
instalação das dependências
```

### Por que usamos `python -m pip`?

Em vez de executar somente:

```powershell
pip install ...
```

utilizamos:

```powershell
python -m pip install ...
```

porque assim garantimos que o `pip` utilizado pertence
ao mesmo Python que está executando o projeto.

Isso reduz problemas com múltiplas instalações do Python.

### O que o `pip list` mostra?

O comando:

```powershell
python -m pip list
```

mostra as bibliotecas instaladas naquele ambiente.

Exemplo:

```text
Package       Version
------------- -------
pytest        8.3.0
mypy          1.11.0
ruff          0.6.0
bandit        1.7.9
pip-audit     2.7.3
```

Isso ajuda a verificar:

- se uma biblioteca está instalada;
- qual versão está sendo utilizada;
- se o ambiente possui as ferramentas necessárias.

### Fluxo correto antes dos testes

```text
Entrar no projeto
↓
Ativar .venv
↓
Instalar requirements
↓
Verificar bibliotecas
↓
Executar Streamlit
↓
Executar testes
```

### Exemplo no PowerShell

Ativar a `.venv`:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependências:

```powershell
python -m pip install -r requirements.txt
```

Consultar bibliotecas:

```powershell
python -m pip list
```

Executar a aplicação:

```powershell
python -m streamlit run app/main.py
```

### Um ponto importante para os testes

Quando um teste apresenta erro, precisamos primeiro perguntar:

> O problema está no código ou no ambiente?

Por exemplo:

```text
ERROR
No module named pytest_cov
```

isso não necessariamente significa que o teste está errado.

Pode significar apenas que falta instalar:

```powershell
python -m pip install pytest-cov
```

⚠️ **Importante:** antes de analisar falhas de teste,
garanta que o ambiente está consistente.

Um bom ambiente de testes deve ser:

- isolado;
- reproduzível;
- documentado;
- consistente;
- fácil de reconstruir.
"""
    )


# ==========================================================
# INSTALAÇÃO DAS DEPENDÊNCIAS
# ==========================================================

st.subheader("📦 Instalação completa")

st.code(
    "python -m pip install -r requirements.txt",
    language="powershell",
)

st.caption(
    "O botão abaixo executa exatamente esse comando usando "
    "o mesmo Python que está executando o Streamlit."
)

if st.button(
    "📦 Instalar / atualizar requirements",
    type="primary",
    use_container_width=True,
):

    result = run_command(
        python_command(
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
        ),
        "requirements",
    )

    show_tool_result(
        result,
        "✅ Dependências instaladas/atualizadas.",
        "❌ A instalação encontrou um problema.",
    )


# ==========================================================
# BIBLIOTECAS INSTALADAS
# ==========================================================

st.subheader("🔎 Bibliotecas instaladas")

st.write(
    "Consulte as bibliotecas e versões instaladas no mesmo "
    "ambiente Python utilizado pelo Streamlit."
)

st.code(
    "python -m pip list",
    language="powershell",
)

if st.button(
    "🔎 Executar pip list",
    use_container_width=True,
):

    result = run_command(
        python_command(
            "-m",
            "pip",
            "list",
        ),
        "pip list",
    )

    show_tool_result(
        result,
        "✅ Ambiente consultado com sucesso.",
        "❌ Não foi possível consultar o ambiente.",
    )


# ==========================================================
# LEITURA DIDÁTICA
# ==========================================================

st.divider()

st.subheader("📚 Leitura didática")

st.code(
    """.venv correta        → ambiente isolado
requirements instalado → dependências disponíveis
pip list              → conferência das versões
ambiente consistente  → testes mais confiáveis""",
    language="text",
)

st.caption(
    "Se o ambiente estiver incorreto, uma falha pode acontecer "
    "antes mesmo de o teste conseguir avaliar o código."
)
