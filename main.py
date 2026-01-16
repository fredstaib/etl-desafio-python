# =========================
# EXTRACT
# =========================
users = [
    {"id": 1, "name": "Ana", "mensagem":"" },
    {"id": 2, "name": "Carlos", "mensagem":"" },
    {"id": 3, "name": "Mariana", "mensagem":"" }
]

# =========================
# TRANSFORM
# =========================
def gerar_mensagem(user):
    return f"Olá, {user['name']}! Seja bem-vindo(a) ao nosso sistema."


for user in users:
    mensagem = gerar_mensagem(user)
    user["mensagem"] = mensagem


# =========================
# LOAD
# =========================
for item in users:
    print(f"Usuário {item['id']}: {item['mensagem']}")

