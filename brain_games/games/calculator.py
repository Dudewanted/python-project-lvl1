#!/usr/bin/env python
import random

from random import randint

TASK = 'What is the result of the expression?'
ops = ['+', '-', '*']


def game_data():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation = random.choice(ops)
    correct_answer = eval(str(num1) + operation + str(num2))
    question = 'Question: {0} {1} {2}'.format(num1, operation, num2)
    return question, correct_answer
