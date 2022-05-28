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

    def get_guess(self, guess):
        self.guesses.append(guess)

    def welcome(self):
        print("============================")
        print("Welcome to the Phrase Hunter Game")
        print("============================")
    
    def game_over(self):
        pass

    def start(self):
        pass