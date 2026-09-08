# 📊 Data Warehouse e ETL

## Banco de Dados e Mineração de Dados

**Professor:** Rodolfo Terra\
**Tema:** Data Warehouse, Modelagem Dimensional e ETL

-   LinkedIn: https://www.linkedin.com/in/rodolffoterra/
-   GitHub: https://github.com/rodolffoterra

------------------------------------------------------------------------

## 📚 Visão geral

Bancos operacionais são excelentes para registrar clientes, produtos,
pedidos, pagamentos e outras transações. Porém, quando uma organização
deseja compreender seu desempenho ao longo do tempo, surgem perguntas
analíticas:

-   Qual produto vende mais?
-   Qual região possui maior faturamento?
-   Qual cliente compra mais?
-   Como as vendas evoluíram?
-   Qual categoria possui maior ticket médio?
-   Quais padrões aparecem no comportamento dos clientes?

Para responder perguntas como essas, precisamos avançar do ambiente
operacional para um ambiente preparado para análise.

``` text
SISTEMAS OPERACIONAIS
        ↓
       OLTP
        ↓
      EXTRACT
        ↓
      STAGING
        ↓
     TRANSFORM
        ↓
       LOAD
        ↓
 DATA WAREHOUSE
        ↓
MODELAGEM DIMENSIONAL
        ↓
       OLAP
        ↓
        BI
        ↓
     DECISÃO
```

------------------------------------------------------------------------

# 1. O problema: os dados estão espalhados

Uma empresa dificilmente possui todas as informações em um único
sistema.

  Área / Sistema   Exemplos de dados
  ---------------- ---------------------------------------
  ERP              pedidos, produtos, fornecedores
  CRM              clientes, contatos, oportunidades
  Financeiro       pagamentos, recebimentos, faturamento
  Estoque          entradas, saídas e saldos
  RH               colaboradores e departamentos
  E-commerce       pedidos, carrinhos e acessos
  Planilhas        controles complementares
  APIs             dados de sistemas externos

Cada sistema conhece uma parte do negócio. Quando uma pergunta depende
de várias fontes, precisamos integrar os dados.

> **Cada sistema conhece uma parte da empresa. O ambiente analítico
> procura construir uma visão integrada do negócio.**

------------------------------------------------------------------------

# 2. OLTP --- o banco da operação

**OLTP (Online Transaction Processing)** representa os ambientes que
suportam as operações do dia a dia.

Características:

-   muitas operações pequenas;
-   `INSERT`, `UPDATE` e `DELETE` constantes;
-   resposta rápida;
-   muitos usuários simultâneos;
-   foco nos dados atuais;
-   consistência transacional;
-   estruturas geralmente normalizadas.

### Exemplo

Uma compra em um e-commerce pode gerar:

``` sql
INSERT INTO pedido (...);
INSERT INTO item_pedido (...);

UPDATE produto
SET estoque = estoque - 1
WHERE produto_id = 10;

INSERT INTO pagamento (...);
```

O objetivo é registrar corretamente aquilo que acabou de acontecer.

**Exemplos:** transferência bancária, cadastro de paciente, emissão de
pedido, pagamento, atualização de estoque e abertura de chamado.

------------------------------------------------------------------------

# 3. OLAP --- o banco da análise

**OLAP (Online Analytical Processing)** é orientado à análise.

Em vez de registrar uma nova venda, queremos analisar milhares ou
milhões de vendas já realizadas.

Características:

-   consultas complexas;
-   grandes volumes;
-   agregações;
-   histórico;
-   relatórios;
-   indicadores;
-   dashboards;
-   apoio à decisão.

Perguntas típicas:

-   Qual foi o faturamento por estado?
-   Qual produto cresceu mais?
-   Qual vendedor possui maior ticket médio?
-   Qual mês vende mais?
-   Como o resultado atual se compara ao ano anterior?

------------------------------------------------------------------------

