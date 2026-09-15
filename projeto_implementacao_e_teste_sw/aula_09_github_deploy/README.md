# 🚀 Aula 09 --- Do Código à Produção

## GitHub, Docker, CI/CD e Deploy em Nuvem

**Disciplina:** Projeto, Implementação e Teste de Software\
**Professor:** Rodolfo Terra\
**Projeto:** TechPort --- Sistema de Gestão de Chamados

🔗 **LinkedIn:** https://www.linkedin.com/in/rodolffoterra/\
🔗 **GitHub:** https://github.com/rodolffoterra

------------------------------------------------------------------------

# 📌 Sobre esta aula

Esta aula encerra a disciplina **Projeto, Implementação e Teste de
Software** acompanhando a última etapa do ciclo de desenvolvimento do
**TechPort**: a preparação do software para entrega.

Ao longo das aulas anteriores, cada parte do projeto foi construída e
estudada separadamente. Nesta aula, o objetivo foi compreender como o
código que funciona no ambiente de desenvolvimento pode ser
**versionado, validado, empacotado e preparado para execução em outros
ambientes**.

O caminho estudado foi:

``` text
CÓDIGO
  ↓
GIT
  ↓
GITHUB
  ↓
TESTES
  ↓
BUILD
  ↓
DOCKER
  ↓
DEPLOY
  ↓
CLOUD
  ↓
PRODUÇÃO
```

> **Atenção:** o projeto completo e funcional do **TechPort**, incluindo
> as interfaces de **Usuário, Técnico e Administrador**, está
> disponibilizado na **Aula 08**.
>
> A Aula 09 utiliza esse projeto como base para estudar **Git, GitHub,
> Docker, CI/CD e conceitos de deploy**. Portanto, não é criada uma nova
> aplicação nesta aula.

------------------------------------------------------------------------

# 🧭 De onde partimos?

Na Aula 08, o TechPort passou a ser analisado como um **produto de
software**, e não apenas como um conjunto de arquivos Python.

A arquitetura trabalhada foi:

``` text
USUÁRIO        TÉCNICO        ADMIN
    \             |             /
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

O sistema já possuía:

-   interface com **Streamlit**;
-   três experiências de utilização;
-   API desenvolvida com **FastAPI**;
-   regras de negócio;
-   camada de serviços;
-   repositories;
-   persistência em **MySQL**;
-   testes automatizados;
-   conceitos de **TDD**;
-   práticas de qualidade de software.

Na Aula 09 surge uma nova pergunta:

> **O sistema funciona no nosso computador. Como ele chega ao usuário?**

------------------------------------------------------------------------

# 💻 O problema do localhost

Durante o desenvolvimento, executamos aplicações utilizando endereços
como:

``` text
http://localhost:8501
http://localhost:8000
```

No TechPort:

``` text
localhost:8501
      ↓
   STREAMLIT

localhost:8000
      ↓
    FASTAPI
```

Isso é adequado para desenvolvimento e testes locais.

Porém:

> **Funcionar no computador do desenvolvedor não significa que o sistema
> esteja disponível para seus usuários.**

Essa discussão introduziu o conceito de **deploy**.

------------------------------------------------------------------------

# 🚀 O que é Deploy?

Deploy é o processo de disponibilizar uma versão do software em um
ambiente onde ela possa ser utilizada.

``` text
DESENVOLVIMENTO
       ↓
     DEPLOY
       ↓
    PRODUÇÃO
       ↓
     USUÁRIO
```

O deploy conecta o desenvolvimento à utilização real do sistema.

------------------------------------------------------------------------

# 🌎 Ambientes de Software

Também discutimos que uma alteração normalmente não precisa sair
diretamente do computador do desenvolvedor para produção.

Um fluxo possível é:

``` text
DESENVOLVIMENTO
       ↓
      TESTE
       ↓
  HOMOLOGAÇÃO
       ↓
    PRODUÇÃO
