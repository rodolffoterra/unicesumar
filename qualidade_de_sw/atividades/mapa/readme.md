# MAPA — Qualidade de Software

## Questão 01 — Proposta de Melhoria da Qualidade de Software

### Contexto

A qualidade de software é um fator essencial para o sucesso de qualquer sistema. Durante a disciplina, foram estudados conceitos relacionados à qualidade do produto e do processo, modelos de maturidade, normas internacionais, métricas, testes, garantia da qualidade, experiência do usuário e tendências atuais, como DevOps e Inteligência Artificial.

No cenário apresentado, uma empresa está desenvolvendo um sistema web para gerenciamento de clínicas médicas. Após seis meses de desenvolvimento, foram identificados diversos problemas relacionados à qualidade do software e aos processos utilizados pela empresa.

Os principais problemas observados são:

- Usuários relatam dificuldades para utilizar algumas funcionalidades.
- O sistema apresenta lentidão nos horários de maior acesso.
- Existem muitos defeitos encontrados após a implantação.
- Não existe um processo formal de revisão de código.
- Os testes são executados apenas manualmente ao final do projeto.
- Não há indicadores para medir a qualidade do software.
- A empresa deseja melhorar seus processos de desenvolvimento.

A seguir, é apresentada uma proposta de melhoria baseada nos conceitos estudados na disciplina.

---

## a) Identificação de quatro problemas de qualidade

### 1. Problemas de usabilidade

Os usuários relatam dificuldades para utilizar algumas funcionalidades do sistema. Isso demonstra um problema relacionado à **usabilidade e à experiência do usuário (UX)**.

Um sistema de qualidade deve permitir que seus usuários compreendam e executem suas tarefas de forma eficiente. A dificuldade de utilização pode aumentar a quantidade de erros, gerar insatisfação e reduzir a produtividade dos profissionais das clínicas.

Para solucionar esse problema, é importante realizar testes de usabilidade, entrevistas com usuários, avaliação da interface e melhorias na navegação e organização das funcionalidades.

### 2. Problemas de desempenho

O sistema apresenta lentidão nos horários de maior acesso, caracterizando um problema de **eficiência de desempenho**.

Esse problema pode estar relacionado ao banco de dados, aos algoritmos utilizados, à infraestrutura ou à quantidade de usuários simultâneos.

Para identificar e corrigir os gargalos, devem ser realizados testes de desempenho e monitoramento do sistema, principalmente nos períodos de maior utilização.

### 3. Grande quantidade de defeitos após a implantação

A existência de muitos defeitos encontrados somente depois da implantação demonstra falhas no processo de **testes e garantia da qualidade**.

Como os testes são realizados apenas manualmente no final do projeto, muitos problemas podem não ser identificados antes da disponibilização do sistema aos usuários.

Uma abordagem mais adequada seria realizar testes continuamente durante o desenvolvimento, incluindo testes automatizados, testes de integração e testes de regressão.

### 4. Ausência de processos formais de qualidade

A empresa não possui um processo formal de revisão de código, não utiliza indicadores de qualidade e executa os testes somente ao final do projeto.

Isso demonstra uma deficiência relacionada ao **processo de desenvolvimento e à garantia da qualidade de software**.

A ausência de processos definidos dificulta a identificação antecipada de problemas e impede que a empresa acompanhe de forma objetiva a evolução da qualidade do sistema.

---

## b) Cinco ações para aumentar a qualidade do software

### 1. Implantar revisão de código

A empresa deve estabelecer um processo formal de **revisão de código**, no qual as alterações realizadas pelos desenvolvedores sejam analisadas por outros integrantes da equipe antes de serem incorporadas ao sistema.

A revisão pode ajudar a identificar:

- Erros de implementação;
- Problemas de segurança;
- Código duplicado;
- Falhas de padronização;
- Problemas de manutenção;
- Possíveis impactos em outras funcionalidades.

Além de melhorar a qualidade do código, essa prática favorece o compartilhamento de conhecimento entre os integrantes da equipe.

### 2. Implantar testes automatizados

Os testes não devem ser executados somente de forma manual e no final do projeto.

A empresa deve criar uma estratégia de testes automatizados, incluindo testes unitários, testes de integração e testes de regressão.

A automação permite executar os testes com maior frequência e identificar rapidamente quando uma alteração introduziu um novo defeito.

Isso contribui para reduzir a quantidade de problemas encontrados após a implantação.

### 3. Utilizar integração e entrega contínuas (CI/CD)

A adoção de práticas de **Integração Contínua (CI)** e **Entrega Contínua (CD)** pode melhorar significativamente o processo de desenvolvimento.

Sempre que uma alteração for realizada, o sistema pode executar automaticamente etapas como:

1. Compilação;
2. Análise do código;
3. Execução dos testes automatizados;
4. Verificação de qualidade;
5. Geração de uma versão para homologação ou implantação.

Dessa maneira, os problemas podem ser identificados mais cedo, reduzindo o risco de falhas em produção.

### 4. Implantar métricas e monitoramento

A empresa deve definir indicadores para acompanhar objetivamente a qualidade do sistema.

Algumas informações que podem ser acompanhadas são:

- Quantidade de defeitos;
- Cobertura de testes;
- Tempo de resposta;
- Taxa de falhas em produção;
- Tempo médio para correção;
- Satisfação dos usuários;
- Disponibilidade do sistema.

