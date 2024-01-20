import json

path = 'question/questions.json'


def load_questions():
    """Загружает вопросы из файла"""
    with open(path, encoding='UTF-8') as f:
        questions = json.load(f)
    return questions
