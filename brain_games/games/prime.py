#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    number = randint(0, 100)
    count = 0
    question = 'Question: {}'.format(number)
    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1
    if count > 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return question, correct_answer
