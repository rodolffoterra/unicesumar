# ==========================================================
# IMPORTAÇÃO DA BIBLIOTECA DE CRIPTOGRAFIA
# ==========================================================

# Fernet faz parte da biblioteca cryptography.
#
# Ele permite:
#
# - gerar uma chave de criptografia;
# - criptografar informações;
# - descriptografar informações;
#
# Neste exemplo vamos utilizar Fernet para proteger
# a senha do banco de dados MySQL.

from cryptography.fernet import Fernet


# ==========================================================
# 1 - GERAR UMA CHAVE DE CRIPTOGRAFIA
# ==========================================================

# generate_key() cria uma nova chave Fernet.
#
# Essa chave será utilizada tanto para criptografar
# quanto para descriptografar a informação.
#
# IMPORTANTE:
#
# A mesma chave utilizada para criptografar deve ser
# utilizada posteriormente para descriptografar.

chave = Fernet.generate_key()


# ==========================================================
# MOSTRAR A CHAVE GERADA
# ==========================================================

print(
    "CHAVE GERADA:"
)


# Fernet.generate_key() retorna o valor no formato bytes.
#
# Exemplo:
#
# b'kT-0YWAM5PeG3d7gP6Z85...'
#
# O método decode() converte bytes para string.

print(
    chave.decode()
)


# ==========================================================
# 2 - CRIAR O OBJETO DE CRIPTOGRAFIA
# ==========================================================

# Agora criamos um objeto Fernet utilizando a chave.
#
# Esse objeto será responsável pelas operações:
#
# encrypt()
# decrypt()

fernet = Fernet(
    chave
)


# ==========================================================
# 3 - DEFINIR A SENHA ORIGINAL
# ==========================================================

# Esta é a senha original que queremos proteger.
#
# Em um cenário real, essa poderia ser:
#
# - senha do MySQL;
# - token;
# - chave de API;
# - outro segredo.
#
# Aqui utilizamos uma senha apenas para demonstração.

senha_original = "1234556"


# ==========================================================
# MOSTRAR SENHA ORIGINAL
# ==========================================================

print(
    "\nSENHA ORIGINAL:"
)

print(
    senha_original
)


# ==========================================================
# 4 - CRIPTOGRAFAR A SENHA
# ==========================================================

# Para criptografar uma informação com Fernet,
# precisamos enviar o conteúdo no formato bytes.
#
# Nossa senha atualmente é uma string:
#
# "1234556"
#
# Por isso utilizamos:
#
# senha_original.encode()
#
# para transformar:
#
# string
#   ↓
# bytes

senha_criptografada = fernet.encrypt(
    senha_original.encode()
)


# ==========================================================
# MOSTRAR SENHA CRIPTOGRAFADA
# ==========================================================

print(
    "\nSENHA CRIPTOGRAFADA:"
)


# O resultado de encrypt() também é retornado
# no formato bytes.
#
# Utilizamos decode() apenas para conseguir
# visualizar e copiar o valor como texto.
#
# Esse é o valor que pode ser colocado no .env.

print(
    senha_criptografada.decode()
)


# ==========================================================
# 5 - DESCRIPTOGRAFAR A SENHA
# ==========================================================

# Agora fazemos o processo inverso.
#
# A senha criptografada é enviada para:
#
# fernet.decrypt()
#
# O Fernet utiliza a mesma chave criada anteriormente
# para recuperar o conteúdo original.

senha_descriptografada = fernet.decrypt(
    senha_criptografada
).decode()


# O método decrypt() retorna bytes.
#
# Por isso utilizamos novamente:
#
# .decode()
#
# para transformar o resultado em string.


# ==========================================================
# MOSTRAR SENHA DESCRIPTOGRAFADA
# ==========================================================

print(
    "\nSENHA DESCRIPTOGRAFADA:"
)

print(
    senha_descriptografada
)