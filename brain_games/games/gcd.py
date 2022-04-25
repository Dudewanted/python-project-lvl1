#!/usr/bin/env python

from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def game_data():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    question = 'Question: {0} {1}'.format(num1, num2)
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    correct_answer = num1 or num2
    return question, correct_answer
