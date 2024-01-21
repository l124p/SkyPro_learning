import json
import requests
import random
from clasess.basic_word import BasicWord

def load_random_word(url):
    """Получить список слов с внешнего ресурса
    вернуть случайное слово
    создать экземпляр класса BasicWord
    вернуть этот экземпляр"""
    response = requests.get(url, verify=False)
    data_words = json.loads(response.text)
    data_word = random.choice(data_words)
    #print(data_word['word'])

    basic_word = BasicWord(data_word['word'], data_word['subwords'])

    return basic_word