```

### Desenvolvimento

Ambiente utilizado para construção e alteração do software.

### Teste

Ambiente utilizado para verificar comportamentos e identificar
problemas.

### Homologação

Ambiente no qual uma versão pode ser validada antes da disponibilização
final.

### Produção

Ambiente utilizado pelos usuários reais do sistema.

------------------------------------------------------------------------

# 🌿 Git

O **Git** foi apresentado como ferramenta de controle de versão.

Um fluxo básico utilizado no laboratório:

``` bash
git status
git add .
git commit -m "Finaliza TechPort"
git push
```

Conceitualmente:

``` text
ALTERAÇÃO
    ↓
  COMMIT
    ↓
HISTÓRICO
```

O commit registra um ponto conhecido da evolução do projeto.

------------------------------------------------------------------------

# 🐙 GitHub

Git e GitHub não são a mesma coisa.

``` text
GIT
↓
Controle de versão

GITHUB
↓
Repositório remoto
Colaboração
Automação
```

O fluxo estudado foi:

``` text
REPOSITÓRIO LOCAL
       ↓
    git push
       ↓
     GITHUB
```

Um repositório de software não deve guardar apenas código. Ele também
pode reunir testes, dependências, documentação e arquivos necessários
para construção e execução do projeto.

Exemplo:

``` text
TechPort/
├── app/
├── tests/
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

# 🤔 "Na minha máquina funciona"

Um dos problemas discutidos foi a diferença entre ambientes.

### Máquina A

``` text
Python          ✓
Bibliotecas     ✓
Configurações   ✓
TechPort        ✓
```

### Máquina B

``` text
Python          ?
Bibliotecas     ?
Configurações   ?
TechPort        ❌
```

Mesmo utilizando o mesmo código, diferenças de versões, dependências e
configurações podem alterar a execução.

A pergunta passou a ser:

> **Como tornar o ambiente de execução mais padronizado?**

------------------------------------------------------------------------

# 🐳 Docker

O Docker foi introduzido como uma forma de empacotar a aplicação e suas
dependências em um ambiente padronizado.

``` text
APLICAÇÃO
    +
DEPENDÊNCIAS
    +
CONFIGURAÇÃO
    ↓
CONTAINER
```

No contexto do TechPort, podemos pensar em:

``` text
┌──────────────────────────┐
│         TECHPORT         │
│                          │
│ Python                   │
│ Streamlit / FastAPI      │
│ Bibliotecas              │
│ Dependências             │
└──────────────────────────┘
```

------------------------------------------------------------------------

# 📦 Imagem x Container

Um conceito fundamental da aula foi a diferença entre **imagem** e
**container**.

``` text
DOCKERFILE
    ↓
  BUILD
    ↓
  IMAGEM
    ↓
   RUN
    ↓
CONTAINER
```

### Imagem

É o modelo construído contendo os elementos necessários para execução da
aplicação.

### Container

É uma instância em execução de uma imagem.

> **Imagem = modelo**\
> **Container = imagem em execução**

------------------------------------------------------------------------

# 📝 Dockerfile

O **Dockerfile** funciona como uma receita para construção da imagem.

Exemplo didático:

``` dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app/laboratorio_aula08.py"]
```

Os principais comandos apresentados foram:

  Comando     Função
  ----------- -----------------------------------
  `FROM`      Define a imagem base
  `WORKDIR`   Define o diretório de trabalho
  `COPY`      Copia arquivos para a imagem
  `RUN`       Executa comandos durante o build
  `CMD`       Define o comando de inicialização

------------------------------------------------------------------------

# 🔨 Docker Build

Depois de criar o Dockerfile, podemos construir uma imagem:

``` bash
docker build -t techport .
```

Fluxo:

``` text
CÓDIGO
  ↓
DOCKERFILE
  ↓
BUILD
  ↓
IMAGEM
```

------------------------------------------------------------------------

# ▶️ Docker Run

Com a imagem construída, podemos iniciar um container:

``` bash
docker run -p 8501:8501 techport
```

Fluxo:

