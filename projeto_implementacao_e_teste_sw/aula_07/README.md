# 🧪 Aula 07 — Desenvolvimento Guiado por Testes (TDD)

## Projeto, Implementação e Teste de Software com Python

**Professor:** Rodolfo Terra  
**Projeto utilizado:** TechPort  
**Tema:** Test Driven Development — TDD

---

## 📚 Visão geral

Nesta aula, os testes deixam de ser utilizados apenas depois da implementação e passam a participar diretamente da construção do software.

A pergunta central é:

> **E se o teste fosse escrito antes do código?**

O foco não é reaprender `pytest`, testes unitários ou cobertura. Esses conhecimentos são utilizados como base para uma nova maneira de pensar o desenvolvimento:

```text
REQUISITO
   ↓
COMPORTAMENTO
   ↓
TESTE
   ↓
RED
   ↓
CÓDIGO
   ↓
GREEN
   ↓
REFACTOR
   ↓
EVOLUÇÃO
```

---

## 🎯 Objetivos de aprendizagem

Ao final da aula, espera-se que o aluno seja capaz de:

- compreender os fundamentos do **Test Driven Development — TDD**;
- diferenciar TDD do fluxo tradicional de desenvolvimento;
- aplicar o ciclo **RED → GREEN → REFACTOR**;
- transformar requisitos em comportamentos verificáveis;
- desenvolver funcionalidades incrementalmente;
- utilizar **Mocks** para isolar dependências;
- compreender a relação entre arquitetura e testabilidade;
- testar cenários válidos, inválidos e casos-limite;
- utilizar testes parametrizados;
- identificar regressões;
- compreender cobertura como uma métrica auxiliar de qualidade.

---

## 🔄 Da verificação para o desenvolvimento

Em uma abordagem tradicional, é comum encontrarmos:

```text
REQUISITO
   ↓
DESENVOLVIMENTO
   ↓
DESENVOLVIMENTO
   ↓
DESENVOLVIMENTO
   ↓
TESTES
```

O TDD propõe ciclos menores:

```text
COMPORTAMENTO
      ↓
    TESTE
      ↓
     RED
      ↓
IMPLEMENTAÇÃO MÍNIMA
      ↓
    GREEN
      ↓
  REFACTOR
```

---

## 🧠 Antes do teste existe um requisito

TDD não começa no `pytest`. O processo começa pela compreensão do problema:

```text
NECESSIDADE
    ↓
REQUISITO
    ↓
COMPORTAMENTO
    ↓
TESTE
    ↓
IMPLEMENTAÇÃO
```

O teste representa um comportamento que o sistema deverá apresentar.

---

## 👤 História de Usuário

Utilizamos o próprio **TechPort** como laboratório.

> **Como operador do TechPort, quero que a prioridade de um chamado seja calculada automaticamente para que solicitações mais importantes sejam atendidas primeiro.**

---

## ✅ Critérios de Aceitação

| Impacto | Urgência | Prioridade |
|---|---|---|
| ALTO | ALTA | CRÍTICA |
| ALTO | MÉDIA | ALTA |
| MÉDIO | MÉDIA | MÉDIA |
| BAIXO | BAIXA | BAIXA |

> **Como saberemos que a funcionalidade está correta?**

---

## 🔴🟢♻️ RED → GREEN → REFACTOR

### 🔴 RED

```python
def test_deve_definir_prioridade_critica():
    resultado = calcular_prioridade(impacto=3, urgencia=3)
    assert resultado == "CRÍTICA"
```

```bash
pytest -v
```

Resultado esperado: `FAILED`.

### 🟢 GREEN

```python
def calcular_prioridade(impacto: int, urgencia: int) -> str:
    return "CRÍTICA"
```

Executamos novamente e buscamos o `PASSED`.

### ♻️ REFACTOR

Refatorar significa melhorar a estrutura interna sem modificar o comportamento externo. Podemos melhorar nomes, eliminar duplicações, reduzir condicionais, separar responsabilidades, melhorar tipagem e diminuir complexidade.

