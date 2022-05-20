#!/usr/bin/env python
import random

from random import randint

TASK = 'What is the result of the expression?'
ops = ['+', '-', '*']


def get_game_data():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operation = random.choice(ops)
    correct_answer = calculate_result(first_number, operation, second_number)
    question = '{0} {1} {2}'.format(first_number, operation, second_number)
    return question, correct_answer


def calculate_result(first_number, operation, second_number):
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    return result
