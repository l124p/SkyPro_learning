def show_question(category, price, questions):
    """Печатает вопрос"""
    # print(questions[category.title()][price]['asked'])
    if not questions.get(category.title(), False):
        print('Нет такой категории. Попробуйте еще раз')
        return False
    elif not questions[category.title()].get(price, False):
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
