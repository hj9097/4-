class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.numTries= 0
        self.guessedChars = []
        self.currentStatus = '_' * len(self.secretWord)


    def display(self):
        print("failed number:" + str(self.numTries))
        print("guessed chars:" + str(self.guessedChars))
        print("current status:" + self.currentStatus)





    def guess(self, character):
        self.guessedChars.append(character)
        if character in self.secretWord:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
        else:
            self.numTries += 1

        if self.currentStatus == self.secretWord:
            finished = True
        else:
            finished = False
        return finished


