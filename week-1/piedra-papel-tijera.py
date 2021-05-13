import random


def who_won(player1, player2):
    print("Jugador = ", player1, ", Computador = ", player2)
    if player1 == "Piedra" and player2 == "Tijeras":
        return "player1"
    elif player1 == "Papel" and player2 == "Piedra":
        return "player1"
    elif player1 == "Tijeras" and player2 == "Papel":
        return "player1"
    elif player1 == "Tijeras" and player2 == "Piedra":
        return "Computer"
    elif player1 == "Piedra" and player2 == "Papel":
        return "Computer"
    elif player1 == "Papel" and player2 == "Tijeras":
        return "Computer"
    else:
        print("Empate")
        return "Empate"


def juego():
    still_playing = True
    player_one = 0
    computer = 0
    options = {"1": "Piedra", "2": "Papel", "3": "Tijeras"}
    while still_playing:
        print("""
===============
Escoja:
1. Piedra
2. Papel
3. Tijeras
===============""")
        choice = int(input(" = "))
        while(choice < 1 or choice > 3):
            choice = int(input("Ingrese un numero valido = "))
        computer_choice = random.randint(1, 3)
        result = who_won(options.get(str(choice)),options.get(str(computer_choice)))
        if result == "player1":
            player_one += 1
            print("Jugador = ", player_one, ", Computador = ", computer)
            if player_one == 2:
                print("Has ganado!")
                still_playing = False
        elif result == "Computer":
            computer += 1
            print("Jugador = ", player_one, ", Computador = ", computer)
            if computer == 2:
                print("Has perdido!")
                still_playing = False
    print("""
===============
Deseas volver a jugar:
1. Si
2. No
===============""")
    choice = int(input(" = "))
    if choice == 1:
        juego()


def run():
    print("""Datacademy | Kenneth Calvo
    Projecto 1 | Python | Reto 2
    Juego Piedra, Papel o Tijeras""")

    juego()

    print("Gracias por usar la aplicacion, nos vemos!")


if __name__ == '__main__':
    run()