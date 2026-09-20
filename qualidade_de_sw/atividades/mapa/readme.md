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

1. **Usabilidade:** os usuários apresentam dificuldades para utilizar algumas funcionalidades do sistema.

2. **Desempenho:** o sistema fica lento nos horários de maior acesso, prejudicando a utilização.

3. **Confiabilidade:** muitos defeitos são encontrados após a implantação, indicando falhas no processo de testes.

4. **Processo de desenvolvimento:** não existe revisão formal de código, os testes são realizados apenas manualmente no final do projeto e não existem indicadores de qualidade.

---

## b) Cinco ações para aumentar a qualidade do software

1. **Revisão de código:** realizar revisões antes de integrar alterações ao sistema, ajudando a identificar erros antecipadamente.

2. **Testes automatizados:** criar testes unitários, de integração e de regressão para encontrar defeitos durante o desenvolvimento.

3. **CI/CD:** utilizar integração e entrega contínuas para automatizar testes e etapas de implantação.

4. **Métricas de qualidade:** definir indicadores como cobertura de testes, quantidade de defeitos e tempo de correção.

5. **Melhoria da experiência do usuário:** realizar testes de usabilidade e coletar feedback dos usuários para melhorar a utilização do sistema.

---

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

A **ISO/IEC 25010** pode ser utilizada como referência para avaliar diferentes características da qualidade do software, como usabilidade, desempenho, confiabilidade e manutenibilidade.

No cenário apresentado, sua aplicação ajudaria a empresa a definir critérios de qualidade e verificar se o sistema atende aos requisitos esperados, não considerando apenas se suas funcionalidades estão funcionando.

---

## d) Três métricas para acompanhar a evolução da qualidade

1. **Cobertura de testes:** indica quanto do sistema está sendo verificado pelos testes automatizados. Ajuda a identificar partes que ainda precisam de testes.

2. **Densidade de defeitos:** permite acompanhar a quantidade de defeitos encontrados em relação ao tamanho do sistema, ajudando a identificar problemas recorrentes.

3. **MTTR (Tempo Médio para Correção):** mede o tempo necessário para corrigir falhas. É importante para avaliar a rapidez da equipe na resolução de problemas.

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
