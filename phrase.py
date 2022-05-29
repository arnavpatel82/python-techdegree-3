# Create your Phrase class logic here.

class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses_list):
        listified_phrase = list(self.phrase)
        for num in range(len(listified_phrase)):
            if listified_phrase[num] not in guesses_list and listified_phrase[num] != ' ':
                listified_phrase[num] = '_'
        return (' '.join(listified_phrase))
        
    def check_letter(self, letter):
        return letter in self.phrase

    def check_complete(self, guesses_list):
        phrase_as_set = set(self.phrase)
        phrase_as_set.discard(' ')
        return phrase_as_set.issubset(set(guesses_list)) or phrase_as_set == set(guesses_list)


if __name__ == "__main__":
    phrase1 = Phrase('Hello world')
    print(phrase1.display(['h', 'e', 'l', 'o', 'w', 'r', 'd']))
    print(phrase1.check_complete(['h', 'e', 'l', 'o', 'w', 'r', 'd']))