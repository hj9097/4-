import hangman

class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = '_'*len(word)


    def display(self):
        print("Current: " + self.currentStatus)
        print("Tries : " + str(self.numTries))
        print("Guessed Chars " + str(self.guessedChars))

    def guess(self, character):

        if character not in self.guessedChars:
            self.guessedChars.append(character)

        if character not in self.secretWord:
            self.numTries += 1
        else:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
            if self.secretWord == self.currentStatus:
                return True