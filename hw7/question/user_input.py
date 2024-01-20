def parse_input():
    """Делит ввод пользователя на категорию и число"""
    while True:
        try:
            category, price = input("Enter question:\n").split()
            break
        except ValueError:
            print("Ошибка выбора вопроса повторите ввод")
            continue

    return category, price