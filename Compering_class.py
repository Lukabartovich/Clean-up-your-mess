class Compering:
    def __init__(self, list_of_words):
        self.list_of_words = list_of_words

    def compere(self, word):
        self.word = word
        for i in range(len(self.list_of_words)):
            word = str(self.list_of_words[i])
            if (len(word) == len(word)) and (word[0] == self.word[0]) and (word[-1] == self.word[-1]):
                return word