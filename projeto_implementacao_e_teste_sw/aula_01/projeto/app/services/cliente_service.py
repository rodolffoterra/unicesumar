# O service concentra regras como:

# validar o nome;
# validar o e-mail;
# impedir cadastro duplicado;
# criar o cliente;
# solicitar o armazenamento dos dados.


from app.models.cliente import Cliente
from app.repositories.cliente_repository import ClienteRepository
from app.utils.validadores import validar_email


class ClienteService:

    def __init__(self):
        self.repository = ClienteRepository()

    def cadastrar(self, nome: str, email: str) -> Cliente:
        if not nome.strip():
            raise ValueError("O nome é obrigatório.")

        if not validar_email(email):
            raise ValueError("O e-mail informado é inválido.")

        cliente_existente = self.repository.buscar_por_email(email)

        if cliente_existente:
            raise ValueError("Já existe um cliente com esse e-mail.")

        cliente = Cliente(nome, email)

        self.repository.salvar(cliente)

        return cliente

    def listar(self) -> list[Cliente]:
        return self.repository.listar_todos()