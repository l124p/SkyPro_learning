from load_data import load_questions
def show_fileld():
    """выводит игровое поле"""
    questions = load_questions()
    for category, prices in questions.items():
        print('-'*44)
        print(f"| {category.ljust(15)}|",end='')
        for price in prices:
            print(f"  {price}  |",end=' ')
            pass
        print()
    print('-' * 44)
