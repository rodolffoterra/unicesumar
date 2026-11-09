# Aula 02 — Ameaças, Ataques e Fundamentos de Segurança Cibernética

**Disciplina:** Ethical Hacker  
**Instituição:** UniCesumar  
**Professor:** Rodolfo Terra  
**Duração:** 90 minutos  
**Modalidade:** Aula expositiva dialogada, com exemplos e situação-problema

> **Questão norteadora:** Contra o que estamos nos protegendo e como podemos reduzir os riscos?

## 📺 Gravação da aula

**YouTube — Aula 02:** *https://www.youtube.com/watch?v=Ed_8jx943Po*

## 🎯 Objetivos de aprendizagem

Ao final da aula, espera-se que o estudante consiga:

- Diferenciar **ameaça, vulnerabilidade, ataque, impacto e risco**.
- Reconhecer os principais tipos de **malware** e suas consequências.
- Identificar fragilidades técnicas, humanas e organizacionais.
- Relacionar incidentes à **confidencialidade, integridade e disponibilidade (Tríade CIA)**.
- Explicar os efeitos dos incidentes sobre pessoas e organizações.
- Compreender a função das **Políticas de Segurança da Informação (PSI)**.
- Reconhecer a importância da integração entre **pessoas, processos e tecnologia**.
- Identificar etapas e estratégias de **gerenciamento contínuo de riscos**.
---

## Bloco 1 — Retomada e conceitos fundamentais

A aula começa retomando a **Tríade CIA**, estudada na Aula 01:

| Princípio | Pergunta central | Exemplo de comprometimento |
|---|---|---|
| **Confidencialidade** | Quem pode acessar a informação? | Exposição indevida de dados pessoais |
| **Integridade** | A informação permanece correta? | Alteração não autorizada de valores |
| **Disponibilidade** | O serviço está acessível quando necessário? | Sistema fora do ar durante uma operação crítica |

**Ponto-chave:** diferentes incidentes podem afetar um ou vários desses princípios.

## Bloco 2 — Ameaças, vulnerabilidades, ataques e riscos

### Conceitos essenciais

| Conceito | Definição didática | Exemplo |
|---|---|---|
| **Ameaça** | Fonte ou circunstância com potencial de causar dano | Ator malicioso, malware ou evento físico |
| **Vulnerabilidade** | Fragilidade que pode ser explorada | Senha fraca ou sistema desatualizado |
| **Ataque** | Ação que busca explorar uma fragilidade ou comprometer um ativo | Tentativa de acesso indevido |
| **Impacto** | Consequência de um incidente | Paralisação, perda financeira ou exposição de dados |
| **Risco** | Possibilidade de consequências negativas, considerando incertezas e contexto | Indisponibilidade de um sistema crítico |

Uma forma **didática e simplificada** de analisar a prioridade de um risco é:

`Risco ≈ Probabilidade × Impacto`

Essa expressão auxilia o raciocínio inicial; avaliações formais também consideram contexto, exposição, controles existentes e critérios da organização.

### Exemplo: duas vulnerabilidades, riscos diferentes

Uma senha fraca em um sistema interno de baixa criticidade e outra em um sistema de pagamentos exposto à Internet não necessariamente representam o mesmo nível de risco. A prioridade depende da exposição, dos controles e das consequências potenciais.

### Analogia da casa

- **Ameaça:** pessoa com intenção de furtar na vizinhança.
- **Vulnerabilidade:** janela destrancada.
- **Ataque:** entrada indevida na residência.
- **Impacto:** furto de um computador.
- **Risco:** possibilidade de ocorrer esse prejuízo dadas as condições existentes.

## Bloco 3 — Malware e principais formas de ataque

### Malware não é sinônimo de vírus

**Malware** é o termo abrangente para software malicioso. **Vírus** é um tipo de malware, mas nem todo malware é um vírus.

| Tipo | Característica principal | Possíveis impactos |
|---|---|---|
| **Vírus** | Infecta arquivos ou programas e pode se replicar quando executado | Corrupção de arquivos e instabilidade |
| **Worm** | Pode se propagar automaticamente entre sistemas | Disseminação rápida e interrupção de serviços |
| **Trojan (cavalo de Troia)** | Apresenta-se como software legítimo para induzir sua execução | Acesso indevido e instalação de outras ameaças |
| **Spyware** | Monitora ou coleta informações sem autorização | Exposição de dados e perda de privacidade |
| **Ransomware** | Pode criptografar arquivos ou bloquear recursos para extorquir a vítima | Indisponibilidade, custos de recuperação e possível exposição de dados |

