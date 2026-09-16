# Aula 02 --- Projeto de Software: dos Requisitos à Arquitetura

> **Transformando necessidades em uma solução estruturada antes de
> começar a implementar.**

**Disciplina:** Projeto, Implementação e Teste de Software\
**Professor:** Rodolfo Terra\
**Projeto aplicado:** TechPort --- Sistema de Gestão de Chamados\
**Instituição:** UniCesumar

[LinkedIn](https://www.linkedin.com/in/rodolffoterra/) •
[GitHub](https://github.com/rodolffoterra)

------------------------------------------------------------------------

## Sobre esta aula

A Aula 02 aprofunda a etapa de **Projeto de Software**, conectando os
requisitos levantados para o sistema às primeiras decisões de
arquitetura, interface, dados e organização da solução.

Depois de compreender **o que o software precisa fazer**, precisamos
responder:

``` text
COMO O SOFTWARE SERÁ CONSTRUÍDO?
```

A evolução trabalhada na aula pode ser representada por:

``` text
REQUISITOS
    ↓
CASOS DE USO
    ↓
PROJETO DE SOFTWARE
    ↓
ARQUITETURA
    ↓
INTERFACE
    ↓
DADOS
    ↓
IMPLEMENTAÇÃO
```

O projeto funciona como uma ponte entre a necessidade do usuário e o
código que será desenvolvido.

------------------------------------------------------------------------

# 1. Do requisito ao projeto

Requisitos descrevem aquilo que o sistema precisa atender.

O projeto de software começa a transformar essas necessidades em uma
solução técnica.

``` text
O QUE O SISTEMA PRECISA FAZER?
              ↓
           REQUISITO
              ↓
COMO VAMOS ORGANIZAR A SOLUÇÃO?
              ↓
            PROJETO
```

Essa etapa reduz improvisações durante a implementação e ajuda a equipe
a construir uma visão compartilhada do sistema.

------------------------------------------------------------------------

# 2. O que é Projeto de Software?

Projeto de software é o processo de definir como o sistema será
estruturado para atender aos requisitos.

Entre as decisões de projeto estão:

-   arquitetura;
-   componentes;
-   responsabilidades;
-   interface;
-   dados;
-   relacionamentos;
-   tecnologias;
-   fluxo de navegação;
-   integração entre partes do sistema.

O projeto não é o código final.

Ele orienta a construção do código.

------------------------------------------------------------------------

# 3. Por que projetar antes de implementar?

Começar diretamente pelo código pode parecer mais rápido, mas aumenta o
risco de:

-   responsabilidades misturadas;
-   retrabalho;
-   dificuldade de manutenção;
-   inconsistências;
-   decisões técnicas improvisadas;
-   componentes fortemente acoplados;
-   dificuldade de testar;
-   dificuldade de evoluir.

O projeto permite antecipar parte dessas decisões.

``` text
SEM PROJETO

REQUISITO
   ↓
CÓDIGO
   ↓
AJUSTES
   ↓
RETRABALHO
```

``` text
COM PROJETO

REQUISITO
   ↓
ANÁLISE
   ↓
ARQUITETURA
   ↓
IMPLEMENTAÇÃO
```

------------------------------------------------------------------------

# 4. O TechPort como estudo de caso

Durante a disciplina, utilizamos o **TechPort --- Sistema de Gestão de
Chamados** para aplicar os conceitos.

O domínio permite trabalhar elementos como:

``` text
USUÁRIO
TÉCNICO
ADMINISTRADOR
CHAMADO
PRIORIDADE
STATUS
COMENTÁRIO
HISTÓRICO
ANEXO
```

O desafio do projeto é transformar esses elementos em uma aplicação
organizada.

------------------------------------------------------------------------

# 5. Atores do sistema

Os atores representam quem interage com o software.

No TechPort, podemos observar diferentes perfis:

``` text
USUÁRIO
   ↓
Abre e acompanha chamados

TÉCNICO
   ↓
Atende e atualiza chamados

ADMINISTRADOR
   ↓
Administra e acompanha o sistema
```

Cada ator possui objetivos e responsabilidades diferentes.

Essa distinção influencia requisitos, casos de uso, telas e regras da
aplicação.

------------------------------------------------------------------------

# 6. Casos de uso

Casos de uso ajudam a representar funcionalidades do ponto de vista de
quem utiliza o sistema.

Exemplos no domínio do TechPort:

``` text
USUÁRIO
 ├── Abrir chamado
 ├── Consultar chamado
 └── Acompanhar andamento

TÉCNICO
 ├── Visualizar chamados
 ├── Assumir chamado
 └── Atualizar status

ADMINISTRADOR
 ├── Gerenciar informações
 └── Acompanhar operação
```

Eles ajudam a conectar:

``` text
ATOR
  ↓
NECESSIDADE
  ↓
FUNCIONALIDADE
```

------------------------------------------------------------------------

# 7. Requisitos funcionais e projeto

Um requisito funcional descreve um comportamento esperado.

Exemplo:

> O usuário deve conseguir abrir um chamado.

Durante o projeto, precisamos transformar essa necessidade em partes
concretas:

``` text
REQUISITO
“O usuário deve abrir um chamado”
              ↓
TELA / FORMULÁRIO
              ↓
VALIDAÇÃO
              ↓
REGRA
              ↓
PERSISTÊNCIA
              ↓
CONFIRMAÇÃO
```

O projeto detalha como a funcionalidade poderá existir tecnicamente.

------------------------------------------------------------------------

# 8. Requisitos não funcionais

Nem todos os requisitos descrevem funcionalidades.

Também precisamos considerar características de qualidade, como:

-   segurança;
-   desempenho;
-   usabilidade;
-   confiabilidade;
-   manutenibilidade;
-   disponibilidade.

Exemplo:

``` text
FUNCIONAL
“O usuário pode abrir um chamado.”

NÃO FUNCIONAL
“O sistema deve proteger os dados do usuário.”
```

Essas características também influenciam decisões arquiteturais.

------------------------------------------------------------------------

# 9. Arquitetura de software

Arquitetura descreve a organização de alto nível da solução.

Ela ajuda a responder:

``` text
QUAIS PARTES EXISTEM?
COMO ELAS SE RELACIONAM?
QUAL É A RESPONSABILIDADE DE CADA PARTE?
COMO OS DADOS CIRCULAM?
```

Uma representação inicial pode ser:

``` text
USUÁRIO
   ↓
INTERFACE
   ↓
APLICAÇÃO
   ↓
DADOS
```

A arquitetura cria uma visão estrutural antes de entrarmos nos detalhes
do código.

------------------------------------------------------------------------

# 10. Separação de responsabilidades

Uma das ideias centrais da aula é evitar que uma única parte do sistema
seja responsável por tudo.

Podemos separar responsabilidades:

``` text
INTERFACE
   ↓
Interação com usuário

LÓGICA
   ↓
Regras da aplicação

DADOS
   ↓
Persistência
```

Essa separação favorece:

-   manutenção;
-   organização;
-   testes;
-   reutilização;
-   evolução.

------------------------------------------------------------------------

# 11. Componentes

Um sistema pode ser dividido em componentes com responsabilidades
específicas.

Exemplo conceitual para o TechPort:

``` text
GESTÃO DE USUÁRIOS
GESTÃO DE CHAMADOS
GESTÃO DE TÉCNICOS
CONTROLE DE STATUS
HISTÓRICO
RELATÓRIOS
```

Cada componente deve ter um propósito compreensível.

A divisão deve ajudar a solução, e não criar complexidade desnecessária.

------------------------------------------------------------------------

# 12. Coesão

**Coesão** está relacionada ao quanto os elementos de um componente
pertencem ao mesmo propósito.

Uma boa organização busca:

``` text
COMPONENTE
    ↓
RESPONSABILIDADES RELACIONADAS
```

Exemplo:

``` text
Chamados
 ├── criar chamado
 ├── consultar chamado
 └── atualizar chamado
```

Quanto mais coerentes forem as responsabilidades internas, mais fácil
será compreender e manter o componente.

------------------------------------------------------------------------

# 13. Acoplamento

**Acoplamento** representa o nível de dependência entre partes do
sistema.

Quando tudo depende diretamente de tudo:

``` text
A ↔ B ↔ C ↔ D
```

uma alteração pode produzir impactos difíceis de prever.

O projeto procura criar relações mais controladas:

``` text
A → B → C
```

O objetivo não é eliminar todas as dependências, mas torná-las claras e
administráveis.

------------------------------------------------------------------------

# 14. Interface do sistema

Projeto de software também envolve pensar na experiência do usuário.

A interface precisa refletir as tarefas que cada ator executará.

No TechPort:

``` text
USUÁRIO
   ↓
ABRIR / ACOMPANHAR CHAMADOS

TÉCNICO
   ↓
ATENDER / ATUALIZAR CHAMADOS

ADMIN
   ↓
ADMINISTRAR / INSPECIONAR
```

A tela não deve ser pensada isoladamente das regras e dos dados.

------------------------------------------------------------------------

# 15. Protótipos

Antes de implementar uma interface completa, podemos utilizar protótipos
para validar ideias.

Um protótipo ajuda a discutir:

-   disposição das informações;
-   navegação;
-   ações disponíveis;
-   fluxo do usuário;
-   entendimento das telas.

``` text
IDEIA
  ↓
PROTÓTIPO
  ↓
VALIDAÇÃO
  ↓
AJUSTES
  ↓
IMPLEMENTAÇÃO
```

Alterar um protótipo normalmente custa menos do que reconstruir uma
funcionalidade já implementada.

------------------------------------------------------------------------

# 16. Fluxo de navegação

O projeto precisa considerar como o usuário percorre a aplicação.

Exemplo:

``` text
LOGIN
  ↓
PAINEL
  ↓
CHAMADOS
  ↓
DETALHE
  ↓
AÇÃO
  ↓
CONFIRMAÇÃO
```

Um fluxo claro ajuda a reduzir dúvidas e ações desnecessárias.

------------------------------------------------------------------------

# 17. Projeto de dados

Além das telas, precisamos pensar nas informações que sustentam o
sistema.

Perguntas importantes:

``` text
Quais dados precisam ser armazenados?
Quais entidades existem?
Como elas se relacionam?
Quais informações são obrigatórias?
Como preservar consistência?
```

No TechPort, entidades podem incluir:

``` text
USUÁRIO
TÉCNICO
CHAMADO
COMENTÁRIO
HISTÓRICO
ANEXO
```

------------------------------------------------------------------------

# 18. Entidades e relacionamentos

As entidades representam elementos relevantes do domínio.

Relacionamentos representam como esses elementos se conectam.

Exemplo conceitual:

``` text
USUÁRIO
   │
   │ abre
   ▼
CHAMADO
   │
   │ atendido por
   ▼
TÉCNICO
```

Outro exemplo:

``` text
CHAMADO
   ├── COMENTÁRIOS
   ├── HISTÓRICO
   └── ANEXOS
```

Essa visão prepara o projeto para a modelagem do banco de dados.

------------------------------------------------------------------------

# 19. Cardinalidade

Ao modelar dados, também precisamos compreender quantos registros podem
se relacionar.

Exemplo:

``` text
1 USUÁRIO
    ↓
N CHAMADOS
```

Um usuário pode abrir vários chamados.

``` text
1 CHAMADO
    ↓
N COMENTÁRIOS
```

Um chamado pode possuir vários comentários.

A cardinalidade ajuda a transformar regras do domínio em estrutura de
dados.

------------------------------------------------------------------------

# 20. Chaves

No projeto de dados, chaves ajudam a identificar e relacionar registros.

``` text
CHAVE PRIMÁRIA
      ↓
Identifica um registro

CHAVE ESTRANGEIRA
      ↓
Relaciona tabelas
```

Exemplo:

``` text
usuarios
id  ← PK

chamados
id
usuario_id ← FK para usuarios.id
```

Esses conceitos serão importantes quando o banco do TechPort for
construído.

------------------------------------------------------------------------

# 21. Da arquitetura para o código

As decisões de projeto começam a orientar a estrutura da implementação.

``` text
ARQUITETURA
    ↓
COMPONENTES
    ↓
MÓDULOS
    ↓
FUNÇÕES / CLASSES
    ↓
CÓDIGO
```

O objetivo é que o código reflita a organização pensada durante o
projeto.

------------------------------------------------------------------------

# 22. Organização do projeto

Uma estrutura de diretórios pode ajudar a representar responsabilidades.

Exemplo conceitual:

``` text
techport/
├── app/
│   ├── pages/
│   ├── models/
│   ├── services/
│   ├── repositories/
│   └── database/
├── tests/
├── requirements.txt
└── README.md
```

Nesta fase, o mais importante é compreender por que cada
responsabilidade precisa ter um lugar definido.

------------------------------------------------------------------------

# 23. Escolha de tecnologias

Projeto também envolve decisões tecnológicas.

No TechPort, a evolução da disciplina utiliza tecnologias como:

``` text
PYTHON
STREAMLIT
MYSQL
FASTAPI
PYTEST
GIT
DOCKER
```

A tecnologia deve ser escolhida para atender às necessidades da solução.

> Tecnologia é meio, não objetivo.

------------------------------------------------------------------------

# 24. Decisões arquiteturais

Uma decisão técnica deve possuir uma justificativa.

Exemplo:

``` text
DECISÃO
Usar banco relacional
       ↓
MOTIVO
Dados estruturados e relacionamentos claros
```

Outro exemplo:

``` text
DECISÃO
Separar interface e persistência
       ↓
MOTIVO
Melhor organização e evolução
```

Registrar decisões ajuda a equipe a compreender por que o sistema foi
construído de determinada maneira.

------------------------------------------------------------------------

# 25. Diagramas como comunicação

Diagramas ajudam a explicar o sistema antes e durante a implementação.

Eles podem representar:

-   atores;
-   funcionalidades;
-   componentes;
-   fluxo;
-   dados;
-   relacionamentos;
-   arquitetura.

O objetivo não é desenhar por desenhar.

> **O diagrama deve tornar uma decisão ou estrutura mais fácil de
> compreender.**

------------------------------------------------------------------------

# 26. Do requisito à solução

Uma funcionalidade pode percorrer várias etapas:

``` text
NECESSIDADE DO USUÁRIO
        ↓
REQUISITO
        ↓
CASO DE USO
        ↓
TELA
        ↓
REGRA
        ↓
DADO
        ↓
COMPONENTE
        ↓
IMPLEMENTAÇÃO
```

Essa visão ajuda a compreender que as etapas do desenvolvimento estão
conectadas.

------------------------------------------------------------------------

# 27. Projeto não é uma etapa isolada

Mesmo depois que a implementação começa, o projeto pode evoluir.

``` text
PROJETAR
   ↓
IMPLEMENTAR
   ↓
VALIDAR
   ↓
APRENDER
   ↓
AJUSTAR O PROJETO
```

Novas informações podem exigir mudanças.

O importante é manter coerência entre requisitos, arquitetura e
implementação.

------------------------------------------------------------------------

# 28. Preparando o TechPort para as próximas aulas

A Aula 02 estabelece a base para as próximas construções.

``` text
AULA 01
Requisitos e visão do sistema
        ↓
AULA 02
Projeto e arquitetura
        ↓
PRÓXIMAS AULAS
Código + Dados + API + Testes + Deploy
```

A partir dessa estrutura, o projeto poderá evoluir progressivamente sem
perder a visão do todo.

------------------------------------------------------------------------

# 29. Principais aprendizados

Ao final desta aula, devemos compreender que:

-   requisitos dizem **o que** o sistema precisa atender;
-   projeto ajuda a definir **como** a solução será estruturada;
-   arquitetura organiza os principais elementos do sistema;
-   componentes devem possuir responsabilidades claras;
-   coesão e acoplamento influenciam a manutenibilidade;
-   interface deve refletir as necessidades dos atores;
-   protótipos permitem validar ideias antes da implementação;
-   fluxos ajudam a compreender a jornada do usuário;
-   projeto de dados identifica entidades e relacionamentos;
-   cardinalidade representa regras importantes do domínio;
-   decisões técnicas precisam ser justificadas;
-   diagramas são instrumentos de comunicação;
-   projeto e implementação evoluem juntos.

------------------------------------------------------------------------

# Tecnologias e conceitos relacionados

  Item                     Papel
  ------------------------ ---------------------------------------------
  **Requisitos**           Definem necessidades e comportamentos
  **Casos de uso**         Representam interações dos atores
  **Arquitetura**          Organiza a solução
  **Componentes**          Dividem responsabilidades
  **Protótipos**           Validam interface e fluxo
  **Modelagem de dados**   Estrutura informações
  **Cardinalidade**        Define relações entre entidades
  **Python**               Base de implementação do projeto
  **Streamlit**            Interface utilizada na evolução do TechPort
  **MySQL**                Persistência utilizada posteriormente
  **Git**                  Versionamento e colaboração

------------------------------------------------------------------------

# Conclusão

A principal transformação da Aula 02 é sair de:

``` text
“EU SEI O QUE O SISTEMA PRECISA FAZER.”
```

para:

``` text
“EU CONSIGO COMEÇAR A DESENHAR COMO ELE SERÁ CONSTRUÍDO.”
```

O fluxo pode ser resumido em:

``` text
REQUISITO
    ↓
PROJETO
    ↓
ARQUITETURA
    ↓
COMPONENTES
    ↓
DADOS
    ↓
INTERFACE
    ↓
IMPLEMENTAÇÃO
```

> **Projetar software é transformar necessidades em decisões técnicas
> compreensíveis antes que essas decisões se tornem código.**

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

`Requisitos → Projeto → Arquitetura → Implementação`
