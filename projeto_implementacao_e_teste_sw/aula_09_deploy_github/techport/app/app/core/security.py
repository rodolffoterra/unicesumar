from cryptography.fernet import Fernet

from app.core.config import DB_ENCRYPTION_KEY


def descriptografar_senha(senha_criptografada: str) -> str:
    """
    Descriptografa uma senha utilizando Fernet.
    """

    if not DB_ENCRYPTION_KEY:
        raise ValueError(
            "DB_ENCRYPTION_KEY não encontrada no arquivo .env."
        )

    if not senha_criptografada:
        raise ValueError(
            "DB_PASSWORD não encontrada no arquivo .env."
        )

    fernet = Fernet(
        DB_ENCRYPTION_KEY.encode()
    )

    senha_descriptografada = fernet.decrypt(
        senha_criptografada.encode()
    )

    return senha_descriptografada.decode()