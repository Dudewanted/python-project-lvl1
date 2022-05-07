#!/usr/bin/env python
import random

from random import randint

ROUNDS = 3
TASK = 'What is the result of the expression?'
ops = ['+', '-', '*']


def get_game_data():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation = random.choice(ops)
    correct_answer = calculate_result(number1, operation, number2)
    question = 'Question: {0} {1} {2}'.format(number1, operation, number2)
    return question, correct_answer


def calculate_result(number1, operation, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    return result
