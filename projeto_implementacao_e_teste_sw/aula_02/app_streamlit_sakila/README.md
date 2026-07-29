# Laboratório Didático Streamlit + MySQL Sakila

Aplicação multipáginas para demonstrar Projeto, Implementação e Teste de Software usando Python, Streamlit, SQL e o banco de exemplo Sakila.

## 1. Preparar o MySQL

No MySQL Workbench, execute nesta ordem:

1. `sql/sakila-schema.sql`
2. `sql/sakila-data.sql`

## 2. Criar o ambiente

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## 3. Configurar a conexão

Copie `.env.example` para `.env` e informe usuário e senha do MySQL.

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DATABASE=sakila
```

## 4. Executar

```powershell
streamlit run app.py
```

## 5. Executar testes

```powershell
python -m pytest -v
```

## Sequência das páginas

1. Sequência didática
2. Arquitetura e C4
3. Modelo Sakila
4. Laboratório SQL
5. Catálogo de filmes
6. CRUD de atores
7. Dashboard
8. Testes e qualidade
