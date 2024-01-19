
balls = 0
count = 0
print('Hello! Will be check english  skill ')
name = input('What is your name? ')
print(f"Hello, {name}, start train")

first_question = 'My name __ Vova'
first_answer = 'is'
second_question = 'I __ a coder'
second_answer = 'am'
third_question = 'I live __ Moscow'
third_answer = 'in'

user_answer = input(first_question)
if user_answer == first_answer:
    print('Right\nYou get 10 balls')
    balls += 10
    count += 1
else:
    print('Answer is not right')
    print(first_answer)

user_answer = input(second_question)
if user_answer == second_answer:
    print('Right\nYou get 10 balls')
    balls += 10
    count += 1
else:
    print('Answer is not right')
    print(second_answer)

user_answer = input(third_question)
if user_answer == third_answer:
    print('Right\nYou get 10 balls')
    balls += 10
    count += 1
else:
    print('Answer is not right')
    print(third_answer)

print('That is all')
print(f'You answered {count} questions')
print(f'We earned {balls} balls')
print(f'This is {balls/30*100} percent')