# Create your Game class logic in here.
import random
from phrase import Phrase

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = []

    def create_phrases(self):
        self.phrases.append(Phrase('hello world'))
        self.phrases.append(Phrase('there is no trying'))
        self.phrases.append(Phrase('may the force be with you'))
        self.phrases.append(Phrase('you have to see the matrix for yourself'))
        self.phrases.append(Phrase('life is like a box of chocolates'))
    
    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        while True:
            guess = input("Guess a letter: ")
            if guess.isalpha() and len(guess) == 1:
                return guess.lower()
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
        self.create_phrases()
        phrase = self.get_random_phrase()
        game_won_yet = False
        while self.missed < 5 and not game_won_yet:
            print(f'Number missed: {self.missed}')
            print(phrase.display(self.guesses))
            guess = self.get_guess()
            self.guesses.append(guess)

            if not phrase.check_letter(guess):
                self.missed = self.missed + 1
            
            game_won_yet = phrase.check_complete(self.guesses)

        self.game_over(game_won_yet)
            
        
if __name__ == "__main__":
    game = Game()
    game.start()
