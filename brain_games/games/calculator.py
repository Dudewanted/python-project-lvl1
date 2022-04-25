#!/usr/bin/env python

import prompt

import random

from random import randint

TASK = 'What is the result of the expression?'
WRONG = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!"
ops = ['+', '-', '*']
def game_data():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation = random.choice(ops)
    correct_answer = eval(str(num1) + operation + str(num2))
    question = 'Question: {0} {1} {2}'.format(num1, operation, num2)
    return question, correct_answer

          
#def game_calc():
#    print('Welcome to the Brain Games!')
#    name = prompt.string('May I have your name? ')
#    print('Hello, {}!'.format(name))
#    print('What is the result of the expression?')
#    counter = 0
#    while counter < 3:
#        ops = ['+', '-', '*']
#        num1 = randint(0, 100)
#        num2 = randint(0, 100)
#        operation = random.choice(ops)
#        print('Question: {} {} {}'.format(num1, operation, num2))
#        maths = eval(str(num1) + operation + str(num2))
#        answer = prompt.string('Your answer: ')
#        if str(maths) == answer:
#            print('Correct!')
#            counter += 1
#        else:
#            return print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
#                         "Let's try again, {}!".format(answer, maths, name))
#    print('Congratulations, {}!'.format(name))
