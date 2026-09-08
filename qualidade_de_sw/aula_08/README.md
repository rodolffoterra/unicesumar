# O Futuro da Qualidade de Software

> **IA • DevOps • Automação • Dados • Cultura • Novas Arquiteturas**

A Qualidade de Software deixou de ser uma atividade concentrada no final
do desenvolvimento. Em ambientes modernos, ela acompanha todo o ciclo de
vida do produto: requisitos, desenvolvimento, testes, integração,
implantação, operação, monitoramento e evolução.

Esta aula apresenta as principais tendências que estão transformando a
área de Qualidade de Software e discute como o papel do profissional de
qualidade está evoluindo diante da Inteligência Artificial, DevOps,
automação, sistemas distribuídos e decisões orientadas por dados.

------------------------------------------------------------------------

## 1. Da inspeção à qualidade contínua

Historicamente, a qualidade estava muito associada à inspeção do produto
depois que grande parte do software já havia sido construída.

A evolução pode ser resumida assim:

**INSPEÇÃO → PROCESSOS → AGILIDADE → DEVOPS → IA + DADOS**

### Inspeção

O foco inicial estava principalmente em:

-   revisões manuais;
-   inspeção de documentos;
-   revisão de código;
-   identificação de defeitos;
-   verificação de conformidade com requisitos.

A qualidade era frequentemente percebida como uma etapa de controle.

### Processos

Com a evolução da Engenharia de Software, surgiram normas, modelos de
maturidade e processos estruturados para tornar o desenvolvimento mais
previsível e controlável.

O foco passou a incluir:

-   padronização;
-   documentação;
-   melhoria de processos;
-   prevenção de defeitos;
-   avaliação da maturidade organizacional.

### Agilidade

As metodologias ágeis aproximaram desenvolvimento, negócio e usuário.

A qualidade passou a depender cada vez mais de:

-   ciclos curtos;
-   feedback frequente;
-   colaboração;
-   entregas incrementais;
-   adaptação rápida.

### DevOps

DevOps ampliou essa visão ao integrar desenvolvimento e operações.

Testes, verificações, deploy e monitoramento passaram a fazer parte de
pipelines automatizados.

### IA + Dados

A etapa atual adiciona Inteligência Artificial e análise de dados ao
processo.

A organização não precisa apenas descobrir o que falhou. Ela pode
utilizar dados históricos para identificar tendências, antecipar riscos
e decidir onde concentrar seus esforços de qualidade.

> **Qualidade deixou de ser uma etapa e passou a acompanhar todo o ciclo
> do software.**

------------------------------------------------------------------------

## 2. Qualidade não significa apenas ausência de bugs

Um software sem erros aparentes não é necessariamente um software de
qualidade.

A avaliação moderna considera diferentes dimensões, como:

-   confiabilidade;
-   segurança;
-   desempenho;
-   experiência do usuário;
-   disponibilidade;
-   capacidade de evolução;
-   geração de valor.

Imagine um sistema que executa todas as funções previstas, mas leva 30
segundos para responder a cada operação. Funcionalmente ele pode estar
correto, mas a experiência oferecida é inadequada.

Da mesma maneira, uma aplicação pode possuir poucos defeitos e ainda:

-   ser difícil de utilizar;
-   apresentar riscos de segurança;
-   não suportar a quantidade necessária de usuários;
-   ficar indisponível com frequência;
-   não resolver adequadamente o problema do cliente.

Portanto:

> **Software sem bugs pode não gerar valor.**

Qualidade precisa ser analisada simultaneamente sob a perspectiva
técnica, do negócio e do usuário.

------------------------------------------------------------------------

## 3. Inteligência Artificial na Qualidade de Software

A Inteligência Artificial está ampliando as possibilidades de automação
e análise dentro da Engenharia de Software.

Uma visão simplificada é:

``` text
REQUISITOS
    ↓
    IA
 ↙  ↓  ↘
TESTES  CÓDIGO  RISCOS
```

Entre as aplicações possíveis estão:

-   geração de casos de teste;
-   apoio à análise de requisitos;
-   revisão automática de código;
-   identificação de padrões de defeitos;
-   priorização de testes;
-   análise de grandes volumes de resultados;
-   apoio à previsão de áreas de maior risco.

### Exemplo

Considere uma empresa que possui milhares de registros históricos de
bugs.

