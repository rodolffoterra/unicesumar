# 🧪 TechPort --- Laboratório de Testes de Software com Python

## Projeto, Implementação e Teste de Software

**Professor Rodolfo Terra**

Este laboratório utiliza o projeto **TechPort** como ambiente prático
para estudar testes de software, qualidade de código, cobertura, análise
estática e segurança utilizando Python.

O objetivo é permitir que o estudante não apenas execute ferramentas,
mas também compreenda **o que cada resultado significa**, como
interpretar falhas e como utilizar testes para aumentar a confiabilidade
de uma aplicação.

------------------------------------------------------------------------

## 🎯 Objetivos do laboratório

Ao final do laboratório, o estudante deverá ser capaz de:

-   preparar um ambiente Python para testes;
-   compreender a importância da Virtual Environment;
-   instalar e validar as dependências do projeto;
-   executar testes automatizados;
-   interpretar resultados `PASSED`, `FAILED`, `ERROR` e `SKIPPED`;
-   compreender os códigos de saída do pytest;
-   medir a cobertura dos testes;
-   identificar partes do código ainda não exercitadas;
-   diferenciar cobertura de qualidade;
-   utilizar ferramentas automatizadas de qualidade;
-   compreender análise estática e segurança;
-   interpretar problemas encontrados pelas ferramentas;
-   relacionar testes automatizados com práticas de qualidade de
    software.

------------------------------------------------------------------------

# 🏗️ Projeto utilizado

O laboratório utiliza o **TechPort**, uma aplicação desenvolvida ao
longo da disciplina.

A arquitetura trabalhada no projeto segue, de forma simplificada:

``` text
STREAMLIT
    ↓
FASTAPI
    ↓
SERVICE
    ↓
REPOSITORY
    ↓
MYSQL
```

A partir dessa aplicação, adicionamos uma nova dimensão:

``` text
DESENVOLVIMENTO
      ↓
   TECHPORT
      ↓
     TESTES
      ↓
   QUALIDADE
      ↓
  CONFIANÇA
```

------------------------------------------------------------------------

# 📁 Estrutura geral

Uma organização típica do laboratório é:

``` text
techport/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── pages/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── utils/
│       └── test_runner.py
│
├── tests/
│   └── test_primeiro_teste.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

A pasta `tests` concentra os testes automatizados, enquanto
`app/utils/test_runner.py` fornece funções auxiliares utilizadas pelas
páginas didáticas do Streamlit.

------------------------------------------------------------------------

# 1️⃣ Preparação do ambiente

Antes de executar qualquer teste, precisamos garantir que o ambiente
esteja corretamente configurado.

Um ambiente inconsistente pode produzir erros mesmo quando o código da
aplicação está correto.

## Criar a Virtual Environment

No terminal do VS Code:

``` powershell
python -m venv .venv
```

## Ativar a `.venv`

No PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Quando estiver ativa, normalmente veremos:

``` text
(.venv)
```

antes do caminho no terminal.

## Instalar as dependências

``` powershell
python -m pip install -r requirements.txt
```

## Conferir as bibliotecas

``` powershell
python -m pip list
```

Utilizamos `python -m pip` para garantir que o `pip` executado pertence
ao mesmo Python utilizado pelo projeto.

------------------------------------------------------------------------

# 2️⃣ Executando o TechPort

Com a `.venv` ativa e as dependências instaladas:

``` powershell
python -m streamlit run app/main.py
```

A aplicação será aberta no navegador e as páginas do laboratório poderão
ser utilizadas para executar e interpretar as ferramentas.

------------------------------------------------------------------------

# 3️⃣ Testes automatizados com pytest

O **pytest** é utilizado para localizar e executar testes Python.

Comando básico:

``` powershell
python -m pytest
```

Para uma saída mais detalhada:

``` powershell
python -m pytest -v
```

## Estrutura básica de um teste

``` python
def somar(a, b):
    return a + b


def test_somar():
    resultado = somar(2, 3)
    assert resultado == 5
```

O fluxo é:

``` text
PREPARAR
   ↓
EXECUTAR
   ↓
OBTER RESULTADO
   ↓
COMPARAR
   ↓
