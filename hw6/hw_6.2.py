import random
name = input('Enter your name:\n')
user_points = 0
max_points = 0
count_games = 0

with open('words.txt') as f:
    for word in f:
        word  = word.rstrip('\n')
        user_answer = input(f"Guess the word {''.join((random.sample(word,len(word))))}: ")
        if user_answer == word:
            print('Right! You got 10 points.')
            user_points += 10
        else:
            print(f'Wrong! Right answer is {word}.')


with open('history.txt', 'a') as f:
    f.write(f'{name} {user_points}\n')


with open('history.txt') as f:
    for raw in f:
        _, points = raw.split()
        points = int(points)
        count_games += 1
        if points > max_points:
            max_points = points

print(f'There are {count_games} games played in total\n'
      f'Maximum record: {max_points}')