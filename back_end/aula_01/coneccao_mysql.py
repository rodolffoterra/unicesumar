import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234556",
    database="loja"
)

print("Conectado com sucesso!")
