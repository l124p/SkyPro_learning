class Player:

    def __init__(self, name):
        self.name = name
        self.user_words = []
    def count(self):
        """Возвращает количество угаданных слов"""
        return len(self.user_words)

    def add_word(self, word):
        """Добавляет слово в список угаданных слов"""
        self.user_words.append(word)

    def check_word(self, word):
        """Проверяет использовано ли уже слово"""
        return word.lower() in self.user_words

    def __repr__(self):
        return f"Игрок: {self.name}. Угаданные слова: {self.user_words}"
