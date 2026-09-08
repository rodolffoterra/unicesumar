from app.utils.validadores import validar_email


def test_email_valido():
    assert validar_email("aluno@email.com") is True


def test_email_invalido():
    assert validar_email("email-invalido") is False