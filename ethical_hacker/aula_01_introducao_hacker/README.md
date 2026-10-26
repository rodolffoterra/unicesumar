# Ethical Hacker — Aula 01: Introdução ao Hacking Ético

<p align="center">
  <strong>UniCesumar | Disciplina: Ethical Hacker</strong><br>
  <strong>Professor Rodolfo Terra</strong><br>
  <a href="https://www.linkedin.com/in/rodolffoterra/">LinkedIn: /in/rodolffoterra/</a> ·
  <a href="https://github.com/rodolffoterra">GitHub: github.com/rodolffoterra</a>
</p>

> **Aula 01 | Duração: 90 minutos | Modalidade: aula expositiva dialogada com situações-problema**

## 📌 Apresentação

Esta aula introduz os fundamentos da **Segurança da Informação** e do **Hacking Ético**, conectando situações do cotidiano de empresas e instituições à atuação responsável de profissionais de segurança. O foco é compreender **o que proteger, por que proteger, como reconhecer incidentes e quais limites éticos e legais orientam testes de segurança**.

O conteúdo está organizado em seis blocos, do cenário digital à reflexão sobre responsabilidades profissionais. Não há exploração prática de sistemas nesta aula introdutória.

## 🎯 Objetivos de aprendizagem

Ao final da aula, o estudante deverá ser capaz de:

1. Explicar por que a informação é um ativo relevante para organizações.
2. Diferenciar **confidencialidade, integridade e disponibilidade** em cenários reais.
3. Distinguir os conceitos de **Hacker, Cracker, Ethical Hacker, White Hat e Black Hat**.
4. Reconhecer a importância da **autorização formal** e do **escopo** antes de testes de segurança.
5. Descrever, em nível introdutório, as etapas de um **Pentest** e a função de um relatório técnico.
6. Analisar dilemas profissionais envolvendo documentação, transparência, confidencialidade e limites legais.

## 🧠 Competências e habilidades

**Competências priorizadas:** pensamento crítico, resolução de problemas, tomada de decisão, ética profissional e comunicação técnica.

**Habilidades desenvolvidas:** classificar incidentes pela tríade CIA; interpretar situações de acesso indevido e indisponibilidade; reconhecer limites de um Pentest; relacionar achados, riscos e recomendações; avaliar condutas éticas em cenários organizacionais.

---

## 🔵 Bloco 01 — Introdução e cenário digital

### Por que a informação precisa ser protegida?

A informação é um **ativo organizacional**. Seu acesso indevido, sua alteração ou sua indisponibilidade podem causar impactos financeiros, operacionais, jurídicos e reputacionais.

| Setor | Exemplos de informações e ativos |
|---|---|
| Banco | Saldos, dados de clientes e transações |
| Hospital | Prontuários, exames e agendamentos |
| Comércio | Preços, vendas, estoque e dados de clientes |
| Universidade | Notas, matrículas e registros acadêmicos |

### Situação-problema: um supermercado, três incidentes

- Um funcionário acessa dados financeiros sem autorização.
- Um preço de **R$ 100,00** é alterado indevidamente para **R$ 1,00**.
- O sistema de vendas fica indisponível no sábado.

**Pergunta norteadora:** os três acontecimentos representam o mesmo tipo de falha de segurança?

A resposta conduz aos três pilares da Segurança da Informação.

## 🔵 Bloco 02 — Confidencialidade, Integridade e Disponibilidade

A **tríade CIA** reúne três princípios fundamentais:

| Princípio | Pergunta-chave | Exemplo de comprometimento | Controles relacionados |
|---|---|---|---|
| **Confidencialidade** (*Confidentiality*) | Quem pode acessar? | Visualização indevida de folha salarial | Autorização, permissões, MFA e proteção de dados |
| **Integridade** (*Integrity*) | A informação continua correta? | Preço de picanha alterado de R$ 89,90 para R$ 0,89 | Permissões, logs, validações e mecanismos de verificação |
| **Disponibilidade** (*Availability*) | O sistema está acessível quando necessário? | E-commerce fora do ar durante a Black Friday | Redundância, monitoramento, recuperação e proteção contra indisponibilidade |

### Autenticação × autorização

- **Autenticação:** verifica a identidade de quem tenta acessar o sistema.
- **Autorização:** determina o que a identidade autenticada pode consultar ou executar.

Uma pessoa pode estar autenticada e, ainda assim, **não ter permissão** para acessar determinada informação.

### Exercício de fixação

Identifique o princípio principalmente afetado:

1. Um invasor visualizou dados sigilosos, mas não alterou nada.
2. O saldo de uma conta foi modificado indevidamente.
3. O sistema acadêmico ficou inacessível durante a matrícula.

<details>
<summary><strong>Ver respostas comentadas</strong></summary>

1. **Confidencialidade:** houve acesso não autorizado à informação.
2. **Integridade:** o valor registrado deixou de representar a informação correta.
3. **Disponibilidade:** o serviço deixou de estar acessível aos usuários.

