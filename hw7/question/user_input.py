def parse_input():
    """Делит ввод пользователя на категорию и число"""
    category, price = input("Enter question:\n").split()
    return category, price