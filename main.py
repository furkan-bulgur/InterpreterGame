from game import Game
import os


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



# now, to clear the screen

def main():
    game = Game()
    game.start_game()

    while True:
        try:
            try:
                text = input('>>> ')
            except NameError:  # Python3
                text = input('>>> ')
        except EOFError:
            break
        if not text:
            continue

        game.run_command(text)


if __name__ == "__main__":
    main()