DECIDIR
```

O `assert` compara o resultado obtido com aquilo que era esperado.

------------------------------------------------------------------------

# 4️⃣ Interpretando o pytest

Os principais estados encontrados durante o laboratório são:

  -----------------------------------------------------------------------
  Estado                              Significado
  ----------------------------------- -----------------------------------
  `PASSED`                            O resultado obtido foi o esperado

  `FAILED`                            O teste executou, mas o resultado
                                      foi diferente do esperado

  `ERROR`                             O pytest encontrou um problema que
                                      impediu a execução normal

  `SKIPPED`                           O teste existe, mas foi ignorado

  `NO TESTS`                          Nenhum teste foi encontrado
  -----------------------------------------------------------------------

## Códigos de saída

    Código Significado
  -------- ----------------------------
       `0` Todos os testes passaram
       `1` Um ou mais testes falharam
       `2` Execução interrompida
       `3` Erro interno do pytest
       `4` Uso incorreto do pytest
       `5` Nenhum teste foi coletado

Um ponto importante:

``` text
Exit Code 5
≠
5 testes passaram
```

Ele significa:

``` text
Nenhum teste foi coletado.
```

------------------------------------------------------------------------

# 5️⃣ Testando regras do TechPort

Os testes não precisam verificar apenas funções matemáticas simples.

Podemos testar regras relacionadas ao próprio sistema.

Exemplos de perguntas que um teste pode responder:

``` text
Todo chamado possui usuário?
Todo chamado da semana possui técnico?
Um chamado pode possuir prioridade inválida?
Os dados retornados possuem a estrutura esperada?
Uma determinada regra de negócio está sendo respeitada?
```

Isso aproxima o teste automatizado das regras reais da aplicação.

------------------------------------------------------------------------

# 6️⃣ Cobertura de testes

Executar testes é importante, mas também precisamos saber **quanto do
código está sendo exercitado**.

Para isso utilizamos:

-   pytest;
-   pytest-cov;
-   coverage.py.

Execute:

``` powershell
python -m pytest --cov=app --cov-report=term-missing
```

## Entendendo o comando

  Comando                       Função
  ----------------------------- ----------------------------------
  `python -m pytest`            Executa os testes
  `--cov=app`                   Mede a cobertura do pacote `app`
  `--cov-report=term-missing`   Exibe as linhas não executadas

Exemplo de relatório:

``` text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
app/services/usuario.py     40      5    88%   32-35, 48
app/main.py                 80     20    75%   50-60
------------------------------------------------------
TOTAL                      120     25    79%
```

## Significado

-   `Name`: arquivo analisado;
-   `Stmts`: instruções existentes;
-   `Miss`: instruções não executadas;
-   `Cover`: percentual de cobertura;
-   `Missing`: linhas ainda não exercitadas.

------------------------------------------------------------------------

# ⚠️ Cobertura não é qualidade

Este é um dos conceitos mais importantes do laboratório.

``` text
100% DE COBERTURA
        ≠
100% DE QUALIDADE
```

Cobertura responde:

> Quais partes do código foram executadas durante os testes?

Ela não responde sozinha:

> O software está completamente correto?

Um projeto pode possuir alta cobertura e ainda apresentar:

-   testes mal escritos;
-   regras de negócio incorretas;
-   asserts fracos;
-   casos extremos não avaliados;
-   vulnerabilidades;
-   problemas de desempenho;
-   comportamentos incorretos.

Portanto:

``` text
COBERTURA
    +
QUALIDADE DOS TESTES
    +
ANÁLISE DO CÓDIGO
    +
SEGURANÇA
    =
MAIOR CONFIANÇA
```

------------------------------------------------------------------------

# 7️⃣ FAILED não significa falha da cobertura

Durante a execução:

``` powershell
python -m pytest --cov=app --cov-report=term-missing
```

é possível obter:

``` text
4 passed
2 failed
```

e ainda assim receber normalmente um relatório de cobertura.

Nesse cenário:

``` text
PYTEST
   ↓
2 TESTES FALHARAM
   ↓
EXIT CODE 1
```

ao mesmo tempo:

``` text
PYTEST-COV
   ↓
MEDIU O CÓDIGO EXECUTADO
   ↓
RELATÓRIO GERADO
```

Portanto, precisamos diferenciar:

**resultado dos testes** de **resultado da medição de cobertura**.

------------------------------------------------------------------------

# 8️⃣ Análise estática

Além dos testes, o projeto pode utilizar ferramentas que analisam o
código sem necessariamente executar todas as regras da aplicação.

## Ruff

Utilizado para encontrar problemas de estilo e qualidade:

``` powershell
python -m ruff check .
```

## mypy

Utilizado para análise de tipos:

``` powershell
python -m mypy app
```

Essas ferramentas ajudam a encontrar problemas antecipadamente.

------------------------------------------------------------------------

# 9️⃣ Segurança

Qualidade de software também envolve segurança.

## Bandit

Analisa código Python procurando padrões potencialmente inseguros:

``` powershell
python -m bandit -r app
```

## pip-audit

Analisa as dependências instaladas procurando vulnerabilidades
conhecidas:

``` powershell
python -m pip_audit
```

Temos então duas perspectivas:

``` text
BANDIT
   ↓
NOSSO CÓDIGO
```

e:

``` text
PIP-AUDIT
   ↓
NOSSAS DEPENDÊNCIAS
```

------------------------------------------------------------------------

# 🔟 Estratégia Shift Left

Uma das ideias trabalhadas no laboratório é detectar problemas **o mais
cedo possível**.

``` text
REQUISITO
   ↓