Depois de cada alteração:

```bash
pytest
```

Os testes precisam continuar verdes.

---

## 🛡️ O teste como rede de segurança

```text
ALTERAR CÓDIGO
      ↓
EXECUTAR TESTES
      ↓
RESULTADO
      ↓
EVIDÊNCIA
```

Os testes não eliminam completamente os riscos, mas oferecem feedback rápido sobre comportamentos já especificados.

---

## 🔁 TDD é incremental

TDD trabalha com pequenos comportamentos:

```text
PEQUENO COMPORTAMENTO
        ↓
      TESTE
        ↓
       RED
        ↓
      CÓDIGO
        ↓
      GREEN
        ↓
    REFACTOR
        ↓
PRÓXIMO COMPORTAMENTO
```

---

## 💎 FIRST — características de bons testes

| Princípio | Significado |
|---|---|
| **F — Fast** | Rápidos |
| **I — Independent** | Independentes |
| **R — Repeatable** | Repetíveis |
| **S — Self-validating** | Autovalidáveis |
| **T — Timely** | Oportunos |

---

## 🎭 Mock dentro do TDD

```text
TESTE
  ↓
ChamadoService
  ↓
 MOCK
  ✕
MySQL
```

Mocks favorecem isolamento, velocidade, previsibilidade, baixo acoplamento e testabilidade.

---

## 💉 Injeção de dependência e testabilidade

```text
API
 ↓
SERVICE
 ↓
REPOSITORY
 ↓
MYSQL
```

```python
class ChamadoService:
    def __init__(self, repository):
        self.repository = repository
```

```text
PRODUÇÃO → Repository real
TESTE    → Mock
```

---

## 🚀 TDD aplicado ao TechPort

Podemos evoluir comportamentos reais:

- chamado deve possuir título;
- descrição deve possuir tamanho mínimo;
- novo chamado inicia como `ABERTO`;
- prioridade deve ser calculada;
- usuário precisa existir;
- técnico pode ser atribuído;
- chamado encerrado não pode ser encerrado novamente.

Cada regra pode representar um novo ciclo **RED → GREEN → REFACTOR**.

---

## ⚠️ Testando cenários e limites

Além do caminho feliz, devemos testar valores fora da faixa, nulos, tipos inválidos e combinações não permitidas.

```text
impacto = 0
impacto = 4
urgência = -1
valor nulo
tipo inválido
```

---

## 🧪 Testes parametrizados

```python
import pytest

@pytest.mark.parametrize(
    ("impacto", "urgencia", "esperado"),
    [
        (3, 3, "CRÍTICA"),
        (3, 2, "ALTA"),
        (2, 2, "MÉDIA"),
        (1, 1, "BAIXA"),
    ],
)
def test_calcular_prioridade(impacto, urgencia, esperado):
    assert calcular_prioridade(impacto, urgencia) == esperado
```

A parametrização permite representar vários comportamentos de negócio de maneira clara e sustentável.

---

## 🔙 TDD e regressão

```text
HOJE
25 TESTES
25 PASSED

APÓS UMA ALTERAÇÃO
25 TESTES
24 PASSED
1 FAILED
```

> **Regressão** é quando um comportamento anteriormente válido deixa de funcionar corretamente após uma alteração.

---

## 📊 TDD e cobertura

```bash
pytest --cov=app --cov-report=term-missing
```

> **100% de cobertura não significa 100% de qualidade.**

A pergunta mais importante é:

> **Os comportamentos importantes estão sendo testados?**

---

## 🧭 O que muda na maneira de desenvolver?

### Sem TDD

> "Vou implementar a funcionalidade."

### Com TDD

> **"Qual comportamento preciso entregar?"**

> **"Como posso demonstrar automaticamente que esse comportamento funciona?"**

> **"Agora vou implementar."**

---

## ⚠️ TDD não resolve tudo

TDD não substitui:

- testes de integração;
- testes de sistema;
- testes de segurança;
- testes de desempenho;
- testes de aceitação;
- revisão de código;
- análise estática;
- observabilidade;
- validação com usuários.

