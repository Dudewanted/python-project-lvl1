#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_data():
    number = randint(0, 100)
    question = 'Question: {}'.format(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
