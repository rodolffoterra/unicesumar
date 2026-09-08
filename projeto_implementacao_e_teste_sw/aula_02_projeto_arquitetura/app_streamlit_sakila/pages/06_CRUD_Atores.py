import streamlit as st

from services.queries import execute_sql, read_sql

st.title("6️⃣ CRUD Didático — Atores")
st.caption("Demonstração de CREATE, READ, UPDATE e DELETE usando a tabela actor.")

abas = st.tabs(["Consultar", "Cadastrar", "Atualizar", "Excluir"])

with abas[0]:
    busca = st.text_input("Buscar por nome")
    try:
        if busca:
            df = read_sql("SELECT * FROM actor WHERE CONCAT(first_name, ' ', last_name) LIKE %s ORDER BY actor_id", (f"%{busca}%",))
        else:
            df = read_sql("SELECT * FROM actor ORDER BY actor_id DESC LIMIT 100")
        st.dataframe(df, use_container_width=True, hide_index=True)
    except Exception as exc:
        st.error(str(exc))

with abas[1]:
    with st.form("novo_ator"):
        nome = st.text_input("Nome")
        sobrenome = st.text_input("Sobrenome")
        salvar = st.form_submit_button("Cadastrar", type="primary")
    if salvar:
        if not nome.strip() or not sobrenome.strip():
            st.error("Preencha nome e sobrenome.")
        else:
            try:
                execute_sql("INSERT INTO actor(first_name, last_name) VALUES (%s, %s)", (nome.upper().strip(), sobrenome.upper().strip()))
                st.success("Ator cadastrado.")
            except Exception as exc:
                st.error(str(exc))

with abas[2]:
    actor_id = st.number_input("ID do ator", min_value=1, step=1, key="update_id")
    nome = st.text_input("Novo nome", key="update_nome")
    sobrenome = st.text_input("Novo sobrenome", key="update_sobrenome")
    if st.button("Atualizar"):
        try:
            n = execute_sql("UPDATE actor SET first_name=%s, last_name=%s WHERE actor_id=%s", (nome.upper().strip(), sobrenome.upper().strip(), actor_id))
            st.success(f"{n} registro(s) atualizado(s).")
        except Exception as exc:
            st.error(str(exc))

with abas[3]:
    actor_id = st.number_input("ID para excluir", min_value=1, step=1, key="delete_id")
    confirmar = st.checkbox("Confirmo a exclusão")
    if st.button("Excluir", disabled=not confirmar):
        try:
            n = execute_sql("DELETE FROM actor WHERE actor_id=%s", (actor_id,))
            st.success(f"{n} registro(s) excluído(s).")
        except Exception as exc:
            st.error("A exclusão pode ser impedida por relacionamentos com filmes. " + str(exc))
