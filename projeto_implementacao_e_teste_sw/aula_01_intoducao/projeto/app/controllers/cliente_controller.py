# O controller:

# recebe os dados;
# chama o service;
# mostra o resultado;
# trata mensagens de erro.

from app.services.cliente_service import ClienteService


class ClienteController:

    def __init__(self):
        self.service = ClienteService()

    def cadastrar_cliente(self, nome: str, email: str):
        try:
            cliente = self.service.cadastrar(nome, email)

            print("Cliente cadastrado com sucesso!")
            print(cliente)

        except ValueError as erro:
            print(f"Erro: {erro}")

    def listar_clientes(self):
        clientes = self.service.listar()

        if not clientes:
            print("Nenhum cliente cadastrado.")
            return

        print("\nClientes cadastrados:")

        for cliente in clientes:
            print(cliente)