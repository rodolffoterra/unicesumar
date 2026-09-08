# 🎫 TechPort — Interfaces, Perfis de Usuário e Qualidade de Software

> **Projeto, Implementação e Teste de Software**  
> **Professor Rodolfo Terra**  
> Aula prática: do código ao produto com **Streamlit + FastAPI + Services + Repositories + MySQL**

---

## 👨‍🏫 Professor

**Rodolfo Terra**

- 💼 LinkedIn: `linkedin.com/in/rodolffoterra/`
- 💻 GitHub: `github.com/rodolffoterra`

---

# 📚 Sobre esta aula

Nesta etapa do projeto **TechPort**, deixamos de observar apenas componentes isolados e passamos a enxergar o sistema como um **produto de software**.

Ao longo da disciplina, o projeto evoluiu por diferentes camadas:

```text
REQUISITO
    ↓
BANCO DE DADOS
    ↓
PYTHON
    ↓
FASTAPI
    ↓
STREAMLIT
    ↓
TESTES
    ↓
TDD
    ↓
QUALIDADE
    ↓
PRODUTO
```

A aplicação desta aula utiliza **uma única aplicação Streamlit**, mas apresenta **três experiências diferentes**, de acordo com o perfil:

```text
                         TECHPORT
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
          👤 USUÁRIO    🛠️ TÉCNICO    ⚙️ ADMIN
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ▼
                         FASTAPI
                            │
                            ▼
                         SERVICE
                            │
                            ▼
                       REPOSITORY
                            │
                            ▼
                          MYSQL
```

> **Uma arquitetura. Diferentes experiências.**

---

# 🎯 Objetivos

Ao utilizar este laboratório, o aluno deverá ser capaz de:

- compreender a diferença entre **interface** e **regra de negócio**;
- reconhecer diferentes necessidades para usuário, técnico e administrador;
- acompanhar o ciclo de vida de um chamado;
- visualizar a integração entre Streamlit e FastAPI;
- compreender o papel das camadas Service e Repository;
- observar a persistência dos dados no MySQL;
- relacionar interface com qualidade de software;
- analisar adequação funcional, usabilidade, confiabilidade, segurança e manutenibilidade.

---

# 🧩 O problema de negócio

O TechPort organiza o ciclo de atendimento de chamados.

```text
PROBLEMA
   ↓
USUÁRIO PRECISA DE SUPORTE
   ↓
CHAMADO
   ↓
ATENDIMENTO
   ↓
SOLUÇÃO
```

O **chamado** é o elemento central do projeto.

Ele não representa apenas uma linha no banco. Ele possui um ciclo de vida:

```text
NOVO CHAMADO
      ↓
    ABERTO
      ↓
  ATRIBUÍDO
      ↓
EM ATENDIMENTO
      ↓
  RESOLVIDO
      ↓
 FINALIZADO
```

Durante esse ciclo podem ser registrados:

- prioridade;
- categoria;
- responsável;
- comentários;
- histórico;
- status;
- datas de atualização.

---

# 👥 Um chamado, três perfis

O mesmo chamado é observado por pessoas com responsabilidades diferentes.

## 👤 Perfil Usuário

O usuário precisa principalmente **registrar e acompanhar seu problema**.

```text
USUÁRIO
   │
   ├── Abrir chamado
   ├── Consultar meus chamados
   ├── Acompanhar status
   ├── Adicionar informações
   └── Consultar histórico
```

### Jornada

```text
ENTRAR
  ↓
MEUS CHAMADOS
  ↓
NOVO CHAMADO
  ↓
DESCREVER PROBLEMA
  ↓
ENVIAR
  ↓
ACOMPANHAR STATUS
```

No laboratório, o usuário pode selecionar um registro existente ou cadastrar um novo usuário.

---

## 🛠️ Perfil Técnico

Para o técnico, o chamado representa **trabalho a ser atendido**.

```text
USUÁRIO
   │ cria
   ▼
CHAMADO ABERTO
   │
   ▼
FILA DE ATENDIMENTO
   │
   ▼
TÉCNICO
```

O técnico pode:

