# Create your Game class logic in here.

class Game:

    def __init__(self, missed, phrases, active_phrase, guesses):
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = []
    
    def get_random_phrase(self):
        pass

    def get_guess(self, guess):
        self.guesses.append(guess)

    def game_over(self):
        pass

    def start(self):
        pass