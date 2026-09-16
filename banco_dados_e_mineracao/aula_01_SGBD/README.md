# Aula 01 --- Projeto de Banco de Dados

**Disciplina:** Banco de Dados e Mineração de Dados\
**Professor:** Rodolfo Terra\
**LinkedIn:**
[linkedin.com/in/rodolffoterra/](https://www.linkedin.com/in/rodolffoterra/)\
**GitHub:** [github.com/rodolffoterra](https://github.com/rodolffoterra)

> **Tema da aula:** Como os dados são organizados para construir
> sistemas inteligentes.

------------------------------------------------------------------------

## 📚 Visão Geral

Bancos de dados fazem parte de praticamente todos os sistemas digitais
que utilizamos.

Quando acessamos um aplicativo, realizamos uma compra, fazemos uma
transferência bancária, solicitamos uma corrida ou ouvimos uma música,
informações precisam ser **armazenadas, organizadas, consultadas e
atualizadas**.

Nesta primeira aula, estudamos os fundamentos necessários para
compreender como um banco de dados funciona, passando por:

-   dados e informação;
-   banco de dados;
-   SGBD;
-   MySQL;
-   tabelas;
-   registros e campos;
-   chave primária;
-   relacionamentos;
-   modelagem de dados;
-   criação de banco e tabelas;
-   inserção de dados;
-   acesso ao banco utilizando Python.

------------------------------------------------------------------------

## 🎯 Objetivos da Aula

Ao final desta aula, o aluno deverá ser capaz de:

-   compreender o que é um banco de dados;
-   identificar onde bancos de dados são utilizados;
-   diferenciar **dado** de **informação**;
-   compreender o papel de um **SGBD**;
-   conhecer o funcionamento básico do **MySQL**;
-   entender tabelas, linhas e colunas;
-   compreender o conceito de **chave primária**;
-   entender como tabelas podem se relacionar;
-   reconhecer a importância da modelagem de dados;
-   criar um banco simples no MySQL;
-   criar uma tabela utilizando SQL;
-   inserir registros;
-   compreender como uma aplicação Python pode acessar um banco de
    dados.

------------------------------------------------------------------------

## 🌎 Onde existem Bancos de Dados?

Bancos de dados estão presentes em grande parte dos sistemas utilizados
diariamente.

Aplicações como sistemas bancários, redes sociais, serviços de
streaming, aplicativos de transporte e sistemas empresariais precisam
armazenar milhões ou até bilhões de informações.

Imagine, por exemplo, um aplicativo de transporte. Ele precisa armazenar
informações sobre:

``` text
Usuários
Motoristas
Veículos
Corridas
Localizações
Pagamentos
Avaliações
```

Sem um banco de dados, essas informações não poderiam ser gerenciadas
adequadamente.

------------------------------------------------------------------------

## 🏪 O Problema

Imagine uma loja que não possui um banco de dados.

As informações dos clientes poderiam estar anotadas em papéis ou
planilhas diferentes.

Isso poderia provocar problemas como:

``` text
Clientes anotados em papel
        ↓
Produtos perdidos
        ↓
Vendas erradas
        ↓
Dados duplicados
        ↓
Informações inconsistentes
```

Com um banco de dados, as informações ficam centralizadas e organizadas,
facilitando cadastro, consultas, controle de estoque, histórico,
relatórios e buscas.

> **Banco de dados organiza informações.**

------------------------------------------------------------------------

## 🗄️ O que é um Banco de Dados?

Um **Banco de Dados** é uma coleção organizada de informações que podem
ser armazenadas, consultadas, atualizadas e removidas.

``` text
Dados
  ↓
Banco de Dados
  ↓
Sistema
  ↓
Usuário
```

O banco funciona como uma estrutura central responsável por manter as
informações necessárias para o funcionamento do sistema.

------------------------------------------------------------------------

## 📊 Dados x Informação

Apesar de frequentemente serem utilizados como sinônimos, **dado** e
**informação** representam conceitos diferentes.

Um dado isolado possui pouco significado:

``` text
Maria
23
MG
Notebook
```

Quando adicionamos contexto, esses dados passam a transmitir informação:

``` text
Maria → Maria possui 23 anos.
23 → idade de Maria.
MG → Maria mora em Minas Gerais.
Notebook → Maria comprou um notebook.
```

> **Dados sozinhos possuem pouco valor. Quando organizados, viram
> informação.**

------------------------------------------------------------------------

## ⚙️ Como um Banco de Dados funciona?

Em uma aplicação tradicional, o usuário normalmente não acessa
diretamente o banco de dados.

``` text
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Aplicação  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Banco     │
│  de Dados   │
└──────┬──────┘
       │
       ▼
    Resposta
```

A aplicação recebe os dados, realiza as validações necessárias e envia
instruções ao banco de dados. Em uma consulta, o banco retorna as
informações solicitadas para a aplicação.

------------------------------------------------------------------------

## 🖥️ O que é um SGBD?

**SGBD** significa **Sistema Gerenciador de Banco de Dados**.

É o software responsável por gerenciar o banco e permitir operações
sobre os dados.

Entre suas responsabilidades estão:

-   armazenar;
-   consultar;
-   alterar;
-   proteger;
-   organizar;
-   gerenciar.

Exemplos:

-   MySQL;
-   PostgreSQL;
-   Oracle Database;
-   Microsoft SQL Server.

> O banco contém os dados. O **SGBD é a ferramenta responsável por
> administrar esses dados**.

------------------------------------------------------------------------

## 🐬 Por que utilizar MySQL?

Nesta disciplina utilizaremos o **MySQL** como uma das principais
ferramentas para estudar bancos de dados relacionais.

Entre suas características estão:

-   gratuito;
-   muito utilizado;
-   grande comunidade;
-   excelente documentação;
-   integração com Python;
-   amplamente utilizado no mercado.

------------------------------------------------------------------------

## 🏗️ Arquitetura utilizada nas aulas

``` text
Python
   │
   ▼
Driver MySQL
   │
   ▼
MySQL Server
   │
   ▼
Banco de Dados
   │
   ▼
Tabelas
   │
   ▼
Dados
```

**Python:** linguagem utilizada para desenvolver a aplicação que
acessará os dados.

**Driver MySQL:** biblioteca responsável por permitir a comunicação
entre Python e MySQL.

**MySQL Server:** servidor responsável pelo gerenciamento do banco.

**Banco:** agrupa logicamente as informações de uma aplicação.

**Tabelas:** estruturas responsáveis por armazenar os dados.

------------------------------------------------------------------------

## 📋 O que é uma Tabela?

Uma tabela é uma estrutura onde os dados são armazenados de forma
organizada em **linhas e colunas**.

    ID Nome             Cidade          Telefone
  ---- ---------------- --------------- -------------------
     1 Ana Silva        Maringá - PR    \(44\) 99999-1111
     2 Bruno Santos     Londrina - PR   \(43\) 98888-2222
     3 Carla Oliveira   Curitiba - PR   \(41\) 97777-3333

Cada **linha** representa um registro.

Cada **coluna** representa uma característica daquele registro.

> **As tabelas permitem armazenar, organizar e relacionar informações.**

------------------------------------------------------------------------

## 🛒 Exemplo Real --- Loja Online

Imagine uma loja virtual.

Uma tabela de produtos poderia possuir:

``` text
Produtos
├── ID
├── Nome
├── Preço
├── Quantidade
└── Categoria
```

Quando um usuário pesquisa um produto, o sistema consulta essa tabela
para descobrir nome, preço, disponibilidade, quantidade em estoque e
categoria.

``` text
Cliente
   ↓
Loja Online
   ↓
Banco de Dados
   ↓
Tabela Produtos
   ↓
Resultado
   ↓
Cliente
```

------------------------------------------------------------------------

## 🔑 Chave Primária

A **chave primária**, ou **Primary Key**, é um campo utilizado para
identificar exclusivamente cada registro de uma tabela.

    ID Nome    Cidade
  ---- ------- ----------
     1 Maria   Maringá
     2 João    Londrina
     3 Pedro   Curitiba

O campo `ID` pode funcionar como chave primária.

> **A chave primária é o coração de uma tabela: ela garante identidade,
> integridade e confiabilidade dos dados.**

------------------------------------------------------------------------

## 🔗 Relacionamentos

Em um banco de dados relacional, tabelas podem se relacionar.

``` text
CLIENTES
----------------
id_cliente
nome
email
cidade
```

``` text
PEDIDOS
----------------
id_pedido
id_cliente
data
valor
```

O campo `id_cliente` permite descobrir qual cliente realizou determinado
pedido.

``` text
CLIENTES
    1
    │
    │ realiza
    │
    N
 PEDIDOS
```

Isso representa um relacionamento **1:N --- um para muitos**.

Um cliente pode realizar vários pedidos, enquanto cada pedido pertence a
um determinado cliente.

------------------------------------------------------------------------

## 🧠 Modelagem de Dados

Antes de criar tabelas, é importante entender **quais informações o
sistema precisa armazenar e como elas se relacionam**.

Para uma loja online, por exemplo:

``` text
Cliente
Produto
Pedido
Pagamento
Entrega
```

Uma representação simplificada:

``` text
Cliente ─── realiza ───► Pedido
Pedido  ─── contém ────► Produto
Pedido  ─── possui ────► Pagamento
Pedido  ─── gera ──────► Entrega
```

A modelagem transforma um problema do mundo real em uma estrutura
organizada de dados.

------------------------------------------------------------------------

## 🛍️ Exemplo de Modelagem --- Loja Online

### Cliente

``` text
id_cliente
nome
email
telefone
```

### Produto

``` text
id_produto
nome
preco
estoque
```

### Pedido

``` text
id_pedido
id_cliente
data
valor
```

### Pagamento

``` text
id_pagamento
id_pedido
forma_pagamento
status
```

### Entrega

``` text
id_entrega
id_pedido
endereco
status
```

------------------------------------------------------------------------

## 🧪 Primeira Demonstração --- Criando um Banco no MySQL

``` sql
CREATE DATABASE loja;
```

Esse comando solicita ao MySQL a criação de um banco chamado `loja`.

------------------------------------------------------------------------

## 🏗️ Criando uma Tabela

``` sql
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(100)
);
```

  Comando          Significado
  ---------------- -----------------------------
  `CREATE TABLE`   cria uma nova tabela
  `clientes`       nome da tabela
  `id`             identificador do cliente
  `INT`            número inteiro
  `PRIMARY KEY`    define a chave primária
  `nome`           armazena o nome
  `VARCHAR(100)`   texto de até 100 caracteres
  `cidade`         armazena a cidade

------------------------------------------------------------------------

## ➕ Inserindo Dados

``` sql
INSERT INTO clientes
VALUES
(1, 'Maria', 'Belo Horizonte');
```

Resultado:

    id nome    cidade
  ---- ------- ----------------
     1 Maria   Belo Horizonte

Cada linha inserida representa um novo registro.

------------------------------------------------------------------------

## 🐍 Python acessando o Banco

Python pode realizar a comunicação com o MySQL utilizando um driver de
conexão.

``` python
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha",
    database="loja"
)
```

Fluxo:

``` text
Python
   │
   ▼
Driver
   │
   ▼
MySQL
   │
   ▼
Banco loja
```

Com a conexão estabelecida, a aplicação pode realizar operações sobre o
banco.

------------------------------------------------------------------------

## 💼 Banco de Dados e Mercado de Trabalho

O conhecimento de banco de dados está presente em diversas carreiras de
tecnologia.

### Engenharia de Dados

-   Pipelines;
-   ETL;
-   Integrações;
-   Data Lakes;
-   Data Warehouses;
-   Processamento de dados.

### Análise de Dados

-   SQL;
-   Consultas;
-   Relatórios;
-   Dashboards;
-   Indicadores;
-   Análises.

### Ciência de Dados

-   Estatística;
-   Machine Learning;
-   Modelos preditivos;
-   Experimentação;
-   Análise de grandes volumes de dados.

------------------------------------------------------------------------

## 🔄 Do Banco de Dados à Mineração de Dados

Os fundamentos desta aula são importantes para compreender a evolução da
disciplina:

``` text
DADOS
   ↓
BANCO DE DADOS
   ↓
ORGANIZAÇÃO
   ↓
CONSULTA
   ↓
ANÁLISE
   ↓
MINERAÇÃO DE DADOS
   ↓
CONHECIMENTO
   ↓
DECISÃO
```

Antes de descobrir padrões nos dados, precisamos compreender como eles
são armazenados, estruturados e relacionados.

------------------------------------------------------------------------

## 📝 Resumo da Aula

Nesta primeira aula estudamos:

-   [x] O que é um Banco de Dados
-   [x] Onde bancos de dados são utilizados
-   [x] Dados x Informação
-   [x] O que é um SGBD
-   [x] MySQL
-   [x] Tabelas
-   [x] Registros e campos
-   [x] Chave Primária
-   [x] Relacionamentos
-   [x] Modelagem
-   [x] Criação de um banco
-   [x] Criação de tabelas
-   [x] Inserção de dados
-   [x] Integração inicial com Python

> **Um banco de dados não é apenas um local para guardar informações.
> Ele fornece uma estrutura organizada para que sistemas consigam
> registrar, relacionar, consultar e utilizar dados de maneira
> confiável.**

------------------------------------------------------------------------

## 🚀 Próximos Passos

``` text
Fundamentos
     ↓
Modelagem
     ↓
SQL
     ↓
Banco de Dados
     ↓
Data Warehouse
     ↓
Mineração de Dados
     ↓
Conhecimento
```

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**\
**Disciplina:** Banco de Dados e Mineração de Dados

🔗 [LinkedIn](https://www.linkedin.com/in/rodolffoterra/)\
💻 [GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

> **Dados bem organizados são a base para transformar informação em
> conhecimento.**
