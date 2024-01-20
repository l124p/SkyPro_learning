import json


path = 'results.json'
def show_stats(answer, category, price, questions, points, results):

    if answer == questions[category.title()][price].get('answer'):
        points += int(price)
        results.append(True)
        print(f'Верно, +{price}. Ваш счёт  = {points}')
        return points
    else:
        points -= int(price)
        results.append(False)
        print(f"Неверно, на самом деле - {questions[category.title()][price]['answer']}."
              f" -{price}. Ваш счёт  = {points}")
        return points


def save_results_to_file(points, correct_answers, incorrect_answers):
    """Записывает результаты в JSON файл"""

    with open(path, 'r') as f:
         results_all = json.load(f)

    results_all.append({'points': points,
                   'correct_answers': correct_answers,
                   'incorrect_answers': incorrect_answers})

    with open('results.json', 'w') as f:
        json.dump(results_all, f)