O acompanhamento contínuo permite identificar tendências e verificar se as ações de melhoria estão produzindo resultados.

### 5. Melhorar a experiência do usuário

A empresa deve envolver os usuários durante o processo de desenvolvimento, principalmente porque já existem reclamações relacionadas à utilização do sistema.

Podem ser realizadas:

- Entrevistas com usuários;
- Testes de usabilidade;
- Avaliações de interface;
- Protótipos;
- Pesquisas de satisfação;
- Análise das principais dificuldades encontradas pelos usuários.

A participação dos usuários ajuda a garantir que o sistema esteja alinhado às necessidades reais das clínicas e dos profissionais que utilizarão a aplicação.

---

## c) Aplicação da ISO/IEC 25010

Entre os modelos e normas estudados, pode ser utilizada a **ISO/IEC 25010**, que apresenta características e subcaracterísticas para avaliação da qualidade de produtos de software.

A aplicação da ISO/IEC 25010 pode ajudar a empresa a definir requisitos de qualidade e estabelecer critérios objetivos para avaliar o sistema.

No cenário apresentado, algumas características são especialmente relevantes.

### Adequação funcional

O sistema deve fornecer as funcionalidades necessárias para atender às necessidades das clínicas médicas.

Além de verificar se uma funcionalidade existe, é necessário avaliar se ela realmente atende ao objetivo para o qual foi desenvolvida.

### Eficiência de desempenho

Essa característica está diretamente relacionada ao problema de lentidão apresentado nos horários de maior acesso.

A empresa pode estabelecer requisitos relacionados ao tempo de resposta e à utilização de recursos, realizando testes de desempenho para verificar se esses requisitos estão sendo atendidos.

### Usabilidade

A usabilidade pode ser utilizada para avaliar as dificuldades relatadas pelos usuários.

A empresa pode definir critérios relacionados à facilidade de aprendizagem, compreensão e utilização das funcionalidades.

Testes de usabilidade e avaliações com usuários podem complementar essa análise.

### Confiabilidade

A quantidade de defeitos encontrados após a implantação indica a necessidade de melhorar a confiabilidade do sistema.

A empresa pode utilizar testes automatizados, testes de regressão e monitoramento para reduzir a ocorrência de falhas em produção.

### Manutenibilidade

A ausência de revisão formal de código pode dificultar a manutenção do sistema.

A adoção de padrões de desenvolvimento, revisão de código, documentação e análise da estrutura do software pode contribuir para tornar o sistema mais fácil de corrigir e evoluir.

### Benefícios para a empresa

A aplicação da ISO/IEC 25010 permitiria transformar conceitos de qualidade em critérios que podem ser avaliados e acompanhados.

Em vez de considerar apenas se as funcionalidades estão funcionando, a empresa passaria a avaliar também aspectos como desempenho, usabilidade, confiabilidade e manutenibilidade.

Dessa forma, a norma pode servir como referência para definir requisitos de qualidade, estabelecer critérios de testes e criar indicadores para acompanhar a evolução do software.

---

## d) Três métricas para acompanhar a evolução da qualidade

### 1. Cobertura de testes

A **cobertura de testes** indica a porcentagem do código ou das funcionalidades que é exercitada pelos testes automatizados.

Por exemplo, se uma aplicação possui 80% de cobertura de testes, significa que uma parcela significativa do código está sendo verificada automaticamente.

Essa métrica é importante porque permite acompanhar a evolução da automação dos testes e identificar áreas do sistema que ainda possuem pouca ou nenhuma cobertura.

Entretanto, uma cobertura elevada não garante sozinha a ausência de defeitos. É necessário que os testes também sejam adequados e relevantes.

### 2. Densidade de defeitos

A **densidade de defeitos** relaciona a quantidade de defeitos encontrados com o tamanho do software, podendo ser calculada, por exemplo, considerando a quantidade de defeitos por mil linhas de código ou por determinada quantidade de funcionalidades.

Essa métrica permite acompanhar a quantidade de problemas encontrados ao longo do desenvolvimento.

Se a densidade de defeitos diminuir ao longo do tempo, isso pode indicar uma melhoria no processo de desenvolvimento e testes.

Também é importante analisar em qual etapa os defeitos foram encontrados, principalmente para verificar quantos chegaram à produção.

### 3. Tempo Médio para Correção (MTTR)

O **MTTR (Mean Time to Repair/Resolve)** representa o tempo médio necessário para solucionar uma falha ou incidente.

Essa métrica é importante porque não basta apenas identificar os problemas. A equipe também precisa ser capaz de corrigi-los em tempo adequado.

A empresa pode acompanhar o MTTR ao longo do tempo para verificar a eficiência do processo de tratamento de defeitos.

Uma redução do tempo necessário para resolver problemas pode indicar melhorias nos processos de diagnóstico, desenvolvimento, testes e implantação.

---

## Plano de melhoria proposto

Com base nos problemas identificados, a empresa poderia implementar o seguinte processo de melhoria:

```text
Identificação dos requisitos
          ↓
Definição dos requisitos de qualidade
          ↓
Desenvolvimento
          ↓
Revisão de código
          ↓
Testes automatizados
          ↓
Integração Contínua (CI)
          ↓
Testes de desempenho e segurança
          ↓
Homologação com usuários
          ↓
Implantação
          ↓
Monitoramento em produção
          ↓
Coleta de métricas
          ↓
Análise dos resultados
          ↓
Melhoria contínua
