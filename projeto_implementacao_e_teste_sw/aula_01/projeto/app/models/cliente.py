# Ele possui:

# nome;
# e-mail;
# comportamentos relacionados ao cliente.

class Cliente:

    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} - {self.email}"