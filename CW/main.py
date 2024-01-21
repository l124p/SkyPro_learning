from clasess.player import Player
from utils import load_random_word, validate_word

url = 'https://jsonkeeper.com/b/NX3W'



def main ():

    basic_word = load_random_word(url)

    user_name = input("Введите имя игрока:\n")
    player = Player(user_name)
    print(f"Привет, {user_name}!\n"
          f"Составте 8 слов из слова - \"{basic_word.word}\"\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите - \"Stop\"\n"
          f"Поехали, ваше первое слово?"
    )

    count_words = basic_word.count()
    while len(player.user_words) < count_words:
        user_answer = input("Введите слово:\n")
        if user_answer.lower() in ('stop','стоп'):
            break
        elif not validate_word(user_answer, player, basic_word):
            continue
        else:
            player.user_words.append(user_answer.lower())
            print("Верно")
        #print(player)

    print(f"Игра завершена, вы угадали {len(player.user_words)} слов")
main()