Ele é uma **estratégia de desenvolvimento** que trabalha em conjunto com outras práticas de qualidade.

---

## 🔗 Fluxo completo

```text
NECESSIDADE
     ↓
HISTÓRIA DE USUÁRIO
     ↓
CRITÉRIOS DE ACEITAÇÃO
     ↓
COMPORTAMENTO
     ↓
TESTE
     ↓
RED
     ↓
IMPLEMENTAÇÃO
     ↓
GREEN
     ↓
REFACTOR
     ↓
NOVO COMPORTAMENTO
     ↓
NOVO CICLO
```

Esse fluxo conecta diretamente **Projeto + Implementação + Teste**.

---

## 🧠 Principais conceitos para memorizar

| Conceito | Definição |
|---|---|
| **TDD** | Desenvolvimento Guiado por Testes |
| **RED** | Criar um teste para um comportamento ainda não implementado e observar sua falha |
| **GREEN** | Implementar o mínimo necessário para satisfazer o teste |
| **REFACTOR** | Melhorar a estrutura preservando o comportamento |
| **FIRST** | Princípios para construção de bons testes |
| **História de Usuário** | Necessidade descrita sob a perspectiva de quem utilizará a funcionalidade |
| **Critério de Aceitação** | Condição verificável para determinar se o comportamento atende à necessidade |
| **Mock** | Objeto simulado utilizado para substituir uma dependência |
| **Regressão** | Comportamento anteriormente válido que deixa de funcionar após uma alteração |
| **Testabilidade** | Facilidade com que um componente pode ser verificado por testes |

---

## 📌 Resumo da aula

```text
REQUISITO
   ↓
COMPORTAMENTO
   ↓
TESTE
   ↓
RED
   ↓
CÓDIGO
   ↓
GREEN
   ↓
REFACTOR
   ↓
EVOLUÇÃO
```

Nesta aula aprendemos que:

- testes podem participar da construção do software;
- TDD modifica o fluxo tradicional de implementação;
- o ciclo fundamental é **RED → GREEN → REFACTOR**;
- requisitos precisam ser transformados em comportamentos verificáveis;
- pequenos testes favorecem desenvolvimento incremental;
- mocks ajudam a isolar dependências;
- arquitetura e testabilidade estão relacionadas;
- testes acumulados ajudam a detectar regressões;
- cobertura é uma métrica auxiliar, e não sinônimo de qualidade.

---

## 🧰 Tecnologias e conceitos utilizados

- Python
- pytest
- pytest-cov
- Mock
- Test Driven Development
- Testes unitários
- Testes parametrizados
- Injeção de dependência
- Refatoração
- Cobertura
- Regressão
- Arquitetura em camadas
- TechPort

---

## ▶️ Comandos úteis

```bash
pytest
```

```bash
pytest -v
```

```bash
pytest --cov=app --cov-report=term-missing
```

---

## 🎓 Conclusão

TDD não deve ser entendido apenas como **"escrever o teste antes do código"**.

```text
O QUE O SISTEMA PRECISA FAZER?
              ↓
COMO POSSO PROVAR QUE FUNCIONA?
              ↓
ESCREVER O TESTE
              ↓
IMPLEMENTAR
              ↓
REFATORAR
              ↓
EVOLUIR
```

> **Testar bem é entregar com confiança.**

> **Qualidade é construída a cada pequeno ciclo.**

---

## 👨‍🏫 Professor

**Professor Rodolfo Terra**

- LinkedIn: https://www.linkedin.com/in/rodolffoterra/
- GitHub: https://github.com/rodolffoterra

---

## 📘 Disciplina

**Projeto, Implementação e Teste de Software com Python**

**Projeto de laboratório:** TechPort — Sistema de Chamados

---

⭐ **RED → GREEN → REFACTOR → EVOLUIR**

> Desenvolva pequenos comportamentos.  
> Teste continuamente.  
> Refatore com segurança.  
> Evolua com confiança.