**Atenção:** um incidente real pode afetar mais de um princípio simultaneamente.
</details>

## 🔵 Bloco 03 — Conceitos e classificações de hackers

### Afinal, todo hacker é criminoso?

**Não.** O conhecimento técnico não determina, isoladamente, se uma atividade é ética ou ilegal. A atuação deve ser analisada considerando **autorização, finalidade, conduta e limites**.

Entre as características associadas à investigação técnica estão curiosidade, análise de sistemas, identificação de falhas e resolução de problemas.

| Termo | Descrição no contexto da aula |
|---|---|
| **Hacker** | Pessoa com conhecimentos técnicos para investigar e compreender sistemas. |
| **Cracker** | Termo utilizado no material da disciplina para quem compromete sistemas de forma maliciosa. |
| **Ethical Hacker** | Profissional que emprega técnicas de segurança ofensiva com autorização e finalidade defensiva. |
| **White Hat** | Perfil de atuação autorizada, com limites definidos e objetivo de fortalecer a segurança. |
| **Black Hat** | Perfil de atuação maliciosa ou não autorizada, visando comprometer sistemas ou dados. |

### A mesma técnica, duas finalidades

Uma técnica de análise de vulnerabilidades pode fazer parte de um **teste autorizado**, com documentação e recomendações, ou ser empregada em uma **exploração indevida**. A técnica, por si só, não torna uma ação legítima.

**Ideia central:** habilidade técnica não substitui autorização.

## 🔵 Bloco 04 — Autorização, escopo e Pentest

### Boa intenção não substitui autorização

Se um estudante encontra uma possível vulnerabilidade no site de uma empresa, isso **não o autoriza a explorá-la** para demonstrar sua existência. A atividade de teste deve estar previamente autorizada e limitada ao que foi acordado.

### O que é escopo?

O **escopo** documenta os limites de uma avaliação de segurança. Deve contemplar, conforme o caso:

- Sistemas, aplicações e endereços autorizados.
- Técnicas e atividades permitidas.
- Atividades expressamente proibidas.
- Datas, horários e janelas de execução.
- Responsáveis e contatos para incidentes.
- Critérios de interrupção e entregáveis esperados.

Uma autorização genérica **não significa liberdade irrestrita**.

### O que é um Pentest?

**Penetration Test (teste de invasão)** é uma avaliação autorizada que simula determinadas ações de um atacante para identificar e, quando permitido, demonstrar vulnerabilidades em um ambiente delimitado.

**Identificar uma possível falha** é diferente de **comprovar sua exploração**: a validação deve respeitar as permissões e os limites estabelecidos.

### Etapas introdutórias de um Pentest

```text
01 Autorização
       ↓
02 Definição do escopo
       ↓
03 Avaliação
       ↓
04 Validação (quando permitida)
       ↓
05 Relatório de achados
       ↓
06 Recomendações
```

### Exemplo fictício de achado técnico

| Campo | Descrição |
|---|---|
| **Achado** | Autenticação sem MFA |
| **Sistema** | Portal administrativo de uma empresa fictícia |
| **Risco** | Maior exposição a acessos indevidos caso credenciais sejam comprometidas |
| **Recomendação** | Implementar autenticação multifator nas contas administrativas |

O objetivo do relatório não é demonstrar capacidade de invasão, mas **apoiar a redução de riscos**.

## 🔵 Bloco 05 — Responsabilidades, ética e legalidade

### O papel do Ethical Hacker na organização

As vulnerabilidades não se limitam ao código-fonte. Elas podem surgir em quatro frentes:

| Origem | Exemplos |
|---|---|
| **Software** | Falhas de desenvolvimento e validação insuficiente |
| **Configurações** | Permissões excessivas e serviços mal configurados |
| **Processos** | Políticas insuficientes e controles mal definidos |
| **Pessoas** | Erros humanos e comportamentos de risco |

### Identificar não é o mesmo que corrigir

**Hacker ético:** avalia, identifica, documenta e recomenda.

**Equipe responsável:** prioriza, planeja, implementa e valida as correções.

A participação do profissional na remediação ou em novos testes depende do **contrato e do escopo**.

### Seis princípios éticos

1. **Confidencialidade:** proteger informações obtidas durante o trabalho.
2. **Respeito ao escopo:** executar somente atividades autorizadas.
3. **Responsabilidade:** evitar danos e agir de forma controlada.
4. **Documentação:** registrar atividades, evidências e achados.
5. **Imparcialidade:** comunicar os resultados com objetividade.
6. **Respeito às pessoas:** identificar problemas sem buscar culpados.

### Legalidade e limites profissionais

A atuação deve considerar quatro dimensões conectadas: **legislação, contrato, políticas organizacionais e escopo**.

No contexto brasileiro, a proteção de dados pessoais e os riscos de acesso indevido a sistemas exigem atenção à legislação aplicável, incluindo, quando pertinente, a **LGPD** e disposições do **Código Penal**. Esta aula faz uma contextualização introdutória, não uma análise jurídica aprofundada.

