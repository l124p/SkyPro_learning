from random import sample


def morse_encode(sentence: str) -> str:
    morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                  'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
                  'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                  'x': '-..-', 'y': '-.--', 'z': '--..'}
    sentence_code = []
    for symbol in sentence:
        sentence_code.append(morse.get(symbol, ''))

    return ' '.join(sentence_code)


def get_word(lst_words: list) -> list:
    words = sample(lst_words, 5)
    return words


def print_statistics(answers: list) -> None:
    count_tasks = len(answers)
    count_true_answers = answers.count(True)
    count_false_answers = count_tasks - count_true_answers
    print(f'\n\nTotal tasks: {count_tasks}\n'
          f'Correct answers: {count_true_answers}\n'
          f'Wrong answers: {count_false_answers}'
          )


list_words = ['code', 'bit', 'list', 'soul', 'next']
answers = []

input('Today we will practice decoding Morse code.\n'
      'Press "Enter" and let\'s start'
      )

i = 0
for word in get_word(list_words):
    i += 1
    morse_code = morse_encode(word)
    print(f'Word {i} - {morse_code}')
    user_answer = input()
    if user_answer == word:
        print(f'True, {word}')
        answers.append(True)
    else:
        print(f'Wrong, {word}')
        answers.append(False)


print_statistics(answers)
