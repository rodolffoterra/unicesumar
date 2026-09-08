# 🧩 Aula 02 --- Projeto de Software e Arquitetura de Sistemas

## Planejando aplicações Python antes da programação

**Disciplina:** Projeto, Implementação e Teste de Software\
**Professor:** Rodolfo Terra

🔗 **LinkedIn:** https://www.linkedin.com/in/rodolffoterra/\
🔗 **GitHub:** https://github.com/rodolffoterra

------------------------------------------------------------------------

# 📌 Sobre a Aula 02

Nesta aula aprofundamos a etapa de **Projeto de Software**, apresentada
na Aula 01 como uma das bases da Engenharia de Software.

A mensagem central é simples:

> **Bons sistemas nascem de bons projetos.**

Antes de começar a programar, precisamos tomar decisões sobre a
estrutura da solução, responsabilidades dos componentes, organização do
código, dados, interfaces, tecnologias e comunicação entre as partes.

``` text
REQUISITOS
    ↓
PROJETO
    ↓
IMPLEMENTAÇÃO
    ↓
TESTES
    ↓
IMPLANTAÇÃO
    ↓
MANUTENÇÃO
```

Nesta aula, nosso foco está principalmente na segunda etapa:

``` text
REQUISITOS
    ↓
[ PROJETO ]
    ↓
IMPLEMENTAÇÃO
```

------------------------------------------------------------------------

# 🔄 Retomando a Engenharia de Software

Na Aula 01 vimos que o desenvolvimento de software não consiste apenas
em escrever código.

O ciclo apresentado foi:

``` text
Requisitos
   ↓
Projeto
   ↓
Implementação
   ↓
Testes
   ↓
Implantação
   ↓
Manutenção
```

Cada etapa influencia as seguintes.

Uma analogia utilizada na aula é a construção de um prédio:

``` text
FUNDAÇÃO
   ↓
ESTRUTURA
   ↓
ACABAMENTO
   ↓
PRÉDIO PRONTO
```

Se a fundação estiver errada, o acabamento não resolve o problema.

No desenvolvimento de software acontece algo semelhante.

> **Projeto é a fundação do software.**

------------------------------------------------------------------------

# 🧠 O que é Projeto de Software?

Uma distinção fundamental desta aula é separar **análise/requisitos** de
**projeto**.

## Análise

Responde:

> **O que o sistema deve fazer?**

Exemplo:

> "Quero um aplicativo para pedidos."

Isso representa uma necessidade ou requisito.

## Projeto

Responde:

> **Como o sistema será construído?**

Agora precisamos tomar decisões:

-   qual banco de dados utilizar;
-   como organizar o código;
-   como será a API;
-   quais módulos existirão;
-   como as partes se comunicarão;
-   onde os dados serão armazenados.

Podemos resumir:

``` text
REQUISITOS
O QUE FAZER?
     ↓
PROJETO
COMO FAZER?
```

> **Requisitos descrevem o problema. Projeto define a solução.**

------------------------------------------------------------------------

# 🏗️ Analogia da construção

Na Engenharia Civil:

``` text
PLANTA
  ↓
CONSTRUÇÃO
```

Na Engenharia de Software:

``` text
PROJETO
  ↓
PROGRAMAÇÃO
```

Nenhum engenheiro deveria iniciar uma obra importante sem planejamento.

Da mesma forma, iniciar um sistema sem pensar em sua estrutura pode
gerar retrabalho.

> **Planejamento evita retrabalho.**

------------------------------------------------------------------------

# 🎯 Objetivos do Projeto de Software

O projeto define como a solução será construída e procura garantir que o
software atenda às necessidades do negócio com qualidade.

Entre os objetivos apresentados estão:

## 1. Definir arquitetura

Determinar a estrutura do sistema, seus componentes e como eles se
relacionam.

## 2. Reduzir riscos

Antecipar problemas antes que eles apareçam durante a implementação.

## 3. Organizar o desenvolvimento

Fornecer um guia para a equipe e melhorar a produtividade.

## 4. Facilitar manutenção

