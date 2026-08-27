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
    page_title="TechPort | mypy",
    page_icon="🔤",
    layout="wide",
)


# ============================================================
# FUNÇÕES AUXILIARES
# Compatíveis com Python 3.9
# ============================================================

def extrair_erros_mypy(output):
    """
    Extrai mensagens do mypy no formato:
    arquivo.py:linha: error: mensagem [codigo]
    """
    erros = []

    padrao = re.compile(
        r"^(.*?\.py):(\d+)(?::(\d+))?:\s+error:\s+(.*?)(?:\s+\[([^\]]+)\])?$"
    )

    for linha in output.splitlines():
        match = padrao.match(linha.strip())

        if match:
            erros.append(
                {
                    "arquivo": match.group(1),
                    "linha": match.group(2),
                    "coluna": match.group(3) or "-",
                    "mensagem": match.group(4),
                    "codigo": match.group(5) or "não informado",
                }
            )

    return erros


def extrair_resumo_mypy(output):
    """
    Extrai o resumo final apresentado pelo mypy.
    """
    resultado = {
        "erros": 0,
        "arquivos_com_erro": 0,
        "arquivos_verificados": 0,
        "sucesso": False,
    }

    match_erro = re.search(
        r"Found\s+(\d+)\s+errors?\s+in\s+(\d+)\s+files?",
        output,
        flags=re.IGNORECASE,
    )

    if match_erro:
        resultado["erros"] = int(match_erro.group(1))
        resultado["arquivos_com_erro"] = int(match_erro.group(2))

    match_sucesso = re.search(
        r"Success:\s+no issues found in\s+(\d+)\s+source files?",
        output,
        flags=re.IGNORECASE,
    )

    if match_sucesso:
        resultado["sucesso"] = True
        resultado["arquivos_verificados"] = int(match_sucesso.group(1))

    return resultado


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🔤 5. mypy — Validação de tipos")

st.write(
    "O mypy realiza análise estática de tipos no código Python. "
    "Ele compara as anotações de tipo declaradas pelo desenvolvedor "
    "com a forma como valores, parâmetros e retornos são utilizados."
)

st.code(
    "python -m mypy app",
    language="powershell",
)

st.caption(
    "Categoria: análise estática de tipos."
)

st.info(
    "O mypy não precisa executar o TechPort para encontrar "
    "inconsistências de tipagem."
)


# ============================================================
# O QUE É TIPAGEM?
# ============================================================

st.subheader("🧠 Primeiro: o que é um tipo?")

st.markdown(
    """
Em Python, os valores possuem tipos.

```python
nome = "Mariana"       # str
idade = 30             # int
ativo = True           # bool
valor = 150.50         # float
```

Podemos também declarar explicitamente o tipo esperado:

```python
nome: str = "Mariana"
idade: int = 30
```

Essas informações ajudam o desenvolvedor e ferramentas como o `mypy`
a compreenderem o que esperamos do código.
"""
)


# ============================================================
# EXEMPLO DE FUNÇÃO
# ============================================================

st.subheader("📌 Exemplo — Parâmetros e retorno")

st.code(
    """def somar(a: int, b: int) -> int:
    return a + b
""",
    language="python",
)

st.markdown(
    """
Podemos interpretar essa assinatura assim:

```text
a: int
   ↓
esperamos um número inteiro

b: int
   ↓
esperamos um número inteiro

-> int
   ↓
esperamos que a função retorne um inteiro
```
"""
)


# ============================================================
# EXEMPLO DE ERRO
# ============================================================

st.subheader("❌ Exemplo — Retorno incompatível")

st.code(
    """def calcular_idade() -> int:
    return "30"
""",
    language="python",
)

st.write(
    "A função declara que retornará um `int`, mas está retornando uma `str`."
)

st.code(
    """DECLARADO
int
 ↓
FUNÇÃO
 ↓
RETORNO REAL
str
 ↓
INCOMPATIBILIDADE
""",
    language="text",
)

st.warning(
    "Esse tipo de inconsistência pode ser identificado pelo mypy "
    "antes mesmo de executarmos a função."
)


