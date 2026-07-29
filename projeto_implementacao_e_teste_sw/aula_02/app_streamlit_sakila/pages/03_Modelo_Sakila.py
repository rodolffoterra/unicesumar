import streamlit as st

from services.queries import read_sql

st.title("3️⃣ Conhecendo o Banco Sakila")

st.markdown("""
O Sakila representa uma locadora de filmes. Ele permite demonstrar entidades, chaves primárias, chaves estrangeiras, relacionamentos N:N, transações, views, procedures, functions e triggers.
""")

relacoes = {
    "Filmes e atores": "film → film_actor → actor",
    "Filmes e categorias": "film → film_category → category",
    "Locações": "customer → rental → inventory → film",
    "Pagamentos": "customer → payment → staff",
    "Localização": "address → city → country",
    "Lojas": "store → staff / address",
}
st.table({"Domínio": list(relacoes.keys()), "Relacionamento": list(relacoes.values())})

try:
    tabelas = read_sql("SHOW FULL TABLES")
    st.subheader("Objetos existentes no banco")
    st.dataframe(tabelas, use_container_width=True, hide_index=True)

    tabela = st.selectbox("Inspecionar tabela", ["actor", "film", "customer", "rental", "payment", "inventory"])
    estrutura = read_sql(f"DESCRIBE {tabela}")
    st.dataframe(estrutura, use_container_width=True, hide_index=True)
except Exception as exc:
    st.error(f"Conecte o MySQL para visualizar o modelo: {exc}")