Esses registros podem conter informações como:

-   módulo afetado;
-   tipo de alteração realizada;
-   quantidade de arquivos modificados;
-   desenvolvedor ou equipe responsável;
-   severidade;
-   causa;
-   tempo de correção.

Ferramentas de análise e IA podem encontrar padrões nesses dados e
ajudar a indicar alterações que merecem maior atenção.

A ideia não é prever o futuro com certeza, mas melhorar a priorização
baseada em evidências.

------------------------------------------------------------------------

## 4. A IA substitui o profissional de qualidade?

A IA pode executar atividades em grande escala, mas isso não elimina a
necessidade de julgamento humano.

### A IA pode ajudar a:

-   executar tarefas;
-   analisar grandes volumes de informação;
-   identificar padrões;
-   gerar sugestões;
-   automatizar atividades repetitivas;
-   criar propostas de cenários de teste.

### O profissional precisa:

-   interpretar resultados;
-   questionar conclusões;
-   definir estratégias;
-   avaliar riscos;
-   compreender o contexto;
-   entender necessidades do usuário;
-   tomar decisões.

Um exemplo ajuda a compreender essa diferença:

> Se uma IA gerar 500 casos de teste automaticamente, quem decide se
> esses testes realmente verificam aquilo que é importante para o
> negócio?

Quantidade de testes não é sinônimo de qualidade dos testes.

A combinação mais relevante é:

**IA + HUMANO → QUALIDADE**

> **A IA automatiza e amplia capacidades. O profissional continua
> responsável pelo contexto e pelas decisões.**

------------------------------------------------------------------------

## 5. Do teste manual à automação inteligente

A automação de testes também está evoluindo.

### Teste manual

``` text
MANUAL
↓
Execução realizada diretamente por pessoas
```

É importante em diversos cenários, principalmente aqueles que exigem
exploração, interpretação e percepção humana.

### Teste automatizado

``` text
AUTOMATIZADO
↓
Scripts executam verificações previamente programadas
```

O teste automatizado aumenta repetibilidade, velocidade e capacidade de
regressão.

### Automação inteligente

``` text
INTELIGENTE
↓
IA auxilia criação, seleção, manutenção e análise dos testes
```

Soluções apoiadas por IA podem auxiliar a:

-   gerar cenários;
-   interpretar requisitos;
-   identificar fluxos relevantes;
-   adaptar testes;
-   priorizar riscos;
-   analisar resultados.

A principal diferença é que a automação tradicional normalmente executa
aquilo que foi explicitamente programado, enquanto técnicas de IA também
podem apoiar a construção e a adaptação das verificações.

------------------------------------------------------------------------

## 6. Qualidade em todo o pipeline DevOps

Na abordagem tradicional, testes podiam aparecer próximos ao final do
desenvolvimento.

Em DevOps, a qualidade é integrada ao fluxo.

``` text
CÓDIGO
  ↓
BUILD
  ↓
TESTES
  ↓
ANÁLISE
  ↓
DEPLOY
  ↓
MONITORAMENTO
  ↓
FEEDBACK
  └──────────→ CÓDIGO
```

Cada alteração pode iniciar automaticamente uma sequência de
verificações.

Isso reduz o intervalo entre:

**INTRODUZIR UM PROBLEMA → IDENTIFICAR O PROBLEMA**

Quanto mais rapidamente um problema é identificado, menor tende a ser o
impacto de sua correção.

> **Qualidade não acontece somente antes do deploy. Ela acontece
> continuamente.**

------------------------------------------------------------------------

## 7. CI/CD como barreira de qualidade

Uma pipeline pode funcionar como uma sequência de barreiras antes que
uma alteração seja promovida para outro ambiente.

Exemplo:

``` text
DESENVOLVEDOR
     ↓
  git push
     ↓
  PIPELINE
     ↓
┌───────────────────────────┐
│ Testes unitários          │
│ Testes de integração      │
│ Testes de regressão       │
│ Verificações de segurança │
│ Qualidade do código       │
│ Build                     │
└───────────────────────────┘
     ↓
  APROVADO?
   ↙     ↘
 NÃO     SIM
  ↓       ↓
CORRIGIR DEPLOY
```

O objetivo de CI/CD não é simplesmente fazer deploy rapidamente.

O objetivo é permitir entregas frequentes mantendo controles
automatizados de qualidade.