# ============================================================
# PYTHON X MYPY
# ============================================================

st.subheader("⚖️ Python × mypy")

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
### 🐍 Python

Python possui tipagem dinâmica.

É possível escrever:

```python
valor = 10
valor = "TechPort"
```

O tipo da variável pode mudar durante a execução.
"""
    )

with col2:
    st.info(
        """
### 🔤 mypy

O mypy utiliza as anotações de tipo para procurar inconsistências.

```text
CÓDIGO
  ↓
ANOTAÇÕES
  ↓
MYPY
  ↓
COERÊNCIA DE TIPOS
```
"""
    )


# ============================================================
# O QUE O MYPY PODE ANALISAR?
# ============================================================

st.subheader("🔎 O que o mypy pode encontrar?")

st.markdown(
    """
Entre as situações analisadas estão:

- retorno incompatível com o tipo declarado;
- argumento incompatível com o parâmetro;
- atribuição de valor com tipo inesperado;
- operações incompatíveis entre tipos;
- atributos inexistentes;
- uso incorreto de valores opcionais;
- incompatibilidades entre funções e métodos;
- problemas em anotações de tipos.
"""
)


# ============================================================
# EXEMPLO ARGUMENTO
# ============================================================

st.subheader("📌 Exemplo — Argumento incompatível")

st.code(
    """def buscar_usuario(usuario_id: int):
    return usuario_id


buscar_usuario("10")
""",
    language="python",
)

st.markdown(
    """
A função espera:

```text
usuario_id
    ↓
   int
```

mas recebeu:

```text
"10"
 ↓
str
```

O mypy pode sinalizar essa diferença antes da execução.
"""
)


# ============================================================
# EXECUTANDO
# ============================================================

st.divider()

st.subheader("💻 Executando no TechPort")

st.code(
    "python -m mypy app",
    language="powershell",
)

st.markdown(
    """
O comando pode ser lido assim:

```text
python
   ↓
executa o módulo

mypy
   ↓
ferramenta de análise

app
   ↓
pasta que será analisada
```
"""
)


# ============================================================
# FLUXO
# ============================================================

st.subheader("🔄 O que acontecerá?")

st.code(
    """CÓDIGO DO TECHPORT
        ↓
      MYPY
        ↓
LÊ AS ANOTAÇÕES DE TIPO
        ↓
COMPARA OS USOS
        ↓
EXISTEM INCONSISTÊNCIAS?
      ↙             ↘
    NÃO              SIM
     ↓                ↓
  SUCESSO          RELATÓRIO
""",
    language="text",
)


# ============================================================
# EXECUÇÃO REAL
# ============================================================

st.divider()

st.subheader("▶ Executar análise de tipos")

if st.button(
    "▶ Executar mypy",
    type="primary",
    use_container_width=True,
):

    result = run_command(
        python_command(
            "-m",
            "mypy",
            "app",
        ),
        "mypy",
    )

    output = result.output

    resumo = extrair_resumo_mypy(output)
    erros = extrair_erros_mypy(output)

    st.subheader("🖥️ Resultado da análise")

    show_command_result(
        result,
        success_message="mypy concluiu sem erros de tipagem.",
        error_message=(
            "mypy encontrou inconsistências de tipos. "
            "Analise os arquivos, linhas e mensagens abaixo."
        ),
    )

    # ========================================================
    # INDICADORES
    # ========================================================

    st.divider()
    st.subheader("📊 Resumo do mypy")

    total_erros = resumo["erros"]

    # Caso o formato do resumo não seja reconhecido,
    # usamos a quantidade extraída das linhas.
    if total_erros == 0 and erros:
        total_erros = len(erros)

    arquivos_com_erro = resumo["arquivos_com_erro"]

    if arquivos_com_erro == 0 and erros:
        arquivos_com_erro = len(
            set(erro["arquivo"] for erro in erros)
        )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🔤 Erros de tipagem",
        total_erros,
    )

    c2.metric(
        "📄 Arquivos com erro",
        arquivos_com_erro,
    )

    if result.returncode == 0:
        c3.metric(
            "✅ Resultado",
            "APROVADO",
        )
    else:
        c3.metric(
            "❌ Resultado",
            "REVISAR",
        )

    # ========================================================
    # ERROS INDIVIDUAIS
    # ========================================================

    if erros:
        st.divider()
        st.subheader("❌ Inconsistências encontradas")

        st.write(
            "Cada bloco abaixo representa um problema de tipagem "
            "identificado pelo mypy."
        )

        for indice, erro in enumerate(erros, start=1):

            st.markdown(
                "### {}. `{}`".format(
                    indice,
                    erro["codigo"],
                )
            )

            c1, c2, c3 = st.columns(3)

            c1.info(
                "**Arquivo**\n\n`{}`".format(
                    erro["arquivo"]
                )
            )

            c2.info(
                "**Linha**\n\n`{}`".format(
                    erro["linha"]
                )
            )

            c3.info(
                "**Código**\n\n`{}`".format(
                    erro["codigo"]
                )
            )

            st.error(
                erro["mensagem"]
            )

            st.markdown(
                """
