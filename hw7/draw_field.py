from load_data import load_questions
def show_fileld(questions):
    """выводит игровое поле"""
    for category, prices in questions.items():
        print('-'*44)
        print(f"| {category.ljust(15)}|",end='')
        for price in prices:
            if prices[price]['asked']:
                print(f"  {price}  |",end=' ')
            else:
                print(f"  --- |", end=' ')
            pass
        print()
    print('-' * 44)

#show_fileld()