Uma pipeline pode impedir a progressão quando, por exemplo:

-   um teste falha;
-   a compilação falha;
-   uma dependência apresenta problema;
-   regras de qualidade não são atendidas;
-   uma análise de segurança identifica uma condição crítica.

------------------------------------------------------------------------

## 8. Qualidade não termina no deploy

A implantação não encerra o trabalho de qualidade.

Produção oferece informações que dificilmente podem ser completamente
reproduzidas em laboratório.

``` text
SOFTWARE
   ↓
PRODUÇÃO
   ↓
MONITORAR
 ↙ ↓  ↓ ↘
ERROS | LATÊNCIA | LOGS | USUÁRIOS
              ↓
           MELHORAR
```

Entre os aspectos que podem ser acompanhados estão:

-   disponibilidade;
-   falhas;
-   desempenho;
-   tempo de resposta;
-   comportamento inesperado;
-   utilização de recursos;
-   experiência do usuário.

### Observabilidade

Observabilidade ajuda as equipes a compreender o comportamento interno
de sistemas a partir das informações que eles produzem.

Entre os elementos frequentemente utilizados estão:

-   **logs** --- registros de eventos;
-   **métricas** --- valores quantitativos ao longo do tempo;
-   **traces** --- rastreamento de uma requisição através de diferentes
    componentes.

Isso se torna especialmente importante em sistemas distribuídos.

------------------------------------------------------------------------

## 9. Qualidade baseada em dados

Decisões de qualidade não devem depender exclusivamente de percepção.

A evolução desejada é:

**DADOS → INFORMAÇÃO → DECISÃO → MELHORIA**

Alguns indicadores que podem ser utilizados:

  -----------------------------------------------------------------------
  Indicador                           Pergunta que ajuda a responder
  ----------------------------------- -----------------------------------
  Cobertura                           Quanto do software está sendo
                                      exercitado pelos testes?

  Taxa de falhas                      Com que frequência estamos
                                      encontrando falhas?

  MTTR                                Quanto tempo levamos para
                                      restaurar/corrigir após um
                                      problema?

  Frequência de deploy                Com que frequência entregamos
                                      alterações?

  Bugs em produção                    Quantos problemas escaparam das
                                      verificações anteriores?

  Testes aprovados                    Qual é o estado atual das
                                      verificações automatizadas?
  -----------------------------------------------------------------------

Nenhuma métrica deve ser interpretada isoladamente.

Por exemplo, cobertura de código alta não garante que os testes sejam
bons. É possível executar muitas linhas de código sem verificar
adequadamente os comportamentos importantes.

> **Métrica sem contexto é apenas um número.**

A pergunta mais importante é:

**Qual decisão essa métrica ajuda a tomar?**

------------------------------------------------------------------------

## 10. O software ficou mais complexo

Aplicações modernas frequentemente dependem de diversos componentes.

``` text
              CLOUD
                |
MICROSSERVIÇOS — APLICAÇÃO — SERVERLESS
       |          |          |
      APIs       IoT      SERVIÇOS
       |          |       EXTERNOS
       └──── BANCO DE DADOS ────┘
```

Um problema observado pelo usuário pode ter origem em:

-   código da aplicação;
-   API;
-   rede;
-   banco de dados;
-   microsserviço;
-   função Serverless;
-   serviço de terceiros;
-   comunicação entre componentes.

Isso aumenta a necessidade de uma visão **end-to-end**.

> **Quanto maior o número de integrações, maior o número de potenciais
> pontos de falha.**

------------------------------------------------------------------------

## 11. Qualidade em microsserviços

Em uma arquitetura de microsserviços, diferentes serviços podem evoluir
independentemente.

É necessário validar:

-   APIs;
-   contratos;
-   comunicação;
-   integração;
-   persistência;
-   comportamento diante de indisponibilidades;
-   logs e rastreamento distribuído.

### Testes de contrato

Imagine dois serviços:

``` text
SERVIÇO DE PEDIDOS
        ↓
SERVIÇO DE PAGAMENTO
```

O serviço de pagamento retornava:

``` json
{
  "status": "approved"
}
```

Depois de uma alteração, passa a retornar:

``` json
{
  "payment_status": "approved"
}
```

O serviço de pagamento pode continuar funcionando perfeitamente quando
testado sozinho.

O serviço de pedidos também pode estar funcionando corretamente de forma
isolada.