```text
TÉCNICO
   │
   ├── Visualizar fila
   ├── Identificar prioridade
   ├── Assumir chamado
   ├── Registrar atendimento
   ├── Alterar status
   └── Finalizar atendimento
```

> **Prioridade + Informação + Ação**

O técnico também pode selecionar um registro existente ou cadastrar um novo técnico.

---

## ⚙️ Perfil Administrador

O administrador possui uma visão mais ampla.

```text
ADMINISTRADOR
      │
      ├── Usuários
      ├── Técnicos
      ├── Chamados
      ├── Categorias
      ├── Indicadores
      └── Visão global
```

> **Gestão + Controle + Visibilidade**

Na interface administrativa é possível acompanhar indicadores e inspecionar chamados, incluindo seus dados principais, histórico e comentários.

---

# 🏗️ Arquitetura

A arquitetura utilizada continua sendo a mesma estudada durante a disciplina:

```text
┌──────────────────────────┐
│        STREAMLIT         │
│       Interface / UI     │
└────────────┬─────────────┘
             │ HTTP
             ▼
┌──────────────────────────┐
│         FASTAPI          │
│        Endpoints         │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│         SERVICE          │
│    Regras de negócio     │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│       REPOSITORY         │
│     Acesso aos dados     │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│          MYSQL           │
│      Persistência        │
└──────────────────────────┘
```

### Exemplo: técnico assume um chamado

```text
TÉCNICO
   ↓
[ASSUMIR CHAMADO]
   ↓
STREAMLIT
   ↓
POST /chamados/{id}/assumir
   ↓
FASTAPI
   ↓
SERVICE
   ↓
REPOSITORY
   ↓
MYSQL
   ↓
STATUS + RESPONSÁVEL + HISTÓRICO
```

Um botão na interface pode iniciar uma cadeia de ações que percorre toda a arquitetura.

---

# 📂 Estrutura principal do projeto

```text
techport/
│
├── app/
│   ├── api/
│   │   ├── fastapi_app.py
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── database.py
│   │   ├── inicializar_banco.py
│   │   └── techport_mysql_volumetria.sql
│   │
│   ├── repositories/
│   │   ├── chamado_repository.py
│   │   ├── usuario_repository.py
│   │   ├── tecnico_repository.py
│   │   └── laboratorio_repository.py
│   │
│   ├── schemas/
│   │   ├── chamado.py
│   │   ├── usuario.py
│   │   ├── tecnico.py
│   │   └── laboratorio.py
│   │
│   ├── services/
│   │   ├── chamado_service.py
│   │   ├── usuario_service.py
│   │   ├── tecnico_service.py
│   │   └── laboratorio_service.py
│   │
│   └── laboratorio_aula08.py
│
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
├── run_api.bat
├── run_api.ps1
├── run_streamlit_aula08.bat
├── run_streamlit_aula08.ps1
└── README.md
```

---

# ⚙️ Pré-requisitos

Antes de iniciar, tenha instalado:

- Python;
- MySQL Server;
- MySQL Workbench (opcional, mas útil para acompanhar os dados);
- VS Code ou outra IDE;
- terminal PowerShell no Windows.

O banco **TechPort** deve estar disponível e configurado conforme as aulas anteriores.

---

# 🚀 Instalação

## 1. Abra o projeto

No PowerShell:

```powershell
cd "CAMINHO\PARA\techport"
```

Exemplo:

```powershell
cd "C:\Users\SEU_USUARIO\Desktop\techport"
```

---

## 2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

A estrutura passará a conter:

```text
techport/
├── .venv/
├── app/
├── requirements.txt
└── ...
```

---

## 3. Ativar a `.venv`

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando estiver ativa, normalmente aparecerá:

```text
(.venv) PS C:\...\techport>
```

### Caso o PowerShell bloqueie a ativação

Pode ser necessário permitir scripts para o usuário atual:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois tente novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 4. Atualizar o `pip`

```powershell
python -m pip install --upgrade pip
```

---

## 5. Instalar as dependências

```powershell
pip install -r requirements.txt
```

O `requirements.txt` deste laboratório inclui:

```text
fastapi
uvicorn[standard]
streamlit
requests
pydantic
mysql-connector-python
python-dotenv
cryptography
```

---