Uma boa estrutura torna o código mais fácil de compreender, alterar e
evoluir.

## 5. Diminuir custos

Problemas encontrados durante o projeto tendem a ser mais baratos de
corrigir do que problemas descobertos depois.

O projeto deve responder perguntas como:

``` text
Quem conversa com quem?

Onde ficam os dados?

Como o sistema poderá crescer?

Como novos desenvolvedores entenderão o código?
```

------------------------------------------------------------------------

# ⚖️ Requisitos × Projeto

  Requisitos    Projeto
  ------------- ----------------------
  O que fazer   Como fazer
  Cliente       Desenvolvedor
  Necessidade   Solução
  Problema      Estrutura da solução

Uma forma simples de identificar a diferença:

``` text
É uma necessidade?
        ↓
    REQUISITO

É uma decisão sobre a solução?
        ↓
      PROJETO
```

> **Entender essa diferença evita erros e retrabalho.**

------------------------------------------------------------------------

# 👨‍💻 Quem é o Arquiteto de Software?

O arquiteto de software não é necessariamente a pessoa que escreve mais
código.

Seu papel está fortemente relacionado à **tomada de decisões técnicas**.

Entre suas responsabilidades estão:

-   escolher tecnologias;
-   organizar módulos;
-   planejar crescimento;
-   avaliar integrações;
-   considerar segurança;
-   reduzir problemas futuros.

Sua visão precisa combinar diferentes áreas:

``` text
                 PYTHON
                   │
CLOUD ───── ARQUITETO DE SOFTWARE ───── BANCO DE DADOS
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
       APIs   ARQUITETURA  SEGURANÇA
                   │
                NEGÓCIO
```

Também é importante conhecer:

-   desenvolvimento de software;
-   regras de negócio;
-   modelagem e design;
-   bancos de dados;
-   gerenciamento de projetos;
-   qualidade;
-   segurança.

> **Arquitetura é tomada de decisão.**

------------------------------------------------------------------------

# 🗺️ O que é Modelagem?

Modelagem significa **desenhar antes de construir**.

``` text
PROBLEMA
Entender o que precisa ser resolvido
        ↓
MODELO
Representar e planejar a solução
        ↓
SOFTWARE
Implementar o que foi planejado
```

A modelagem serve para:

### Explicar

Facilitar a comunicação.

### Documentar

Registrar decisões.

### Validar

Verificar se a solução atende ao objetivo.

### Corrigir

Ajustar a solução antes de escrever grandes quantidades de código.

> **Modelagem reduz erros.**

------------------------------------------------------------------------

# 🧱 Tipos de Projeto

Um software pode ser analisado a partir de diferentes perspectivas.

Na aula foram apresentadas cinco:

``` text
                 PROJETO
              /     |     \
             /      |      \
     ARQUITETURA   DADOS   INTERFACES
             \      |      /
              \     |     /
             COMPONENTES
                  |
              ALGORITMOS
```

## Arquitetura

Define a estrutura geral do sistema, os principais módulos e seus
relacionamentos.

Pergunta:

> Qual é a visão macro do sistema?

## Dados

Define como os dados serão organizados, armazenados e acessados.

Pergunta:

> Como os dados serão usados e protegidos?

## Interfaces

Define como usuários e sistemas interagem com a aplicação.

Pergunta:

> Como pessoas e sistemas utilizarão o software?

## Componentes

Define módulos e serviços e suas responsabilidades.

Pergunta:

> De quais partes o sistema será formado?

## Algoritmos

Define regras de processamento e lógica.

Pergunta:

> Como as tarefas serão realizadas?

------------------------------------------------------------------------

# 🔎 Abstração

Abstrair significa **esconder detalhes desnecessários e mostrar apenas o
que importa para determinado objetivo**.

A aula utiliza a analogia de mapas:

``` text
BRASIL
  ↓
ESTADO
  ↓
CIDADE
  ↓
RUA
```

Cada nível apresenta mais detalhes.

No software ocorre o mesmo.

Dependendo de quem está analisando o sistema, não precisamos mostrar
todos os detalhes técnicos.

A abstração:

-   reduz complexidade;
-   facilita entendimento;
-   melhora comunicação;
-   permite decisões mais rápidas;
-   apresenta o nível de detalhe adequado para cada público.

> **Nem sempre precisamos enxergar todos os detalhes.**

------------------------------------------------------------------------

# 🔬 Refinamento

Refinamento é o processo de adicionar detalhes progressivamente até
transformar uma ideia em uma solução implementável.

``` text
1. IDEIA
   ↓
2. PROTÓTIPO
   ↓
3. ARQUITETURA
   ↓
4. CÓDIGO
```

## Ideia

Entendimento inicial do problema e do objetivo.

## Protótipo

Representação simples para validar funcionalidades principais.

## Arquitetura

Definição da estrutura, módulos, tecnologias, dados e regras.

## Código

Implementação dos detalhes definidos no projeto.

O refinamento permite:

-   validar ideias antes de grandes investimentos;
-   ajustar caminhos rapidamente;
-   reduzir riscos;
-   evitar retrabalho;
-   aumentar gradualmente o nível de detalhe.

> **Refinar é evoluir com método.**

------------------------------------------------------------------------

# 🧩 Modularidade em Python

Modularidade significa dividir o sistema em partes com responsabilidades
específicas.

Uma estrutura apresentada na aula foi:

``` text
app/
│
├── api/
│   └── __init__.py
│
├── models/
│   └── __init__.py
│
├── services/
│   └── __init__.py
│
├── database/
│   └── __init__.py
│
├── schemas/
│   └── __init__.py
│
├── utils/
│   └── __init__.py
│
└── tests/
    └── __init__.py
```

## `api/`

Contém rotas e endpoints da aplicação.

## `models/`

Representa modelos relacionados aos dados.

## `services/`

Contém regras de negócio.

## `database/`

Responsável pela conexão e configurações do banco de dados.

## `schemas/`

Define e valida estruturas de entrada e saída.

## `utils/`

Funções auxiliares reutilizáveis.

## `tests/`

Testes da aplicação.

### Por que modularizar?

-   código mais organizado;
-   facilidade de testes;
-   melhor trabalho em equipe;
-   manutenção mais simples;
-   reutilização;
-   crescimento controlado.

> **Cada módulo possui uma responsabilidade.**

------------------------------------------------------------------------

# 🧰 Padrões de Projeto

Padrões de projeto são soluções conhecidas para problemas recorrentes de
desenvolvimento.

Eles não são código pronto nem regras obrigatórias.

São modelos que ajudam a estruturar soluções.

Na aula foram apresentados:

## MVC

Separa responsabilidades entre:

``` text
MODEL
VIEW
CONTROLLER
```

## Factory

Centraliza ou organiza a criação de objetos.

## Singleton

Busca garantir uma única instância compartilhada de determinado recurso.

## Observer

Permite que objetos sejam notificados quando determinado estado muda.

## Strategy

Permite encapsular algoritmos ou comportamentos intercambiáveis.

### Por que utilizar padrões?

-   evitar reinventar soluções;
-   facilitar comunicação;
-   organizar o código;
-   melhorar manutenção;
-   apoiar escalabilidade.

> **Use o padrão adequado ao problema adequado.**

------------------------------------------------------------------------

# 🏛️ Qualidade da Arquitetura

Arquitetura define como o sistema será construído hoje e como poderá
evoluir amanhã.

A aula compara dois cenários.

## Projeto ruim

``` text
CÓDIGO CONFUSO
      ↓
ERROS
      ↓
RETRABALHO
      ↓
SISTEMA DIFÍCIL DE MANTER
```

## Projeto bom

``` text
CÓDIGO ORGANIZADO
       ↓
POUCOS ERROS
       ↓
FACILIDADE DE EVOLUÇÃO
       ↓
SISTEMA ESTÁVEL E ESCALÁVEL
```

Uma boa arquitetura ajuda a:

-   reduzir riscos;
-   aumentar produtividade;
-   facilitar manutenção;
-   permitir crescimento;
-   diminuir custos.

> **Arquitetura não é burocracia. É estratégia.**

