#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    number = randint(2, 100)
    question = '{}'.format(number)
    if is_prime(number):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer


def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return True
