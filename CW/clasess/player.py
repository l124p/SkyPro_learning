class Player:

    def __init__(self, name):
        self.name = name
        self.user_words = []
    def count(self):
        """Возвращает количество угаданных слов"""
        return len(self.user_words)

    def add_word(self, word):
        self.user_words.append(word)
        pass

    def check_word(self, word):
        """Проверка использовано ли уже слово"""
        return word in self.user_words

    def __repr__(self):
        return f"Игрок: {self.name}. Угаданные слова: {self.user_words}"