Mas a integração entre os dois pode quebrar.

Por isso:

**TESTAR COMPONENTES + TESTAR INTERAÇÕES**

Testes de contrato ajudam a detectar incompatibilidades entre serviços
antes que elas causem falhas no sistema completo.

------------------------------------------------------------------------

## 12. Qualidade em Serverless

Arquiteturas Serverless introduzem características próprias.

É necessário considerar:

-   eventos;
-   funções;
-   integrações;
-   permissões;
-   serviços externos;
-   monitoramento;
-   tratamento de falhas;
-   tempo de inicialização.

### Cold Start

Funções Serverless podem precisar inicializar um ambiente de execução
antes de processar determinadas solicitações.

Esse tempo adicional é conhecido como **Cold Start**.

Dependendo da aplicação, ele pode afetar o tempo de resposta percebido
pelo usuário.

Em ambientes orientados a eventos, também é importante testar o fluxo
completo:

``` text
EVENTO
  ↓
FUNÇÃO
  ↓
SERVIÇO
  ↓
BANCO / FILA / API
  ↓
RESULTADO
```

Testar somente a função isoladamente pode não revelar problemas de
integração.

------------------------------------------------------------------------

## 13. Modelos de qualidade também evoluem

Modelos tradicionais continuam relevantes, mas as organizações precisam
adaptá-los ao contexto atual.

### TMMi --- Test Maturity Model integration

O TMMi é voltado à maturidade e melhoria dos processos de teste.

Ele ajuda organizações a estruturar e evoluir suas práticas de teste de
maneira progressiva.

### Qualidade e maturidade em DevOps

Em ambientes DevOps, maturidade de qualidade está fortemente associada a
aspectos como:

-   automação;
-   colaboração;
-   integração contínua;
-   feedback rápido;
-   monitoramento;
-   melhoria contínua.

### Abordagens híbridas

Na prática, organizações podem combinar diferentes referências:

**ISO + CMMI + Scrum + Lean + DevOps**

Não é necessário tratar esses modelos como concorrentes.

Uma organização pode utilizar:

-   governança e padronização de normas;
-   práticas de melhoria de processos;
-   métodos ágeis para desenvolvimento;
-   DevOps para integração e operação;
-   automação para acelerar verificações.

> **As organizações adaptam práticas de qualidade ao seu contexto.**

------------------------------------------------------------------------

## 14. Qualidade de IA também é ética

Um sistema pode funcionar tecnicamente e ainda produzir resultados
inadequados.

Considere:

``` text
SISTEMA DE IA
     ↓
   DECISÃO
     ↓
IMPACTO REAL
```

Quando sistemas automatizados influenciam decisões que afetam pessoas,
qualidade também precisa considerar:

-   viés;
-   discriminação;
-   privacidade;
-   transparência;
-   segurança dos dados;
-   explicabilidade.

### Exemplo: recrutamento

Imagine um modelo treinado com dados históricos de contratações.

Se esses dados carregarem padrões discriminatórios ou distorções
históricas, o modelo pode aprender e reproduzir parte desses padrões.

Mesmo que o algoritmo apresente boa performance estatística, suas
decisões podem produzir impactos inadequados.

Portanto:

> **Acurácia técnica sozinha não representa qualidade.**

No tratamento de dados pessoais e no desenvolvimento de soluções
digitais, também é necessário observar requisitos legais e regulatórios
aplicáveis, incluindo referências como:

-   LGPD;
-   GDPR.

> **Qualidade também significa produzir decisões responsáveis.**

------------------------------------------------------------------------

## 15. Qualidade é cultura

Uma das mudanças mais importantes na Engenharia de Software moderna é
compreender que qualidade não pertence exclusivamente à equipe de
testes.

Ela envolve:

### Desenvolvedor

Constrói código testável, seguro e sustentável.

### QA

Planeja estratégias de qualidade, identifica riscos e apoia diferentes
níveis de validação.

### DevOps

Automatiza pipelines, ambientes, verificações, deploy e monitoramento.

### Product Owner

Ajuda a garantir que requisitos, prioridades e critérios estejam
relacionados ao valor do produto.

### Gestor

Cria condições para que qualidade seja prioridade e não apenas uma
exigência final.

### UX

Avalia a experiência oferecida às pessoas.

### Usuário

Fornece feedback sobre o comportamento real do produto.