### Exemplo: incidente de ransomware

1. A organização opera normalmente.
2. Um software malicioso é executado, por exemplo, após um e-mail fraudulento ou exploração de vulnerabilidade.
3. Arquivos ou sistemas ficam inacessíveis.
4. Os criminosos exigem resgate, sem garantia de recuperação.
5. A empresa precisa acionar seus procedimentos de resposta e continuidade.

**Relação com a Tríade CIA:** a disponibilidade costuma ser diretamente afetada; a integridade e a confidencialidade também podem ser comprometidas conforme o incidente.

### Formas de ataque apresentadas

- **Ataques a credenciais:** tentativas de obter ou usar indevidamente dados de autenticação.
- **Engenharia social:** manipulação de pessoas para obter informações ou induzir ações.
- **Phishing:** mensagens ou páginas fraudulentas usadas para enganar vítimas.
- **Ataques a aplicações web:** exploração de falhas em aplicações e seus controles.
- **Ataques à disponibilidade:** ações que buscam interromper serviços, como negação de serviço.
- **Exploração de vulnerabilidades:** aproveitamento de falhas técnicas ou de configuração.

Essas categorias podem se sobrepor ou ser combinadas em um mesmo incidente.

## Bloco 4 — Pessoas, organizações e impactos

### O fator humano

Firewalls, antivírus, backups e atualizações são importantes, mas não eliminam riscos associados a mensagens fraudulentas, processos inadequados e decisões humanas. A proteção exige **treinamento, conscientização e mecanismos técnicos complementares**, como autenticação multifator (MFA).

### Riscos para pessoas

O comprometimento de uma conta de e-mail pode facilitar tentativas de acesso a redes sociais, serviços financeiros, comércio eletrônico e armazenamento em nuvem, especialmente quando há reutilização de senhas ou recuperação de contas por e-mail.

### Riscos para organizações

Um incidente pode gerar uma cadeia de consequências:

**Exposição de dados → Custos e perdas financeiras → Interrupção operacional → Perda de clientes → Danos à reputação**

A sequência é ilustrativa: os impactos não precisam ocorrer nessa ordem e nem todos os incidentes envolvem vazamento de dados.

### Exemplo: supermercado indisponível

Falhas nos caixas, pagamentos e sistemas de estoque podem provocar filas, perda de vendas e insatisfação de clientes. **Mesmo sem roubo de informações**, a indisponibilidade já pode representar um prejuízo significativo para o negócio.

## Bloco 5 — Políticas, conscientização e gerenciamento de riscos

### Política de Segurança da Informação (PSI)

A PSI estabelece regras, diretrizes, responsabilidades e comportamentos esperados para proteger as informações da organização. Exemplos abordados:

1. Política de senhas e autenticação.
2. Controle de acesso e permissões.
3. Uso e proteção de equipamentos.
4. Cópias de segurança e recuperação.
5. Resposta a incidentes.

**Criar uma política não significa estar seguro:** é necessário comunicar, treinar, aplicar, acompanhar e revisar as regras.

### Pessoas + Processos + Tecnologia

| Dimensão | Exemplos de controles |
|---|---|
| **Pessoas** | Treinamento, conscientização, responsabilidade e comunicação de incidentes |
| **Processos** | Políticas, gestão de acessos, gestão de riscos, resposta a incidentes e auditoria |
| **Tecnologia** | Firewall, antivírus, MFA, criptografia, backup, monitoramento e atualizações |

A eficácia depende da integração dessas dimensões, e não de uma ferramenta isolada.

### Ciclo de gerenciamento contínuo de riscos

**Identificar → Analisar → Tratar → Monitorar → Revisar → Identificar novamente**

- **Identificar:** reconhecer ativos, ameaças, vulnerabilidades e cenários.
- **Analisar:** estimar probabilidade, impacto e prioridade.
- **Tratar:** selecionar e implementar medidas.
- **Monitorar:** acompanhar indicadores, eventos e eficácia dos controles.
- **Revisar:** reavaliar decisões diante de mudanças e novas ameaças.

### Quatro estratégias de tratamento

