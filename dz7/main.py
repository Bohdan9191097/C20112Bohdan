
class WordLengths:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word_length = len(self.words[self.index])
        self.index += 1
        return word_length

user_input = input("Введіть слова через пробіл: ")
words = user_input.split()

for length in WordLengths(words):
    print(length)