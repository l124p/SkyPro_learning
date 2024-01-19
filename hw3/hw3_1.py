balls = 0
count = 0
questions = ['My name __ Vova', 'I __ a coder', 'I live __ Moscow']
answers = ['is', 'am', 'in']

print('Hello! Will be check english  skill ')

if input() == 'ready':
    for i in range(len(questions)):
        user_answer = input(f'{questions[i]}: ')
        if user_answer == answers[i]:
            print('Right')
            balls += 10
            count += 1
        else:
            print(f'Answer is not right\n'
                  f'Answer: {answers[i]}')

    print(f'That is all! '
          f'You answered {count} questions from {len(questions)}. '
          f'This is {round(balls / 30 * 100)} percent'
          )
else:
    print("You don't want to play. I am very sorry")
