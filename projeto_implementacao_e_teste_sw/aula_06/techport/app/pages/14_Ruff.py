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
    page_title="TechPort | Ruff",
    page_icon="🧹",
    layout="wide",
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🧹 4. Ruff — Qualidade do código")

st.write(
    "O Ruff realiza uma análise estática do código Python. "
    "Ele procura problemas de qualidade, organização e estilo "
    "sem precisar executar a aplicação."
)

st.code(
    "python -m ruff check .",
    language="powershell",
)

st.caption("Categoria: análise estática de qualidade.")


# ============================================================
# O QUE É ANÁLISE ESTÁTICA?
# ============================================================

st.subheader("🧠 O que estamos fazendo?")

st.markdown(
    """
Diferentemente do `pytest`, o Ruff **não executa as funcionalidades
do TechPort**.

Ele lê os arquivos Python e procura padrões que podem indicar
problemas.

```text
CÓDIGO PYTHON
      ↓
     RUFF
      ↓
ANÁLISE ESTÁTICA
      ↓
PROBLEMAS ENCONTRADOS
```

Chamamos isso de **análise estática** porque o código é analisado
sem que a aplicação precise estar em execução.
"""
)


# ============================================================
# PYTEST X RUFF
# ============================================================

st.subheader("⚖️ pytest × Ruff")

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
### 🧪 pytest

Executa o código e verifica o comportamento da aplicação.

```text
ENTRADA
   ↓
FUNÇÃO
   ↓
RESULTADO
   ↓
ASSERT
```

**Pergunta principal:**

O software está produzindo o resultado esperado?
"""
    )

with col2:
    st.info(
        """
### 🧹 Ruff

Analisa o código sem precisar executar a aplicação.

```text
ARQUIVO .PY
    ↓
   RUFF
    ↓
ANÁLISE
    ↓
AVISOS
```

**Pergunta principal:**

Existe algum problema identificável no código?
"""
    )


# ============================================================
# O QUE O RUFF PODE ENCONTRAR?
# ============================================================

st.subheader("🔎 O que o Ruff pode encontrar?")

st.markdown(
    """
Entre os problemas que podem aparecer estão:

- imports não utilizados;
- variáveis não utilizadas;
- erros simples de programação;
- código redundante;
- problemas de organização;
- problemas de estilo;
- algumas construções inadequadas.
"""
)


# ============================================================
# EXEMPLO 01
# ============================================================

st.subheader("📌 Exemplo — Import não utilizado")

st.code(
    """import os
import sys

print("TechPort")
""",
    language="python",
)

st.write(
    "O módulo `os` foi importado, mas não está sendo utilizado."
)

st.code(
    "F401 `os` imported but unused",
    language="text",
)

st.info(
    "Isso não significa necessariamente que a aplicação deixou de funcionar. "
    "Significa que existe um problema de qualidade ou organização do código."
)


# ============================================================
# EXEMPLO 02
# ============================================================

st.subheader("📌 Exemplo — Variável não utilizada")

st.code(
    """def cadastrar_usuario():
    nome = "Mariana"
    idade = 30

    return nome
""",
    language="python",
)

st.write(
    "A variável `idade` foi criada, mas nunca foi utilizada."
)

st.code(
    """MAIS LIMPO
    ↓
MAIS LEGÍVEL
    ↓
MAIS FÁCIL DE MANTER
""",
    language="text",
)


# ============================================================
# COMANDO
# ============================================================

st.divider()

st.subheader("💻 Executando no TechPort")

st.write("O comando utilizado no projeto é:")

st.code(
    "python -m ruff check .",
    language="powershell",
)

st.markdown(
    """
O ponto final (`.`) significa:

> Analise o projeto a partir do diretório atual.
"""
)


# ============================================================
# FLUXO
# ============================================================

st.subheader("🔄 O que acontecerá?")

st.code(
    """python -m ruff check .
          ↓
Ruff percorre os arquivos
          ↓
Analisa o código Python
          ↓
Aplica suas regras
          ↓
Encontra problemas?
       ↙       ↘
     NÃO        SIM
      ↓          ↓
   SUCESSO    RELATÓRIO
""",
    language="text",
)


# ============================================================
# EXECUTAR RUFF
# ============================================================

st.divider()

st.subheader("▶ Executar análise")

if st.button(
    "▶ Executar Ruff",
    type="primary",
    use_container_width=True,
):
    result = run_command(
        python_command(
            "-m",
            "ruff",
            "check",
            ".",
        ),
        "Ruff",
    )

    st.subheader("🖥️ Resultado da análise")

    show_command_result(
        result,
        success_message="Ruff não encontrou violações bloqueantes.",
        error_message=(
            "Ruff encontrou problemas no código. "
            "Analise as informações apresentadas no terminal."
        ),
    )


# ============================================================
# COMO LER O RESULTADO
# ============================================================

st.divider()

st.subheader("📖 Como interpretar o resultado do Ruff")

st.markdown(
    """
Quando o Ruff encontra um problema, normalmente apresenta informações
que ajudam a localizar exatamente onde ele está.

Exemplo:

```text
app/main.py:10:1: F401 `os` imported but unused
```
"""
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info(
        """
### Arquivo

`app/main.py`

Arquivo onde o problema foi encontrado.
"""
    )

with col2:
    st.info(
        """
### Linha

`10`

Linha do código onde o problema está localizado.
"""
    )

with col3:
    st.info(
        """
### Código

`F401`

Identificador da regra que foi violada.
"""
    )

with col4:
    st.info(
        """
### Descrição

`imported but unused`

Explicação do problema encontrado.
"""
    )


# ============================================================
# CÓDIGOS DO RUFF
# ============================================================

st.subheader("🏷️ O que são códigos como F401?")

st.write(
    "O Ruff utiliza códigos para identificar diferentes categorias "
    "de problemas."
)

st.code(
    """QUAL REGRA
    ↓
FOI VIOLADA
    ↓
EM QUAL ARQUIVO
    ↓
EM QUAL LINHA
""",
    language="text",
)


# ============================================================
# RESULTADO SEM PROBLEMAS
# ============================================================

st.subheader("✅ E se o Ruff não encontrar problemas?")

st.code(
    """RUFF
  ↓
ANALISA
  ↓
0 PROBLEMAS
  ↓
SUCESSO
""",
    language="text",
)

st.success(
    "Isso significa que o código passou pelas regras de análise "
    "estática configuradas no Ruff."
)


# ============================================================
# RESULTADO COM PROBLEMAS
# ============================================================

st.subheader("❌ E se o Ruff encontrar problemas?")

st.code(
    """RUFF
  ↓
ANALISA
  ↓
ENCONTRA PROBLEMAS
  ↓
MOSTRA ARQUIVO
  ↓
MOSTRA LINHA
  ↓
MOSTRA REGRA
  ↓
MOSTRA DESCRIÇÃO
""",
    language="text",
)

st.warning(
    "Um problema encontrado pelo Ruff não é necessariamente uma "
    "falha funcional da aplicação. Ele representa uma violação "
    "de alguma regra de análise estática."
)


# ============================================================
# RELAÇÃO COM SHIFT LEFT
# ============================================================

st.divider()

st.subheader("⬅️ Ruff e Shift Left")

st.markdown(
    """
O Ruff também representa a ideia de **Shift Left** estudada na aula.

Em vez de descobrir problemas somente depois da aplicação estar pronta:

```text
DESENVOLVER
    ↓
ENTREGAR
    ↓
DESCOBRIR PROBLEMA
```

podemos analisar o código enquanto estamos desenvolvendo:

```text
ESCREVER CÓDIGO
      ↓
     RUFF
      ↓
IDENTIFICAR PROBLEMA
      ↓
   CORRIGIR
      ↓
CONTINUAR DESENVOLVENDO
```

Quanto mais cedo identificamos problemas, mais fácil tende a ser
a correção.
"""
)


# ============================================================
# RUFF NO TECHPORT
# ============================================================

st.subheader("🏗️ Ruff dentro do TechPort")

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
└── tests/
        ↓
       RUFF
        ↓
ANÁLISE ESTÁTICA
""",
    language="text",
)

st.write(
    "Dessa forma, podemos analisar diferentes partes do projeto "
    "antes mesmo de executar a aplicação."
)


# ============================================================
# KIT DE QUALIDADE
# ============================================================

st.divider()

st.subheader("🧰 Onde o Ruff entra no nosso kit de qualidade?")

st.code(
    """pytest
   ↓
O comportamento está correto?

pytest-cov
   ↓
Quanto do código foi executado pelos testes?

Ruff
   ↓
O código possui problemas de qualidade detectáveis estaticamente?

mypy
   ↓
Os tipos utilizados no código estão coerentes?

Bandit
   ↓
Existem padrões potencialmente inseguros?

pip-audit
   ↓
Existem vulnerabilidades conhecidas nas dependências?
""",
    language="text",
)

st.info(
    "Nenhuma dessas ferramentas substitui completamente as outras. "
    "Cada uma analisa uma dimensão diferente da qualidade do software."
)


# ============================================================
# RESUMO
# ============================================================

st.divider()

st.subheader("📘 Resumo para memorizar")

st.code(
    """RUFF
    ↓
ANÁLISE ESTÁTICA
    ↓
NÃO EXECUTA A APLICAÇÃO
    ↓
ANALISA O CÓDIGO
    ↓
IDENTIFICA VIOLAÇÕES
    ↓
ARQUIVO + LINHA + REGRA + DESCRIÇÃO
""",
    language="text",
)

st.markdown(
    """
**Ruff**  
Ferramenta rápida de análise estática para código Python.

**Análise estática**  
Análise realizada sem precisar executar a aplicação.

**Código da regra**  
Identificador do tipo de problema encontrado, como `F401`.

**Linha**  
Localização do problema dentro do arquivo.

**Shift Left**  
Identificar problemas o mais cedo possível durante o desenvolvimento.
"""
)

st.success(
    "🧹 O objetivo do Ruff não é provar que o sistema funciona. "
    "O objetivo é ajudar a manter o código mais consistente, "
    "organizado e fácil de manter."
)