**Como interpretar:**

```text
ARQUIVO
   ↓
onde o problema está

LINHA
   ↓
posição aproximada no código

CÓDIGO
   ↓
categoria do problema

MENSAGEM
   ↓
explicação do que o mypy encontrou
```
"""
            )

            st.divider()

    elif result.returncode == 0:
        st.success(
            "✅ Nenhuma inconsistência de tipos foi encontrada "
            "nas regras analisadas pelo mypy."
        )


# ============================================================
# COMO LER UMA MENSAGEM
# ============================================================

st.divider()

st.subheader("📖 Como ler uma mensagem do mypy")

st.code(
    'app/services/usuario_service.py:20: error: '
    'Incompatible return value type (got "str", expected "int") '
    '[return-value]',
    language="text",
)

st.markdown(
    """
Podemos dividir esse resultado em partes:
"""
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info(
        """
### Arquivo

`usuario_service.py`

Local onde a inconsistência foi encontrada.
"""
    )

with c2:
    st.info(
        """
### Linha

`20`

Linha aproximada onde o mypy encontrou o problema.
"""
    )

with c3:
    st.info(
        """
### Código

`return-value`

Categoria da inconsistência encontrada.
"""
    )

with c4:
    st.info(
        """
### Mensagem

`got str, expected int`

Recebido `str`, mas era esperado `int`.
"""
    )


# ============================================================
# GOT X EXPECTED
# ============================================================

st.subheader("🎯 Entendendo `got` e `expected`")

st.code(
    """expected int
      ↓
o código declarou que esperava inteiro

got str
   ↓
o mypy encontrou uma string
""",
    language="text",
)

st.markdown(
    """
Essa leitura é muito importante:

> **expected** = o tipo esperado.

> **got** = o tipo realmente identificado pelo mypy.
"""
)


# ============================================================
# CÓDIGOS COMUNS
# ============================================================

st.subheader("🏷️ Exemplos de categorias de erro")

st.markdown(
    """
O código exibido entre colchetes ajuda a classificar o problema.

| Exemplo | Interpretação didática |
|---|---|
| `return-value` | retorno incompatível |
| `arg-type` | argumento com tipo incompatível |
| `assignment` | atribuição incompatível |
| `attr-defined` | atributo não reconhecido |
| `operator` | operação incompatível entre tipos |
| `union-attr` | acesso potencialmente inválido em tipo opcional/união |

Os códigos exibidos dependem do problema encontrado e da configuração
do mypy utilizada no projeto.
"""
)


# ============================================================
# EXEMPLO TECHPORT
# ============================================================

st.divider()

st.subheader("🏗️ Exemplo aplicado ao TechPort")

st.code(
    """def buscar_usuario(usuario_id: int) -> dict:
    ...

usuario = buscar_usuario("ABC")
""",
    language="python",
)

st.markdown(
    """
A regra declarada foi:

```text
usuario_id
    ↓
   int
```