DESENVOLVIMENTO
   ↓
TESTES
   ↓
PRODUÇÃO
```

Quanto mais cedo encontrarmos um defeito, mais cedo podemos corrigi-lo.

Por isso incorporamos verificações durante o desenvolvimento:

``` text
CÓDIGO
  ↓
RUFF
  ↓
MYPY
  ↓
BANDIT
  ↓
PYTEST
  ↓
COVERAGE
  ↓
PIP-AUDIT
  ↓
MAIOR CONFIANÇA
```

------------------------------------------------------------------------

# 🧠 Erro, defeito e falha

Esses conceitos não representam exatamente a mesma coisa.

``` text
ERRO HUMANO
     ↓
DEFEITO NO SOFTWARE
     ↓
EXECUÇÃO
     ↓
FALHA OBSERVÁVEL
```

Os testes procuram aumentar nossa capacidade de encontrar defeitos antes
que eles causem problemas aos usuários.

------------------------------------------------------------------------

# 🔄 TDD --- Red, Green, Refactor

Outra estratégia importante é o **Test-Driven Development**.

``` text
RED
↓
escrever um teste que falha

GREEN
↓
implementar o mínimo necessário para passar

REFACTOR
↓
melhorar o código mantendo o teste funcionando
```

Fluxo:

``` text
RED → GREEN → REFACTOR → RED → GREEN → REFACTOR
```

O teste passa a fazer parte do processo de desenvolvimento.

------------------------------------------------------------------------

# 🏭 Integração contínua

As ferramentas executadas manualmente no laboratório também podem fazer
parte de uma esteira automatizada.

Exemplo:

``` text
DESENVOLVEDOR
      ↓
     GIT
      ↓
   PUSH / PR
      ↓
CI / GITHUB ACTIONS
      ↓
┌─────────────────┐
│ Ruff            │
│ mypy            │
│ Bandit          │
│ pip-audit       │
│ pytest          │
│ pytest-cov      │
└─────────────────┘
      ↓
RESULTADO AUTOMÁTICO
```

Assim, a qualidade deixa de depender exclusivamente de verificações
manuais.

------------------------------------------------------------------------

# 🧪 Sequência sugerida para o laboratório

1.  Abrir o projeto TechPort.
2.  Criar ou ativar a `.venv`.
3.  Instalar o `requirements.txt`.
4.  Conferir o Python utilizado.
5.  Executar o Streamlit.
6.  Abrir o ambiente de testes.
7.  Conferir as bibliotecas instaladas.
8.  Executar os testes com pytest.
9.  Interpretar `PASSED`, `FAILED`, `ERROR` e `SKIPPED`.
10. Executar a cobertura.
11. Identificar arquivos com baixa cobertura.
12. Relacionar testes com as regras do TechPort.
13. Executar ferramentas de análise estática.
14. Executar verificações de segurança.
15. Discutir como essas verificações poderiam ser automatizadas em
    CI/CD.

------------------------------------------------------------------------

# 📚 Comandos principais

``` powershell
# Criar ambiente virtual
python -m venv .venv

# Ativar
.\.venv\Scripts\Activate.ps1

# Instalar dependências
python -m pip install -r requirements.txt

# Listar bibliotecas
python -m pip list

# Executar Streamlit
python -m streamlit run app/main.py

# Executar pytest
python -m pytest -v

# Executar cobertura
python -m pytest --cov=app --cov-report=term-missing

# Ruff
python -m ruff check .

# mypy
python -m mypy app

# Bandit
python -m bandit -r app

# pip-audit
python -m pip_audit
```

------------------------------------------------------------------------

# 🎓 O que aprendemos?

Ao final deste laboratório, o principal aprendizado não é simplesmente
executar comandos.

Precisamos compreender que:

``` text
TESTAR
   ≠
APENAS PROCURAR ERROS
```

Testar significa produzir evidências sobre o comportamento e a qualidade
do software.

O processo completo pode ser resumido como:

``` text
DESENVOLVER
     ↓
VERIFICAR
     ↓
TESTAR
     ↓
MEDIR
     ↓
ANALISAR
     ↓
CORRIGIR
     ↓
MELHORAR
```

## Conclusão

> **Testes não provam que um software não possui defeitos. Eles aumentam
> nossa confiança de que o sistema se comporta como esperamos.**

A qualidade é construída continuamente durante todo o processo de
desenvolvimento.

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**\
**Disciplina:** Projeto, Implementação e Teste de Software

**LinkedIn:** https://www.linkedin.com/in/rodolffoterra/\
**GitHub:** https://github.com/rodolffoterra

------------------------------------------------------------------------

### TechPort

Projeto acadêmico utilizado para demonstrar, de forma prática, conceitos
de arquitetura, banco de dados, APIs, desenvolvimento, testes e
qualidade de software.
