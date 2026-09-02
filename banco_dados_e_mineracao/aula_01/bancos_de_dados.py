import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234556"
)

cursor = conexao.cursor()

cursor.execute("SHOW DATABASES")

print("Bancos de dados disponíveis:")
print("-" * 40)

for banco in cursor:
    print(banco[0])

cursor.close()
conexao.close()