# 🔐 Configuração do `.env`

O projeto utiliza variáveis de ambiente para configurações sensíveis e parâmetros de execução.

Use `.env.example` como modelo.

```env
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=techport
DB_USER=root
DB_ENCRYPTION_KEY=COLE_SUA_CHAVE_FERNET
DB_PASSWORD=COLE_SUA_SENHA_CRIPTOGRAFADA

API_BASE_URL=http://127.0.0.1:8000

ADMIN_USER=admin
ADMIN_PASSWORD=techport123
```

> ⚠️ **Importante:** as credenciais administrativas utilizadas aqui são propositalmente simples e existem somente para o laboratório.

O arquivo `.env` **não deve ser enviado ao GitHub**.

Por isso, confirme que ele está no `.gitignore`.

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# ▶️ Como executar a aplicação

Para a aula, utilizaremos **dois terminais**.

```text
┌─────────────────────────┐     ┌─────────────────────────┐
│      TERMINAL 01        │     │      TERMINAL 02        │
│                         │     │                         │
│        FASTAPI          │◄────│       STREAMLIT         │
│     porta 8000          │ HTTP│      porta 8501         │
└────────────┬────────────┘     └─────────────────────────┘
             │
             ▼
           MYSQL
```

---

# 🟢 Terminal 01 — FastAPI

Abra um terminal na raiz do projeto e ative a `.venv`.

```powershell
.\.venv\Scripts\Activate.ps1
```

Depois:

```powershell
python -m uvicorn app.api.fastapi_app:app --reload
```

Também é possível utilizar:

```text
run_api.bat
```

ou:

```powershell
.\run_api.ps1
```

Quando a API estiver funcionando, você deverá ver algo semelhante a:

```text
Uvicorn running on http://127.0.0.1:8000
```

### Endereços importantes

API:

```text
http://127.0.0.1:8000
```

Swagger / documentação interativa:

```text
http://127.0.0.1:8000/docs
```

> 💡 Durante a aula, mantenha `/docs` aberto em uma aba. Isso ajuda a mostrar que as ações do Streamlit estão utilizando endpoints reais.

---

# 🔵 Terminal 02 — Streamlit

Abra **outro terminal**, também na raiz do projeto.

Ative novamente a `.venv`:

```powershell
.\.venv\Scripts\Activate.ps1
```

Execute:

```powershell
python -m streamlit run app/laboratorio_aula08.py
```

Também é possível utilizar:

```text
run_streamlit_aula08.bat
```

ou:

```powershell
.\run_streamlit_aula08.ps1
```

O endereço normalmente será:

```text
http://localhost:8501
```

---

# 🔄 Visão da execução

```text
NAVEGADOR
   │
   ▼
STREAMLIT :8501
   │
   │ HTTP
   ▼
FASTAPI :8000
   │
   ▼
SERVICE
   │
   ▼
REPOSITORY
   │
   ▼
MYSQL
```

Se a API estiver desligada, o Streamlit não conseguirá executar as operações que dependem dela.

---

# 🧪 Laboratório completo

A melhor forma de demonstrar o sistema é acompanhar **um único chamado** através das três interfaces.

---

## 👤 Etapa 1 — Entrar como Usuário

No menu lateral, selecione:

```text
👤 USUÁRIO
```

Você poderá:

1. selecionar um usuário existente; ou
2. cadastrar um novo usuário.

Para uma demonstração rápida, pode utilizar um usuário existente.

---

## 📝 Etapa 2 — Criar o chamado

Crie:

```text
Título:
Notebook não inicializa

Descrição:
Equipamento não liga após pressionar
o botão de energia.

Categoria:
Hardware

Prioridade:
ALTA
```

Clique em:

```text
[ ABRIR CHAMADO ]
```

Anote o ID criado.

Exemplo:

```text
Chamado #501 criado com sucesso.
```

### O que acontece?

```text
USUÁRIO
   ↓
STREAMLIT
   ↓
POST /chamados
   ↓
FASTAPI
   ↓
SERVICE
   ↓
REPOSITORY
   ↓
MYSQL
```

---

# 🛠️ Etapa 3 — Trocar para Técnico

No menu lateral:

```text
🛠️ TÉCNICO
```

Selecione um técnico existente ou cadastre um novo.

Na fila, localize o chamado recém-criado.

Exemplo:

```text
┌────────────────────────────────────┐
│ #501 — Notebook não inicializa     │
│                                    │
│ Prioridade: ALTA                   │
│ Status: ABERTO                     │
│                                    │
│          [ ASSUMIR CHAMADO ]       │
└────────────────────────────────────┘
```

Clique em:

```text
ASSUMIR CHAMADO
```

---

# 🔁 O que muda ao assumir?

O fluxo é:

```text
TÉCNICO
   ↓
STREAMLIT
   ↓
FASTAPI
   ↓
SERVICE
   ↓
REPOSITORY
   ↓
MYSQL
```

O chamado passa a possuir:

```text
tecnico_id = técnico selecionado
status = em_atendimento
data_atualizacao = atualizada
histórico = registrado
```

Visualmente:

```text
ANTES                     DEPOIS

#501                       #501
ABERTO          →          EM ATENDIMENTO
Sem técnico                Técnico atribuído
```

---

# 💬 Etapa 4 — Registrar atendimento

O técnico pode adicionar uma informação, por exemplo:

```text
Equipamento em análise.
Identificada possível falha na fonte de alimentação.
```

O comentário passa a fazer parte do acompanhamento do chamado.

---

# 👤 Etapa 5 — Voltar para Usuário

Troque novamente:

```text
🛠️ TÉCNICO
      ↓
👤 USUÁRIO
```

Selecione o mesmo usuário.

O chamado que antes estava:

```text
#501
ABERTO
```

deverá aparecer como:

```text
#501
EM ATENDIMENTO
```

O usuário consegue acompanhar a evolução sem precisar telefonar ou utilizar uma planilha paralela.

---

# ⚙️ Etapa 6 — Administrador

No menu lateral, selecione:

```text
⚙️ ADMINISTRADOR
```

Para o laboratório:

```text
Usuário: admin
Senha: techport123
```

> Essas credenciais podem ser alteradas pelo `.env`.

---

# 📊 Dashboard Administrativo

O administrador possui uma visão global.

Exemplo conceitual:

```text
┌─────────────────────────────────────────────────────┐
│                TECHPORT — ADMIN                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│   👥 Usuários      🛠 Técnicos      🎫 Chamados     │
│      1.000             120             5.000        │
│                                                     │
├─────────────────────────────────────────────────────┤
│ CHAMADOS POR STATUS                                 │
│                                                     │
│ Aberto           ███████████                        │
│ Em atendimento   ███████                            │
│ Finalizado       ███████████████                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

O administrador consegue observar o sistema de uma perspectiva diferente:

```text
DADO OPERACIONAL
       ↓
CONSOLIDAÇÃO
       ↓
INDICADOR
       ↓
INFORMAÇÃO
       ↓
GESTÃO
```

---

# 🔎 Inspecionar chamado no Administrador

Acesse:

```text
ADMINISTRADOR
      ↓
CHAMADOS
      ↓
INSPECIONAR CHAMADO
```

Selecione um chamado.

A interface apresenta seus dados principais mesmo quando ele ainda não possui comentários ou histórico.

Exemplo:

```text
Chamado #501
────────────────────────────────────

Status:        EM ATENDIMENTO
Prioridade:    ALTA
Categoria:     Hardware

Título:
Notebook não inicializa

Descrição:
Equipamento não liga após pressionar
o botão de energia.

Usuário ID:    ...
Técnico ID:    ...
Canal:         ...

Data abertura: ...
Atualização:   ...
Fechamento:    ...
```

Depois são apresentados:

```text
┌─────────────────────┐    ┌─────────────────────┐
│      HISTÓRICO      │    │     COMENTÁRIOS     │
└─────────────────────┘    └─────────────────────┘
```

Se não existirem registros, a aplicação informa isso ao invés de deixar a área sem explicação.

---

# 🌐 Endpoints utilizados no laboratório

Além do CRUD já desenvolvido anteriormente, esta etapa adiciona endpoints didáticos:

| Método | Endpoint | Objetivo |
|---|---|---|
| `POST` | `/chamados/{id}/assumir` | Técnico assume um chamado |
| `PATCH` | `/chamados/{id}/status` | Altera o status |
| `POST` | `/chamados/{id}/comentarios` | Registra comentário |
| `GET` | `/chamados/{id}/comentarios` | Consulta comentários |
| `GET` | `/chamados/{id}/historico` | Consulta histórico |
| `GET` | `/dashboard/resumo` | Obtém dados do dashboard |

Essas funcionalidades foram organizadas em:

```text
app/schemas/laboratorio.py
        ↓