# 4. OLTP × OLAP

  Característica      OLTP                       OLAP
  ------------------- -------------------------- ----------------------------
  Objetivo            Operação                   Análise
  Dados               Atuais                     Históricos
  Operações           INSERT / UPDATE / DELETE   SELECT / agregações
  Consultas           Pequenas e rápidas         Complexas
  Usuários            Operacionais               Analistas e gestores
  Frequência          Alta                       Menor
  Volume consultado   Pequeno por transação      Grandes volumes
  Modelagem           Normalizada                Frequentemente dimensional
  Finalidade          Registrar o negócio        Compreender o negócio

> **OLTP registra o negócio. OLAP ajuda a compreender o negócio.**

Um não substitui o outro.

------------------------------------------------------------------------

# 5. Data Warehouse

Um **Data Warehouse (DW)** é um repositório integrado de dados,
principalmente históricos, organizado para análise e apoio à tomada de
decisão.

``` text
ERP --------CRM ---------E-commerce ---Planilhas -----+----> DATA WAREHOUSE ----> BI / ANALYTICS
APIs ---------/
Bancos -------/
```

O Data Warehouse permite:

1.  **centralizar** informações;
2.  **integrar** sistemas;
3.  **historizar** dados;
4.  **analisar** grandes volumes;
5.  **decidir** com base em informação.

``` text
CENTRALIZAR
     ↓
INTEGRAR
     ↓
HISTORIZAR
     ↓
ANALISAR
     ↓
DECIDIR
```

------------------------------------------------------------------------

# 6. Do dado à decisão

Ter milhões de registros não significa possuir conhecimento.

``` text
DADOS
  ↓
INFORMAÇÃO
  ↓
INDICADOR
  ↓
CONHECIMENTO
  ↓
DECISÃO
```

Dez milhões de vendas são dados. Descobrir que uma categoria cresceu 40%
em determinada região produz informação. Acompanhar isso como KPI cria
um indicador. Usar esse indicador para ajustar estoque transforma
informação em decisão.

------------------------------------------------------------------------

# 7. Modelagem Dimensional

A **Modelagem Dimensional** organiza dados para facilitar análises.

Seus dois conceitos centrais são:

> **Fato = o que aconteceu?**

> **Dimensão = em qual contexto aconteceu?**

------------------------------------------------------------------------

# 8. Tabela Fato

A tabela fato representa um evento mensurável do negócio.

Exemplo:

### FATO_VENDAS

  Campo         Papel
  ------------- ---------------------
  cliente_id    chave para dimensão
  produto_id    chave para dimensão
  tempo_id      chave para dimensão
  vendedor_id   chave para dimensão
  quantidade    medida
  valor         medida
  desconto      medida
  lucro         medida

Medidas podem ser agregadas:

``` sql
SUM(valor)
AVG(valor)
COUNT(*)
SUM(quantidade)
```

Outros possíveis fatos:

-   hospital: atendimento, internação, exame;
-   banco: transação, pagamento, transferência;
-   logística: entrega, movimentação.

------------------------------------------------------------------------

# 9. Dimensões

As dimensões descrevem o contexto.

  Dimensão       Pergunta
  -------------- ----------------
  DIM_CLIENTE    Quem comprou?
  DIM_PRODUTO    O que comprou?
  DIM_TEMPO      Quando?
  DIM_VENDEDOR   Quem vendeu?
  DIM_LOCAL      Onde?

Exemplo:

> **Qual foi o faturamento por produto, por estado e por mês?**

O faturamento vem da **fato**. Produto, estado e mês vêm das
**dimensões**.

------------------------------------------------------------------------

# 10. Star Schema

No **Star Schema**, a fato fica no centro e as dimensões ao redor.

``` text
                  DIM_TEMPO
                      |
DIM_CLIENTE ---- FATO_VENDAS ---- DIM_PRODUTO
                      |
                DIM_VENDEDOR
```

A fato contém medidas e chaves. As dimensões fornecem características
para filtrar, agrupar e contextualizar.

------------------------------------------------------------------------

# 11. Snowflake Schema

No **Snowflake**, determinadas dimensões são normalizadas.