Mas a chamada enviou:

```text
"ABC"
  ↓
 str
```

O mypy pode identificar essa incompatibilidade antes que esse fluxo
chegue ao Repository ou ao banco de dados.
"""
)


# ============================================================
# MYPY NÃO É TESTE FUNCIONAL
# ============================================================

st.subheader("⚠️ mypy não substitui pytest")

st.markdown(
    """
Um código pode passar no mypy e ainda possuir uma regra de negócio errada.

Exemplo:

```python
def somar(a: int, b: int) -> int:
    return a - b
```

Os tipos estão corretos:

```text
int + int
    ↓
retorno int
```

Porém a lógica está errada.

Por isso:

```text
MYPY
 ↓
TIPOS

PYTEST
 ↓
COMPORTAMENTO
```

As ferramentas são complementares.
"""
)


# ============================================================
# MYPY E SHIFT LEFT
# ============================================================

st.divider()

st.subheader("⬅️ mypy e Shift Left")

st.code(
    """DESENVOLVEDOR ESCREVE O CÓDIGO
            ↓
      DECLARA OS TIPOS
            ↓
           MYPY
            ↓
IDENTIFICA INCOMPATIBILIDADE
            ↓
         CORRIGE
            ↓
CONTINUA O DESENVOLVIMENTO
""",
    language="text",
)

st.write(
    "Isso permite descobrir determinados problemas antes de "
    "executar a aplicação, integrar módulos ou entregar o software."
)


# ============================================================
# KIT DE QUALIDADE
# ============================================================

st.divider()

st.subheader("🧰 Onde o mypy entra no nosso kit de qualidade?")

st.code(
    """pytest
   ↓
O comportamento está correto?

pytest-cov
   ↓
Quanto do código foi exercitado?

Ruff
   ↓
Existem problemas de qualidade detectáveis estaticamente?

mypy
   ↓
Os tipos utilizados estão coerentes?

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
    "Cada ferramenta observa uma dimensão diferente da qualidade. "
    "O mypy está focado principalmente na coerência dos tipos."
)


# ============================================================
# RESULTADOS POSSÍVEIS
# ============================================================

st.subheader("🚦 Como interpretar o resultado geral?")

col1, col2 = st.columns(2)

with col1:
    st.success(
        """
### ✅ Sem erros

O mypy terminou sem encontrar inconsistências dentro da análise realizada.

Isso significa:

```text
ANOTAÇÕES
   ↓
USOS ANALISADOS
   ↓
COERENTES
```

Não significa que o sistema inteiro está livre de defeitos.
"""
    )

with col2:
    st.error(
        """
### ❌ Com erros

O mypy encontrou uma ou mais inconsistências.

O próximo passo é observar:

```text
arquivo
  ↓
linha
  ↓
código
  ↓
mensagem
  ↓
correção
```
"""
    )


# ============================================================
# RESUMO
# ============================================================

st.divider()

st.subheader("📘 Resumo para memorizar")

st.code(
    """MYPY
   ↓
ANÁLISE ESTÁTICA DE TIPOS
   ↓
NÃO PRECISA EXECUTAR A APLICAÇÃO
   ↓
COMPARA TIPOS DECLARADOS E UTILIZADOS
   ↓
IDENTIFICA INCONSISTÊNCIAS
   ↓
ARQUIVO + LINHA + CÓDIGO + MENSAGEM
""",
    language="text",
)

st.markdown(
    """
**mypy**  
Ferramenta de análise estática de tipos para Python.

**Type hint**  
Anotação que informa qual tipo esperamos em uma variável, parâmetro ou retorno.

**expected**  
Tipo que o código declarou como esperado.

**got**  
Tipo que o mypy identificou no uso analisado.

**Análise estática**  
Análise feita sem precisar executar a aplicação.

**Importante**  
Passar no mypy não significa que a regra de negócio está correta.
"""
)

st.success(
    "🔤 O objetivo do mypy é encontrar incompatibilidades de tipos "
    "o mais cedo possível e tornar o código mais previsível e fácil de manter."
)
