#iniciar o sistema;
# chamar os componentes principais;
# controlar o fluxo inicial da aplicação.

from app.controllers.cliente_controller import ClienteController


def main():
    controller = ClienteController()

    controller.cadastrar_cliente(
        nome="Maria Silva",
        email="maria@email.com"
    )

    controller.listar_clientes()


if __name__ == "__main__":
    main()