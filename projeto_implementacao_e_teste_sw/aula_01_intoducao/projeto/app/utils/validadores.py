# Essa pasta pode conter:

# validadores;
# conversores;
# formatadores;
# funções de data;
# funções reutilizáveis.


def validar_email(email: str) -> bool:
    return (
        isinstance(email, str)
        and "@" in email
        and "." in email
        and len(email.strip()) >= 5
    )