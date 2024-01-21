class BasicWord:
    word = '' #исходное слово
    words = []#набор доступных подслов

    def __init__(self, word, words):
        self.word = word
        self.words = words

    def __repr__ (self):
        return f"\nСлово:{self.word}.\nНаборы со слова:{self.words}"

    def check(self):
        pass
    #Проверка исходного слова в списке

    def count(self):
        pass
    #Подсчет количества подслов