------------------------------------------------------------------------

# 💰 Qualidade tem custo --- e erro tardio também

A aula apresenta a ideia de que o custo de corrigir um problema tende a
aumentar conforme ele avança no ciclo de desenvolvimento.

``` text
REQUISITOS
   ↓
PROJETO
   ↓
IMPLEMENTAÇÃO
   ↓
TESTES
   ↓
PRODUÇÃO

custo de correção  ────────────────► tende a aumentar
```

Por isso:

-   planejar bem evita caminhos errados;
-   projetar bem reduz retrabalho;
-   testar ajuda a encontrar defeitos;
-   documentar facilita manutenção.

> **Quanto mais cedo o erro é encontrado, menor tende a ser o custo para
> corrigi-lo.**

------------------------------------------------------------------------

# 🗺️ C4 Model --- o "Google Maps" da Arquitetura

O C4 Model é apresentado como uma forma de modelar e comunicar
arquitetura em diferentes níveis de abstração.

A analogia é semelhante ao zoom de um mapa.

``` text
CONTINENTE
   ↓
PAÍS / ESTADO
   ↓
CIDADE
   ↓
RUA
```

No C4:

``` text
NÍVEL 1 — CONTEXTO
        ↓
NÍVEL 2 — CONTÊINERES
        ↓
NÍVEL 3 — COMPONENTES
        ↓
NÍVEL 4 — CÓDIGO
```

Cada nível responde perguntas diferentes e atende públicos diferentes.

------------------------------------------------------------------------

# 🌍 C4 --- Nível 1: Contexto

O Nível 1 apresenta uma **visão executiva do sistema**.

Ele mostra:

-   quem usa o sistema;
-   qual é o sistema principal;
-   sistemas externos;
-   relações importantes;
-   ambiente em que a solução está inserida.

Exemplo:

``` text
             USUÁRIO
                ↓
        ┌──────────────┐
        │   SISTEMA    │
        └──────────────┘
          ↙          ↘
BANCO DE DADOS    SISTEMA EXTERNO
```

Perguntas respondidas:

-   Quem utiliza o sistema?
-   Qual é o propósito?
-   Quais sistemas externos interagem com ele?
-   Onde estão os dados?

> **Comece pelo Nível 1: ele conta a história do sistema de forma
> simples.**

------------------------------------------------------------------------

# 📦 C4 --- Nível 2: Contêineres

O Nível 2 apresenta as principais aplicações ou contêineres que formam a
solução.

Um exemplo apresentado:

``` text
FRONTEND
   ↓ HTTPS / JSON
API FASTAPI
   ↓ SQL / ORM
POSTGRESQL
   ↓
SERVIÇOS EXTERNOS
```

Aqui analisamos:

-   aplicações existentes;
-   responsabilidades;
-   comunicação;
-   tecnologias;
-   integrações.

> **O Nível 2 funciona como um mapa das aplicações que trabalham
> juntas.**

------------------------------------------------------------------------

# ⚙️ C4 --- Nível 3: Componentes

O Nível 3 entra na estrutura interna de uma aplicação.

Exemplo:

``` text
API FASTAPI
     ↓
CONTROLLERS
     ↓
SERVICES
     ↓
REPOSITORIES
     ↓
MODELS
```

O fluxo de uma requisição pode ser compreendido assim:

``` text
1. API recebe a requisição
        ↓
2. Controller valida e encaminha
        ↓
3. Service aplica regras de negócio
        ↓
4. Repository acessa os dados
        ↓
5. Model representa os dados
        ↓
6. Resposta retorna ao usuário
```

Esse nível ajuda a visualizar responsabilidades e dependências internas.

> **Cada camada deve possuir uma responsabilidade clara.**

------------------------------------------------------------------------

# 💻 C4 --- Nível 4: Código

O Nível 4 apresenta detalhes de implementação.

Pode mostrar:

-   classes;
-   métodos;
-   objetos;
-   relacionamentos.

``` text
CLASSE
   ↓
MÉTODOS
   ↓
OBJETOS
   ↓
RELACIONAMENTOS
```

