# Projeto, Implementação e Teste de Software

> **Do requisito à produção: projetar, implementar, testar e entregar
> software com qualidade.**

**Professor:** Rodolfo Terra\
**Projeto Integrador:** TechPort --- Sistema de Gestão de Chamados\
**Instituição:** UniCesumar

[LinkedIn](https://www.linkedin.com/in/rodolffoterra/) •
[GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## Sobre a disciplina

A disciplina **Projeto, Implementação e Teste de Software** foi
desenvolvida de forma progressiva e prática, utilizando o **TechPort ---
Sistema de Gestão de Chamados** como projeto integrador.

Durante **9 aulas**, acompanhamos a evolução de uma aplicação desde os
fundamentos de projeto e arquitetura até banco de dados, interface, API,
testes, qualidade, versionamento, Docker, CI/CD e deploy.

``` text
REQUISITO
    ↓
PROJETO
    ↓
ARQUITETURA
    ↓
BANCO DE DADOS
    ↓
BACK-END / API
    ↓
INTERFACE
    ↓
TESTES
    ↓
QUALIDADE
    ↓
GIT / GITHUB
    ↓
DOCKER
    ↓
CI/CD
    ↓
DEPLOY
    ↓
PRODUÇÃO
```

------------------------------------------------------------------------

## Projeto Integrador --- TechPort

O TechPort representa um sistema de gestão de chamados e foi utilizado
para conectar os conteúdos das nove aulas em uma única evolução prática.

``` text
USUÁRIO / TÉCNICO / ADMINISTRADOR
                ↓
            STREAMLIT
                ↓
              HTTP
                ↓
             FASTAPI
                ↓
             SERVICE
                ↓
           REPOSITORY
                ↓
              MYSQL
```

------------------------------------------------------------------------

# Resumo das 9 aulas

## Aula 01 --- Introdução ao Projeto, Implementação e Teste de Software

A primeira aula apresentou a visão geral da disciplina e o ciclo de
construção de software. Foram introduzidos requisitos, projeto,
implementação, validação, testes e qualidade, além do **TechPort** como
projeto que acompanharia a evolução da disciplina.

**Principais pontos:** ciclo de desenvolvimento, requisitos, projeto,
implementação, testes, qualidade e visão inicial do TechPort.

▶️ **[Assistir à Aula 01 no
YouTube](https://www.youtube.com/watch?v=i-nF3zmlZ8w)**

------------------------------------------------------------------------

## Aula 02 --- Projeto de Software e Arquitetura

A segunda aula avançou do requisito para a estrutura da solução. Foram
trabalhados arquitetura de software, separação de responsabilidades,
organização do projeto e divisão da aplicação em componentes e camadas.

**Principais pontos:** arquitetura, responsabilidades, organização do
código, componentes, camadas e preparação da arquitetura do TechPort.

▶️ **[Assistir à Aula 02 no
YouTube](https://www.youtube.com/watch?v=nXygooJmjHc)**

------------------------------------------------------------------------

## Aula 03 --- Banco de Dados e Persistência com MySQL

O TechPort ganhou persistência em **MySQL**. A aula abordou modelagem,
criação de tabelas, relacionamentos, cardinalidade, volumetria,
população do banco e consultas SQL para validar a estrutura e os dados.

**Principais pontos:** modelagem, tabelas, PK/FK, relacionamentos,
integridade, volumetria, consultas e validação.

▶️ **[Assistir à Aula 03 no
YouTube](https://www.youtube.com/watch?v=ZQF9PWNmmrY)**

------------------------------------------------------------------------

## Aula 04 --- Python, Streamlit e Integração com MySQL

A aplicação passou a acessar e manipular os dados utilizando **Python e
Streamlit**. Também foram trabalhados ambiente virtual, dependências,
`requirements.txt`, configuração por `.env` e proteção das credenciais
de conexão.

**Principais pontos:** Python, Streamlit, MySQL, ambiente virtual,
dependências, `.env`, credenciais e persistência.

▶️ **[Assistir à Aula 04 no
YouTube](https://www.youtube.com/watch?v=TCYYVBr5HQ8)**

------------------------------------------------------------------------

## Aula 05 --- FastAPI e Construção da API

A **FastAPI** foi introduzida como camada de comunicação entre a
interface e o back-end. O fluxo do TechPort evoluiu para:

``` text
Streamlit → HTTP → FastAPI → Service → Repository → MySQL
```

Foram explorados endpoints, requisições, respostas JSON, Swagger e
operações de criação, consulta e exclusão de registros.

**Principais pontos:** API, HTTP, FastAPI, endpoints, JSON, Services,
Repositories, MySQL e Swagger.

▶️ **[Assistir à Aula 05 no
YouTube](https://www.youtube.com/watch?v=8_-Fu6ZEGDQ)**

------------------------------------------------------------------------

## Aula 06 --- Testes e Qualidade de Software

Com a aplicação integrada, o foco passou para sua confiabilidade. Foram
estudadas **verificação e validação**, níveis de testes e ferramentas
para automatizar qualidade e segurança.

**Principais pontos:** testes unitários, integração, sistema, aceitação,
`pytest`, Ruff, mypy, Bandit, pip-audit, SAST, DAST e SCA.

▶️ **[Assistir à Aula 06 no
YouTube](https://www.youtube.com/watch?v=Girb_Mzx_NA)**

------------------------------------------------------------------------

## Aula 07 --- TDD: Test-Driven Development

A aula aprofundou o papel dos testes na construção do software por meio
do **TDD**.

``` text
REQUISITO → COMPORTAMENTO → TESTE → RED → CÓDIGO → GREEN → REFACTOR → EVOLUÇÃO
```

O objetivo foi compreender que testes também podem participar da
definição e evolução do comportamento esperado da aplicação.

**Principais pontos:** TDD, Red, Green, Refactor, comportamento
esperado, evolução segura e testes como documentação.

▶️ **[Assistir à Aula 07 no
YouTube](https://www.youtube.com/watch?v=qs71uIVefCI)**

------------------------------------------------------------------------

## Aula 08 --- Interfaces, Perfis e Qualidade de Software

O TechPort foi analisado pela perspectiva dos três perfis da aplicação:
**Usuário, Técnico e Administrador**. Foram trabalhadas jornadas,
responsabilidades, usabilidade, segurança e características de qualidade
relacionadas à **ISO/IEC 25010**.

O laboratório permitiu acompanhar o ciclo de um chamado pelos diferentes
perfis.

**Principais pontos:** perfis, autorização, jornada, usabilidade,
segurança, qualidade, ISO/IEC 25010 e fluxo completo do chamado.

▶️ **[Assistir à Aula 08 no
YouTube](https://www.youtube.com/watch?v=tGN1JCPPJ6E)**

------------------------------------------------------------------------

## Aula 09 --- GitHub, Docker, CI/CD e Deploy

A última aula conecta o projeto ao processo de entrega. Git e GitHub são
relacionados ao versionamento e colaboração; Docker à padronização do
ambiente; Docker Compose à execução dos serviços; e CI/CD à automação de
qualidade e entrega.

O laboratório final trabalha a criação das imagens do Streamlit e da
FastAPI, execução dos containers e validação da comunicação com o
TechPort.

``` text
DESENVOLVEDOR
      ↓
    COMMIT
      ↓
     PUSH
      ↓
    GITHUB
      ↓
      CI
      ↓
RUFF / MYPY / BANDIT / PYTEST
      ↓
 DOCKER BUILD
      ↓
    IMAGEM
      ↓
    DEPLOY
      ↓
   PRODUÇÃO
```

**Principais pontos:** Git, GitHub, Docker, Dockerfile, imagem,
container, Docker Compose, CI/CD, GitHub Actions, secrets, deploy, logs
e monitoramento.

📺 **Vídeo da Aula 09:** link ainda não informado.

------------------------------------------------------------------------

# Acesso rápido às aulas

  -------------------------------------------------------------------------------------------------------
  Aula                    Tema                    Vídeo
  ----------------------- ----------------------- -------------------------------------------------------
  01                      Introdução ao Projeto,  [▶️ Abrir no
                          Implementação e Teste   YouTube](https://www.youtube.com/watch?v=i-nF3zmlZ8w)
                          de Software             

  02                      Projeto de Software e   [▶️ Abrir no
                          Arquitetura             YouTube](https://www.youtube.com/watch?v=nXygooJmjHc)

  03                      Banco de Dados e        [▶️ Abrir no
                          Persistência com MySQL  YouTube](https://www.youtube.com/watch?v=ZQF9PWNmmrY)

  04                      Python, Streamlit e     [▶️ Abrir no
                          Integração com MySQL    YouTube](https://www.youtube.com/watch?v=TCYYVBr5HQ8)

  05                      FastAPI e Construção da [▶️ Abrir no
                          API                     YouTube](https://www.youtube.com/watch?v=8_-Fu6ZEGDQ)

  06                      Testes e Qualidade de   [▶️ Abrir no
                          Software                YouTube](https://www.youtube.com/watch?v=Girb_Mzx_NA)

  07                      TDD --- Test-Driven     [▶️ Abrir no
                          Development             YouTube](https://www.youtube.com/watch?v=qs71uIVefCI)

  08                      Interfaces, Perfis e    [▶️ Abrir no
                          Qualidade               YouTube](https://www.youtube.com/watch?v=tGN1JCPPJ6E)

  09                      GitHub, Docker, CI/CD e **Vídeo a disponibilizar**
                          Deploy                  
  -------------------------------------------------------------------------------------------------------

> **Observação:** os links são clicáveis no README do GitHub. A abertura
> em uma nova guia ou janela é controlada pelo navegador; o GitHub não
> preserva de forma confiável `target="_blank"` em README Markdown.

------------------------------------------------------------------------

# Tecnologias utilizadas

  Tecnologia       Aplicação
  ---------------- ----------------------------------
  Python           Linguagem principal
  Streamlit        Interface
  FastAPI          API
  MySQL            Persistência
  pytest           Testes automatizados
  Ruff             Qualidade do código
  mypy             Verificação de tipos
  Bandit           Análise de segurança
  pip-audit        Auditoria de dependências
  Git              Controle de versão
  GitHub           Repositório e integração
  Docker           Containerização
  Docker Compose   Execução coordenada dos serviços
  GitHub Actions   CI/CD

------------------------------------------------------------------------

# Do requisito à produção

Ao final da disciplina, o TechPort permite visualizar o ciclo completo:

``` text
REQUISITO
   ↓
ARQUITETURA
   ↓
IMPLEMENTAÇÃO
   ↓
BANCO DE DADOS
   ↓
API
   ↓
INTERFACE
   ↓
TESTES
   ↓
QUALIDADE
   ↓
VERSIONAMENTO
   ↓
CONTAINERIZAÇÃO
   ↓
CI/CD
   ↓
DEPLOY
```

> **Software não termina quando o código funciona. Ele precisa ser
> projetado, implementado, testado, versionado, empacotado, entregue e
> operado com qualidade.**

------------------------------------------------------------------------

# Professor

**Professor Rodolfo Terra**

-   [LinkedIn ---
    linkedin.com/in/rodolffoterra/](https://www.linkedin.com/in/rodolffoterra/)
-   [GitHub ---
    github.com/rodolffoterra](https://github.com/rodolffoterra)

------------------------------------------------------------------------

**Projeto, Implementação e Teste de Software**\
**TechPort --- do requisito à produção.**

`Projeto → Implementação → Testes → Qualidade → GitHub → Docker → CI/CD → Deploy`
