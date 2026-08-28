# 🧪 Revisões e Testes de Software

> **Qualidade de Software --- Revisões, Testes, Automação e Métricas**

Material desenvolvido para a disciplina de **Qualidade de Software**,
abordando como revisões, diferentes níveis de testes, automação e
métricas contribuem para a construção de softwares mais confiáveis.

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**

-   LinkedIn: https://www.linkedin.com/in/rodolffoterra/
-   GitHub: https://github.com/rodolffoterra

------------------------------------------------------------------------

# 🎯 Objetivo da Aula

Esta aula apresenta as **revisões e os testes de software como
mecanismos fundamentais para garantia da qualidade**.

Ao final da aula, o aluno deverá ser capaz de:

-   compreender o papel dos testes na qualidade;
-   diferenciar revisão e teste;
-   conhecer técnicas de revisão;
-   compreender os níveis de teste;
-   diferenciar testes funcionais e não funcionais;
-   compreender testes manuais e automatizados;
-   reconhecer o papel dos testes em pipelines de CI/CD;
-   utilizar métricas para avaliar a efetividade dos testes;
-   relacionar testes, riscos, confiabilidade e melhoria contínua.

------------------------------------------------------------------------

# 🔄 Qualidade de Software

A qualidade não aparece apenas no final do desenvolvimento. Ela é
construída durante todo o ciclo de vida do software.

``` text
REQUISITOS
    ↓
BOAS PRÁTICAS
    ↓
REVISÕES
    ↓
TESTES UNITÁRIOS
    ↓
TESTES DE INTEGRAÇÃO
    ↓
TESTES DE SISTEMA
    ↓
TESTES DE ACEITAÇÃO
    ↓
MÉTRICAS
    ↓
QUALIDADE
```

> **Não existe uma única atividade responsável pela qualidade.**

------------------------------------------------------------------------

# 🧪 O que significa testar software?

Testar não significa simplesmente verificar se uma funcionalidade
"funciona".

Testar significa produzir **evidências sobre o comportamento e a
qualidade do software**.

Os testes ajudam a verificar se o sistema:

-   atende aos requisitos;
-   apresenta o comportamento esperado;
-   responde adequadamente a entradas inválidas;
-   mantém características de qualidade;
-   possui riscos aceitáveis para utilização.

> **Um teste aprovado não significa que todo o sistema está correto.**

Ele representa apenas uma evidência sobre determinado comportamento
avaliado.

------------------------------------------------------------------------

# ⚠️ Testes e Riscos

Não é possível testar todas as combinações existentes em um sistema
real.

Além dos dados de entrada, existem diferentes navegadores, dispositivos,
sistemas operacionais, conexões, integrações, perfis de usuários e
sequências de utilização.

Por isso, uma estratégia de testes deve considerar:

``` text
PROBABILIDADE × IMPACTO
          ↓
        RISCO
          ↓
    PRIORIZAÇÃO
          ↓
        TESTES
```

Quanto maior a criticidade de determinado cenário, maior tende a ser a
necessidade de validação.

------------------------------------------------------------------------

# ⏱️ Quanto mais cedo, melhor

Um defeito identificado durante o desenvolvimento normalmente possui
impacto menor do que o mesmo problema encontrado em produção.

``` text
REQUISITO
   ↓
DESENVOLVIMENTO
   ↓
TESTES
   ↓
HOMOLOGAÇÃO
   ↓
PRODUÇÃO
```

Problemas encontrados em produção podem envolver investigação, suporte,
correção emergencial, novo deploy, rollback, indisponibilidade,
comunicação com clientes, prejuízo financeiro e perda de confiança.

> **Quanto mais cedo identificamos um defeito, menor tende a ser o
> impacto de sua correção.**

------------------------------------------------------------------------

# ⬅️ Shift Left Testing

Os testes não devem acontecer somente quando o sistema estiver pronto.

A abordagem **Shift Left Testing** procura aproximar as atividades
relacionadas à qualidade das primeiras etapas do desenvolvimento.

Em vez de:

``` text
DESENVOLVER → DESENVOLVER → DESENVOLVER → TESTAR
```

Buscamos:

``` text
DESENVOLVER
     ↕
  REVISAR
     ↕
   TESTAR
     ↕
  CORRIGIR
     ↕
   EVOLUIR
```

------------------------------------------------------------------------

