from random import sample
from utils import load_question, result


def choose_question(lst_questions):
    """Возвращает вопросы из файла в случайном порядке"""
    print("Программа: Игра начинается")
    for quest in sample(lst_questions, len(lst_questions)):
        print("Программа:")
        print(quest.build_question())
        print("Пользователь:")
        quest.user_answer = input()

        if quest.is_correct():
            print(quest.build_positive_feedback())
        else:
            print(quest.build_negative_feedback())


def main():
    lst_question = load_question()
    #print(lst_question)

    choose_question(lst_question)

    result(lst_question)


main()
