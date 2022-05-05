#!/usr/bin/env python

from random import randint

ROUNDS = 3
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    number = randint(0, 100)
    question = 'Question: {}'.format(number)
    if is_parity_checker(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

def is_parity_checker(number):
    if number % 2 == 0:
        return True
