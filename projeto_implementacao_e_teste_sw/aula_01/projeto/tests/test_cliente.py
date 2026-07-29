from app.models.cliente import Cliente


def test_criar_cliente():
    cliente = Cliente(
        nome="Maria Silva",
        email="maria@email.com"
    )

    assert cliente.nome == "Maria Silva"
    assert cliente.email == "maria@email.com"