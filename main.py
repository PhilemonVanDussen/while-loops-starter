# PJ VanDussen
# 11/25/24
# While loops

# Guess game
# import random

# name = input('Hello what is your name? ')
# number = random.randint(1, 100)
# print(f'Hi {name} im thinking od a number between 1 and 100.')
# guesses_taken = 0

# while guesses_taken < 5:
#     guess = input('Enter a guess: ')
#     guess = int(guess)
#     guesses_taken = guesses_taken + 1
#     if guess < number:
#         print('That was too low.')
#     elif guess > number:
#         print('That was too high')
#     else:
#         break
   
# if guess == number:
#     print(f'You won {name}!!!!!!!!!!!!!!! Good Job')
# else:
#     print(f'You lose, the number was {number}, try again')

# Average Temperature
temps = []
user_int = 0
while user_int != -9999 :
    user_int = int(input('Enter a temperature in Fahrenheit (-9999 to quit) '))
    temps.append(user_int)

temps.pop()

list_length = len(temps)
if list_length > 0:
    print(f'Temperatures entered: {temps}')
    average_temp = sum(temps) / len(temps)
    print(f'Average temperature: {average_temp}')
else:
    print('No temperatures entered')