# 🔎 Revisão × Teste

  -----------------------------------------------------------------------
  Revisão                             Teste
  ----------------------------------- -----------------------------------
  Analisa artefatos                   Avalia comportamentos

  Pode ocorrer sem executar código    Frequentemente envolve execução

  Procura defeitos antecipadamente    Procura falhas e comportamentos
                                      inadequados

  Pode analisar requisitos,           Valida comportamentos e
  arquitetura e código                características
  -----------------------------------------------------------------------

As duas práticas são complementares.

------------------------------------------------------------------------

# 👀 Revisões de Código

As revisões podem identificar erros de lógica, código duplicado, padrões
inadequados, problemas de legibilidade, vulnerabilidades, dificuldades
de manutenção e oportunidades de melhoria.

Além de melhorar o código, as revisões ajudam no **compartilhamento de
conhecimento da equipe**.

------------------------------------------------------------------------

# 👥 Peer Review

Na revisão por pares, outro desenvolvedor analisa uma alteração antes de
sua integração ao projeto.

``` text
DESENVOLVEDOR
      ↓
    COMMIT
      ↓
PULL REQUEST
      ↓
   REVISÃO
      ↓
AJUSTES / APROVAÇÃO
      ↓
     MERGE
```

Esse processo é comum em plataformas como GitHub e GitLab.

------------------------------------------------------------------------

# 📝 Técnicas de Revisão

## Inspeção

Processo formal e estruturado que pode envolver planejamento, critérios,
papéis definidos, checklist, registro de defeitos e acompanhamento das
correções.

É especialmente importante quando **controle e rastreabilidade** são
necessários.

## 🚶 Walkthrough

O próprio autor apresenta o código, requisito ou solução para outros
integrantes da equipe.

O objetivo é explicar decisões, discutir soluções, encontrar problemas,
compartilhar conhecimento e alinhar entendimento.

> **Palavra-chave: Discussão**

## 👨‍💻 Pair Programming

Na programação em par existem dois papéis principais:

**Driver:** responsável pela implementação imediata do código.

**Navigator:** observa, revisa, questiona decisões e pensa nos próximos
passos.

``` text
DRIVER + NAVIGATOR
        ↓
DESENVOLVIMENTO
        ↓
REVISÃO CONTÍNUA
```

------------------------------------------------------------------------

# 🏗️ Níveis de Teste

``` text
             ACEITAÇÃO
                ▲
              SISTEMA
                ▲
            INTEGRAÇÃO
                ▲
             UNITÁRIO
```

Cada nível procura responder perguntas diferentes sobre o software.

------------------------------------------------------------------------

# 1️⃣ Testes Unitários

Testam pequenas unidades do código.

``` python
def calcular_desconto(valor, percentual):
    return valor - (valor * percentual / 100)

assert calcular_desconto(100, 10) == 90
```

Características:

-   rápidos;
-   isolados;
-   automatizáveis;
-   executados frequentemente;
-   importantes para refatoração;
-   úteis para detectar regressões.

------------------------------------------------------------------------

# 2️⃣ Testes de Integração

Verificam se componentes diferentes conseguem trabalhar corretamente
juntos.

``` text
FRONT-END
    ↓
   API
    ↓
 SERVICE
    ↓
BANCO DE DADOS
```

Podem avaliar APIs, bancos de dados, serviços, filas, microsserviços e
contratos entre componentes.

------------------------------------------------------------------------

# 3️⃣ Testes de Sistema

Avaliam o comportamento da aplicação completa.

``` text
LOGIN
  ↓
PRODUTO
  ↓
CARRINHO
  ↓
PAGAMENTO
  ↓
PEDIDO
  ↓
CONFIRMAÇÃO
```

Podem verificar fluxos completos, regras de negócio, requisitos
funcionais, requisitos não funcionais e comportamento próximo ao
ambiente real.

------------------------------------------------------------------------

# 4️⃣ Testes de Aceitação

Procuram responder:

> **O software realmente resolve o problema do negócio?**

Podem envolver cliente, usuário, Product Owner e analista de negócio.

Um sistema pode funcionar tecnicamente e ainda assim não entregar o
resultado que o negócio necessita.

------------------------------------------------------------------------

# 🔺 Pirâmide de Testes

``` text
              /\
             /E2E\
            /─────\
           /INTEGR.\
          /─────────\
         / UNITÁRIOS \
        /_____________\
```

**Muitos testes rápidos na base. Menos testes complexos no topo.**