``` text
IMAGEM
  ↓
 RUN
  ↓
CONTAINER
  ↓
APLICAÇÃO
```

No caso do Streamlit:

``` text
NAVEGADOR
    ↓
localhost:8501
    ↓
CONTAINER
    ↓
STREAMLIT
```

------------------------------------------------------------------------

# 🧩 O TechPort possui vários componentes

O TechPort não é formado por apenas um processo.

Temos:

``` text
STREAMLIT
    ↓
 FASTAPI
    ↓
  MYSQL
```

Cada componente possui uma responsabilidade.

  Componente     Responsabilidade
  -------------- -------------------
  Streamlit      Interface
  FastAPI        API
  Services       Regras de negócio
  Repositories   Persistência
  MySQL          Banco de dados

Por isso introduzimos o conceito de **Docker Compose**.

------------------------------------------------------------------------

# 🐳 Docker Compose

O Docker Compose permite definir e coordenar múltiplos serviços.

``` text
             DOCKER COMPOSE
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
    STREAMLIT   FASTAPI     MYSQL
      :8501      :8000      :3306
```

Comando básico:

``` bash
docker compose up
```

Com reconstrução das imagens:

``` bash
docker compose up --build
```

Em segundo plano:

``` bash
docker compose up -d
```

Para encerrar:

``` bash
docker compose down
```

------------------------------------------------------------------------

# ☁️ E a nuvem?

Docker resolve a questão de **padronização do ambiente**, mas um
container executado no notebook do desenvolvedor ainda continua no
notebook do desenvolvedor.

Precisamos de infraestrutura para disponibilizar o sistema.

``` text
CONTAINER
    ↓
SERVIDOR
    ↓
 INTERNET
```

Em um cenário de produção:

``` text
USUÁRIO
   ↓
INTERNET
   ↓
 CLOUD
   ↓
TECHPORT
```

A nuvem pode fornecer infraestrutura para manter a aplicação disponível
para seus usuários.

------------------------------------------------------------------------

# 🏗️ A arquitetura continua a mesma

Uma mensagem importante da aula:

> **A arquitetura permanece. O ambiente muda.**

O TechPort continua conceitualmente com:

``` text
             INTERNET
                 ↓
              TECHPORT
                 ↓
             STREAMLIT
                 ↓
              FASTAPI
                 ↓
               MYSQL
                 ↓
               DADOS
```

Não precisamos abandonar o que construímos anteriormente apenas porque
mudamos o ambiente de execução.

------------------------------------------------------------------------

# 🧪 E os testes?

Os testes estudados anteriormente passam a fazer parte do processo de
entrega.

Um exemplo apresentado:

``` text
git push
   ↓
GITHUB
   ↓
 RUFF
   ↓
 MYPY
   ↓
BANDIT
   ↓
PYTEST
```

Ferramentas já estudadas na disciplina podem participar de verificações
automáticas:

  Ferramenta   Objetivo
  ------------ -----------------------------------------
  Ruff         Qualidade e padronização do código
  mypy         Verificação de tipos
  Bandit       Análise de segurança
  pytest       Execução de testes
  pip-audit    Verificação de dependências vulneráveis

Assim, os testes deixam de ser apenas algo executado manualmente pelo
desenvolvedor.

------------------------------------------------------------------------

# ⚙️ Integração Contínua --- CI

**CI --- Continuous Integration** representa a integração e verificação
frequente das alterações.

Exemplo:

``` text
DESENVOLVEDOR
      ↓
   git push
      ↓
    GITHUB
      ↓
GITHUB ACTIONS
      ↓
    TESTES
      ↓
     BUILD
```

O GitHub Actions pode automatizar esse processo.

> **Cada alteração pode ser verificada automaticamente.**

------------------------------------------------------------------------

# 🛑 Falhou? Não segue.

Uma das ideias centrais da aula foi utilizar os testes como **barreira
de qualidade**.