## 🔵 Bloco 06 — Discussão e encerramento

### Síntese dos aprendizados

- A Segurança da Informação protege ativos essenciais ao negócio.
- Confidencialidade, integridade e disponibilidade representam impactos distintos, mas relacionados.
- Conhecimento técnico não define, por si só, uma conduta ética.
- Pentests exigem autorização válida, escopo e comunicação responsável.
- A documentação dos achados deve ser fiel, objetiva e confidencial.

### Questões de revisão

1. Qual é a diferença entre autenticação e autorização?
2. Uma alteração indevida de preço compromete qual princípio da tríade CIA?
3. Por que a boa intenção não autoriza um teste em sistemas de terceiros?
4. O que deve constar no escopo de um Pentest?
5. Quem é responsável pela correção de uma vulnerabilidade encontrada?
6. Por que a imparcialidade é indispensável no relatório técnico?

---

## 📚 Estudo de caso extraclasse — O relatório que ninguém quer receber

### Cenário

Durante um **Pentest autorizado** em uma empresa fictícia, um hacker ético identifica vulnerabilidades graves. O gerente de TI pede que algumas delas sejam **omitidas do relatório** para evitar problemas com a diretoria.

**Questão central:** qual deve ser a postura do profissional?

### Orientações para análise

Considere a integridade do relatório, a responsabilidade profissional, a confidencialidade dos achados e os canais de comunicação definidos contratualmente.

<details>
<summary><strong>Ver proposta de solução comentada</strong></summary>

O Ethical Hacker deve **recusar a omissão de vulnerabilidades relevantes**, preservar as evidências e apresentar os achados com clareza, imparcialidade, classificação de riscos e recomendações. A comunicação deve ocorrer **somente pelos canais autorizados**, seguindo o contrato e, quando necessário, os procedimentos formais de escalonamento.

A finalidade do trabalho é apoiar a segurança da organização, não proteger a imagem de gestores nem atribuir culpa a pessoas.

**Critérios esperados:** ética profissional, integridade, responsabilidade, confidencialidade e respeito aos procedimentos contratuais.
</details>

**Reflexão adicional:** quais seriam as consequências para a empresa e para a credibilidade do profissional se uma falha omitida fosse explorada posteriormente?

> **Mensagem central:** identificar e comunicar riscos com transparência é parte essencial do trabalho do Ethical Hacker.

## 🧑‍🏫 Metodologias e recursos

**Metodologias:** aula expositiva dialogada, situações-problema, discussão orientada e estudo de caso extraclasse.

**Recursos:** slides da Aula 01, apostila da disciplina, exercícios conceituais e material HTML do estudo de caso.

**Avaliação diagnóstica e formativa:** perguntas sobre conhecimentos prévios, interpretação dos cenários e participação nas discussões. As avaliações somativas seguem o planejamento institucional da disciplina.

## 🗂️ Estrutura sugerida do repositório

```text
ethical-hacker/
└── aula-01-introducao/
    ├── README.md
    ├── slides/
    │   └── aula-01-apresentacao.pdf
    ├── atividades/
    │   └── estudo-de-caso.html
    └── imagens/
        └── capa-aula-01.png
```

> **Nota:** a estrutura acima é uma sugestão. Adicione os arquivos correspondentes e ajuste os nomes conforme os materiais efetivamente publicados. Os links para arquivos locais só funcionarão após o envio desses arquivos ao repositório.

## 📖 Referências e materiais de apoio

- **UNICESUMAR.** *Ethical Hacker*. Material didático da disciplina disponibilizado no ambiente institucional. Consulte a edição utilizada para os dados bibliográficos completos.
- **BRASIL.** Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD). [Texto oficial](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).
- **BRASIL.** Decreto-Lei nº 2.848, de 7 de dezembro de 1940 — Código Penal. [Texto oficial](https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm).
- **OWASP.** *Web Security Testing Guide*. [Projeto oficial](https://owasp.org/www-project-web-security-testing-guide/). Material complementar para aprofundamento posterior.

## ⚖️ Aviso de uso responsável

Este material tem finalidade **exclusivamente educacional**. Os exemplos são fictícios ou conceituais. Não realize varreduras, tentativas de acesso ou exploração de vulnerabilidades em sistemas de terceiros sem autorização expressa e escopo definido. A utilização de técnicas de segurança deve respeitar a legislação, os contratos e as políticas aplicáveis.

---

## 👨‍🏫 Professor e contato

**Professor Rodolfo Terra**  
**Disciplina:** Ethical Hacker — UniCesumar  
**LinkedIn:** [linkedin.com/in/rodolffoterra/](https://www.linkedin.com/in/rodolffoterra/)  
**GitHub:** [github.com/rodolffoterra](https://github.com/rodolffoterra)

> *Segurança não é apenas identificar falhas: é agir com responsabilidade para reduzir riscos e proteger pessoas, dados e organizações.*