------------------------------------------------------------------------

# ⚙️ Testes Funcionais

Respondem principalmente:

> **O que o sistema faz?**

Exemplos: login, cadastro, consulta, compra, pagamento, emissão de
relatório, recuperação de senha e cálculo de valores.

Sua principal referência são os **requisitos funcionais**.

------------------------------------------------------------------------

# 🚀 Testes Não Funcionais

Respondem principalmente:

> **Como o sistema se comporta?**

Podem avaliar desempenho, segurança, acessibilidade, confiabilidade,
compatibilidade, disponibilidade e usabilidade.

Um software pode possuir todas as funcionalidades solicitadas e ainda
apresentar baixa qualidade.

------------------------------------------------------------------------

# 👤 Teste Manual × 🤖 Teste Automatizado

  Manual                                Automatizado
  ------------------------------------- ---------------------------------
  Executado por uma pessoa              Executado por script/ferramenta
  Flexível                              Repetível
  Excelente para exploração             Excelente para regressão
  Depende de esforço em cada execução   Pode executar continuamente

> **Automação não elimina testes manuais.**

------------------------------------------------------------------------

# 🤖 Automação de Testes

``` text
ALTERAÇÃO NO CÓDIGO
        ↓
EXECUÇÃO AUTOMÁTICA
        ↓
      TESTES
        ↓
 PASSOU / FALHOU
        ↓
     FEEDBACK
```

Entre os principais benefícios estão velocidade, repetibilidade,
feedback rápido, testes de regressão e integração contínua.

------------------------------------------------------------------------

# 🧰 Ferramentas de Teste

  Ferramenta   Principal utilização
  ------------ --------------------------
  JUnit        Testes unitários em Java
  pytest       Testes em Python
  Selenium     Automação Web
  Cypress      Testes Web / E2E
  Postman      Testes de APIs
  JMeter       Desempenho e carga

> **Primeiro definimos o que queremos avaliar. Depois escolhemos a
> ferramenta.**

------------------------------------------------------------------------

# 🔁 Testes no CI/CD

``` text
DESENVOLVEDOR
      ↓
    COMMIT
      ↓
     BUILD
      ↓
TESTES AUTOMÁTICOS
      ↓
   APROVADO?
    ↙    ↘
  NÃO    SIM
   ↓      ↓
PARAR   DEPLOY
```

O pipeline pode executar automaticamente testes unitários, testes de
integração, análise estática, verificações de segurança e validações de
qualidade.

------------------------------------------------------------------------

# ⚠️ Automatizar não garante qualidade

Também é possível automatizar testes ruins.

Um teste automatizado pode testar o cenário errado, possuir uma
expectativa incorreta, ignorar situações importantes, não representar o
requisito, gerar falsos positivos ou tornar-se difícil de manter.

> **Automação aumenta a velocidade da estratégia de testes --- seja ela
> boa ou ruim.**

------------------------------------------------------------------------

# 📊 Métricas de Testes

Alguns indicadores:

-   cobertura de código;
-   quantidade de testes;
-   taxa de sucesso;
-   defeitos encontrados;
-   defeitos em produção;
-   tempo médio de correção;
-   densidade de defeitos;
-   duração da suíte de testes.

------------------------------------------------------------------------

# 📈 Cobertura de Código

``` text
1.000 linhas relevantes
        ↓
800 executadas pelos testes
        ↓
Cobertura = 80%
```

> **100% de cobertura ≠ 100% de qualidade**

Cobertura indica que determinada parte do código foi executada durante
os testes. Não garante que todas as regras foram corretamente
verificadas.

------------------------------------------------------------------------

# 🐛 Defeitos Encontrados

  Sprint       Defeitos
  ---------- ----------
  Sprint 1           25
  Sprint 2           18
  Sprint 3           11
  Sprint 4            8

Os defeitos diminuíram. A qualidade melhorou?

**Talvez.**

Também pode ter ocorrido redução na quantidade de testes, testes
superficiais, menor quantidade de funcionalidades ou alteração na forma
de registrar defeitos.

> **Uma métrica isolada pode enganar.**

------------------------------------------------------------------------

# 🚨 Defeitos Pós-Produção --- Defect Leakage

São defeitos que escaparam do processo de qualidade.

``` text
DESENVOLVIMENTO
      ↓
    TESTES
      ↓
 HOMOLOGAÇÃO
      ↓
  PRODUÇÃO
      ↓
   DEFEITO!
```