É o nível mais detalhado e normalmente é direcionado a desenvolvedores
que precisam implementar, testar, depurar, refatorar e manter o código.

> **O Nível 4 representa o "zoom máximo" da arquitetura.**

------------------------------------------------------------------------

# 🎫 Estudo de Caso da Disciplina --- Sistema de Gestão de Chamados

Nesta aula também é apresentado o estudo de caso que servirá como
laboratório ao longo da disciplina.

## Problemas atuais

O cenário parte de dificuldades como:

-   chamados perdidos;
-   demora no atendimento;
-   falta de prioridade;
-   falta de acompanhamento.

## Solução proposta

Construiremos progressivamente um **Sistema de Gestão de Chamados**,
contemplando recursos como:

-   cadastro de chamados;
-   definição de prioridade;
-   atribuição de técnico;
-   acompanhamento de status;
-   histórico;
-   notificações.

``` text
PROBLEMAS
   ↓
PROJETO
   ↓
SISTEMA DE GESTÃO DE CHAMADOS
   ↓
EVOLUÇÃO DURANTE A DISCIPLINA
```

Esse sistema será utilizado para aplicar os conceitos de projeto,
implementação e testes.

------------------------------------------------------------------------

# 🏗️ Arquitetura de referência do Sistema de Chamados

A aula apresenta uma arquitetura em camadas para mostrar como as
responsabilidades podem ser separadas.

``` text
USUÁRIO
   ↓
FRONTEND
   ↓
FASTAPI
   ↓
SERVICES
   ↓
SQLALCHEMY / ORM
   ↓
POSTGRESQL
```

Também são apresentadas tecnologias de apoio como:

``` text
JWT
DOCKER
PYTEST
```

A intenção é mostrar como diferentes componentes podem cooperar mantendo
responsabilidades separadas.

------------------------------------------------------------------------

# 🛠️ Tecnologias apresentadas para o projeto didático

A aula também apresenta uma vertente didática utilizando **Streamlit +
Python + MySQL/Sakila** para explorar os conceitos de maneira prática.

Entre as tecnologias mostradas estão:

  Tecnologia            Papel
  --------------------- ---------------------------------------
  **Streamlit**         Interface web
  **Python**            Linguagem principal
  **MySQL**             Sistema gerenciador de banco de dados
  **Sakila**            Banco de exemplo
  **SQL**               Consultas e manipulação de dados
  **mysql-connector**   Comunicação Python ↔ MySQL
  **Plotly / Pandas**   Análise e visualização
  **pytest**            Testes automatizados

Essa combinação permite trabalhar:

-   interfaces;
-   banco de dados;
-   consultas;
-   CRUD;
-   visualizações;
-   testes;
-   organização do projeto.

------------------------------------------------------------------------

# 🧭 C4 aplicado à aplicação Streamlit + MySQL

A arquitetura apresentada na aula também é representada pelos níveis do
C4.

## Contexto

``` text
USUÁRIO
   ↓
STREAMLIT APP
   ↕
MYSQL / SAKILA
```

## Contêineres

``` text
NAVEGADOR
    ↓
STREAMLIT
    ↓
SERVIÇOS PYTHON
    ↓
ACESSO A DADOS
    ↓
MYSQL
```

## Componentes

``` text
STREAMLIT
├── UI / componentes
├── tabelas e gráficos
├── formulários
├── navegação
└── sessão

SERVIÇOS
├── queries.py
└── database.py

MYSQL / SAKILA
├── tabelas
├── views
├── procedures
├── functions
└── triggers
```

## Código

A estrutura do projeto é refinada até arquivos, módulos, páginas e
testes.

Isso demonstra, na prática, a ideia central do C4:

> **A mesma solução pode ser observada em diferentes níveis de
> detalhe.**

------------------------------------------------------------------------

# 🔄 Fluxo de dados da solução didática

O fluxo apresentado pode ser resumido assim:

``` text
USUÁRIO
   ↓
NAVEGADOR
   ↓
STREAMLIT
   ↓
SERVIÇOS
   ↓
MYSQL / SAKILA
   ↓
RESULTADOS
   ↓
TABELAS / GRÁFICOS
```

