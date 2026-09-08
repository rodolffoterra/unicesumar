import streamlit as st

st.title("1️⃣ Sequência Didática da Aula")

conteudos = [
    ("Requisitos", "O que o sistema deve fazer?", "Consultar catálogo, clientes, locações e indicadores."),
    ("Projeto", "Como o sistema será construído?", "Streamlit + serviços Python + MySQL Sakila."),
    ("Implementação", "Transformar projeto em código", "Páginas, componentes, consultas e CRUD."),
    ("Testes", "Verificar comportamento", "Conexão, consultas, validações e regras de negócio."),
    ("Implantação", "Disponibilizar a aplicação", "Execução local ou publicação em servidor."),
    ("Manutenção", "Evoluir com segurança", "Novos relatórios, filtros, perfis e testes."),
]

for i, (titulo, pergunta, exemplo) in enumerate(conteudos, 1):
    with st.expander(f"Etapa {i} — {titulo}", expanded=i == 1):
        st.subheader(pergunta)
        st.write(exemplo)