Muitos defeitos encontrados em produção podem indicar cobertura
inadequada, ambientes diferentes, requisitos mal compreendidos, ausência
de determinados testes ou cenários importantes não considerados.

------------------------------------------------------------------------

# ⏱️ MTTR --- Mean Time to Repair/Restore

Qualidade também envolve **capacidade de recuperação**.

``` text
Falha detectada
     14:00
       ↓
   CORREÇÃO
       ↓
Sistema recuperado
     16:30

MTTR = 2h30
```

> **Quando ocorrer uma falha, quanto tempo levamos para restaurar o
> serviço?**

------------------------------------------------------------------------

# 📊 Dashboard de Qualidade

  Indicador                Resultado
  ---------------------- -----------
  Cobertura                      82%
  Testes automatizados           850
  Taxa de sucesso                96%
  Defeitos abertos                18
  Defeitos em produção             4
  MTTR                            2h

A interpretação deve considerar tendência, histórico, metas, contexto,
criticidade e relacionamento entre indicadores.

> Cobertura aumentando enquanto defeitos em produção também aumentam
> pode indicar que estamos **testando muito, mas talvez testando as
> coisas erradas**.

------------------------------------------------------------------------

# ♻️ Melhoria Contínua

``` text
REVISAR
   ↓
TESTAR
   ↓
MEDIR
   ↓
ANALISAR
   ↓
MELHORAR
   ↓
REVISAR...
```

**Revisar:** prevenir problemas.\
**Testar:** descobrir problemas.\
**Medir:** produzir evidências.\
**Analisar:** compreender os resultados.\
**Melhorar:** transformar conhecimento em evolução.

> **Qualidade é um processo contínuo.**

------------------------------------------------------------------------

# 🧱 A Qualidade é Construída em Camadas

``` text
             QUALIDADE
                 ▲
              ACEITAÇÃO
                 ▲
               SISTEMA
                 ▲
             INTEGRAÇÃO
                 ▲
              UNITÁRIOS
                 ▲
              REVISÕES
                 ▲
          BOAS PRÁTICAS
                 ▲
             REQUISITOS
```

Construímos confiança progressivamente.

Qualidade é resultado da combinação de **pessoas, processos, práticas,
ferramentas, testes, métricas e decisões**.

------------------------------------------------------------------------

# 🏁 Conclusão

## Revisar → Testar → Medir → Evoluir

> **Não testamos software apenas para encontrar erros.**

> **Testamos para produzir evidências, reduzir riscos e aumentar a
> confiança naquilo que entregamos.**

``` text
REVISÕES  → PREVINEM
TESTES    → DETECTAM
MÉTRICAS  → REVELAM
MELHORIA  → TRANSFORMA
```

Qualidade não é responsabilidade exclusiva da equipe de QA.

**Desenvolvedores → Arquitetos → Analistas → Product Owners → QA/Testers
→ Usuários**

------------------------------------------------------------------------

## 💡 Mensagem Final

> **O objetivo da Engenharia de Software não é provar que o sistema
> nunca falhará. É construir evidências suficientes para que possamos
> entregar, operar e evoluir o software com um nível de risco conhecido
> e aceitável.**

------------------------------------------------------------------------

# 🧪 Próxima Etapa --- Laboratório

``` text
SISTEMA COM DEFEITOS
        ↓
REVISÃO DE CÓDIGO
        ↓
TESTE UNITÁRIO
        ↓
TESTE DE INTEGRAÇÃO / API
        ↓
AUTOMAÇÃO
        ↓
COBERTURA
        ↓
MÉTRICAS
        ↓
DASHBOARD DE QUALIDADE
```

O objetivo será transformar os conceitos apresentados nesta aula em
**evidências reais de qualidade de software**.

------------------------------------------------------------------------

## 📚 Disciplina

**Qualidade de Software**

**Professor Rodolfo Terra**

🔗 LinkedIn: https://www.linkedin.com/in/rodolffoterra/\
💻 GitHub: https://github.com/rodolffoterra

------------------------------------------------------------------------

### ⭐ Sobre este material

Este repositório possui finalidade **educacional**, sendo utilizado como
material de apoio para aulas e atividades práticas relacionadas à
Engenharia e Qualidade de Software.

Se este conteúdo foi útil para seus estudos, considere deixar uma ⭐ no
repositório.
