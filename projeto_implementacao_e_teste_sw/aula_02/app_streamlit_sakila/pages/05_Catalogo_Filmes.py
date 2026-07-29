import streamlit as st

from services.queries import read_sql

st.title("5️⃣ Catálogo de Filmes")

try:
    categorias = read_sql("SELECT name FROM category ORDER BY name")["name"].tolist()
    col1, col2, col3 = st.columns(3)
    categoria = col1.selectbox("Categoria", ["Todas"] + categorias)
    rating = col2.selectbox("Classificação", ["Todas", "G", "PG", "PG-13", "R", "NC-17"])
    titulo = col3.text_input("Título contém")

    filtros, params = [], []
    if categoria != "Todas":
        filtros.append("c.name = %s")
        params.append(categoria)
    if rating != "Todas":
        filtros.append("f.rating = %s")
        params.append(rating)
    if titulo:
        filtros.append("f.title LIKE %s")
        params.append(f"%{titulo}%")

    where = "WHERE " + " AND ".join(filtros) if filtros else ""
    query = f"""
    SELECT f.film_id, f.title, c.name AS category, f.rating,
           f.length, f.rental_rate, f.replacement_cost
    FROM film f
    JOIN film_category fc ON fc.film_id = f.film_id
    JOIN category c ON c.category_id = fc.category_id
    {where}
    ORDER BY f.title
    LIMIT 300
    """
    df = read_sql(query, tuple(params))
    st.metric("Filmes encontrados", len(df))
    st.dataframe(df, use_container_width=True, hide_index=True)
except Exception as exc:
    st.error(str(exc))
