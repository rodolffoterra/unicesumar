from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="TechPort API",
    description="""
API REST desenvolvida para o projeto TechPort.

Esta API será responsável pela comunicação entre:

- Streamlit
- Regras de negócio
- Banco de dados MySQL

Projeto utilizado na disciplina:
Projeto, Implementação e Teste de Software.
""",
    version="1.0.0"
)


# ---------------------------------------------------------
# ROTAS DA APLICAÇÃO
# ---------------------------------------------------------

app.include_router(router)


# ---------------------------------------------------------
# ROTA PRINCIPAL
# ---------------------------------------------------------

@app.get(
    "/",
    tags=["Sistema"]
)
def inicio():

    return {
        "sistema": "TechPort",
        "api": "TechPort API",
        "versao": "1.0.0",
        "status": "online",
        "mensagem": "API funcionando corretamente."
    }