No centro está:

# QUALIDADE

E a resposta para a pergunta "quem é responsável?" é:

# TODOS.

> **Qualidade não pertence a uma área. Pertence ao produto.**

Quanto mais tarde um problema é descoberto, maior pode ser o retrabalho
envolvido.

Por isso, a preocupação com qualidade deve começar ainda na definição
dos requisitos.

------------------------------------------------------------------------

## 16. Errar, aprender e melhorar

Falhas fazem parte de sistemas complexos.

O diferencial de uma organização madura está na maneira como ela
responde a essas falhas.

``` text
ERRO
 ↓
IDENTIFICAR
 ↓
INVESTIGAR
 ↓
CAUSA RAIZ
 ↓
CORRIGIR
 ↓
PREVENIR
 ↓
APRENDER
 └────────→ melhoria contínua
```

O objetivo não deve ser simplesmente corrigir o sintoma.

É necessário perguntar:

-   O que aconteceu?
-   Por que aconteceu?
-   Por que nossas verificações não detectaram antes?
-   Como corrigimos?
-   Como evitamos recorrência?
-   Que aprendizado pode ser incorporado ao processo?

Uma falha pode resultar em:

-   novo teste automatizado;
-   alteração de arquitetura;
-   melhoria de monitoramento;
-   revisão de processo;
-   nova validação na pipeline;
-   melhoria na documentação.

> **Organizações maduras não procuram culpados. Procuram causas e
> melhorias.**

Ambientes em que as pessoas escondem problemas por medo dificultam a
evolução da qualidade.

------------------------------------------------------------------------

## 17. O profissional de qualidade do futuro

O profissional moderno precisa combinar conhecimento técnico com
habilidades humanas.

### Hard Skills

Entre as competências técnicas relevantes estão:

-   testes;
-   automação;
-   CI/CD;
-   Cloud;
-   dados;
-   Inteligência Artificial;
-   APIs;
-   observabilidade.

### Soft Skills

Também são fundamentais:

-   comunicação;
-   pensamento crítico;
-   colaboração;
-   adaptabilidade;
-   resiliência;
-   visão de negócio.

### Aprendizado contínuo

Ferramentas mudam.

Frameworks mudam.

Arquiteturas mudam.

As capacidades mais duradouras são:

-   aprender;
-   investigar;
-   analisar;
-   questionar;
-   comunicar;
-   adaptar;
-   resolver problemas.

> **O profissional não precisa apenas saber utilizar ferramentas.
> Precisa compreender problemas e escolher boas soluções.**

------------------------------------------------------------------------

## 18. Estudo de caso: da qualidade reativa à qualidade contínua

Considere uma organização hipotética com o seguinte cenário.

### Antes

-   muitos bugs;
-   testes predominantemente manuais;
-   entregas lentas;
-   equipes isoladas;
-   pouca visibilidade do comportamento em produção.

A organização trabalhava principalmente de maneira reativa:

**PROBLEMA → DESCOBRIR → CORRIGIR**

### Transformação

A empresa começa a combinar:

**CI/CD + AUTOMAÇÃO + MÉTRICAS + MONITORAMENTO + CULTURA**

CI/CD reduz o tempo de feedback.

Automação aumenta a capacidade de repetir verificações.

Métricas aumentam a visibilidade.

Monitoramento mostra o comportamento real do produto.

Cultura aproxima as equipes e distribui a responsabilidade pela
qualidade.

### Depois

A organização passa a buscar:

-   entregas mais rápidas;
-   maior estabilidade;
-   feedback contínuo;
-   decisões baseadas em dados;
-   maior satisfação do usuário;
-   identificação antecipada de problemas.

O ponto principal não é atribuir a transformação a uma ferramenta
específica.

> **O resultado vem da combinação de processos, pessoas, tecnologia e
> dados.**

------------------------------------------------------------------------

## 19. O novo papel do profissional de qualidade

O papel do profissional de qualidade está mudando.

### Ontem --- atuação predominantemente reativa

``` text
TESTAR
  ↓
ENCONTRAR DEFEITO
  ↓
REPORTAR
```

O foco estava fortemente associado a encontrar problemas depois que
funcionalidades haviam sido desenvolvidas.

### Hoje --- atuação preventiva e estratégica