app/services/laboratorio_service.py
        ↓
app/repositories/laboratorio_repository.py
```

Assim, a aplicação continua respeitando a separação de responsabilidades estudada durante a disciplina.

---

# ✨ Qualidade de Software aplicada ao TechPort

Uma interface bonita e funcional, sozinha, não garante qualidade.

```text
BONITA + FUNCIONA
        │
        ▼
   É SUFICIENTE?
        │
        ▼
       NÃO
```

Para este laboratório, podemos avaliar:

```text
                    QUALIDADE
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
 Funcionalidade    Usabilidade   Confiabilidade
        │              │              │
        └──────────────┼──────────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
         Segurança         Manutenibilidade
```

---

# ✅ Checklist de qualidade

| Pergunta | Característica |
|---|---|
| A função faz o que deveria? | Adequação funcional |
| O perfil entende facilmente o que fazer? | Usabilidade |
| O sistema trata falhas adequadamente? | Confiabilidade |
| Cada perfil acessa somente o necessário? | Segurança |
| O software pode evoluir sem concentrar tudo em uma única camada? | Manutenibilidade |

---

# 🎯 Adequação funcional por perfil

| 👤 Usuário | 🛠️ Técnico | ⚙️ Administrador |
|---|---|---|
| Abrir chamado | Assumir | Gerenciar |
| Acompanhar | Atender | Monitorar |
| Comentar | Atualizar | Analisar |

> **Função certa para o usuário certo.**

---

# 🧭 Usabilidade

Evite fazer o usuário pensar em termos técnicos.

### ❌ Menos adequado

```text
[ EXECUTAR ]
[ PROCESSAR ]
[ UPDATE STATUS ]
```

### ✅ Mais adequado

```text
[ ABRIR CHAMADO ]
[ ASSUMIR CHAMADO ]
[ FINALIZAR ATENDIMENTO ]
```

> **Clareza reduz erro.**

---

# 🚨 Confiabilidade e feedback

Uma aplicação não deve despejar erros técnicos para o usuário.

### ❌ Evitar

```text
requests.exceptions.ConnectionError
HTTPConnectionPool...
500 Internal Server Error
```

### ✅ Preferir

```text
⚠️ Não foi possível concluir a operação.

Tente novamente em alguns instantes.
```

O usuário precisa compreender **o que aconteceu** e **o que pode fazer**.

---

# 🔒 Segurança

Uma ideia essencial desta aula:

```text
ESCONDER UM BOTÃO
       ≠
GARANTIR SEGURANÇA
```

Exemplo:

```text
STREAMLIT
    ↓
esconde opção administrativa

        NÃO GARANTE

FASTAPI
    ↓
autorização real
```

> **Interface ≠ autorização**

O controle de perfis deste laboratório é propositalmente simplificado.

Em produção, seriam necessários mecanismos reais de autenticação e autorização, com validação também no backend.

---

# 🔧 Manutenibilidade

A separação de camadas ajuda o sistema a evoluir.

```text
REQUISITO NOVO
      ↓
ALTERAÇÃO
      ↓
CÓDIGO
      ↓
TESTES
      ↓
VALIDAÇÃO
```

As estruturas estudadas ajudam nesse processo:

```text
SCHEMAS
   +
SERVICES
   +
REPOSITORIES
   +
TESTES
   +
