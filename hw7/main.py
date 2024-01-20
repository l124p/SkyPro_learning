from load_data import load_questions
from draw_field import show_fileld
def parse_input():
    """Делит ввод пользователя на категорию и число"""
    category, price = input("Enter question:\n").split()
    return category, price
def show_question(category, price, questions):
    """Печатает вопрос"""
    print(f"Слово {questions[category.title()][price]['question']} в переводе означает?")
    questions[category.title()][price]['asked'] = False
    questions[category.title()][price] = '---'
    print(questions)

def show_stats():
    """Выводит статистику"""
    pass

def save_results_to_file(answer):
    """Записывает резулбтаты в JSON файл"""
    pass

def main():

    questions = load_questions()
    #print(questions)
    for i in range(5):
        show_fileld()
        category, price = parse_input()
        show_question(category, price, questions)
        answer = input('Введите ответ:\n')
        save_results_to_file(answer)
main()