#!/usr/bin/env python

import prompt

import random

from random import randint


def game_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        ops = ['+', '-', '*']
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        operation = random.choice(ops)
        print('Question: {} {} {}'.format(num1, operation, num2))
        maths = eval(str(num1) + operation + str(num2))
        answer = prompt.string('Your answer: ')
        if maths == int(answer):
            print('Correct!')
            counter += 1
        else:
            return print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                         "Let's try again, {}!".format(answer, maths, name))
    print('Congratulations, {}!'.format(name))
