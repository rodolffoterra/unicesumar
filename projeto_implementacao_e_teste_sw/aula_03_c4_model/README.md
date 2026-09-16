# Aula 03 --- Projeto de Arquitetura e Construção do Código

> **Transformando requisitos em diagramas arquiteturais e preparando a
> estrutura para a implementação.**

**Disciplina:** Projeto, Implementação e Teste de Software\
**Professor:** Rodolfo Terra\
**Projeto aplicado:** TechPort --- Sistema de Gestão de Chamados\
**Instituição:** UniCesumar

[LinkedIn](https://www.linkedin.com/in/rodolffoterra/) •
[GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## Sobre a aula

A Aula 03 aprofunda o **projeto de arquitetura de software** e mostra
como decisões tomadas durante o projeto começam a se transformar em
organização concreta do código.

A aula conecta arquitetura, organização da aplicação Python, colaboração
com Git, projeto de dados, segurança, componentes reutilizáveis, padrões
arquiteturais e documentação por diagramas.

A ideia central é compreender que:

> **Arquitetura é comunicação.**

Antes de implementar um sistema maior, precisamos compreender seus
componentes, suas responsabilidades e como eles se relacionam.

``` text
REQUISITOS
    ↓
ARQUITETURA
    ↓
COMPONENTES
    ↓
DADOS
    ↓
ORGANIZAÇÃO DO CÓDIGO
    ↓
IMPLEMENTAÇÃO
```

------------------------------------------------------------------------

# 1. Organização da aplicação Python

Uma aplicação profissional não deve crescer como um único arquivo.

A estrutura do projeto precisa separar responsabilidades e facilitar:

-   manutenção;
-   leitura;
-   testes;
-   colaboração;
-   evolução do sistema;
-   reutilização de componentes.

Exemplo conceitual:

``` text
techport/
├── app/
│   ├── pages/
│   ├── models/
│   ├── services/
│   ├── repositories/
│   ├── database/
│   └── utils/
├── tests/
├── requirements.txt
└── README.md
```

A estrutura de pastas começa a representar a própria arquitetura do
software.

------------------------------------------------------------------------

# 2. Projeto com mais de um desenvolvedor

Quando mais pessoas trabalham no mesmo projeto, controlar alterações
passa a ser essencial.

O **Git** permite registrar a evolução do código e organizar o trabalho
colaborativo.

Fluxo conceitual:

``` text
DESENVOLVEDOR
      ↓
ALTERAÇÃO
      ↓
COMMIT
      ↓
REPOSITÓRIO
      ↓
INTEGRAÇÃO COM O TRABALHO DA EQUIPE
```

Versionamento não é apenas guardar arquivos: ele ajuda a preservar o
histórico das decisões e alterações realizadas no software.

------------------------------------------------------------------------

# 3. Visões da arquitetura

Um sistema pode ser observado por perspectivas diferentes.

Entre as visões trabalhadas na aula estão:

-   **casos de uso** --- o que os usuários precisam realizar;
-   **visão lógica** --- como responsabilidades e elementos do sistema
    se organizam;
-   **implementação** --- como o código será estruturado;
-   **infraestrutura** --- onde os componentes serão executados.

Cada visão responde a perguntas diferentes sobre o mesmo software.

> Uma única representação raramente explica toda a arquitetura.

------------------------------------------------------------------------

# 4. Refatoração

Refatorar significa melhorar a estrutura interna do código sem alterar
seu comportamento esperado.

``` text
CÓDIGO FUNCIONANDO
       ↓
IDENTIFICAR PROBLEMAS DE ORGANIZAÇÃO
       ↓
REFATORAR
       ↓
MESMO COMPORTAMENTO
       +
MELHOR ESTRUTURA
```

A refatoração pode melhorar:

-   legibilidade;
-   organização;
-   reutilização;
-   manutenção;
-   separação de responsabilidades.

O objetivo não é simplesmente "reescrever" o sistema, mas tornar sua
estrutura mais sustentável.

------------------------------------------------------------------------

# 5. Projeto de dados

A arquitetura também precisa considerar os dados.

O projeto de dados envolve decisões como:

-   quais informações precisam ser armazenadas;
-   quais entidades existem;
-   como elas se relacionam;
-   quais regras garantem consistência;
-   qual tecnologia de banco atende ao cenário.

No TechPort, o projeto de dados está relacionado ao domínio de gestão de
chamados.

``` text
USUÁRIO
   ↓
CHAMADO
   ↓
TÉCNICO
   ↓
STATUS / HISTÓRICO / COMENTÁRIOS
```

A modelagem de dados precisa refletir as necessidades da aplicação.

------------------------------------------------------------------------

# 6. Estudo de caso --- TechPort

O **TechPort --- Sistema de Gestão de Chamados** é utilizado como estudo
de caso para transformar requisitos em decisões arquiteturais.

O sistema possui diferentes participantes e responsabilidades,
permitindo discutir:

-   usuários;
-   técnicos;
-   administradores;
-   abertura e acompanhamento de chamados;
-   atualização de status;
-   histórico;
-   dados persistentes;
-   componentes da aplicação.

O objetivo é deixar de enxergar o TechPort apenas como uma lista de
requisitos e começar a enxergá-lo como um **sistema composto por partes
relacionadas**.

------------------------------------------------------------------------

# 7. Projeto de Arquitetura e Construção do Código

A arquitetura funciona como uma ponte:

``` text
REQUISITOS
     ↓
ARQUITETURA
     ↓
COMPONENTES
     ↓
CÓDIGO
```

Antes de programar, precisamos responder:

``` text
Quais componentes existem?
Quem é responsável por cada tarefa?
Como os componentes se comunicam?
Onde os dados ficam?
Como o sistema poderá evoluir?
```

Essas respostas orientam a implementação.

------------------------------------------------------------------------

# 8. Arquitetura monolítica × separada

A aula compara diferentes formas de organizar uma aplicação.

## Arquitetura monolítica

``` text
INTERFACE
LÓGICA
ACESSO A DADOS
OUTRAS RESPONSABILIDADES
        ↓
MESMA APLICAÇÃO
```

Pode ser adequada para cenários menores e mais simples, mas o
crescimento exige atenção à organização interna.

## Arquitetura separada

``` text
FRONT-END
    ↓
BACK-END / API
    ↓
BANCO DE DADOS
```

A separação permite responsabilidades mais explícitas e evolução
independente de partes da solução.

A escolha arquitetural deve considerar o problema e a escala esperada.

------------------------------------------------------------------------

# 9. C4 Model

O **C4 Model** é apresentado como uma forma de documentar a arquitetura
em diferentes níveis de detalhe.

``` text
NÍVEL 1 → CONTEXTO
NÍVEL 2 → CONTÊINERES
NÍVEL 3 → COMPONENTES
NÍVEL 4 → CÓDIGO
```

A ideia é começar pela visão mais ampla e aprofundar progressivamente.

------------------------------------------------------------------------

# 10. Diagrama de Contexto --- C4 Nível 1

O Diagrama de Contexto mostra o sistema dentro do ambiente em que
existe.

Ele responde principalmente:

-   quem utiliza o sistema;
-   qual é o sistema central;
-   com quais sistemas externos ele se comunica.

Exemplo conceitual:

``` text
USUÁRIO ─────┐
TÉCNICO ─────┼──→ TECHPORT
ADMIN ───────┘       │
                     └──→ SISTEMAS / SERVIÇOS EXTERNOS
```

Nesse nível, detalhes internos ainda não são o foco.

------------------------------------------------------------------------

# 11. Diagrama de Contêiner --- C4 Nível 2

No C4, "contêiner" representa uma unidade executável ou armazenadora da
arquitetura, e não necessariamente um container Docker.

No TechPort, uma visão desse nível pode separar elementos como:

``` text
USUÁRIO
   ↓
INTERFACE
   ↓
APLICAÇÃO / BACK-END
   ↓
BANCO DE DADOS
```

O objetivo é mostrar as grandes partes técnicas e a comunicação entre
elas.

------------------------------------------------------------------------

# 12. Projeto de componentes

Depois de compreender contexto e contêineres, podemos aprofundar os
componentes internos.

Um componente deve possuir responsabilidade clara.

No TechPort, componentes podem representar áreas relacionadas a:

``` text
USUÁRIOS
CHAMADOS
TÉCNICOS
PRIORIDADES
RELATÓRIOS
```

Ao projetar componentes, devemos avaliar:

-   responsabilidade;
-   dependências;
-   interfaces;
-   reutilização;
-   manutenção.

------------------------------------------------------------------------

# 13. Como o projeto vira código

Uma decisão arquitetural precisa aparecer de alguma forma na
implementação.

``` text
ARQUITETURA
    ↓
PASTAS
    ↓
MÓDULOS
    ↓
CLASSES / FUNÇÕES
    ↓
CÓDIGO EXECUTÁVEL
```

Por isso, a organização do projeto Python não é apenas estética.

Ela materializa as responsabilidades definidas na arquitetura.

------------------------------------------------------------------------

# 14. Projeto de arquitetura

O projeto de arquitetura organiza o fluxo de funcionamento do sistema.

``` text
ENTRADA
   ↓
PROCESSAMENTO
   ↓
PERSISTÊNCIA
   ↓
SAÍDA
```

No TechPort, isso ajuda a responder:

-   onde a entrada é recebida;
-   onde as regras são executadas;
-   onde os dados são armazenados;
-   como o resultado volta ao usuário.

> Um bom projeto de arquitetura garante organização, segurança e
> eficiência em todas as etapas do sistema.

------------------------------------------------------------------------

# 15. Evolução da arquitetura

Arquitetura não precisa permanecer congelada.

Um sistema pode começar simples e evoluir conforme surgem novas
necessidades.

``` text
SOLUÇÃO INICIAL
      ↓
NOVOS REQUISITOS
      ↓
REFATORAÇÃO
      ↓
NOVOS COMPONENTES
      ↓
ARQUITETURA EVOLUÍDA
```

O importante é evitar complexidade sem necessidade e, ao mesmo tempo,
preparar o projeto para mudanças justificadas.

------------------------------------------------------------------------

# 16. Versionamento da arquitetura

Não apenas o código evolui.

Diagramas, decisões e documentação arquitetural também precisam
acompanhar a evolução do sistema.

O versionamento ajuda a registrar:

-   mudanças estruturais;
-   decisões técnicas;
-   novas integrações;
-   alteração de componentes;
-   evolução dos diagramas;
-   histórico do projeto.

``` text
ARQUITETURA V1
      ↓
DECISÃO / MUDANÇA
      ↓
ARQUITETURA V2
```

Arquitetura bem documentada reduz perda de contexto ao longo do projeto.

------------------------------------------------------------------------

# 17. Padrões arquiteturais

Padrões arquiteturais representam formas recorrentes de organizar
sistemas.

A aula apresenta diferentes possibilidades para mostrar que não existe
uma única arquitetura universal.

A escolha depende de fatores como:

-   tamanho do sistema;
-   complexidade;
-   escala;
-   equipe;
-   integração;
-   manutenção;
-   necessidade de evolução.

> O padrão deve servir ao problema. O problema não deve ser forçado a
> caber em um padrão.

------------------------------------------------------------------------

# 18. Pequena escala × grande escala

A arquitetura necessária para um sistema pequeno pode ser diferente
daquela exigida por um sistema de grande escala.

## Pequena escala

Pode priorizar:

-   simplicidade;
-   menor quantidade de componentes;
-   implementação mais direta;
-   menor custo operacional.

## Grande escala

Pode exigir:

-   separação maior de responsabilidades;
-   escalabilidade;
-   tolerância a falhas;
-   observabilidade;
-   distribuição de componentes;
-   maior automação.

``` text
PEQUENA ESCALA
Simplicidade primeiro
        ↓
CRESCIMENTO
        ↓
NOVAS NECESSIDADES
        ↓
EVOLUÇÃO ARQUITETURAL
```

------------------------------------------------------------------------

# 19. Componentes reutilizáveis

Projetos profissionais utilizam bibliotecas e componentes para evitar
reconstruir soluções já consolidadas.

Entre as tecnologias destacadas na aula:

  Componente       Possível utilização
  ---------------- ------------------------------
  **FastAPI**      Construção de APIs
  **SQLAlchemy**   Acesso e abstração de dados
  **Pydantic**     Validação e modelos de dados
  **pytest**       Testes
  **Paramiko**     Comunicação SSH
  **httpx**        Cliente HTTP

A reutilização adequada reduz esforço e aproveita soluções mantidas pela
comunidade.

> Reutilizar não significa usar qualquer biblioteca: é necessário
> avaliar qualidade, manutenção, segurança e aderência ao projeto.

------------------------------------------------------------------------

# 20. Segurança e LGPD

Segurança precisa fazer parte da arquitetura desde o projeto.

A aula relaciona arquitetura a preocupações como:

-   senhas;
-   hashes;
-   permissões;
-   logs;
-   autenticação;
-   variáveis de ambiente;
-   LGPD;
-   proteção de dados pessoais.

``` text
SEGURANÇA
    ↓
NÃO É UMA ETAPA FINAL
    ↓
É UMA DECISÃO DE PROJETO
```

O sistema deve considerar proteção de dados durante toda sua construção.

------------------------------------------------------------------------

# 21. O papel do arquiteto de software

O arquiteto de software ajuda a conectar necessidades do negócio e
decisões técnicas.

Entre suas responsabilidades estão:

-   compreender requisitos;
-   estruturar a solução;
-   definir componentes;
-   avaliar tecnologias;
-   documentar decisões;
-   antecipar impactos;
-   apoiar evolução e manutenção.

O arquiteto não substitui o desenvolvedor.

Seu papel é ajudar a organizar tecnicamente a solução e tornar as
decisões compreensíveis para a equipe.

------------------------------------------------------------------------

# 22. Visão consolidada do TechPort

A arquitetura do TechPort pode ser resumida como uma evolução:

``` text
REQUISITOS
    ↓
CASOS DE USO
    ↓
C4 — CONTEXTO
    ↓
C4 — CONTÊINERES
    ↓
COMPONENTES
    ↓
ORGANIZAÇÃO PYTHON
    ↓
PROJETO DE DADOS
    ↓
IMPLEMENTAÇÃO
```

A arquitetura cria a ponte entre aquilo que o sistema precisa fazer e a
forma como será construído.

------------------------------------------------------------------------

# 23. Principais aprendizados

Ao final desta aula, devemos compreender que:

-   arquitetura antecede e orienta a implementação;
-   um sistema pode ser representado por diferentes visões;
-   o C4 Model permite documentar a arquitetura progressivamente;
-   contexto, contêineres, componentes e código possuem níveis
    diferentes de detalhe;
-   a organização de pastas e módulos reflete decisões arquiteturais;
-   refatoração permite melhorar a estrutura sem alterar o comportamento
    esperado;
-   projeto de dados faz parte da arquitetura;
-   padrões arquiteturais devem ser escolhidos conforme o problema;
-   pequena e grande escala possuem necessidades diferentes;
-   componentes reutilizáveis aceleram o desenvolvimento;
-   segurança e LGPD devem ser consideradas desde o projeto;
-   Git ajuda a versionar código e também a evolução das decisões;
-   arquitetura precisa ser comunicável, compreensível e evolutiva.

------------------------------------------------------------------------

# Tecnologias e conceitos trabalhados

``` text
Python
Git
C4 Model
FastAPI
SQLAlchemy
Pydantic
pytest
Paramiko
httpx
Projeto de Dados
Refatoração
Padrões Arquiteturais
Segurança
LGPD
```

------------------------------------------------------------------------

# Conclusão

A Aula 03 estabelece a transição entre **pensar o sistema** e **começar
a materializar sua estrutura**.

``` text
REQUISITO
    ↓
ARQUITETURA
    ↓
DIAGRAMA
    ↓
COMPONENTE
    ↓
CÓDIGO
```

> **Todo código começa com um bom projeto.**

E um bom projeto arquitetural não existe apenas para produzir diagramas:
ele serve para que a equipe compreenda **o que construir, onde cada
responsabilidade deve ficar e como o sistema poderá evoluir**.

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

`Requisitos → Arquitetura → Componentes → Código`