``` text
PAÍS
  |
ESTADO
  |
CIDADE
  |
DIM_CLIENTE
  |
FATO_VENDAS
```

### Star × Snowflake

  Star Schema                  Snowflake
  ---------------------------- ------------------------------
  mais simples                 mais normalizado
  menos JOINs                  mais JOINs
  consultas intuitivas         estrutura mais detalhada
  maior redundância possível   menor redundância
  muito utilizado em BI        útil em cenários específicos

> **Não existe modelo perfeito. Existe modelo adequado ao problema.**

------------------------------------------------------------------------

# 12. ETL --- Extract, Transform, Load

ETL significa:

``` text
EXTRACT → TRANSFORM → LOAD
```

ou:

``` text
EXTRAIR → TRANSFORMAR → CARREGAR
```

O processo retira dados das fontes, prepara esses dados e os carrega no
ambiente analítico.

------------------------------------------------------------------------

# 13. Extract

A extração busca dados em diferentes fontes:

-   MySQL;
-   PostgreSQL;
-   SQL Server;
-   Oracle;
-   APIs;
-   CSV;
-   Excel;
-   sistemas externos.

``` text
ERP --------CRM ---------MySQL --------+----> EXTRAÇÃO
Excel --------/
CSV ----------/
API ----------/
```

------------------------------------------------------------------------

# 14. Transform

Dados de fontes diferentes raramente possuem o mesmo padrão.

Exemplo:

``` text
SP
São Paulo
SAO PAULO
são paulo
```

Após a padronização:

``` text
São Paulo
```

Transformações comuns:

-   remover duplicados;
-   tratar `NULL`;
-   padronizar textos;
-   converter tipos;
-   padronizar datas;
-   validar CPF/CNPJ;
-   aplicar regras de negócio;
-   calcular métricas;
-   integrar fontes;
-   validar qualidade.

``` text
DADOS BRUTOS
     ↓
   LIMPEZA
     ↓
PADRONIZAÇÃO
     ↓
  CONVERSÃO
     ↓
  VALIDAÇÃO
     ↓
  INTEGRAÇÃO
     ↓
DADOS CONFIÁVEIS
```

------------------------------------------------------------------------

# 15. Staging Area

A **Staging Area** é uma área intermediária de preparação.

``` text
FONTES
  ↓
EXTRAÇÃO
  ↓
+----------------------+
|     STAGING AREA     |
| Dados temporários    |
| Limpeza              |
| Padronização         |
| Validação            |
+----------------------+
  ↓
DATA WAREHOUSE
```

Ela pode apoiar isolamento, processamento intermediário,
rastreabilidade, validação e integração.

> **Staging não é o Data Warehouse. É uma área intermediária do
> processo.**

------------------------------------------------------------------------

# 16. Load

Após preparar os dados, realizamos a carga.

``` text
STAGING
   ↓
TRANSFORMAÇÃO
   ↓
DATA WAREHOUSE
   |
   +-- DIM_CLIENTE
   +-- DIM_PRODUTO
   +-- DIM_TEMPO
   +-- FATO_VENDAS
```

Em modelos dimensionais, normalmente as dimensões precisam estar
disponíveis antes da carga da fato, pois fornecem as chaves utilizadas
nos relacionamentos.

------------------------------------------------------------------------

# 17. ETL completo

``` text
ERP / CRM / MySQL / CSV
          ↓
       EXTRACT
          ↓
       STAGING
          ↓
      TRANSFORM
          ↓
        LOAD
          ↓
   DATA WAREHOUSE
          ↓
        OLAP
          ↓
      DASHBOARD
          ↓
       DECISÃO
```

Existe todo um processo entre uma venda acontecer e aparecer
corretamente em um dashboard.

------------------------------------------------------------------------

# 18. Histórico dos dados

Considere:

``` text
CLIENTE: MARIA

2024 → Campinas
2025 → Sorocaba
2026 → São Paulo
```

Se simplesmente atualizarmos a cidade para São Paulo, uma venda de 2024
poderá ser associada à cidade atual.

Em ambientes analíticos, frequentemente precisamos saber:

> **Qual era o valor de determinado atributo quando o evento
> aconteceu?**

------------------------------------------------------------------------

# 19. Slowly Changing Dimension --- SCD Tipo 2

No **SCD Tipo 2**, uma mudança relevante não sobrescreve o histórico.
Criamos uma nova versão do registro.

  Cliente   Cidade        Início    Fim Atual
  --------- ----------- -------- ------ -------
  Maria     Campinas        2024   2025 Não
  Maria     Sorocaba        2025   2026 Não
  Maria     São Paulo       2026    --- Sim

Assim podemos saber onde Maria mora hoje e também onde morava quando uma
venda histórica aconteceu.

> **Não sobrescrever. Criar uma nova versão.**

------------------------------------------------------------------------

# 20. Parte prática --- pequeno Data Warehouse

Banco operacional:

``` text
CLIENTE
PRODUTO
PEDIDO
ITEM_PEDIDO
```

Antes de modelar, perguntamos:

-   Qual o faturamento total?
-   Qual produto vende mais?
-   Qual cliente compra mais?
-   Qual mês vende mais?
-   Qual região possui maior faturamento?

As perguntas do negócio ajudam a definir fatos, medidas e dimensões.

------------------------------------------------------------------------

# 21. Nosso primeiro Star Schema

``` text
                   DIM_TEMPO
                       |
DIM_CLIENTE ----- FATO_VENDAS ----- DIM_PRODUTO
```

### DIM_CLIENTE

``` text
cliente_id
nome
cidade
estado
```

### DIM_PRODUTO

``` text
produto_id
produto
categoria
marca
```

### DIM_TEMPO

``` text
tempo_id
data
dia
mes
ano
```

### FATO_VENDAS

``` text
cliente_id
produto_id
tempo_id
quantidade
valor
desconto
```

Temos:

-   Cliente → quem comprou;
-   Produto → o que foi comprado;
-   Tempo → quando aconteceu;
-   Fato Vendas → aquilo que queremos medir.

------------------------------------------------------------------------

# 22. Simulando o ETL

### 1 --- Extract

``` text
SELECT clientes
SELECT produtos
SELECT pedidos
SELECT item_pedido
```

### 2 --- Transform

``` text
Remover duplicados
Tratar NULL
Padronizar estados
Calcular valor
Criar dimensão tempo
Validar registros
```

Exemplo:

``` text
valor_total = quantidade × preco_unitario
```

### 3 --- Load

``` text
DIM_CLIENTE
DIM_PRODUTO
DIM_TEMPO
FATO_VENDAS
```

------------------------------------------------------------------------

# 23. Consultando o Data Warehouse

``` sql
SELECT
    t.ano,
    t.mes,
    p.categoria,
    SUM(f.valor) AS faturamento
FROM fato_vendas f
JOIN dim_tempo t
    ON f.tempo_id = t.tempo_id
JOIN dim_produto p
    ON f.produto_id = p.produto_id
GROUP BY
    t.ano,
    t.mes,
    p.categoria;
```

Resultado conceitual:

     Ano Mês   Categoria       Faturamento
  ------ ----- ------------- -------------
    2026 Jan   Eletrônicos         125.000
    2026 Fev   Eletrônicos         142.000
    2026 Mar   Eletrônicos         158.000

Aqui:

-   `f.valor` fornece a medida;
-   `t.ano` e `t.mes` fornecem contexto temporal;
-   `p.categoria` fornece contexto do produto.

A modelagem dimensional não substitui SQL. Ela organiza os dados para
facilitar perguntas analíticas.

------------------------------------------------------------------------

# 24. Da transação ao conhecimento

``` text
OLTP
 ↓
EXTRACT
 ↓
STAGING
 ↓
TRANSFORM
 ↓
LOAD
 ↓
DATA WAREHOUSE
 ↓
FATOS + DIMENSÕES + HISTÓRICO
 ↓
OLAP
 ↓
BI
 ↓
DECISÃO
```

### A essência da aula

> **OLTP registra os acontecimentos.**

