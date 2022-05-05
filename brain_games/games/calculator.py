#!/usr/bin/env python
import random

from random import randint

ROUNDS = 3
TASK = 'What is the result of the expression?'
ops = ['+', '-', '*']


def get_game_data():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation = random.choice(ops)
    correct_answer = is_calculator(num1, operation, num2)
    question = 'Question: {0} {1} {2}'.format(num1, operation, num2)
    return question, correct_answer

def is_calculator(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    return result



