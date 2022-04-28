#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    number = randint(2, 100)
    question = 'Question: {}'.format(number)
    if is_prime(number):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer


def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1
    return count > 2
