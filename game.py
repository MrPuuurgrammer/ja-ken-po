import random

OPCOES = ["pedra", "papel", "tesoura"]
EMOJIS = {"pedra": "✊", "papel": "✋", "tesoura": "✌️"}


def vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    if (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "papel" and computador == "pedra")
        or (jogador == "tesoura" and computador == "papel")
    ):
        return "jogador"
    return "computador"


def jogar():
    print("=== JANKENPÔ ===")
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador not in OPCOES:
        print("Jogada inválida.")
        return

    computador = random.choice(OPCOES)
    print(f"Você: {jogador}  {EMOJIS[jogador]}")
    print(f"Computador: {computador} {EMOJIS[computador]}")

    resultado = vencedor(jogador, computador)
    if resultado == "empate":
        print("Empate!")
    elif resultado == "jogador":
        print("Você venceu!")
    else:
        print("Computador venceu!")


if __name__ == "__main__":
    jogar()