``` text
             TESTES
             /    \
            ↓      ↓
         PASSOU   FALHOU
            │       │
            ↓       ↓
          BUILD    PARA
            │
            ↓
          DEPLOY
```

Se uma alteração quebra um comportamento esperado, o processo pode ser
interrompido antes que a versão chegue à produção.

> **Código precisa provar que continua funcionando.**

Isso conecta diretamente esta aula às aulas de **testes e TDD**.

------------------------------------------------------------------------

# 🔄 CI/CD

Com os conceitos reunidos, chegamos ao fluxo completo:

``` text
CÓDIGO
   ↓
GIT
   ↓
GITHUB
   ↓
TESTES
   ↓
BUILD
   ↓
DOCKER
   ↓
DEPLOY
   ↓
CLOUD
   ↓
PRODUÇÃO
```

Esse fluxo conecta:

-   desenvolvimento;
-   versionamento;
-   qualidade;
-   automação;
-   empacotamento;
-   infraestrutura;
-   entrega.

------------------------------------------------------------------------

# 🔐 Segurança --- senhas não vão para o GitHub

Também discutimos um ponto essencial de segurança.

Nunca devemos fazer:

``` python
DB_PASSWORD = "123456"
```

e publicar essa credencial no repositório.

O conceito correto é:

``` text
CÓDIGO
  ↓
SEM CREDENCIAIS

AMBIENTE / SECRET
       ↓
   CREDENCIAL
```

Arquivos locais e sensíveis devem ser tratados adequadamente.

Exemplo de `.gitignore`:

``` gitignore
.env
.venv/
__pycache__/
*.pyc
```

> **As credenciais pertencem ao ambiente, não ao código.**

------------------------------------------------------------------------

# 📊 Produção não é o fim

Depois do deploy, o ciclo do software continua.

``` text
PRODUÇÃO
   ↓
 LOGS
   ↓
 ERROS
   ↓
MÉTRICAS
   ↓
MONITORAMENTO
   ↓
MELHORIA
```

Em produção temos:

-   usuários reais;
-   dados reais;
-   erros reais;
-   necessidades reais;
-   oportunidades reais de evolução.

Por isso:

> **Software em produção precisa ser observado, medido e melhorado.**

------------------------------------------------------------------------

# 🧪 Laboratório Final

Na parte prática, o objetivo foi transformar os conceitos da aula em um
fluxo executável.

``` text
TECHPORT
   ↓
 GIT
   ↓
GITHUB
   ↓
DOCKER
   ↓
CONTAINER
```

### Objetivo

> **Versionar → Construir → Executar**

------------------------------------------------------------------------

## 1️⃣ Git e GitHub

``` bash
git status
git add .
git commit -m "Finaliza TechPort"
git push
```

O objetivo é registrar e publicar uma versão conhecida do projeto.

------------------------------------------------------------------------

## 2️⃣ Verificando Docker

``` bash
docker --version
docker compose version
```

Teste básico:

``` bash
docker run hello-world
```

------------------------------------------------------------------------

## 3️⃣ Construindo a imagem

Exemplo:

``` bash
docker build -t techport .
```

Ou, quando utilizado um Dockerfile específico:

``` bash
docker build -f Dockerfile.streamlit -t techport-streamlit:1.0 .
```

------------------------------------------------------------------------

## 4️⃣ Executando o container

``` bash
docker run -p 8501:8501 techport
```

Depois:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

## 5️⃣ Projeto completo com Compose

Para múltiplos serviços:

``` bash
docker compose up --build
```

Visualização:

``` bash
docker compose ps
```

Logs:

``` bash
docker compose logs -f
```

Encerramento:

``` bash
docker compose down
```

------------------------------------------------------------------------

# 📦 Publicando uma imagem

Também foi apresentado o conceito de **registry de imagens**.

Fluxo:

``` text
CÓDIGO
  ↓
BUILD
  ↓
IMAGEM
  ↓
 TAG
  ↓
PUSH
  ↓
REGISTRY
```

Exemplo:

``` bash
docker login
```

Criar uma tag:

``` bash
docker tag techport:latest SEU_USUARIO/techport:1.0
```

Enviar:

``` bash
docker push SEU_USUARIO/techport:1.0
```

Baixar novamente:

``` bash
docker pull SEU_USUARIO/techport:1.0
```

------------------------------------------------------------------------

# ⚠️ Observação sobre o projeto da Aula 08

## O código completo do TechPort está na Aula 08

Esta Aula 09 tem como foco **entrega de software**, e não a reconstrução
da aplicação.

Por isso, para executar o laboratório, utilize o projeto completo
desenvolvido na:

# 📂 Aula 08 --- Interfaces, Perfis de Usuário e Qualidade de Software

É na Aula 08 que está o TechPort com:

``` text
TECHPORT
│
├── Interface do Usuário
│
├── Interface do Técnico
│
├── Interface Administrativa
│
├── Streamlit
│
├── FastAPI
│
├── Services
│
├── Repositories
│
├── MySQL
└── Integrações do laboratório
```

Portanto, a relação entre as duas aulas é:

``` text
AULA 08
   ↓
PROJETO TECHPORT COMPLETO
   ↓
AULA 09
   ↓
GIT + GITHUB
   ↓
TESTES / CI
   ↓
DOCKER
   ↓
CONTAINER
   ↓
DEPLOY / CLOUD
```

> **A Aula 08 entrega o produto que será utilizado como base. A Aula 09
> mostra como preparar esse produto para entrega.**

------------------------------------------------------------------------

# 🧠 O caminho completo da disciplina

Ao final, conseguimos enxergar toda a evolução do TechPort:

``` text
REQUISITO
    ↓
BANCO DE DADOS
    ↓
PYTHON
    ↓
FASTAPI
    ↓
INTERFACE
    ↓
TESTES
    ↓
TDD
    ↓
QUALIDADE
    ↓
GIT
    ↓
GITHUB
    ↓
DOCKER
    ↓
CI/CD
    ↓
DEPLOY
    ↓
PRODUÇÃO
```

Cada conteúdo estudado representa uma parte do processo de construção de
software.

------------------------------------------------------------------------

# 🏁 Encerramento da disciplina

O TechPort começou como um problema:

``` text
Usuário precisa de suporte
        ↓
      CHAMADO
        ↓
    ATENDIMENTO
        ↓
      SOLUÇÃO
```

Depois ganhou dados:

``` text
MYSQL
```

Ganhou comportamento:

``` text
PYTHON
```

Ganhou comunicação:

``` text
FASTAPI
```

Ganhou interfaces:

``` text
STREAMLIT
```

Ganhou diferentes experiências:

``` text
USUÁRIO
TÉCNICO
ADMINISTRADOR
```

Ganhou proteção contra regressões:

``` text
TESTES
TDD
```

Ganhou critérios de produto:

``` text
QUALIDADE DE SOFTWARE
```

E, finalmente, discutimos como prepará-lo para entrega:

``` text
GIT
GITHUB
DOCKER
CI/CD
DEPLOY
CLOUD
```

------------------------------------------------------------------------

# 🎓 Mensagem final

> **Desenvolver software não é apenas escrever código.**
>
> É compreender requisitos, modelar dados, implementar regras, integrar
> componentes, construir interfaces, testar comportamentos, garantir
> qualidade, controlar versões e preparar o produto para ser entregue e
> continuar evoluindo.

``` text
REQUISITO
    ↓
IMPLEMENTAÇÃO
    ↓
TESTE
    ↓
QUALIDADE
    ↓
ENTREGA
    ↓
EVOLUÇÃO
```

# Isso é desenvolvimento de software.

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**\
Projeto, Implementação e Teste de Software

🔗 LinkedIn: https://www.linkedin.com/in/rodolffoterra/\
🔗 GitHub: https://github.com/rodolffoterra

------------------------------------------------------------------------

**TechPort --- Sistema de Gestão de Chamados**\
*Do requisito ao produto. Do código à produção.*
