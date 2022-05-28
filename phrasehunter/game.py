# Create your Game class logic in here.
import random


class Game:

    def __init__(self, missed, phrases, active_phrase, guesses):
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = []
    
    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        while True:
            guess = input("Guess a letter. ")
            if guess.isalpha() and len(guess) == 1:
                break
            else:
                print("Your guess must be a letter of the alphabet")

        self.guesses.append(guess)

    def welcome(self):
        print("============================")
        print("Welcome to the Phrase Hunter Game")
        print("============================")
        print()
    
    def game_over(self, win):
        if win:
            print("Congratulations you won!")
        else:
            print("Game over! Better luck next time!")

    def start(self):
        self.welcome()
        
