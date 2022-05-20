#!/usr/bin/env python

from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    question = '{0} {1}'.format(first_number, second_number)
    correct_answer = get_gcd(first_number, second_number)
    return question, correct_answer


def get_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number >= second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return first_number or second_number
