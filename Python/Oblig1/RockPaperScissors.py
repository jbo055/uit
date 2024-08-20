# Write a program that plays the popular scissor-rock-paper game. 
# (A scissor can cut a paper, a rock can knock a scissor, and a paper can wrap a rock.) 
# The program randomly generates a number 0 , 1 , or 2 representing scissor, rock, and paper. 
# The program prompts the user to enter a number 0 , 1 , or 2 and displays a message 
# indicating whether the user or the computer wins, loses, or draws.

import random

scissor = 0
rock = 1
paper = 2

# Generate a random number between 0 and 2
computer = random.randint(0, 2)
# print(computer)
human = int(input('Enter 0 for scissor, 1 for rock, or 2 for paper: '))

if computer == human:
    print('It is a draw! You both chose the same.')
elif computer == scissor and human == rock:
    print('You win! Rock knocks scissor.')
elif computer == scissor and human == paper:
    print('You lose! Scissor cuts paper.')
elif computer == rock and human == scissor:
    print('You lose! Rock knocks scissor.')
elif computer == rock and human == paper:
    print('You win! Paper wraps rock.')
elif computer == paper and human == scissor:
    print('You win! Scissor cuts paper.')
elif computer == paper and human == rock:
    print('You lose! Paper wraps rock.')
else:
    print('Invalid input!')
    