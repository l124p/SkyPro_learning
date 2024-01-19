
# task 1-----------------------------------------

errors = {
"out": "Вы вышли из системы ",
"noaccess": "У вас нет доступа в этот раздел", "unknown": "Неизвестная ошибка",
"timeout": "Система долго не отвечает",
"robot": "Ваши действия похожи на робота",
}

def get_errors(*args):
    errors_ru = []
    for error in args:
        errors_ru.append(errors[error])
    return errors_ru

print(*get_errors('out', 'robot'), sep=',')

# task 2 -----------------------------------------

def draw_carpet(w, h):
    first_line = chr(179) + chr(219)*(h-2) + chr(178)
    print(first_line)

draw_carpet(4,4)

# task 3 -----------------------------------------
def shift_encoding(string: str) -> str:
    str_encoding = ''
    for letter in string:
        str_encoding += chr(ord(letter) + 1)
    return str_encoding

def shift_decoding(string: str) -> str:
    str_decoding = ''
    for letter in string:
        str_decoding += chr(ord(letter) - 1)
    return str_decoding
string = input()
string_encoding = shift_encoding(string)
print(string_encoding)
print(shift_decoding(string_encoding))


