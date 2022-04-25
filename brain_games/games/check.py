#!/usr/bin/env python

import prompt

from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
WRONG = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!"
def game_data():
    number = randint(0, 100)
    question = 'Question: {}'.format(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer



# def parity_check():
#   print('Welcome to the Brain Games!')
#   name = prompt.string('May I have your name? ')
#   print('Hello, {}!'.format(name))
#   print('Answer "yes" if the number is even, otherwise answer "no".')
#   counter = 0
#   while counter < 3:
#       number = randint(0, 100)
#       print('Question: {}'.format(number))
#       answer = prompt.string('Your answer: ')
#       if number % 2 == 0 and answer.lower() == 'yes' or \
#               number % 2 != 0 and answer.lower() == 'no':
#           print('Correct!')
#           counter += 1
#       else:
#           return print("'yes' is wrong answer ;(. Correct answer was 'no'.\n"
#                        "Let's try again, {}!".format(name))
#   print('Congratulations, {}!'.format(name))
