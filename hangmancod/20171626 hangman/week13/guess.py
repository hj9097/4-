class Guess:

    def __init__(self, word):

        self.numTries = 0
        self.guessedChars = []
        self.secretWord = word
        self.currentStatus = "-"*len(self.secretWord)


    def display(self):
        print("Current :", self.currentStatus)
        print("Tries : ", self.numTries)


    def guess(self, character):
        character = character.lower()
        count = 0
        for i in range (len(self.secretWord)):
            if self.secretWord[i] == character:
                self.currentStatus = self.currentStatus[:i] + character  + self.currentStatus[i+1:]
                self.guessedChars.append(character)
                count += 1
        if count == 0:
            self.numTries += 1
        if self.secretWord == self.currentStatus:
            return True