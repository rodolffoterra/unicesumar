import mysql.connector

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234556",
    database="loja"
)

print("Conectado com sucesso!")

# Cria um cursor
cursor = conexao.cursor()

# Executa a consulta
cursor.execute("SELECT * FROM clientes")

# Obtém todos os registros
clientes = cursor.fetchall()

print("\nTabela: clientes")
print("-" * 60)

# Exibe os registros
for cliente in clientes:
    print(f"ID: {cliente[0]}")
    print(f"Nome: {cliente[1]}")
    print(f"Cidade: {cliente[2]}")
    print(f"E-mail: {cliente[3]}")
    print("-" * 60)

# Fecha o cursor e a conexão
cursor.close()
conexao.close()

print("Conexão encerrada.")
