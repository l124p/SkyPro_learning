from load_data import load_questions
from draw_field import show_fileld
def parse_input():
    """Делит ввод пользователя на категорию и число"""
    category, price = input("Enter question:\n").split()
    return category, price
def show_question(category, price, questions):
    """Печатает вопрос"""
    #print(questions[category.title()][price]['asked'])
    if not questions.get(category.title(),False):
        print('Нет такой категории. Попробуйте еще раз')
        return False
    elif not questions[category.title()].get(price,False):
        print('Нет такого вопроса. Попробуйте еще раз')
        return False
    elif not questions[category.title()][price]['asked']:
            print('Вопрос уже был задан. Попробуйте еще раз')
            return False
    else:
        quest = questions[category.title()][price].get('question')
        print(f"Слово {quest} в переводе означает?")
        questions[category.title()][price]['asked'] = False
        return True


def show_stats(point, result):
    """Выводит статистику"""
    pass

def count_results(answer, category, price, questions):
    if answer == questions[category.title()][price].get('answer'):
       return int(price) , 1
    else:
        return -int(price), 0
def save_results_to_file(answer):
    """Записывает резулбтаты в JSON файл"""
    pass

def main():

    questions = load_questions()
    #print(questions)
    for i in range(5):
        show_fileld(questions)
        category, price = parse_input()
        if not show_question(category, price, questions):
            continue
        answer = input('Введите ответ:\n')
        point, result = count_results(answer, category, price, questions)
        show_stats(point, result)
        save_results_to_file(answer)
main()