``` text
PLANEJAR
   ↓
PREVENIR
   ↓
AUTOMATIZAR
   ↓
MEDIR
   ↓
ANALISAR
   ↓
MELHORAR
```

O profissional passa a participar de decisões relacionadas a:

-   requisitos;
-   riscos;
-   arquitetura;
-   estratégia de testes;
-   automação;
-   pipelines;
-   métricas;
-   produção;
-   experiência do usuário;
-   melhoria contínua.

> **O profissional de qualidade deixa de atuar apenas como detector de
> defeitos e passa a participar das decisões do produto.**

O QA moderno precisa compreender:

**TECNOLOGIA + NEGÓCIO + USUÁRIO + RISCOS + DADOS**

------------------------------------------------------------------------

## 20. O futuro da qualidade é contínuo

Os principais conceitos desta aula convergem para uma visão integrada:

``` text
IA
 ↓
AUTOMAÇÃO
 ↓
DEVOPS
 ↓
DADOS
 ↓
CULTURA
 ↓
QUALIDADE CONTÍNUA
```

### Inteligência Artificial

Amplia nossa capacidade de analisar, gerar e priorizar.

### Automação

Reduz trabalho repetitivo e acelera feedback.

### DevOps

Integra qualidade ao fluxo de desenvolvimento e operação.

### Dados

Transformam percepção em evidência.

### Cultura

Distribui a responsabilidade e sustenta a melhoria.

### Qualidade contínua

Une essas capacidades durante todo o ciclo de vida do software.

> **Qualidade de software não é responsabilidade de uma equipe. É uma
> capacidade da organização.**

------------------------------------------------------------------------

# Pergunta para reflexão

> **Se a IA consegue gerar código e testes, qual será o papel do
> profissional de qualidade?**

A resposta está menos relacionada à execução mecânica de tarefas e mais
relacionada à capacidade de:

-   entender riscos;
-   tomar decisões;
-   questionar resultados;
-   compreender o usuário;
-   interpretar dados;
-   conectar tecnologia ao negócio;
-   promover melhoria contínua;
-   garantir que o produto realmente gere valor.

------------------------------------------------------------------------

# Resumo da aula

``` text
QUALIDADE TRADICIONAL
        ↓
PROCESSOS E MODELOS
        ↓
AGILIDADE
        ↓
DEVOPS + CI/CD
        ↓
AUTOMAÇÃO
        ↓
MONITORAMENTO + DADOS
        ↓
IA
        ↓
CULTURA + PESSOAS
        ↓
QUALIDADE CONTÍNUA
```

## Principais aprendizados

1.  Qualidade não é apenas ausência de bugs.
2.  A qualidade precisa acompanhar todo o ciclo de vida do software.
3.  IA amplia a capacidade do profissional, mas não elimina a
    necessidade de julgamento humano.
4.  Automação e CI/CD reduzem o tempo de feedback.
5.  Produção também é uma fonte essencial de informação sobre qualidade.
6.  Métricas precisam apoiar decisões, não apenas preencher dashboards.
7.  Sistemas distribuídos exigem testes de componentes e de interações.
8.  Qualidade em IA também envolve ética, privacidade e impacto.
9.  Qualidade é responsabilidade compartilhada.
10. Falhas devem gerar aprendizado e prevenção.
11. Hard skills e soft skills precisam evoluir juntas.
12. O profissional de qualidade está migrando da detecção para a
    prevenção e para a atuação estratégica.

------------------------------------------------------------------------

# Conclusão

O futuro da Qualidade de Software não será definido por uma única
ferramenta, metodologia ou tecnologia.

Ele será resultado da integração entre:

**PESSOAS + PROCESSOS + TECNOLOGIA + DADOS**

Ferramentas de IA serão cada vez mais capazes de gerar código, sugerir
testes, analisar resultados e identificar padrões. Pipelines serão cada
vez mais automatizadas. Sistemas serão cada vez mais distribuídos.

Nesse cenário, o profissional de qualidade ganha um papel ainda mais
importante: **entender contexto, avaliar riscos, interpretar evidências,
conectar equipes e garantir que a tecnologia entregue valor de maneira
confiável e responsável.**

# Qualidade não é o final do processo.

# Qualidade é parte de todo o processo.

------------------------------------------------------------------------

## Professor

**Professor Rodolfo Terra**

**LinkedIn:** linkedin.com/in/rodolffoterra/\
**GitHub:** github.com/rodolffoterra
