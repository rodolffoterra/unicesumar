import streamlit as st

st.title("2️⃣ Projeto de Software e C4 Model")

nivel = st.radio("Selecione o nível de zoom", ["Contexto", "Contêiner", "Componentes", "Código"], horizontal=True)

diagramas = {
"Contexto": """Aluno / Professor\n      ↓\nSistema Didático Sakila\n      ↓\nBanco MySQL""",
"Contêiner": """Navegador\n   ↓\nAplicação Streamlit\n   ↓\nMySQL Connector\n   ↓\nBanco Sakila""",
"Componentes": """Páginas Streamlit\n   ↓\nservices/queries.py\n   ↓\nservices/database.py\n   ↓\nMySQL""",
"Código": """read_sql(query)\nexecute_sql(query, params)\nget_connection()\ntest_connection()""",
}
st.code(diagramas[nivel], language="text")

st.subheader("Modularidade do projeto")
st.code("""
app_streamlit_sakila/
├── app.py
├── pages/
├── services/
│   ├── database.py
│   └── queries.py
├── sql/
├── tests/
├── .env
└── requirements.txt
""", language="text")

st.info("Cada módulo possui uma responsabilidade: interface, regras/consultas, conexão e testes.")
