 # Python hangman
from console import console
from time import sleep
from hangman_pics import HANGMAN_PICS

def get_word():
    word = console.input("[bold red]Ingrese la palabra a adivinar: [/]")
    console.print("[frame blink green]Iniciando juego...[/]")
    sleep(2)
    console.clear()
    return word

def draw_hangman(stage):
    """Draw hangman on the console. Stage 0 is complete hangman, 6 is no hangman."""
    
    console.print(HANGMAN_PICS[stage], style="deep_pink4")
    console.print()

def start_guessing(word):
    word_str = word
    word = list(word)

    # Wait for player
    console.print("[green]Ya estás aquí?[/][italic] Presionar Enter si es así...[/]")
    while input() != "":
        console.print("[blue]Es eso un sí?[/] Presionar Enter para continuar")

    console.print("Perfecto!", style="bold red")
    sleep(1)

    guessed_word = ["__ "] * len(word)
    alert = ""
    stage = 0
    lose_state = 0 # 1 if player loses

    # Start game
    while guessed_word != word:
        console.clear()
        console.print(guessed_word, style="blue")

        if alert:
            console.print()
            console.print(alert, style="red")
            alert = ""

        draw_hangman(stage)

        guessed_char = console.input("[bold red]Cuál será la primer letra?: [/]")

        # Check for a valid char
        if guessed_char == "" or len(guessed_char) != 1:
            alert = "Ese no es un caracter correcto :C"
            continue

        # Continue game if valid char
        if guessed_char in word:
            i = word_str.find(guessed_char)
            guessed_word[i] = f"{guessed_char}"
            alert = "Bien! Adivinaste una letra!"
        else:
            if stage != 5:
                stage += 1
                alert = "Oh no! Te equivocaste! Intenta de nuevo!"
            else:
                lose_state = 1
                break

    # Finish the game
    console.clear()

    if lose_state != 1:
        console.print("Felicidades!!! Ganaste el juego!!!", style="bold green")
    else:
        draw_hangman(6)
        console.print()
        console.print("Lo siento. Perdiste el juego :c", style="bold red")

    console.print("\nPresiona Enter para finalizar el juego", style="white")
    console.input()

if __name__ == "__main__":
    console.clear()

    word = get_word()
    start_guessing(word)