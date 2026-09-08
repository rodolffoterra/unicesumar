import streamlit as st

from services.database import test_connection

st.set_page_config(
    page_title="Laboratório Sakila",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.block-container {padding-top: 1.4rem; padding-bottom: 2rem;}
[data-testid="stMetric"] {background:#f7f8fa;border:1px solid #e7e9ee;padding:14px;border-radius:14px;}
.didatico {padding:16px;border-left:5px solid #ff4b4b;background:#fff7f7;border-radius:8px;margin:10px 0 18px;}
</style>
""", unsafe_allow_html=True)

st.title("🎬 Laboratório Didático — Python, Streamlit, SQL e Sakila")
st.caption("Projeto, Implementação e Teste de Software")

ok, message = test_connection()
if ok:
    st.success(message)
else:
    st.warning("MySQL ainda não conectado. Configure o arquivo .env para liberar as páginas práticas.")
    with st.expander("Detalhes da conexão"):
        st.code(message)

st.markdown("""
<div class="didatico">
<b>Objetivo didático:</b> acompanhar a evolução de um software desde os requisitos e a arquitetura até a implementação, consultas SQL, CRUD, dashboard e testes.
</div>
""", unsafe_allow_html=True)

cols = st.columns(6)
etapas = [
    ("1", "Requisitos"), ("2", "Projeto"), ("3", "Banco"),
    ("4", "Implementação"), ("5", "Testes"), ("6", "Dashboard")
]
for col, (n, nome) in zip(cols, etapas):
    col.metric(f"Etapa {n}", nome)

st.subheader("Sequência recomendada para a aula")
st.markdown("""
1. **Visão da disciplina** — ciclo da Engenharia de Software e diferença entre requisitos e projeto.  
2. **Arquitetura** — abstração, refinamento, modularidade e C4 Model.  
3. **Banco Sakila** — tabelas, chaves, relacionamentos, views, procedures e funções.  
4. **SQL na prática** — SELECT, filtros, agregações, JOIN, subconsultas e views.  
5. **Aplicação Streamlit** — telas, filtros, formulários e CRUD.  
6. **Indicadores** — locações, faturamento, clientes, filmes e categorias.  
7. **Testes** — conexão, funções de acesso a dados e regras de negócio.
""")

st.subheader("Arquitetura usada")
st.code("""
Usuário
  ↓
Streamlit (interface)
  ↓
Services / Queries (regras e acesso a dados)
  ↓
MySQL Connector
  ↓
Banco Sakila
""", language="text")

st.info("Use o menu lateral para avançar pelas páginas na ordem numérica.")
