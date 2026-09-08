import streamlit as st

from services.queries import read_sql

st.title("4️⃣ Laboratório SQL")

exemplos = {
"SELECT básico": "SELECT film_id, title, rating, rental_rate FROM film LIMIT 20;",
"WHERE e ORDER BY": "SELECT title, length, rating FROM film WHERE rating = 'PG-13' ORDER BY length DESC LIMIT 20;",
"GROUP BY": "SELECT rating, COUNT(*) AS quantidade, ROUND(AVG(length), 1) AS duracao_media FROM film GROUP BY rating ORDER BY quantidade DESC;",
"INNER JOIN": """SELECT f.title, c.name AS categoria\nFROM film f\nJOIN film_category fc ON fc.film_id = f.film_id\nJOIN category c ON c.category_id = fc.category_id\nORDER BY f.title\nLIMIT 30;""",
"JOIN completo": """SELECT CONCAT(c.first_name, ' ', c.last_name) AS cliente,\n       f.title AS filme, r.rental_date, r.return_date\nFROM rental r\nJOIN customer c ON c.customer_id = r.customer_id\nJOIN inventory i ON i.inventory_id = r.inventory_id\nJOIN film f ON f.film_id = i.film_id\nORDER BY r.rental_date DESC\nLIMIT 30;""",
"VIEW": "SELECT * FROM sales_by_film_category ORDER BY total_sales DESC;",
}

escolha = st.selectbox("Exemplo", list(exemplos))
query = st.text_area("Consulta SQL", exemplos[escolha], height=220)

st.warning("Por segurança didática, esta página aceita apenas consultas iniciadas por SELECT, SHOW, DESCRIBE ou EXPLAIN.")
if st.button("Executar consulta", type="primary"):
    inicio = query.strip().split(maxsplit=1)[0].upper() if query.strip() else ""
    if inicio not in {"SELECT", "SHOW", "DESCRIBE", "DESC", "EXPLAIN"}:
        st.error("Comando não permitido nesta página.")
    else:
        try:
            df = read_sql(query)
            st.success(f"Consulta concluída: {len(df)} linha(s).")
            st.dataframe(df, use_container_width=True, hide_index=True)
        except Exception as exc:
            st.error(str(exc))
