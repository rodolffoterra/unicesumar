# Aula 05 --- Do Streamlit à API REST

> **Integrando Streamlit, FastAPI e MySQL no Projeto TechPort**

**Disciplina:** Projeto, Implementação e Teste de Software\
**Professor:** Rodolfo Terra\
**Projeto aplicado:** TechPort --- Sistema de Gestão de Chamados\
**Instituição:** UniCesumar

[LinkedIn](https://www.linkedin.com/in/rodolffoterra/) •
[GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## Sobre esta aula

Até esta etapa do projeto, o **TechPort** já possuía interface
construída com Streamlit, código Python e persistência em MySQL.

Nesta aula, a arquitetura evolui com a introdução de uma **API REST
utilizando FastAPI**.

A principal mudança é a criação de uma camada intermediária entre a
interface e os dados:

``` text
ANTES

Streamlit
    ↓
Python
    ↓
MySQL
```

``` text
AGORA

Streamlit
    ↓
HTTP
    ↓
FastAPI
    ↓
Service
    ↓
Repository
    ↓
MySQL
```

A partir desse ponto, a interface deixa de concentrar todas as
responsabilidades. Cada camada passa a possuir um papel específico
dentro da aplicação.

------------------------------------------------------------------------

# 1. Onde paramos na aula anterior?

Na Aula 04, o TechPort já era capaz de:

-   executar uma interface em Streamlit;
-   utilizar Python para implementar a aplicação;
-   conectar-se ao banco MySQL;
-   consultar e manipular dados persistidos.

O fluxo básico era:

``` text
STREAMLIT
    ↓
PYTHON
    ↓
MYSQL
```

Essa arquitetura funciona, mas cria uma dependência direta entre a
interface e a lógica de acesso aos dados.

A pergunta que conduz a Aula 05 é:

> **E se amanhã tivermos outra aplicação consumindo os mesmos dados e
> regras do TechPort?**

Por exemplo:

``` text
Aplicação Web ─┐
Aplicativo     ├──→ API ───→ MySQL
Outro sistema ┘
```

É nesse cenário que a API passa a fazer sentido.

------------------------------------------------------------------------

# 2. Criando uma camada intermediária

A API funciona como uma camada de comunicação entre quem solicita uma
operação e a aplicação responsável por executá-la.

No TechPort:

``` text
STREAMLIT
    ↓
FASTAPI
    ↓
MYSQL
```

O Streamlit não precisa conhecer diretamente todos os detalhes de
persistência.

Ele faz uma **requisição HTTP** para a API, e a API coordena a operação.

------------------------------------------------------------------------

# 3. O que é uma API?

**API --- Application Programming Interface** é uma interface que
permite a comunicação entre aplicações.

Uma forma simples de visualizar:

``` text
CLIENTE
   │
   │ REQUISIÇÃO
   ▼
  API
   │
   │ RESPOSTA
   ▼
CLIENTE
```

No contexto desta aula:

-   o **Streamlit** pode atuar como cliente;
-   a **FastAPI** recebe a requisição;
-   a aplicação processa a solicitação;
-   o **MySQL** mantém os dados;
-   a API devolve uma resposta.

A API estabelece um contrato de comunicação entre as partes.

------------------------------------------------------------------------

# 4. Como uma aplicação conversa com uma API?

A comunicação ocorre principalmente por meio do protocolo **HTTP**.

Uma requisição normalmente envolve:

-   um endereço;
-   um método HTTP;
-   dados de entrada, quando necessários;
-   uma resposta da API.

Exemplo conceitual:

``` text
CLIENTE
   │
   │ GET /chamados
   ▼
FASTAPI
   │
   │ consulta
   ▼
MYSQL
   │
   │ resultado
   ▼
FASTAPI
   │
   │ JSON
   ▼
CLIENTE
```

------------------------------------------------------------------------

# 5. Endpoint --- a porta de acesso da API

Um **endpoint** representa um endereço disponibilizado pela API para
executar determinada operação.

Exemplos do domínio do TechPort:

``` text
GET    /usuarios
GET    /tecnicos
GET    /chamados
GET    /prioridades
GET    /status
GET    /comentarios
GET    /historico_chamados
GET    /anexos
```

Cada endpoint deve possuir uma responsabilidade clara.

------------------------------------------------------------------------

# 6. Recursos da API

Os recursos refletem os elementos do domínio da aplicação.

No TechPort, podemos trabalhar com recursos como:

``` text
USUÁRIOS
TÉCNICOS
CHAMADOS
PRIORIDADES
STATUS
COMENTÁRIOS
HISTÓRICO
ANEXOS
```

A API organiza a forma como esses recursos podem ser consultados ou
modificados.

------------------------------------------------------------------------

# 7. Métodos HTTP e CRUD

Os métodos HTTP expressam a intenção da operação.

  Método            Operação comum         CRUD
  ----------------- ---------------------- --------
  `GET`             Consultar dados        READ
  `POST`            Criar um recurso       CREATE
  `PUT` / `PATCH`   Atualizar um recurso   UPDATE
  `DELETE`          Excluir um recurso     DELETE

Exemplo:

``` text
GET /chamados
```

significa solicitar à API uma leitura da coleção de chamados.

Outro exemplo:

``` text
GET /chamados/25
```

representa a consulta de um chamado específico.

------------------------------------------------------------------------

# 8. CRUD do TechPort através da API

Com a API, operações antes executadas diretamente pela interface passam
a ser expostas por endpoints.

Exemplo conceitual:

``` text
Criar chamado
POST /chamados

Consultar chamado
GET /chamados/{id}

Atualizar chamado
PUT/PATCH /chamados/{id}

Excluir chamado
DELETE /chamados/{id}
```

Isso separa a experiência visual da regra utilizada para acessar e
modificar os dados.

------------------------------------------------------------------------

# 9. Requisição e resposta

Toda comunicação com uma API possui duas partes fundamentais:

``` text
REQUISIÇÃO
    ↓
   API
    ↓
RESPOSTA
```

A requisição informa o que o cliente deseja.

A resposta informa o resultado da operação.

Essa resposta pode conter:

-   dados;
-   mensagens;
-   códigos HTTP;
-   informações de erro;
-   estruturas JSON.

------------------------------------------------------------------------

# 10. Como a API devolve os dados?

APIs REST frequentemente utilizam **JSON** para representar os dados.

Exemplo:

``` json
{
  "id": 25,
  "titulo": "Problema de acesso",
  "status": "aberto"
}
```

Uma lista de registros pode ser representada como:

``` json
[
  {
    "id": 25,
    "titulo": "Problema de acesso"
  },
  {
    "id": 26,
    "titulo": "Erro no sistema"
  }
]
```

O JSON é independente da interface. Isso permite que diferentes clientes
consumam a mesma API.

------------------------------------------------------------------------

# 11. FastAPI

Nesta aula utilizamos **FastAPI** para construir a API do TechPort.

Ela passa a ocupar a camada intermediária:

``` text
STREAMLIT
    ↓
FASTAPI
    ↓
MYSQL
```

Com FastAPI podemos definir rotas e métodos HTTP de forma explícita.

Exemplo simplificado:

``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"msg": "TechPort API funcionando"}
```

------------------------------------------------------------------------

# 12. Interpretando o código

No exemplo anterior:

``` python
app = FastAPI()
```

cria a aplicação.

``` python
@app.get("/")
```

define uma rota HTTP utilizando o método `GET`.

``` python
def inicio():
```

define a função executada quando a rota é chamada.

``` python
return {"msg": "TechPort API funcionando"}
```

devolve uma resposta que será representada em JSON.

------------------------------------------------------------------------

# 13. A API precisa de um servidor

Criar o código da API não é suficiente. É necessário um servidor ASGI
para executá-la.

Nesta aula utilizamos **Uvicorn**.

Exemplo:

``` powershell
python -m uvicorn app.api.fastapi_app:app --reload
```

O servidor inicia a aplicação e disponibiliza os endpoints para receber
requisições HTTP.

Um endereço comum durante o desenvolvimento é:

``` text
http://127.0.0.1:8000
```

------------------------------------------------------------------------

# 14. Como testar a API?

Uma das vantagens da FastAPI é disponibilizar documentação interativa
automaticamente.

Com a API em execução:

``` text
http://127.0.0.1:8000/docs
```

abre a interface **Swagger UI**.

No Swagger podemos:

1.  visualizar os endpoints;
2.  selecionar uma operação;
3.  clicar em **Try it out**;
4.  executar a requisição;
5.  analisar o status e a resposta JSON.

``` text
FastAPI
   ↓
Swagger UI
   ↓
Endpoint
   ↓
Execute
   ↓
Response
```

------------------------------------------------------------------------

# 15. Swagger e Front-End

O Swagger é extremamente útil para validar a API antes de integrar o
front-end.

Isso permite separar dois problemas:

``` text
1. A API está funcionando?
2. O Streamlit está consumindo a API corretamente?
```

Fluxo recomendado:

``` text
Construir API
      ↓
Testar no Swagger
      ↓
Validar resposta
      ↓
Integrar ao Streamlit
```

------------------------------------------------------------------------

# 16. Arquitetura profissional

À medida que o projeto cresce, não devemos colocar toda a aplicação em
um único arquivo.

A Aula 05 introduz uma arquitetura organizada em responsabilidades:

``` text
INTERFACE
    ↓
API / ROUTES
    ↓
SERVICES
    ↓
REPOSITORIES
    ↓
DATABASE
```

Essa divisão facilita:

-   manutenção;
-   testes;
-   evolução;
-   reutilização;
-   leitura do código;
-   isolamento de responsabilidades.

------------------------------------------------------------------------

# 17. Fluxo completo da aplicação

A partir desta aula, o fluxo conceitual do TechPort passa a ser:

``` text
STREAMLIT
    ↓
FASTAPI
    ↓
ROUTES
    ↓
SERVICES
    ↓
REPOSITORIES
    ↓
MYSQL
```

A resposta percorre o caminho inverso até chegar novamente à interface.

------------------------------------------------------------------------

# 18. Responsabilidade de cada camada

  Camada           Responsabilidade
  ---------------- ---------------------------------------------------
  **Streamlit**    Interface com o usuário
  **Route**        Receber a requisição HTTP e direcionar a operação
  **Service**      Executar regras de negócio
  **Repository**   Acessar e manipular os dados
  **Database**     Gerenciar conexão e persistência
  **MySQL**        Armazenar os dados

O princípio central é:

> **Cada camada possui uma responsabilidade.**

------------------------------------------------------------------------

# 19. Routes

As **Routes** representam os endpoints expostos pela API.

Exemplo:

``` text
GET /usuarios
GET /tecnicos
GET /chamados
GET /prioridades
GET /status
GET /comentarios
GET /historico
GET /anexos
```

A Route recebe a solicitação e encaminha o processamento para a camada
apropriada.

Ela não deve concentrar toda a regra de negócio nem o acesso direto ao
banco.

------------------------------------------------------------------------

# 20. Services

A camada **Service** concentra as regras de negócio.

Exemplos de responsabilidades:

-   validar dados;
-   verificar regras;
-   determinar se uma operação pode ocorrer;
-   coordenar diferentes operações;
-   preparar o resultado para a Route.

Fluxo:

``` text
ROUTE
   ↓
SERVICE
   ↓
REPOSITORY
```

------------------------------------------------------------------------

# 21. Repository

O **Repository** é responsável pelo acesso aos dados.

Exemplos:

-   executar `SELECT`;
-   executar `INSERT`;
-   executar `UPDATE`;
-   executar `DELETE`;
-   transformar resultados do banco em estruturas utilizadas pela
    aplicação.

``` text
SERVICE
    ↓
REPOSITORY
    ↓
MYSQL
```

Assim, as regras de negócio não precisam conhecer detalhes de SQL ou de
conexão.

------------------------------------------------------------------------

# 22. Database

A camada de **Database** centraliza aspectos relacionados à conexão com
o banco.

Ela pode ser responsável por:

-   abrir conexões;
-   recuperar configurações;
-   controlar acesso ao MySQL;
-   disponibilizar a conexão para os repositories.

``` text
Repository
    ↓
Database
    ↓
MySQL
```

------------------------------------------------------------------------

# 23. API Router

À medida que a quantidade de endpoints cresce, a aplicação pode utilizar
`APIRouter` para organizar as rotas por domínio.

Exemplo conceitual:

``` text
FastAPI
   ↓
APIRouter
   ├── /usuarios
   ├── /tecnicos
   ├── /chamados
   └── /anexos
```

Isso evita concentrar todos os endpoints no arquivo principal da API.

------------------------------------------------------------------------

# 24. Primeira integração

Depois de validar a API, podemos realizar a primeira integração do
front-end.

Exemplo conceitual em Python:

``` python
import requests

response = requests.get("http://127.0.0.1:8000/chamados")
dados = response.json()
```

Agora o Streamlit não precisa executar diretamente a consulta SQL.

Ele solicita os dados à API.

------------------------------------------------------------------------

# 25. Depois faremos chamadas

Com a integração funcionando, o front-end pode executar diferentes
operações:

``` text
GET /chamados
GET /chamados/{id}
POST /chamados
PUT /chamados/{id}
DELETE /chamados/{id}
```

O fluxo completo se torna:

``` text
Streamlit
    ↓ requests
FastAPI
    ↓
Routes
    ↓
Services
    ↓
Repositories
    ↓
MySQL
```

------------------------------------------------------------------------

# 26. A API não substitui o MySQL

A API não é um banco de dados.

Ela cria uma camada de comunicação e organização entre o cliente e a
persistência.

``` text
STREAMLIT
Interface
    ↓
FASTAPI
Comunicação + regras
    ↓
MYSQL
Persistência
```

Cada tecnologia continua tendo sua própria responsabilidade.

------------------------------------------------------------------------

# 27. O que muda no Streamlit?

Antes, o Streamlit podia realizar diretamente uma operação no banco.

``` text
Streamlit → MySQL
```

Depois da evolução arquitetural:

``` text
Streamlit → FastAPI → MySQL
```

Na prática, o front-end passa a utilizar requisições HTTP.

Exemplo:

``` python
requests.get(...)
requests.post(...)
requests.put(...)
requests.delete(...)
```

------------------------------------------------------------------------

# 28. Agora temos duas aplicações

Ao executar o TechPort nesta arquitetura, temos dois processos
principais:

``` text
FASTAPI
Servidor da API
Porta 8000
```

e

``` text
STREAMLIT
Interface
Porta 8501
```

Durante o desenvolvimento, normalmente utilizamos terminais separados
para executar cada aplicação.

------------------------------------------------------------------------

# 29. Ordem para executar o sistema

Uma sequência didática para iniciar o TechPort:

``` text
1. MySQL disponível
2. Ambiente Python preparado
3. FastAPI iniciada
4. Swagger validado
5. Streamlit iniciado
6. Interface acessa a API
7. API executa regras e acessa o banco
8. Resultado retorna ao usuário
```

Essa sequência facilita a identificação de problemas durante a
integração.

------------------------------------------------------------------------

# 30. Roteiro da prática

Durante a prática, o objetivo é acompanhar o dado atravessando a
arquitetura.

``` text
Usuário
   ↓
Streamlit
   ↓
FastAPI
   ↓
Service
   ↓
Repository
   ↓
MySQL
```

A ideia não é apenas "fazer funcionar", mas compreender **qual camada
executa cada responsabilidade**.

------------------------------------------------------------------------

# 31. Evolução do TechPort

Ao final desta aula, o projeto deixa de ser apenas uma interface
conectada diretamente ao banco.

``` text
AULA ANTERIOR

STREAMLIT
    ↓
MYSQL
```

``` text
AULA 05

STREAMLIT
    ↓
FASTAPI
    ↓
ROUTES
    ↓
SERVICES
    ↓
REPOSITORIES
    ↓
MYSQL
```

Essa evolução prepara o projeto para testes, novas interfaces,
manutenção e crescimento.

------------------------------------------------------------------------

# 32. Objetivo final da aula

Ao clicar em uma ação no Streamlit, queremos compreender o fluxo
completo:

``` text
INTERFACE
    ↓
API
    ↓
REGRA
    ↓
DADOS
```

Ou, tecnicamente:

``` text
STREAMLIT
    ↓ HTTP
FASTAPI
    ↓
SERVICE
    ↓
REPOSITORY
    ↓
MYSQL
```

------------------------------------------------------------------------

# 33. Resumo

Nesta aula aprendemos que:

-   uma API cria uma camada de comunicação entre aplicações;
-   HTTP é utilizado para realizar requisições e receber respostas;
-   endpoints representam portas de acesso aos recursos;
-   métodos como `GET`, `POST`, `PUT/PATCH` e `DELETE` expressam
    operações;
-   JSON é utilizado para troca estruturada de dados;
-   FastAPI permite construir APIs em Python;
-   Uvicorn executa a aplicação FastAPI;
-   Swagger facilita testes e documentação;
-   uma aplicação pode ser organizada em Routes, Services, Repositories
    e Database;
-   o Streamlit pode consumir a API utilizando requisições HTTP;
-   a API **não substitui** o MySQL;
-   separar responsabilidades prepara o software para crescer com mais
    organização e qualidade.

------------------------------------------------------------------------

# Tecnologias trabalhadas

  Tecnologia         Papel
  ------------------ --------------------------------------
  **Python**         Linguagem da aplicação
  **Streamlit**      Interface do usuário
  **FastAPI**        API REST
  **Uvicorn**        Servidor ASGI
  **Requests**       Comunicação HTTP pelo cliente Python
  **JSON**           Formato de troca de dados
  **Swagger UI**     Teste e documentação da API
  **MySQL**          Persistência
  **Routes**         Endpoints
  **Services**       Regras de negócio
  **Repositories**   Acesso aos dados

------------------------------------------------------------------------

# Conclusão

A principal evolução da Aula 05 pode ser resumida em uma mudança
simples:

``` text
ANTES
Interface → Dados
```

``` text
AGORA
Interface → API → Regras → Dados
```

> **Uma boa arquitetura não existe apenas para fazer o sistema funcionar
> hoje. Ela organiza responsabilidades para permitir que o software seja
> compreendido, testado e evoluído amanhã.**

------------------------------------------------------------------------

## Professor

**Professor Rodolfo Terra**

-   [LinkedIn ---
    linkedin.com/in/rodolffoterra/](https://www.linkedin.com/in/rodolffoterra/)
-   [GitHub ---
    github.com/rodolffoterra](https://github.com/rodolffoterra)

------------------------------------------------------------------------

**Projeto, Implementação e Teste de Software**\
**TechPort --- Sistema de Gestão de Chamados**

`Streamlit → HTTP → FastAPI → Services → Repositories → MySQL`
