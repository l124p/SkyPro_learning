class BasicWord:

    def __init__(self, word, words):
        self.word = word #исходное слово
        self.words = words #набор доступных подслов

    def __repr__ (self):
        return f"\nСлово:{self.word}.\nНаборы со слова:{self.words}"

    def check(self, word):
        """Проверяет наличие исходного слова в списке из слов"""
        return word in self.words

    def count(self):
       """Cчитает количества возможных подслов"""
       return len(self.words)
