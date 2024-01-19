from  validators import *

pin = input('Pin')
password = input('Password')
email = input('email')
name = input('Name')

print(check_pin(pin), check_pass(password),checkjnail(email),check_name(name))