| Estratégia | O que significa | Exemplo empresarial |
|---|---|---|
| **Aceitar** | Assumir conscientemente um risco dentro dos critérios definidos | Manter um risco residual de baixo impacto, com monitoramento |
| **Mitigar** | Reduzir a probabilidade ou o impacto | Implantar MFA para contas administrativas |
| **Eliminar / Evitar** | Deixar de realizar a atividade que origina determinado risco | Descontinuar um serviço legado desnecessário |
| **Transferir / Compartilhar** | Compartilhar consequências financeiras ou responsabilidades contratualmente | Contratar seguro cibernético ou serviço com garantias contratuais |

**Observação:** transferir ou compartilhar não elimina integralmente a responsabilidade nem o risco residual da organização.

## Bloco 6 — Situação-problema e encerramento

### Situação-problema: uma empresa protegida pode ser invadida?

Uma empresa possui **firewall, antivírus, backups e servidores atualizados**, mas não realiza treinamentos periódicos de segurança. Um colaborador recebe uma mensagem aparentemente legítima solicitando a atualização de suas credenciais e informa seus dados em uma página fraudulenta. Um atacante passa a ter condições de tentar acessar sistemas internos.

**Questões para reflexão:**

1. Onde estava a principal fragilidade desse cenário?
2. Quais riscos foram gerados?
3. Quais controles poderiam reduzir a probabilidade ou o impacto do incidente?
4. Por que a análise deve priorizar a melhoria dos controles em vez de buscar culpados?

<details>
<summary><strong>Resposta esperada — orientação para estudo</strong></summary>

A fragilidade envolvia conscientização insuficiente e procedimentos inadequados de verificação de solicitações, associados à necessidade de controles complementares. Os riscos incluem acesso indevido, exposição de informações, fraudes e interrupção de serviços. Treinamentos, campanhas de conscientização, MFA, processos de confirmação, monitoramento e canais de comunicação de suspeitas podem reduzir os riscos. A organização deve aprender com o incidente e fortalecer seus controles, sem depender de culpabilização individual.

</details>

### Mapa mental de revisão

```text
SEGURANÇA DA INFORMAÇÃO
├── Ameaças
├── Vulnerabilidades
├── Ataques
├── Impactos
├── Riscos
└── Gerenciamento contínuo
    ├── Identificar
    ├── Analisar
    ├── Tratar
    ├── Monitorar
    └── Revisar

Base de sustentação: PESSOAS + PROCESSOS + TECNOLOGIA
```

> **Mensagem principal:** Uma organização não está segura porque nunca foi atacada. Ela está mais segura quando conhece seus riscos, reduz suas vulnerabilidades, prepara suas pessoas e está pronta para responder quando um incidente acontecer.

## 📝 Revisão rápida

1. Qual é a diferença entre ameaça e vulnerabilidade?
2. Por que todo vírus é malware, mas nem todo malware é vírus?
3. Um incidente sem vazamento de dados pode prejudicar uma empresa? Explique.
4. Por que publicar uma política de segurança não é suficiente?
5. Como pessoas, processos e tecnologia se complementam?
6. Quais são as cinco etapas do gerenciamento contínuo de riscos?
7. Em que situações uma organização pode aceitar, mitigar, evitar ou compartilhar um risco?

## 📚 Materiais e referências

- **Livro da disciplina Ethical Hacker:** disponível no ambiente virtual de aprendizagem da UniCesumar.
- **Slides da Aula 02:** *https://github.com/rodolffoterra/unicesumar/blob/main/ethical_hacker/aula_02_ameacas_ataques_fund_de_seg_cib/ethical_hacker_aula_02.pdf*.
- **Vídeo da Aula 02:** *https://www.youtube.com/watch?v=Ed_8jx943Po*.
- **NIST Cybersecurity Framework (CSF) 2.0:** https://www.nist.gov/cyberframework
- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **CERT.br — Cartilha de Segurança para Internet:** https://cartilha.cert.br/

Os recursos externos são indicações de aprofundamento; não substituem o material oficial da disciplina.

---

## 👨‍🏫 Professor

**Rodolfo Terra**  
**Disciplina:** Ethical Hacker — UniCesumar  
**LinkedIn:** [linkedin.com/in/rodolffoterra/](https://www.linkedin.com/in/rodolffoterra/)  
**GitHub:** [github.com/rodolffoterra](https://github.com/rodolffoterra)

> Material didático para fins educacionais. Testes de segurança em sistemas de terceiros exigem autorização válida e respeito ao escopo definido.
