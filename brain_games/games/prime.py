#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(number):
    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1
    return count <= 1 

def game_data():
    number = randint(0, 100)
    count = 0
    question = 'Question: {}'.format(number)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
