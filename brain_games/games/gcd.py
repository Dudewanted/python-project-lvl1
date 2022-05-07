#!/usr/bin/env python

from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    question = 'Question: {0} {1}'.format(number1, number2)
    correct_answer = get_gcd(number1, number2)
    return question, correct_answer


def get_gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 >= number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 or number2
