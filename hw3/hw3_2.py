balls = 0
count = 0
count_attempts = 0
questions = ['My name __ Vova', 'I __ a coder', 'I live __ Moscow']
answers = ['is', 'am', 'in']

print(f'Hello! Will be check english  skill.\n'
      f'Enter "ready" to start')

if input() == 'ready':

    for i in range(len(questions)):
        user_answer = input(f'{questions[i]}: ')
        count_attempts = 3
        while True:
            count_attempts -= 1
            if user_answer == answers[i]:
                print('Right')
                balls += 3
                count += 1
                break
            elif count_attempts > 0:
                print(f'attempts left {count_attempts}. Try again.')
                user_answer = input(f'{questions[i]}: ')
                if user_answer == answers[i]:
                    print('Right')
                    balls += count_attempts
                    count += 1
                    break
            else:
                print(f'Answer is not right\n'
                      f'Answer: {answers[i]}')
                break

    print(f'That is all! '
          f'You answered {count} questions from {len(questions)}. '
          f'This is {round(balls / 30 * 100)} percent. '
          f'You earned {balls} balls'
          )
else:
    print("You don't want to play. I am very sorry")
