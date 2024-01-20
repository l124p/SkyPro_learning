from os import system
from hw7.question.load_data import load_questions
from hw7.draw_field.draw_field import show_fileld
from hw7.question.user_input import parse_input
from hw7.question.show_question import show_question
from results.results import show_stats, save_results_to_file


def main():
    points = 0
    results = []
    questions = load_questions()
    for i in range(len(questions)*len(questions.values())):
        show_fileld(questions)
        category, price = parse_input()
        if not show_question(category, price, questions):
            continue
        answer = input('Введите ответ:\n')
        system('cls')
        points = show_stats(answer, category, price, questions, points, results)

    correct_answers = sum(results)
    incorrect_answers = len(results) - sum(results)
    print('У нас закончились вопросы')
    print(f'Ваш счет: {points}\n'
          f'Верных ответов: {correct_answers}\n'
          f'Неверных ответов: {incorrect_answers}\n')
    save_results_to_file(points, correct_answers, incorrect_answers)



main()
