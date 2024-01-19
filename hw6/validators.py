# task 4 -----------------------------------------
import re


def check_pin(pin):
    """Check pin to 4 letter. Don't contain the same numbers and 1234"""
    return len(pin) == 4 and pin != '1234' and len(set([i for i in pin])) == 4


def check_pass(password: str) -> bool:
    """Check password to > 8 letter, include letter and numbers"""
    return len(password) > 8 and bool(re.match("^[A-Za-z0-9]*$", password))


def checkjnail(email: str) -> bool:
    """Check @ and . """
    return '@' in email and '.' in email


def check_name(name):
    """Check only russian letter and ' '"""
    return bool(re.match("^[А-Яа-я ]*$", name))

assert check_pin('1239') == True , 'Error pin'
assert check_pin('3333') == False, 'Error pin'
assert check_pin('1234') == False, 'Error pin'
assert check_pin('000011') == False, 'Error pin'
assert check_pin('8765') == True, 'Error pin'

assert check_pass('secretdOOr') == True, 'Error password'
assert check_pass('huskyeye5') == True, 'Error password'
assert check_pass('secret') == False, 'Error password'
assert check_pass('m3wm3wm3w') == True, 'Error password'
assert check_pass('fh43j_!') == False, 'Error password'

assert checkjnail('local@skypro') == False, 'Error email'
assert checkjnail('voutattsky.Dro') == False, 'Error email'
assert checkjnail('me(g)sky.pro') == False, 'Error email'
assert checkjnail('@lizaveta') == False, 'Error email'
assert checkjnail('alarm(q)qmail.com') == False, 'Error email'

assert check_name('Даниl') == False, 'Error name'
assert check_name('Р_и_т_а') == False, 'Error name'
assert check_name('Константин') == True, 'Error name'
assert check_name('АФ') == True, 'Error name'
assert check_name('Елена') == True, 'Error name'