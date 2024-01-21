class Player:
    name = '' # Имя пользователя
    user_words = [] #Использованные слова пользователя

    def __init__(self, name):
        self.name = name
    def count(self):
        pass
    #Подсчет использованных слов

    def add_word(self, word):
        self.user_words.append(word)
        pass

    def check_word(self):
        #Проверка использования данного слова до этого
        #return bool
        pass
    def __repr__(self):
        return f"Игрок: {self.name}. Угаданные слова: {self.user_words}"