# Aula 02 --- Linguagem SQL: Consultando e Analisando Dados

**Disciplina:** Banco de Dados e Mineração de Dados\
**Professor:** Rodolfo Terra

🔗 [LinkedIn](https://www.linkedin.com/in/rodolffoterra/)\
💻 [GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## 📚 Visão Geral

Nesta aula avançamos dos fundamentos de Banco de Dados para a utilização
da **SQL (Structured Query Language)**, linguagem utilizada para
consultar, manipular e estruturar dados em bancos relacionais.

A aula utiliza o banco de dados de exemplo **WORLD**, do MySQL, para
transformar perguntas de negócio em consultas SQL e, posteriormente,
transformar os resultados dessas consultas em informação útil para
análise e tomada de decisão.

A evolução da aula segue uma ideia central:

``` text
DADOS
   ↓
SQL
   ↓
CONSULTAS
   ↓
INFORMAÇÃO
   ↓
DECISÃO
```

------------------------------------------------------------------------

## 🎯 O que vamos aprender?

Ao final da aula, o aluno deverá ser capaz de:

-   compreender o que é SQL;
-   reconhecer as principais categorias de comandos SQL;
-   utilizar o comando `SELECT`;
-   selecionar apenas as colunas necessárias;
-   filtrar registros utilizando `WHERE`;
-   utilizar operadores de comparação;
-   combinar condições com `AND` e `OR`;
-   ordenar resultados com `ORDER BY`;
-   limitar resultados utilizando `LIMIT`;
-   aplicar funções de agregação;
-   utilizar `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`;
-   agrupar informações utilizando `GROUP BY`;
-   combinar `GROUP BY` e `ORDER BY`;
-   compreender relacionamentos entre tabelas;
-   utilizar `JOIN` e `INNER JOIN`;
-   combinar `JOIN` com filtros;
-   utilizar aliases para melhorar a legibilidade;
-   resolver consultas práticas utilizando o banco WORLD.

------------------------------------------------------------------------

# 🧠 O que é SQL?

**SQL --- Structured Query Language** é a linguagem utilizada para
trabalhar com bancos de dados relacionais.

Com SQL podemos:

``` text
CRIAR
CONSULTAR
INSERIR
ALTERAR
EXCLUIR
ORGANIZAR
```

Uma aplicação pode enviar comandos SQL para um SGBD, como o MySQL, que
processa a solicitação e devolve os dados correspondentes.

``` text
Pergunta
   ↓
Comando SQL
   ↓
Banco de Dados
   ↓
Resultado
   ↓
Informação
```

------------------------------------------------------------------------

# 🗂️ Categorias da SQL

Os comandos SQL podem ser organizados em categorias conforme sua
finalidade.

## DDL --- Data Definition Language

A **DDL** está relacionada à definição e alteração da estrutura do banco
de dados.

Exemplos:

``` sql
CREATE
ALTER
DROP
```

Ela é utilizada para criar ou modificar objetos como bancos, tabelas e
estruturas.

## DML --- Data Manipulation Language

A **DML** está relacionada à manipulação dos dados armazenados.

Entre os comandos estudados estão:

``` sql
SELECT
INSERT
UPDATE
DELETE
```

Nesta aula, nosso principal foco será a consulta dos dados utilizando
`SELECT`.

------------------------------------------------------------------------

# 🌎 Nosso laboratório: Banco WORLD

Para praticar SQL utilizaremos o banco de dados **WORLD**,
disponibilizado como base de exemplo do MySQL.

Ele permite trabalhar com dados relacionados a países, cidades e
idiomas.

Entre suas principais tabelas estão:

``` text
WORLD
│
├── city
├── country
└── countrylanguage
```

Esse banco permite construir consultas semelhantes a perguntas
encontradas em situações reais de análise de dados.

------------------------------------------------------------------------

# 🔍 Conhecendo as tabelas

Antes de consultar os dados, precisamos compreender o que cada tabela
representa.

## CITY

Contém informações sobre cidades.

Exemplos de atributos:

``` text
ID
Name
CountryCode
District
Population
```

## COUNTRY

Contém informações sobre países.

Exemplos:

``` text
Code
Name
Continent
Region
Population
LifeExpectancy
GNP
Capital
```

## COUNTRYLANGUAGE

Contém informações relacionadas aos idiomas falados nos países.

As tabelas possuem campos que permitem relacionar as informações entre
si.

------------------------------------------------------------------------

# 🔎 SELECT --- Nosso principal comando

O `SELECT` é utilizado para consultar dados.

Estrutura básica:

``` sql
SELECT coluna
FROM tabela;
```

Para consultar todas as colunas:

``` sql
SELECT *
FROM city;
```

O caractere `*` indica que desejamos retornar todas as colunas da
tabela.

------------------------------------------------------------------------

# 🎯 Não precisamos trazer tudo

Uma boa consulta deve retornar apenas os dados necessários para
responder à pergunta.

Em vez de:

``` sql
SELECT *
FROM city;
```

podemos utilizar:

``` sql
SELECT
    Name,
    District,
    Population
FROM city;
```

Isso reduz informações desnecessárias e deixa o resultado mais objetivo.

> **Uma boa consulta busca somente os dados necessários.**

------------------------------------------------------------------------

# 🔎 WHERE --- Filtrando dados

O `WHERE` permite selecionar somente os registros que atendem a
determinada condição.

Exemplo:

``` sql
SELECT
    Name,
    Population
FROM city
WHERE CountryCode = 'BRA';
```

Nesse caso, a consulta retorna somente cidades associadas ao código
informado.

A estrutura lógica é:

``` text
Tabela completa
      ↓
    WHERE
      ↓
Somente registros
que atendem à condição
```

------------------------------------------------------------------------

# ⚖️ Operadores de comparação

O `WHERE` pode trabalhar com diferentes operadores.

  Operador       Significado
  -------------- ----------------
  `=`            igual
  `<>` ou `!=`   diferente
  `>`            maior que
  `<`            menor que
  `>=`           maior ou igual
  `<=`           menor ou igual

Exemplo:

``` sql
SELECT
    Name,
    CountryCode,
    Population
FROM city
WHERE Population > 1000000;
```

A pergunta deixa de ser apenas "quais dados existem?" e passa a ser
"quais registros atendem à condição que desejo analisar?".

------------------------------------------------------------------------

# 🔗 Combinando condições

Consultas reais normalmente precisam considerar mais de uma condição.

## AND

O operador `AND` exige que **todas as condições sejam verdadeiras**.

``` sql
SELECT
    Name,
    CountryCode,
    Population
FROM city
WHERE CountryCode = 'BRA'
  AND Population > 1000000;
```

Representação:

``` text
Condição A
    +
Condição B
    ↓
AMBAS precisam
ser verdadeiras
```

## OR

O operador `OR` permite que **pelo menos uma condição seja verdadeira**.

``` sql
SELECT
    Name,
    CountryCode,
    Population
FROM city
WHERE CountryCode = 'BRA'
   OR CountryCode = 'ARG';
```

> `AND` restringe a consulta.\
> `OR` amplia as possibilidades de correspondência.

------------------------------------------------------------------------

# ↕️ ORDER BY

O `ORDER BY` organiza o resultado de uma consulta.

Exemplo para descobrir as cidades mais populosas:

``` sql
SELECT
    Name,
    Population
FROM city
ORDER BY Population DESC;
```

## ASC

``` sql
ORDER BY Population ASC;
```

`ASC` significa ordem crescente:

``` text
MENOR
  ↓
MAIOR
```

## DESC

``` sql
ORDER BY Population DESC;
```

`DESC` significa ordem decrescente:

``` text
MAIOR
  ↓
MENOR
```

> **ORDER BY organiza os resultados para facilitar a análise e a
> resposta à pergunta.**

------------------------------------------------------------------------

# 🔢 LIMIT

O `LIMIT` restringe a quantidade de registros retornados.

Por exemplo, para obter apenas algumas das cidades mais populosas:

``` sql
SELECT
    Name,
    Population
FROM city
ORDER BY Population DESC
LIMIT 10;
```

A consulta primeiro organiza os dados e depois retorna apenas a
quantidade solicitada.

Isso é especialmente útil para consultas como:

``` text
TOP 5
TOP 10
TOP 20
```

------------------------------------------------------------------------

# 📊 Transformando dados em indicadores

Além de retornar registros individuais, SQL também permite produzir
**indicadores**.

As funções de agregação resumem vários registros em um resultado
analítico.

Principais funções estudadas:

  Função      Objetivo
  ----------- -----------------------
  `COUNT()`   contar registros
  `SUM()`     somar valores
  `AVG()`     calcular média
  `MIN()`     encontrar menor valor
  `MAX()`     encontrar maior valor

------------------------------------------------------------------------

# 🔢 COUNT

`COUNT()` é utilizado para contar registros.

Exemplo:

``` sql
SELECT COUNT(*)
FROM city;
```

Podemos combinar a função com filtros:

``` sql
SELECT COUNT(*)
FROM city
WHERE CountryCode = 'BRA';
```

Agora não estamos perguntando **quais** registros existem, mas
**quantos** atendem à condição.

------------------------------------------------------------------------

# ➕ SUM

`SUM()` calcula a soma de uma coluna numérica.

Exemplo:

``` sql
SELECT SUM(Population)
FROM city
WHERE CountryCode = 'BRA';
```

Podemos utilizar essa função para responder perguntas como:

> Qual é a população registrada nas cidades de determinado país?

------------------------------------------------------------------------

# 📈 AVG

`AVG()` calcula a média de uma coluna numérica.

Exemplo:

``` sql
SELECT AVG(Population)
FROM city
WHERE CountryCode = 'BRA';
```

A função transforma vários registros em um único indicador médio.

------------------------------------------------------------------------

# 📉 MIN e MAX

As funções `MIN()` e `MAX()` permitem encontrar os menores e maiores
valores.

Exemplo:

``` sql
SELECT
    MIN(Population) AS menor_populacao,
    MAX(Population) AS maior_populacao
FROM city;
```

Essas funções ajudam a identificar extremos dentro dos dados.

------------------------------------------------------------------------

# 🧩 GROUP BY

Até aqui conseguimos calcular indicadores gerais.

Mas frequentemente queremos responder perguntas como:

> Quantas cidades existem em cada país?

Nesse caso utilizamos `GROUP BY`.

Exemplo:

``` sql
SELECT
    CountryCode,
    COUNT(*) AS quantidade_cidades
FROM city
GROUP BY CountryCode;
```

Conceitualmente:

``` text
Registros
   ↓
Separação por grupo
   ↓
Agregação
   ↓
Resultado por grupo
```

O `GROUP BY` transforma registros individuais em informações resumidas
por categoria.

------------------------------------------------------------------------

# 📊 GROUP BY + ORDER BY

Também podemos ordenar os grupos calculados.

``` sql
SELECT
    CountryCode,
    COUNT(*) AS quantidade_cidades
FROM city
GROUP BY CountryCode
ORDER BY quantidade_cidades DESC;
```

Fluxo:

``` text
Dados
   ↓
GROUP BY
   ↓
Agregação
   ↓
ORDER BY
   ↓
Ranking
```

Isso permite identificar rapidamente os maiores ou menores resultados.

------------------------------------------------------------------------

# 🔗 Como os dados estão relacionados?

No banco WORLD, informações relacionadas estão distribuídas em tabelas
diferentes.

Por exemplo:

``` text
CITY
----------------
CountryCode
```

e:

``` text
COUNTRY
----------------
Code
```

Esses campos permitem estabelecer uma relação:

``` text
CITY.CountryCode
       │
       ▼
COUNTRY.Code
```

Com isso, podemos combinar informações de cidades e países em uma única
consulta.

------------------------------------------------------------------------

# 🤝 JOIN

O `JOIN` permite combinar dados de tabelas relacionadas.

Imagine que queremos exibir:

``` text
Cidade
+
País
```

Essas informações podem estar em tabelas diferentes.

Exemplo:

``` sql
SELECT
    city.Name,
    country.Name
FROM city
JOIN country
    ON city.CountryCode = country.Code;
```

A condição `ON` informa ao banco como os registros das duas tabelas
devem ser relacionados.

> **JOIN permite combinar informações de tabelas relacionadas.**

------------------------------------------------------------------------

# 🔗 INNER JOIN

O `INNER JOIN` retorna os registros que possuem correspondência entre as
tabelas envolvidas.

``` sql
SELECT
    city.Name,
    country.Name
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code;
```

Conceitualmente:

``` text
CITY              COUNTRY
  \                  /
   \                /
    \              /
     CORRESPONDÊNCIA
           ↓
       RESULTADO
```

------------------------------------------------------------------------

# 🔍 JOIN + WHERE

Podemos combinar relacionamento e filtragem.

``` sql
SELECT
    city.Name,
    country.Name,
    city.Population
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code
WHERE country.Name = 'Brazil';
```

A lógica é:

``` text
CITY + COUNTRY
      ↓
     JOIN
      ↓
Relacionamento
      ↓
    WHERE
      ↓
Resultado filtrado
```

O `JOIN` combina as tabelas e o `WHERE` define quais registros queremos
analisar.

------------------------------------------------------------------------

# ✨ Melhorando a consulta com aliases

Consultas envolvendo várias tabelas podem ficar extensas.

Aliases permitem utilizar nomes menores.

Sem aliases:

``` sql
SELECT
    city.Name,
    country.Name
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code;
```

Com aliases:

``` sql
SELECT
    c.Name,
    p.Name
FROM city AS c
INNER JOIN country AS p
    ON c.CountryCode = p.Code;
```

Aliases tornam consultas maiores mais legíveis e facilitam sua
manutenção.

------------------------------------------------------------------------

# 🧠 SQL começa com uma pergunta

Uma consulta não deve começar pelo comando.

Ela deve começar pela **pergunta que queremos responder**.

Exemplo:

> Quais cidades brasileiras possuem mais de 1 milhão de habitantes?

Podemos decompor:

``` text
1. PERGUNTA
      ↓
2. CONDIÇÃO
      ↓
3. CONSULTA
      ↓
4. RESPOSTA
```

SQL é uma ferramenta para transformar uma pergunta em uma busca
estruturada sobre os dados.

------------------------------------------------------------------------

# 🔄 Evolução das nossas consultas

Durante a aula, as consultas evoluem progressivamente:

``` text
SELECT
   ↓
WHERE
   ↓
AND / OR
   ↓
ORDER BY
   ↓
LIMIT
   ↓
COUNT / SUM / AVG / MIN / MAX
   ↓
GROUP BY
   ↓
GROUP BY + ORDER BY
   ↓
JOIN
   ↓
JOIN + WHERE
   ↓
ALIASES
```

Quanto mais comandos combinamos corretamente, mais perguntas conseguimos
responder.

------------------------------------------------------------------------

# 🧪 Laboratório WORLD

A etapa prática consolida os conceitos utilizando o banco WORLD.

O objetivo é construir consultas progressivamente, aplicando os recursos
estudados.

Uma sequência de prática pode envolver:

``` text
01 → Explorar as tabelas

02 → SELECT

03 → WHERE

04 → AND / OR

05 → ORDER BY

06 → LIMIT

07 → Funções de agregação

08 → GROUP BY

09 → JOIN

10 → JOIN + WHERE
```

O objetivo não é apenas executar comandos SQL, mas compreender **qual
pergunta cada consulta responde**.

------------------------------------------------------------------------

# 💡 Do dado à informação

SQL não deve ser entendido apenas como uma linguagem para escrever
comandos.

Seu valor está em transformar dados armazenados em respostas úteis.

``` text
DADOS
   ↓
SQL
   ↓
INFORMAÇÃO
   ↓
CONHECIMENTO
```

Exemplos:

``` text
Registros de cidades
        ↓
COUNT()
        ↓
Quantidade de cidades

Populações
        ↓
AVG()
        ↓
População média

Cidades + Países
        ↓
JOIN
        ↓
Informação combinada

Dados agrupados
        ↓
GROUP BY
        ↓
Indicadores por categoria
```

------------------------------------------------------------------------

# 📝 Resumo da Aula

Nesta aula estudamos:

-   [x] Linguagem SQL;
-   [x] categorias da SQL;
-   [x] banco WORLD;
-   [x] estrutura das tabelas;
-   [x] `SELECT`;
-   [x] seleção de colunas;
-   [x] `WHERE`;
-   [x] operadores de comparação;
-   [x] `AND` e `OR`;
-   [x] `ORDER BY`;
-   [x] `ASC` e `DESC`;
-   [x] `LIMIT`;
-   [x] `COUNT`;
-   [x] `SUM`;
-   [x] `AVG`;
-   [x] `MIN`;
-   [x] `MAX`;
-   [x] `GROUP BY`;
-   [x] `GROUP BY + ORDER BY`;
-   [x] relacionamentos entre tabelas;
-   [x] `JOIN`;
-   [x] `INNER JOIN`;
-   [x] `JOIN + WHERE`;
-   [x] aliases;
-   [x] construção progressiva de consultas.

------------------------------------------------------------------------

# 🎓 O principal aprendizado

A sintaxe SQL é importante, mas o objetivo principal é aprender a
transformar uma necessidade de informação em uma consulta.

``` text
PERGUNTA
   ↓
IDENTIFICAR OS DADOS
   ↓
ESCOLHER AS TABELAS
   ↓
APLICAR FILTROS
   ↓
RELACIONAR DADOS
   ↓
AGREGAR / ORDENAR
   ↓
OBTER A RESPOSTA
```

> **SQL é uma ferramenta utilizada para perguntar aos dados e
> transformar registros armazenados em informação útil.**

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**\
**Disciplina:** Banco de Dados e Mineração de Dados

🔗 [LinkedIn](https://www.linkedin.com/in/rodolffoterra/)\
💻 [GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

> **Quanto mais dominamos SQL, mais perguntas conseguimos fazer aos
> dados --- e melhores respostas conseguimos encontrar.**