> **ETL movimenta e prepara os dados.**

> **Data Warehouse organiza, integra e preserva as informações.**

> **OLAP permite analisá-las.**

> **BI comunica resultados por indicadores e visualizações.**

> **O objetivo final é apoiar decisões.**

------------------------------------------------------------------------

# 25. Preparando para Mineração de Dados

Até aqui utilizamos os dados principalmente para responder perguntas
conhecidas.

O próximo nível é descobrir padrões que ainda não conhecemos.

### Quais clientes possuem comportamento semelhante?

**Clusterização**

### Quais produtos são comprados juntos?

**Regras de Associação**

### Quais clientes podem deixar de comprar?

**Classificação**

### Qual poderá ser o faturamento futuro?

**Regressão**

### Existe comportamento fora do padrão?

**Detecção de Anomalias**

``` text
DADOS
  ↓
DATA WAREHOUSE
  ↓
ANÁLISE
  ↓
PADRÕES
  ↓
CONHECIMENTO
  ↓
DECISÃO
```

É nesse ponto que entramos no universo da **Mineração de Dados**.

------------------------------------------------------------------------

# 26. Resumo dos conceitos

  Conceito                Resumo
  ----------------------- ----------------------------------------------------
  OLTP                    registra operações
  OLAP                    realiza análises
  Data Warehouse          integra e preserva dados analíticos
  Modelagem Dimensional   organiza dados para análise
  Tabela Fato             contém eventos, chaves e medidas
  Dimensão                fornece contexto
  Star Schema             fato central ligada às dimensões
  Snowflake               dimensões podem ser normalizadas
  ETL                     extrair, transformar e carregar
  Staging Area            área intermediária de preparação
  SCD Tipo 2              mantém versões históricas
  BI                      transforma análises em indicadores e visualizações

------------------------------------------------------------------------

# 27. Questões para revisão

1.  Qual é a principal diferença entre OLTP e OLAP?
2.  Por que separar ambientes operacionais e analíticos?
3.  O que é um Data Warehouse?
4.  Qual é a finalidade da modelagem dimensional?
5.  Qual a diferença entre fato e dimensão?
6.  O que são medidas?
7.  Como funciona um Star Schema?
8.  Qual a diferença entre Star e Snowflake?
9.  O que significa ETL?
10. O que acontece na transformação?
11. Para que serve uma Staging Area?
12. Por que o histórico é importante?
13. Como funciona o SCD Tipo 2?
14. Como SQL é utilizado em um ambiente analítico?
15. Como o Data Warehouse prepara os dados para Mineração de Dados?

------------------------------------------------------------------------

# 28. Conclusão

Dados contam a história de uma empresa.

Os sistemas operacionais registram o presente. O Data Warehouse integra
os registros, organiza o contexto e preserva a evolução histórica. A
modelagem dimensional estrutura os dados para análise. O ETL garante que
informações provenientes de diferentes fontes sejam extraídas,
preparadas e carregadas. OLAP e BI transformam esses dados em análises,
indicadores e dashboards.

> **Os sistemas operacionais registram o que está acontecendo.**

> **O Data Warehouse preserva o que aconteceu.**

> **A análise ajuda a decidir o que fazer a seguir.**

Quando passamos a procurar relações, comportamentos, tendências e
padrões ocultos, chegamos ao próximo tema:

# 🔍 Mineração de Dados

------------------------------------------------------------------------

## 🎯 Fluxo final

``` text
TRANSAÇÃO
    ↓
DADOS
    ↓
ETL
    ↓
DATA WAREHOUSE
    ↓
INFORMAÇÃO
    ↓
ANÁLISE
    ↓
CONHECIMENTO
    ↓
DECISÃO
```

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**\
**Disciplina:** Banco de Dados e Mineração de Dados

-   LinkedIn: https://www.linkedin.com/in/rodolffoterra/
-   GitHub: https://github.com/rodolffoterra

------------------------------------------------------------------------

> **"Dados organizados geram informação. Informação analisada gera
> conhecimento. Conhecimento apoia decisões."**
