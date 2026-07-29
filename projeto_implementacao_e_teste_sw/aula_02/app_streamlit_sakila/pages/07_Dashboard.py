import plotly.express as px
import streamlit as st

from services.queries import read_sql

st.title("7️⃣ Dashboard Executivo da Locadora")

try:
    kpis = read_sql("""
    SELECT
      (SELECT COUNT(*) FROM film) AS filmes,
      (SELECT COUNT(*) FROM customer WHERE active = 1) AS clientes_ativos,
      (SELECT COUNT(*) FROM rental) AS locacoes,
      (SELECT ROUND(SUM(amount), 2) FROM payment) AS faturamento
    """).iloc[0]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Filmes", f"{int(kpis.filmes):,}".replace(",", "."))
    c2.metric("Clientes ativos", f"{int(kpis.clientes_ativos):,}".replace(",", "."))
    c3.metric("Locações", f"{int(kpis.locacoes):,}".replace(",", "."))
    c4.metric("Faturamento", f"R$ {float(kpis.faturamento):,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    categorias = read_sql("SELECT category, total_sales FROM sales_by_film_category ORDER BY total_sales DESC")
    fig = px.bar(categorias, x="category", y="total_sales", title="Faturamento por categoria")
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    ratings = read_sql("SELECT rating, COUNT(*) quantidade FROM film GROUP BY rating ORDER BY quantidade DESC")
    col1.plotly_chart(px.pie(ratings, names="rating", values="quantidade", title="Filmes por classificação"), use_container_width=True)

    clientes = read_sql("""
    SELECT CONCAT(c.first_name, ' ', c.last_name) cliente, SUM(p.amount) total
    FROM customer c JOIN payment p ON p.customer_id = c.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name
    ORDER BY total DESC LIMIT 10
    """)
    col2.plotly_chart(px.bar(clientes.sort_values("total"), x="total", y="cliente", orientation="h", title="Top 10 clientes"), use_container_width=True)
except Exception as exc:
    st.error(str(exc))
