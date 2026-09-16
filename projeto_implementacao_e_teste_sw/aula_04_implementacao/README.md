# Aula 04 --- Integração Python + MySQL no TechPort

> **Da interface aos dados: conectando a aplicação ao banco de dados com
> segurança e organização.**

**Disciplina:** Projeto, Implementação e Teste de Software\
**Professor:** Rodolfo Terra\
**Projeto aplicado:** TechPort --- Sistema de Gestão de Chamados\
**Instituição:** UniCesumar

[LinkedIn](https://www.linkedin.com/in/rodolffoterra/) •
[GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## Sobre esta aula

Nesta etapa da disciplina, o **TechPort** deixa de trabalhar apenas com
estruturas isoladas e passa a integrar a aplicação Python ao banco de
dados **MySQL**.

O objetivo é compreender o caminho percorrido pelos dados entre a
interface, o código Python e a persistência:

``` text
USUÁRIO
   ↓
STREAMLIT
   ↓
PYTHON
   ↓
CONEXÃO
   ↓
MYSQL
```

A aula também prepara o ambiente do projeto para uma evolução mais
organizada, utilizando **ambiente virtual**, arquivo de dependências e
**variáveis de ambiente** para configurações sensíveis.

------------------------------------------------------------------------

# 1. Evolução do TechPort

Até este momento, diferentes partes do sistema já começaram a tomar
forma.

Agora precisamos fazer com que a aplicação consiga efetivamente
conversar com o banco.

``` text
INTERFACE
    ↓
APLICAÇÃO PYTHON
    ↓
BANCO DE DADOS
```

Isso significa transformar ações realizadas pelo usuário em operações
persistentes.

Por exemplo:

``` text
Usuário preenche formulário
          ↓
Python recebe os dados
          ↓
Executa uma operação SQL
          ↓
MySQL grava os dados
          ↓
Aplicação apresenta o resultado
```

------------------------------------------------------------------------

# 2. Por que utilizar um banco de dados?

Uma aplicação precisa manter informações mesmo depois de ser encerrada.

Sem persistência:

``` text
Aplicação encerra
      ↓
Dados em memória desaparecem
```

Com persistência:

``` text
Aplicação
    ↓
MySQL
    ↓
Dados permanecem armazenados
```

No TechPort, o banco mantém informações relacionadas aos elementos do
sistema, como usuários, técnicos, chamados, comentários, histórico e
anexos.

------------------------------------------------------------------------

# 3. Preparando o ambiente Python

Antes de instalar as bibliotecas do projeto, criamos um **ambiente
virtual**.

O ambiente virtual permite isolar as dependências utilizadas pelo
TechPort das demais instalações Python existentes no computador.

Criar:

``` powershell
python -m venv .venv
```

Ativar no PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Quando estiver ativo, o terminal normalmente passa a apresentar:

``` text
(.venv) PS C:\...\techport>
```

------------------------------------------------------------------------

# 4. Por que utilizar uma VENV?

Imagine dois projetos:

``` text
PROJETO A
Python
Biblioteca X 1.0

PROJETO B
Python
Biblioteca X 2.0
```

Sem isolamento, diferentes versões podem gerar conflitos.

Com ambientes virtuais:

``` text
PROJETO A → .venv própria
PROJETO B → .venv própria
```

Cada projeto mantém suas dependências de forma independente.

------------------------------------------------------------------------

# 5. requirements.txt

As bibliotecas necessárias ao projeto podem ser registradas no arquivo:

``` text
requirements.txt
```

A instalação pode ser realizada com:

``` powershell
pip install -r requirements.txt
```

Isso torna a preparação do ambiente mais reproduzível.

Em vez de instalar manualmente cada biblioteca em outro computador, o
projeto informa quais dependências são necessárias.

------------------------------------------------------------------------

# 6. Estrutura básica do projeto

Uma organização coerente facilita a evolução da aplicação.

Exemplo conceitual:

``` text
techport/
│
├── .venv/
├── app/
│   ├── pages/
│   ├── database/
│   ├── models/
│   └── ...
│
├── requirements.txt
└── ...
```

O objetivo não é apenas fazer o código executar, mas manter o projeto
compreensível e preparado para crescer.

------------------------------------------------------------------------

# 7. Conectando Python ao MySQL

Para que o Python acesse o banco, precisamos de um **driver/conector**.

O fluxo passa a ser:

``` text
PYTHON
   ↓
CONECTOR MYSQL
   ↓
MYSQL SERVER
   ↓
BANCO TECHPORT
```

A conexão utiliza informações como:

``` text
HOST
PORTA
USUÁRIO
SENHA
BANCO
```

Essas configurações identificam onde o banco está e como a aplicação
pode acessá-lo.

------------------------------------------------------------------------

# 8. O problema das credenciais no código

Uma prática inadequada seria escrever diretamente no código:

``` python
senha = "minha_senha"
```

Isso cria riscos porque a credencial pode acabar:

-   no Git;
-   no GitHub;
-   em um ZIP;
-   em prints;
-   em compartilhamentos do projeto;
-   no histórico do código.

A aplicação precisa da senha, mas a senha **não deve fazer parte do
código-fonte**.

------------------------------------------------------------------------

# 9. Variáveis de ambiente e arquivo .env

Uma alternativa é manter configurações sensíveis em um arquivo `.env`.

Exemplo conceitual:

``` env
DB_HOST=localhost
DB_PORT=3306
DB_USER=usuario
DB_PASSWORD=senha
DB_NAME=techport
```

E no código Python recuperar os valores do ambiente.

A separação passa a ser:

``` text
CÓDIGO PYTHON
     +
CONFIGURAÇÃO .env
     ↓
CONEXÃO
     ↓
MYSQL
```

> O `.env` contém configuração do ambiente e não deve ser publicado
> junto com as credenciais reais.

------------------------------------------------------------------------

# 10. Carregando configurações

Com `python-dotenv`, o projeto pode carregar variáveis definidas no
`.env`.

Exemplo conceitual:

``` python
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")
```

O código conhece o **nome da variável**, mas não precisa armazenar
diretamente o segredo.

------------------------------------------------------------------------

# 11. .gitignore

Se o projeto utilizar Git, arquivos sensíveis devem ser ignorados.

Exemplo:

``` gitignore
.env
.venv/
__pycache__/
*.pyc
```

Assim:

``` text
CÓDIGO                    → pode ser versionado
requirements.txt          → pode ser versionado
.env com credenciais      → NÃO deve ser versionado
.venv                     → NÃO precisa ser versionada
```

Esse cuidado será importante quando o projeto avançar para GitHub e
deploy.

------------------------------------------------------------------------

# 12. Abrindo a conexão

Uma conexão com MySQL pode seguir a ideia:

``` python
import mysql.connector

conexao = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha,
    database=banco
)
```

Depois da conexão, a aplicação pode criar um cursor para executar
comandos SQL.

``` python
cursor = conexao.cursor()
```

------------------------------------------------------------------------

# 13. Executando uma consulta

Exemplo conceitual:

``` python
cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()
```

Fluxo:

``` text
PYTHON
   ↓
SELECT
   ↓
MYSQL
   ↓
RESULTADO
   ↓
PYTHON
```

O resultado pode então ser utilizado pela interface.

------------------------------------------------------------------------

# 14. Streamlit + Python + MySQL

Agora conseguimos conectar as três partes:

``` text
STREAMLIT
Interface
    ↓
PYTHON
Lógica da aplicação
    ↓
MYSQL
Persistência
```

Uma consulta pode ser exibida em tela:

``` python
dados = consultar_usuarios()
st.dataframe(dados)
```

A interface deixa de trabalhar apenas com informações estáticas e passa
a refletir os dados armazenados.

------------------------------------------------------------------------

# 15. Operações CRUD

CRUD representa quatro operações fundamentais:

  Operação     SQL
  ------------ ----------
  **Create**   `INSERT`
  **Read**     `SELECT`
  **Update**   `UPDATE`
  **Delete**   `DELETE`

No TechPort:

``` text
CRIAR USUÁRIO       → INSERT
LISTAR USUÁRIOS     → SELECT
ALTERAR USUÁRIO     → UPDATE
EXCLUIR USUÁRIO     → DELETE
```

Essas operações conectam as ações da aplicação à persistência.

------------------------------------------------------------------------

# 16. INSERT

Exemplo conceitual:

``` sql
INSERT INTO usuarios (nome, email)
VALUES ('Aluno TechPort', 'aluno@techport.com');
```

Após alterações no banco, normalmente precisamos confirmar a transação:

``` python
conexao.commit()
```

Fluxo:

``` text
FORMULÁRIO
    ↓
PYTHON
    ↓
INSERT
    ↓
COMMIT
    ↓
MYSQL
```

------------------------------------------------------------------------

# 17. SELECT

Uma consulta recupera informações existentes.

``` sql
SELECT *
FROM usuarios;
```

Ou:

``` sql
SELECT id, nome, email
FROM usuarios
ORDER BY nome;
```

Na aplicação:

``` text
MySQL
   ↓
Resultado da consulta
   ↓
Python
   ↓
Streamlit
   ↓
Tabela na tela
```

------------------------------------------------------------------------

# 18. UPDATE

Atualizações modificam registros existentes.

``` sql
UPDATE usuarios
SET nome = 'Novo Nome'
WHERE id = 10;
```

O `WHERE` é fundamental.

Sem ele:

``` sql
UPDATE usuarios
SET nome = 'Novo Nome';
```

a alteração pode atingir todos os registros da tabela.

------------------------------------------------------------------------

# 19. DELETE

A exclusão também exige atenção:

``` sql
DELETE FROM usuarios
WHERE id = 10;
```

Sem `WHERE`:

``` sql
DELETE FROM usuarios;
```

todos os registros podem ser removidos.

> Operações de escrita exigem validação e cuidado, principalmente
> `UPDATE` e `DELETE`.

------------------------------------------------------------------------

# 20. Consultar antes e depois

Uma prática didática importante é observar o estado do banco antes e
depois de uma operação.

Exemplo:

``` sql
SELECT COUNT(*) FROM usuarios;
```

Depois:

``` sql
INSERT INTO usuarios (...);
```

E novamente:

``` sql
SELECT COUNT(*) FROM usuarios;
```

Assim podemos comprovar que a operação executada pela aplicação
realmente alterou o banco.

------------------------------------------------------------------------

# 21. A interface e o dado real

Uma das mudanças mais importantes desta aula é perceber que aquilo que
aparece na interface pode representar um dado real armazenado no MySQL.

``` text
USUÁRIO CLICA
     ↓
STREAMLIT
     ↓
PYTHON
     ↓
SQL
     ↓
MYSQL
     ↓
RESULTADO
     ↓
STREAMLIT
```

Isso transforma a interface em parte de um sistema integrado.

------------------------------------------------------------------------

# 22. Tratamento de erros

Conexões e operações de banco podem falhar.

Exemplos:

-   servidor MySQL indisponível;
-   usuário ou senha incorretos;
-   banco inexistente;
-   SQL inválido;
-   violação de restrição;
-   conexão encerrada.

Por isso, o código deve prever tratamento de exceções.

Exemplo conceitual:

``` python
try:
    # conectar e executar operação
    pass
except Exception as erro:
    print(erro)
```

O tratamento de erros ajuda a identificar problemas sem esconder a causa
da falha.

------------------------------------------------------------------------

# 23. Segurança da senha

A aula também reforça a diferença entre **proteger a credencial** e
**criptografar dados**.

No contexto da conexão:

``` text
SENHA REAL
   ↓
ARMAZENAMENTO SEGURO / VARIÁVEL DE AMBIENTE
   ↓
APLICAÇÃO RECUPERA EM EXECUÇÃO
   ↓
CONEXÃO COM MYSQL
```

O ponto central é evitar credenciais sensíveis expostas diretamente no
código-fonte.

------------------------------------------------------------------------

# 24. Fluxo de inicialização do projeto

Uma sequência prática para executar o TechPort:

``` text
1. Abrir o terminal na pasta do projeto
2. Criar a .venv, se necessário
3. Ativar a .venv
4. Instalar requirements.txt
5. Configurar o .env
6. Garantir que o MySQL esteja disponível
7. Executar a aplicação
8. Validar consultas e operações
```

Comandos principais:

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

------------------------------------------------------------------------

# 25. Executando o Streamlit

Com o ambiente preparado:

``` powershell
python -m streamlit run app.py
```

ou, dependendo da estrutura do projeto:

``` powershell
python -m streamlit run app/<arquivo_principal>.py
```

O importante é executar o arquivo que representa a entrada da interface
do projeto.

------------------------------------------------------------------------

# 26. Encerrando o ambiente virtual

Quando terminar:

``` powershell
deactivate
```

O comando encerra a ativação da `.venv` naquele terminal.

Ele **não exclui** o ambiente virtual.

``` text
activate   → entra no ambiente
deactivate → sai do ambiente
```

------------------------------------------------------------------------

# 27. Evolução arquitetural

A Aula 04 estabelece uma arquitetura inicial:

``` text
STREAMLIT
    ↓
PYTHON
    ↓
MYSQL
```

Essa estrutura será importante para a próxima evolução do TechPort.

Em vez de manter a interface diretamente ligada à lógica de
persistência, poderemos inserir uma nova camada:

``` text
STREAMLIT
    ↓
API
    ↓
PYTHON
    ↓
MYSQL
```

Essa será a ponte para a **FastAPI**.

------------------------------------------------------------------------

# 28. Resumo da aula

Nesta aula aprendemos a:

-   preparar um ambiente virtual Python;
-   ativar e desativar a `.venv`;
-   instalar dependências por `requirements.txt`;
-   compreender o papel do conector MySQL;
-   configurar a conexão da aplicação;
-   separar credenciais do código;
-   utilizar variáveis de ambiente e `.env`;
-   proteger arquivos sensíveis com `.gitignore`;
-   executar consultas SQL pelo Python;
-   relacionar CRUD a `INSERT`, `SELECT`, `UPDATE` e `DELETE`;
-   utilizar `commit` em operações de escrita;
-   validar alterações diretamente no banco;
-   integrar Streamlit, Python e MySQL;
-   reconhecer a necessidade de tratamento de erros;
-   preparar a arquitetura para a próxima etapa do projeto.

------------------------------------------------------------------------

# Tecnologias e conceitos

  Item                         Papel na aula
  ---------------------------- ----------------------------------------------------
  **Python**                   Implementação da aplicação
  **Streamlit**                Interface
  **MySQL**                    Persistência
  **mysql-connector-python**   Comunicação Python ↔ MySQL
  **venv**                     Isolamento das dependências
  **requirements.txt**         Dependências reproduzíveis
  **python-dotenv**            Leitura das variáveis de ambiente
  **.env**                     Configuração local/sensível
  **.gitignore**               Exclusão de arquivos que não devem ser versionados
  **SQL / CRUD**               Manipulação dos dados

------------------------------------------------------------------------

# Conclusão

A principal evolução desta aula pode ser representada por:

``` text
INTERFACE
    ↓
LÓGICA
    ↓
PERSISTÊNCIA
```

No TechPort:

``` text
STREAMLIT
    ↓
PYTHON
    ↓
MYSQL
```

> **Uma aplicação passa a representar um sistema real quando suas ações
> deixam de existir apenas na tela e passam a manipular dados
> persistentes de forma organizada e segura.**

A próxima evolução será desacoplar ainda mais essas responsabilidades:

``` text
Streamlit → FastAPI → MySQL
```

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

`Streamlit → Python → MySQL`
