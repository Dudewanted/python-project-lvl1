#!/usr/bin/env python
import random


TASK = 'What number is missing in the progression?'


def game_data():
    num = random.randint(1, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    index = random.randint(0, length - 1)
    mas = []
    correct_answer = 0
    for i in range(length):
        num += step
        if i != index:
           mas.append(num)
        else:
           mas.append('..')
           correct_answer = num
    convertList = ' '.join(map(str, mas))
    question = 'Question: {}'.format(convertList)
    return question, correct_answer
