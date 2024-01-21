import json
import requests
import random
from clasess.basic_word import BasicWord

def load_random_word(url):
    """Получает список слов с внешнего ресурса,
    создает экземпляр класса BasicWord,
    возвращает экземпляр класса BasicWord"""

    response = requests.get(url, verify=False)
    data_words = json.loads(response.text)
    data_word = random.choice(data_words)
    basic_word = BasicWord(data_word['word'], data_word['subwords'])

    return basic_word

def validate_word(word, player, basic_word):
    if len(word) < 3:
        print("Слишком короткое слово")
        return False
    elif not basic_word.check(word):
        print("неверно")
        return False
    elif player.check_word(word):
        print("уже использовано")
        return False
    else:
        return True