Essa visão será importante nas próximas aulas, quando cada parte começar
a ser implementada e evoluída.

------------------------------------------------------------------------

# 🧠 O que aprendemos nesta aula?

A Aula 02 consolidou os seguintes conceitos:

1.  **Projeto de Software** --- planejar antes de codificar;
2.  **Requisitos × Projeto** --- problema versus solução;
3.  **Arquitetura** --- decisões estruturais do sistema;
4.  **Modelagem** --- representar a solução antes de construir;
5.  **Tipos de projeto** --- arquitetura, dados, interfaces, componentes
    e algoritmos;
6.  **Abstração** --- mostrar somente o nível de detalhe necessário;
7.  **Refinamento** --- aumentar progressivamente os detalhes;
8.  **Modularidade** --- separar responsabilidades;
9.  **Padrões de Projeto** --- soluções recorrentes para problemas
    conhecidos;
10. **Qualidade da Arquitetura** --- facilitar manutenção e evolução;
11. **C4 Model** --- comunicar arquitetura em quatro níveis;
12. **Estudo de Caso** --- Sistema de Gestão de Chamados;
13. **Tecnologias do laboratório** --- Python, Streamlit, MySQL, Sakila,
    SQL, Pandas/Plotly e pytest.

------------------------------------------------------------------------

# 🔗 Como os conceitos se conectam

``` text
REQUISITOS
    ↓
PROJETO
    ↓
MODELAGEM
    ↓
ARQUITETURA
    ↓
ABSTRAÇÃO
    ↓
REFINAMENTO
    ↓
MODULARIDADE
    ↓
PADRÕES
    ↓
C4 MODEL
    ↓
IMPLEMENTAÇÃO
```

Não são assuntos isolados.

Todos ajudam a responder uma pergunta central:

> **Como transformar uma necessidade em uma solução de software
> organizada e preparada para evoluir?**

------------------------------------------------------------------------

# 🚀 Preparação para as próximas aulas

A Aula 02 constrói a fundação conceitual para o projeto que será
desenvolvido ao longo da disciplina.

A partir daqui, o foco começa a avançar do projeto para a implementação:

``` text
AULA 01
Engenharia de Software
       ↓
AULA 02
Projeto + Arquitetura
       ↓
MODELAGEM
       ↓
C4 MODEL
       ↓
ORGANIZAÇÃO DO PROJETO
       ↓
PYTHON
       ↓
INTERFACE
       ↓
BANCO DE DADOS
       ↓
API
       ↓
TESTES
       ↓
EVOLUÇÃO DO SISTEMA
```

O estudo de caso apresentado nesta aula será a referência para conectar
teoria e prática ao longo da disciplina.

------------------------------------------------------------------------

# 🏁 Resumo final

Nesta aula aprendemos que um software de qualidade não começa no editor
de código.

Ele começa com decisões.

``` text
ENTENDER
   ↓
PLANEJAR
   ↓
MODELAR
   ↓
PROJETAR
   ↓
ORGANIZAR
   ↓
IMPLEMENTAR
   ↓
TESTAR
   ↓
EVOLUIR
```

Antes de criar classes, APIs, telas ou bancos de dados, precisamos
compreender **como essas partes formarão uma solução coerente**.

> **Um bom software nasce de um bom projeto e evolui com uma boa
> arquitetura.**

------------------------------------------------------------------------

# 🎓 Mensagem da Aula 02

``` text
REQUISITOS dizem O QUE precisamos.

PROJETO define COMO faremos.

ARQUITETURA organiza AS PARTES.

MODELAGEM permite ENXERGAR.

C4 permite COMUNICAR.

MODULARIDADE permite EVOLUIR.

IMPLEMENTAÇÃO transforma tudo isso em SOFTWARE.
```

> **Planeje bem. Construa melhor.**

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**\
**Disciplina: Projeto, Implementação e Teste de Software**

🔗 LinkedIn: https://www.linkedin.com/in/rodolffoterra/\
🔗 GitHub: https://github.com/rodolffoterra
