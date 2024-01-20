import json
from question import Question


def load_question():
    lst_questions = []
    with open('question.json', 'r') as f:
        for i in json.load(f):
            lst_questions.append(Question(
                i['q'],
                int(i['d']),
                i['a']
            ))
    return lst_questions


def result(lst_questions):
    summa = 0
    count = 0
    for i in lst_questions:
        if i.is_correct():
            summa += i.get_points()
            count += 1
    print('Вот и всё')
    print(f'Отвечено {count} вопроса из {len(lst_questions)}')
    print('Набрано баллов:', summa)