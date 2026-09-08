# Nesse primeiro projeto, os dados ficam em uma lista.

# Posteriormente, o repository poderá acessar:

# SQLite;
# MySQL;
# PostgreSQL;
# arquivos;
# serviços externos.

from app.models.cliente import Cliente


class ClienteRepository:

    def __init__(self):
        self.clientes: list[Cliente] = []

    def salvar(self, cliente: Cliente):
        self.clientes.append(cliente)

    def listar_todos(self) -> list[Cliente]:
        return self.clientes

    def buscar_por_email(self, email: str):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente

        return None