TDD
```

---

# 🧯 Solução de problemas

## `No module named uvicorn`

Confirme que a `.venv` está ativa:

```powershell
.\.venv\Scripts\Activate.ps1
```

Depois:

```powershell
pip install -r requirements.txt
```

---

## `No module named streamlit`

```powershell
pip install streamlit
```

ou:

```powershell
pip install -r requirements.txt
```

---

## Streamlit abre, mas não consegue carregar dados

Verifique se a API está executando.

Abra:

```text
http://127.0.0.1:8000/docs
```

Se não abrir, volte ao Terminal 01 e execute:

```powershell
python -m uvicorn app.api.fastapi_app:app --reload
```

---

## Erro de conexão com MySQL

Verifique:

1. se o MySQL está iniciado;
2. se o banco `techport` existe;
3. se as configurações do `.env` estão corretas;
4. se usuário e senha possuem acesso ao banco.

Fluxo de diagnóstico:

```text
STREAMLIT
   ↓
FASTAPI
   ↓
CONEXÃO MYSQL
   ↓
BANCO TECHPORT
```

---

## Porta 8000 ocupada

Você pode encerrar o processo anterior ou iniciar em outra porta:

```powershell
python -m uvicorn app.api.fastapi_app:app --reload --port 8001
```

Se fizer isso, ajuste:

```env
API_BASE_URL=http://127.0.0.1:8001
```

e reinicie o Streamlit.

---

## Porta 8501 ocupada

O Streamlit pode escolher outra porta automaticamente ou você pode definir:

```powershell
python -m streamlit run app/laboratorio_aula08.py --server.port 8502
```

---

# ⛔ Encerrar a aplicação

Nos terminais onde FastAPI e Streamlit estão executando:

```text
CTRL + C
```

Para sair da `.venv`:

```powershell
deactivate
```

---

# 🧑‍🏫 Roteiro rápido para demonstração em sala

```text
01. Iniciar MySQL
        ↓
02. Terminal 01 → FastAPI
        ↓
03. Terminal 02 → Streamlit
        ↓
04. Usuário → criar chamado
        ↓
05. Anotar ID
        ↓
06. Técnico → localizar chamado
        ↓
07. Técnico → assumir
        ↓
08. Técnico → comentar / atualizar
        ↓
09. Usuário → acompanhar alteração
        ↓
10. Admin → visualizar indicadores
        ↓
11. Admin → inspecionar o chamado
        ↓
12. Relacionar tudo com qualidade
```

---

# 🔄 O que aconteceu durante o laboratório?

```text
                         USUÁRIO
                            │
                            ▼
                        STREAMLIT
                            │
                          HTTP
                            │
                            ▼
                         FASTAPI
                            │
                            ▼
                         SERVICE
                            │
                            ▼
                       REPOSITORY
                            │
                            ▼
                          MYSQL
                            │
                            ▼
                       REPOSITORY
                            │
                            ▼
                         FASTAPI
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          USUÁRIO        TÉCNICO         ADMIN
```

O que antes foi estudado separadamente passa a funcionar como **um único produto**.

---

# 🏁 Encerramento

## Construímos um produto.

```text
REQUISITO
    ↓
BANCO DE DADOS
    ↓
PYTHON
    ↓
API
    ↓
INTERFACE
    ↓
TESTES
    ↓
TDD
    ↓
QUALIDADE
    ↓
PRODUTO
```

> **Qualidade não é uma etapa no final do desenvolvimento.  
> Ela precisa estar presente em todo o produto.**

O TechPort deixou de ser apenas código, tabelas, endpoints e testes isolados.

Agora temos:

```text
PESSOAS
   +
COMPORTAMENTOS
   +
RESPONSABILIDADES
   +
DADOS
   +
INTEGRAÇÃO
   +
QUALIDADE
   =
PRODUTO DE SOFTWARE
```

---

# ➡️ Próxima etapa

Existe apenas um problema:

```text
http://localhost:8501
```

O TechPort ainda está executando em nosso computador.

A próxima etapa é compreender:

```text
CÓDIGO
   ↓
GITHUB
   ↓
DOCKER
   ↓
CI/CD
   ↓
CLOUD
   ↓
PRODUÇÃO
```

---

## 👨‍🏫 Professor Rodolfo Terra

**Projeto, Implementação e Teste de Software**

💼 `linkedin.com/in/rodolffoterra/`  
💻 `github.com/rodolffoterra`

---

> **TechPort — do requisito ao produto.**
