# Aula 03 — FastAPI, Streamlit e MySQL Sakila

Projeto reduzido para demonstrar quatro operações de uma API:

- GET: listar atores;
- POST: cadastrar ator;
- PUT: atualizar ator;
- DELETE: excluir ator.

O projeto utiliza diretamente a tabela `actor` que já existe no banco `sakila`.
Nenhuma tabela é criada pelo projeto.

## Arquitetura

```text
Streamlit -> API FastAPI -> MySQL -> sakila.actor
```

## Configuração

O arquivo `.env` contém:

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=1234556
MYSQL_DATABASE=sakila

API_URL=http://127.0.0.1:8000
```

## Execução

### 1. Preparar o ambiente

Execute:

```text
preparar_ambiente.bat
```

### 2. Executar a API

Execute:

```text
executar_api.bat
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

Teste de conexão:

```text
http://127.0.0.1:8000/health
```

### 3. Executar o Streamlit

Em outra janela, execute:

```text
executar_streamlit.bat
```

## Endpoints

```text
GET    /atores
POST   /atores
PUT    /atores/{actor_id}
DELETE /atores/{actor_id}
```

## Observação

A exclusão de um ator pode ser impedida pelo MySQL caso esse ator esteja
relacionado a registros da tabela `film_actor`. Para testar o DELETE em aula,
cadastre primeiro um ator novo e depois exclua esse mesmo registro.
