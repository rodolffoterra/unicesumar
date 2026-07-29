import pytest

from app.services.cliente_service import ClienteService


def test_cadastrar_cliente():
    service = ClienteService()

    cliente = service.cadastrar(
        nome="João Silva",
        email="joao@email.com"
    )

    assert cliente.nome == "João Silva"
    assert cliente.email == "joao@email.com"


def test_nao_deve_cadastrar_email_invalido():
    service = ClienteService()

    with pytest.raises(ValueError):
        service.cadastrar(
            nome="João Silva",
            email="email-invalido"
        )


def test_nao_deve_cadastrar_email_repetido():
    service = ClienteService()

    service.cadastrar(
        nome="Maria",
        email="maria@email.com"
    )

    with pytest.raises(ValueError):
        service.cadastrar(
            nome="Outra Maria",
            email="maria@email.com"
        )