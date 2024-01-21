from  clasess.basic_word import BasicWord
from clasess.player import Player
from utils import load_random_word

url = 'https://jsonkeeper.com/b/NX3W'

def validate_word(word, words, user_words):
    if len(word) < 3:
        print("Слишком короткое слово")
        return False
    elif word not in words:
        print("неверно")
        return False
    elif word in user_words:
        print("уже использовано")
        return False
    else:
        return True

def main ():

    basis_word = load_random_word(url)

    user_name = input("Введите имя игрока:\n")
    player = Player(user_name)
    print(f"Привет, {user_name}!\n"
          f"Составте 8 слов из слова - \"{basis_word.word}\"\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите - \"Stop\"\n"
          f"Поехали, ваше первое слово?"
    )

    count_words = len(basis_word.words)
    while len(player.user_words) < count_words:
        user_answer = input()
        if user_answer.lower() in ('stop','стоп'):
            break
        elif not validate_word(user_answer, basis_word.words, player.user_words):
            print("Ошибка валидации")
            continue
        else:
            player.user_words.append(user_answer.lower())
            print("Верно")
        print(player)
main()