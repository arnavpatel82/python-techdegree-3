# Import your Game class
from game import Game
# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

if __name__ == "__main__":

    y_or_n = (input("do you want to play the phrase hunter game? ")).lower()

    while True:
        while y_or_n != 'y' and y_or_n != 'n':
            print("Please only enter 'y' or 'n'")
            y_or_n = input("do you want to play the phrase hunter game? ")

        if y_or_n == 'y':
            print()
            game = Game()
            game.start()
            print()
            y_or_n = input("do you want to play the phrase hunter game again? ")
        else:
            print('Bye!')
            break
        
