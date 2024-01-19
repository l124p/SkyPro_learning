easy = {
    "OK": "Нормально",
    "Fife": "пять",
    "ten": "десять",
    "nine": "девять",
    "two": 'два'
}

medium = {
    "mouse": 'мышь',
    "cat": ['кот', 'кошка'],
    "dog": 'собака',
    'duck': 'утка',
    'bear': 'медведь'
}

hard = {
    "red": 'красный',
    "blue": 'синий',
    "black": 'черный',
    'white': 'белый',
    'yellow': 'желтый'
}

levels = {
    0: "null",
    1: "so-so",
    2: "can better",
    3: "Fine",
    4: "Good",
    5: "Great",

}
# ОТветы пользователя
results = {}

level = input(f'Select difficulty level\n'
              f'easy, medium, hard\n')
print(f'Selected {level} difficutly level, we will offer five words, choose a translation'
      )
#words = dict()
match level.lower():
    case 'easy':
        words = easy.copy()
    case 'medium':
        words = medium.copy()
    case 'hard':
        words = hard.copy()

for key, item in words.items():
    print(f'{key}, {len(item)} letter, starts with "{item[0]}..."')
    answer_user = input('Enter translation\n')
    print(f'Right. {key.title()} that is {item}' if answer_user == item else f'Wrong. {key.title()} that is {item}')
    results[key] = answer_user == item

right_results = [key for key, value in results.items() if value]
wrong_results = [key for key, value in results.items() if not value]
if len(right_results):
    print('Right answered words:', *right_results, sep='\n')
if len(wrong_results):
    print('Wrong answered words:', *wrong_results, sep='\n')

print('Ваш ранг:', levels[len(right_results)], sep='\n')
