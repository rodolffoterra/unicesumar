# 📊 Banco de Dados e Mineração de Dados

## Material da Disciplina

**Professor:** Rodolfo Terra

🔗 [LinkedIn](https://www.linkedin.com/in/rodolffoterra/)\
💻 [GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## 📚 Sobre a disciplina

A disciplina de **Banco de Dados e Mineração de Dados** apresenta uma
jornada que começa na organização e estruturação dos dados e avança até
sua utilização para análise e descoberta de conhecimento.

Ao longo das quatro aulas, o conteúdo evolui de forma progressiva:

``` text
BANCO DE DADOS
      ↓
MODELAGEM
      ↓
SQL
      ↓
CONSULTAS E ANÁLISES
      ↓
DATA WAREHOUSE
      ↓
ETL
      ↓
MODELAGEM DIMENSIONAL
      ↓
MINERAÇÃO DE DADOS
      ↓
MACHINE LEARNING
      ↓
CONHECIMENTO
      ↓
DECISÃO
```

A proposta é compreender que os dados não possuem valor apenas por
estarem armazenados. Eles precisam ser **organizados, relacionados,
consultados, preparados e analisados** para gerar informação útil.

------------------------------------------------------------------------

# 🎯 Objetivos da disciplina

Ao final das aulas, o estudante deverá ser capaz de:

-   compreender os fundamentos de bancos de dados;
-   diferenciar dados de informação;
-   compreender o papel de um SGBD;
-   reconhecer tabelas, registros, campos, chaves e relacionamentos;
-   compreender os fundamentos da modelagem de dados;
-   utilizar SQL para consultar e analisar informações;
-   aplicar filtros, ordenações, agregações e agrupamentos;
-   relacionar tabelas utilizando `JOIN`;
-   diferenciar ambientes OLTP e OLAP;
-   compreender o conceito e a finalidade de um Data Warehouse;
-   conhecer modelagem dimensional, fatos e dimensões;
-   compreender Star Schema e Snowflake Schema;
-   compreender o processo ETL;
-   reconhecer a importância de Staging e histórico;
-   compreender o conceito de SCD Tipo 2;
-   entender o processo KDD;
-   diferenciar classificação, regressão, clusterização e associação;
-   utilizar o WEKA para experimentos de Mineração de Dados;
-   interpretar métricas básicas de avaliação de modelos.

------------------------------------------------------------------------

# 🎬 Aulas gravadas

Todas as aulas possuem gravação disponível no YouTube.

  -------------------------------------------------------------------------------------------------------------
  Aula              Tema              Conteúdo          Vídeo
                                      principal         
  ----------------- ----------------- ----------------- -------------------------------------------------------
  **Aula 01**       Fundamentos de    Banco de Dados,   [▶️ Assistir no
                    Banco de Dados e  SGBD, MySQL,      YouTube](https://www.youtube.com/watch?v=FKiKdDIGD7s)
                    Modelagem         tabelas, chaves e 
                                      relacionamentos   

  **Aula 02**       Linguagem SQL     SELECT, WHERE,    [▶️ Assistir no
                                      ORDER BY,         YouTube](https://www.youtube.com/watch?v=SB6BJ1bs1V0)
                                      agregações, GROUP 
                                      BY e JOIN         

  **Aula 03**       Data Warehouse e  OLTP × OLAP, DW,  [▶️ Assistir no
                    ETL               modelagem         YouTube](https://www.youtube.com/watch?v=WxkP1Rt6OVg)
                                      dimensional, ETL, 
                                      Staging e SCD     
                                      Tipo 2            

  **Aula 04**       Mineração de      KDD, Machine      [▶️ Assistir no
                    Dados com WEKA    Learning,         YouTube](https://www.youtube.com/watch?v=fw3-umGhQlg)
                                      classificação,    
                                      regressão, WEKA e 
                                      métricas          
  -------------------------------------------------------------------------------------------------------------

> 💡 Os links acima abrem diretamente as gravações das quatro aulas da
> disciplina.

------------------------------------------------------------------------

# 🗄️ Aula 01 --- Fundamentos de Banco de Dados e Modelagem

🎥 **[Assistir Aula 01 no
YouTube](https://www.youtube.com/watch?v=FKiKdDIGD7s)**

A primeira aula estabelece a base conceitual da disciplina.

Começamos compreendendo o que são dados, informação e bancos de dados,
além do papel de um **Sistema Gerenciador de Banco de Dados (SGBD)**.

## Principais assuntos

-   Dados × Informação;
-   Banco de Dados;
-   SGBD;
-   MySQL;
-   tabelas;
-   linhas e colunas;
-   registros e campos;
-   chave primária;
-   relacionamentos;
-   modelagem de dados;
-   criação de banco;
-   criação de tabelas;
-   inserção de registros;
-   introdução à integração entre Python e MySQL.

## Conceito central

``` text
DADOS
  ↓
ORGANIZAÇÃO
  ↓
BANCO DE DADOS
  ↓
SISTEMA
  ↓
INFORMAÇÃO
```

Um banco de dados não é apenas um local para armazenar informações. Ele
fornece uma estrutura para que aplicações consigam registrar, consultar
e relacionar dados de forma organizada.

## Relacionamentos

Um dos fundamentos apresentados é o relacionamento entre tabelas.

Exemplo:

``` text
CLIENTE
   1
   │
   │ realiza
   │
   N
PEDIDO
```

Um cliente pode realizar vários pedidos, estabelecendo um relacionamento
**1:N**.

Essa ideia será fundamental nas aulas seguintes, especialmente ao
trabalhar com SQL e modelagem dimensional.

------------------------------------------------------------------------

# 💻 Aula 02 --- Linguagem SQL

🎥 **[Assistir Aula 02 no
YouTube](https://www.youtube.com/watch?v=SB6BJ1bs1V0)**

Depois de compreender como os dados são organizados, avançamos para a
linguagem utilizada para conversar com bancos relacionais: **SQL ---
Structured Query Language**.

O banco de exemplo **WORLD**, do MySQL, é utilizado para transformar
perguntas em consultas.

## Principais assuntos

-   SQL;
-   DDL;
-   DML;
-   banco WORLD;
-   `SELECT`;
-   seleção de colunas;
-   `WHERE`;
-   operadores de comparação;
-   `AND`;
-   `OR`;
-   `ORDER BY`;
-   `ASC`;
-   `DESC`;
-   `LIMIT`;
-   `COUNT`;
-   `SUM`;
-   `AVG`;
-   `MIN`;
-   `MAX`;
-   `GROUP BY`;
-   relacionamentos;
-   `JOIN`;
-   `INNER JOIN`;
-   aliases.

## Evolução das consultas

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
FUNÇÕES DE AGREGAÇÃO
   ↓
GROUP BY
   ↓
JOIN
```

A ideia principal é que uma consulta SQL deve começar com uma pergunta.

``` text
PERGUNTA
   ↓
IDENTIFICAR OS DADOS
   ↓
ESCOLHER AS TABELAS
   ↓
FILTRAR
   ↓
RELACIONAR
   ↓
AGREGAR
   ↓
ORDENAR
   ↓
RESPOSTA
```

> **SQL transforma perguntas sobre os dados em consultas estruturadas.**

------------------------------------------------------------------------

# 📊 Aula 03 --- Data Warehouse e ETL

🎥 **[Assistir Aula 03 no
YouTube](https://www.youtube.com/watch?v=WxkP1Rt6OVg)**

Na terceira aula, avançamos do ambiente operacional para o ambiente
analítico.

Os bancos utilizados por sistemas transacionais são excelentes para
registrar operações. Entretanto, organizações também precisam analisar o
histórico para compreender desempenho, tendências e indicadores.

## Principais assuntos

-   sistemas operacionais;
-   OLTP;
-   OLAP;
-   Data Warehouse;
-   integração de dados;
-   histórico;
-   Modelagem Dimensional;
-   Tabela Fato;
-   Dimensões;
-   Star Schema;
-   Snowflake Schema;
-   ETL;
-   Extract;
-   Transform;
-   Load;
-   Staging Area;
-   SCD Tipo 2;
-   construção de um pequeno Data Warehouse.

## OLTP × OLAP

  Característica   OLTP                       OLAP
  ---------------- -------------------------- ----------------------------
  Objetivo         Operação                   Análise
  Dados            Atuais                     Históricos
  Operações        INSERT / UPDATE / DELETE   SELECT / agregações
  Consultas        Pequenas e rápidas         Complexas
  Modelagem        Normalizada                Frequentemente dimensional
  Finalidade       Registrar o negócio        Compreender o negócio

> **OLTP registra o negócio. OLAP ajuda a compreender o negócio.**

## Data Warehouse

Um **Data Warehouse** é um repositório integrado de dados,
principalmente históricos, organizado para análise e apoio à tomada de
decisão.

``` text
ERP
CRM
E-commerce
Planilhas
APIs
   ↓
  ETL
   ↓
DATA WAREHOUSE
   ↓
OLAP / BI
   ↓
ANÁLISE
   ↓
DECISÃO
```

## Modelagem Dimensional

Dois conceitos são fundamentais:

> **Fato = o que aconteceu?**

> **Dimensão = em qual contexto aconteceu?**

Exemplo de Star Schema:

``` text
                   DIM_TEMPO
                       |
DIM_CLIENTE ----- FATO_VENDAS ----- DIM_PRODUTO
```

A tabela fato contém eventos, chaves e medidas. As dimensões fornecem
contexto para análise.

## ETL

``` text
EXTRACT
   ↓
TRANSFORM
   ↓
LOAD
```

Ou:

``` text
EXTRAIR
   ↓
TRANSFORMAR
   ↓
CARREGAR
```

O processo permite retirar dados de diferentes fontes, tratar e
padronizar essas informações e carregá-las no ambiente analítico.

## SCD Tipo 2

Outro conceito importante é a preservação do histórico.

``` text
Maria

2024 → Campinas
2025 → Sorocaba
2026 → São Paulo
```

Em vez de simplesmente substituir a cidade anterior, o **SCD Tipo 2**
permite manter diferentes versões históricas do registro.

Isso permite analisar os fatos considerando o contexto existente no
momento em que aconteceram.

------------------------------------------------------------------------

# ⛏️ Aula 04 --- Mineração de Dados com WEKA

🎥 **[Assistir Aula 04 no
YouTube](https://www.youtube.com/watch?v=fw3-umGhQlg)**

Depois de armazenar, consultar, integrar e organizar os dados, chegamos
à descoberta de conhecimento.

A pergunta muda:

> **O que podemos descobrir a partir dos dados?**

A Mineração de Dados utiliza técnicas computacionais e estatísticas para
identificar padrões, relações, tendências e estruturas úteis.

## Principais assuntos

-   Mineração de Dados;
-   KDD;
-   seleção de dados;
-   pré-processamento;
-   transformação;
-   mineração;
-   avaliação;
-   aprendizado supervisionado;
-   aprendizado não supervisionado;
-   classificação;
-   regressão;
-   clusterização;
-   regras de associação;
-   WEKA;
-   CSV;
-   ARFF;
-   treino e teste;
-   Percentage Split;
-   Cross-Validation;
-   Accuracy;
-   Matriz de Confusão;
-   MAE;
-   RAE;
-   Overfitting.

## KDD

A Mineração de Dados faz parte de um processo maior de descoberta de
conhecimento:

``` text
SELEÇÃO
   ↓
PRÉ-PROCESSAMENTO
   ↓
TRANSFORMAÇÃO
   ↓
MINERAÇÃO
   ↓
AVALIAÇÃO
   ↓
CONHECIMENTO
```

> **Mineração de Dados é uma etapa do processo de descoberta de
> conhecimento.**

## Tipos de aprendizado

### Aprendizado supervisionado

Existe uma variável que queremos prever.

``` text
ATRIBUTOS
    ↓
 MODELO
    ↓
VARIÁVEL-ALVO
```

Duas tarefas fundamentais:

``` text
CLASSIFICAÇÃO → prevê uma categoria
REGRESSÃO     → prevê um valor numérico
```

### Aprendizado não supervisionado

Não fornecemos uma classe conhecida para o algoritmo prever.

``` text
DADOS
  ↓
ALGORITMO
  ↓
ESTRUTURAS / GRUPOS / RELAÇÕES
```

Exemplos:

-   clusterização;
-   regras de associação.

------------------------------------------------------------------------

# 🧪 WEKA

O **WEKA --- Waikato Environment for Knowledge Analysis** é utilizado
como ambiente didático para experimentação com técnicas de Machine
Learning e Mineração de Dados.

No WEKA Explorer encontramos:

``` text
Preprocess
Classify
Cluster
Associate
Select attributes
Visualize
```

Um fluxo básico de experimento é:

``` text
1. Abrir WEKA
        ↓
2. Explorer
        ↓
3. Preprocess
        ↓
4. Carregar dataset
        ↓
5. Inspecionar atributos
        ↓
6. Definir variável-alvo
        ↓
7. Escolher algoritmo
        ↓
8. Definir estratégia de avaliação
        ↓
9. Start
        ↓
10. Interpretar resultados
```

------------------------------------------------------------------------

# 📏 Avaliação dos modelos

Executar um algoritmo não significa que encontramos uma boa solução.

Precisamos avaliar os resultados.

## Accuracy

Utilizada principalmente em problemas de classificação.

``` text
Accuracy =
Previsões corretas
------------------
Total de previsões
```

Uma acurácia alta não deve ser analisada isoladamente, especialmente em
datasets desbalanceados.

## MAE --- Mean Absolute Error

Utilizado em regressão.

``` text
MAE = média dos erros absolutos
```

Quanto menor, melhor.

A unidade do MAE é a mesma da variável prevista.

## RAE --- Relative Absolute Error

Compara o erro absoluto do modelo com o erro de uma referência simples.

``` text
RAE =
Erro do modelo
--------------
Erro de referência
```

Quanto menor, melhor.

------------------------------------------------------------------------

# 🔄 A jornada completa da disciplina

As quatro aulas formam uma sequência integrada.

``` text
AULA 01
FUNDAMENTOS DE BANCO DE DADOS
          ↓
TABELAS + CHAVES + RELACIONAMENTOS
          ↓

AULA 02
SQL
          ↓
CONSULTAS + FILTROS + AGREGAÇÕES + JOINS
          ↓

AULA 03
DATA WAREHOUSE
          ↓
ETL + FATOS + DIMENSÕES + HISTÓRICO
          ↓

AULA 04
MINERAÇÃO DE DADOS
          ↓
KDD + MACHINE LEARNING + WEKA
          ↓

CONHECIMENTO
          ↓
DECISÃO
```

------------------------------------------------------------------------

# 🧠 Do dado à decisão

Podemos resumir toda a disciplina em um único fluxo:

``` text
DADOS
  ↓
BANCO DE DADOS
  ↓
ORGANIZAÇÃO
  ↓
SQL
  ↓
CONSULTA
  ↓
INTEGRAÇÃO
  ↓
ETL
  ↓
DATA WAREHOUSE
  ↓
ANÁLISE
  ↓
MINERAÇÃO DE DADOS
  ↓
PADRÕES
  ↓
CONHECIMENTO
  ↓
DECISÃO
```

------------------------------------------------------------------------

# 📌 Resumo das quatro aulas

  -----------------------------------------------------------------------
  Aula                                Conhecimento central
  ----------------------------------- -----------------------------------
  **01**                              Como os dados são estruturados e
                                      relacionados

  **02**                              Como consultar e analisar dados
                                      utilizando SQL

  **03**                              Como integrar, historizar e
                                      organizar dados para análise

  **04**                              Como descobrir padrões e construir
                                      modelos a partir dos dados
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 🎥 Acesso rápido às gravações

### 🗄️ Aula 01 --- Fundamentos de Banco de Dados e Modelagem

[![YouTube](https://img.shields.io/badge/YouTube-Assistir_Aula_01-red?logo=youtube)](https://www.youtube.com/watch?v=FKiKdDIGD7s)

### 💻 Aula 02 --- Linguagem SQL

[![YouTube](https://img.shields.io/badge/YouTube-Assistir_Aula_02-red?logo=youtube)](https://www.youtube.com/watch?v=SB6BJ1bs1V0)

### 📊 Aula 03 --- Data Warehouse e ETL

[![YouTube](https://img.shields.io/badge/YouTube-Assistir_Aula_03-red?logo=youtube)](https://www.youtube.com/watch?v=WxkP1Rt6OVg)

### ⛏️ Aula 04 --- Mineração de Dados com WEKA

[![YouTube](https://img.shields.io/badge/YouTube-Assistir_Aula_04-red?logo=youtube)](https://www.youtube.com/watch?v=fw3-umGhQlg)

------------------------------------------------------------------------

# 📚 Revisão geral

Ao terminar a disciplina, procure responder:

1.  O que é um banco de dados?
2.  Qual é o papel de um SGBD?
3.  O que são chave primária e relacionamentos?
4.  Para que serve SQL?
5.  Como `WHERE`, `GROUP BY` e `JOIN` modificam uma consulta?
6.  Qual é a diferença entre OLTP e OLAP?
7.  O que é um Data Warehouse?
8.  Qual é a diferença entre fato e dimensão?
9.  Como funciona um Star Schema?
10. O que significa ETL?
11. Para que serve uma Staging Area?
12. Como o SCD Tipo 2 preserva histórico?
13. O que é Mineração de Dados?
14. O que significa KDD?
15. Qual é a diferença entre classificação e regressão?
16. O que é clusterização?
17. O que são regras de associação?
18. Para que serve o WEKA?
19. Por que precisamos separar treino e teste?
20. Como interpretar Accuracy, MAE e RAE?

------------------------------------------------------------------------

# 🎓 Conclusão

A disciplina começa com uma pergunta fundamental:

> **Como podemos organizar os dados?**

Depois avançamos para:

> **Como podemos consultar esses dados?**

Em seguida:

> **Como podemos integrar e preparar esses dados para análise?**

E finalmente:

> **O que podemos descobrir a partir desses dados?**

Essa evolução representa grande parte da jornada moderna de dados:

``` text
ARMAZENAR
   ↓
ORGANIZAR
   ↓
CONSULTAR
   ↓
INTEGRAR
   ↓
ANALISAR
   ↓
DESCOBRIR
   ↓
DECIDIR
```

> **Dados armazenados permitem registrar o negócio. Dados organizados
> permitem compreender o negócio. Dados analisados podem revelar padrões
> e apoiar melhores decisões.**

------------------------------------------------------------------------

# 👨‍🏫 Professor

**Professor Rodolfo Terra**\
**Disciplina:** Banco de Dados e Mineração de Dados

🔗 [LinkedIn](https://www.linkedin.com/in/rodolffoterra/)\
💻 [GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## ▶️ Playlist da disciplina

  --------------------------------------------------------------------------------------------
  Aula                                Assistir
  ----------------------------------- --------------------------------------------------------
  Aula 01 --- Fundamentos de Banco de [YouTube](https://www.youtube.com/watch?v=FKiKdDIGD7s)
  Dados e Modelagem                   

  Aula 02 --- Linguagem SQL           [YouTube](https://www.youtube.com/watch?v=SB6BJ1bs1V0)

  Aula 03 --- Data Warehouse e ETL    [YouTube](https://www.youtube.com/watch?v=WxkP1Rt6OVg)

  Aula 04 --- Mineração de Dados com  [YouTube](https://www.youtube.com/watch?v=fw3-umGhQlg)
  WEKA                                
  --------------------------------------------------------------------------------------------

------------------------------------------------------------------------

> **"Dados organizados geram informação. Informação analisada gera
> conhecimento. Conhecimento apoia decisões."**
