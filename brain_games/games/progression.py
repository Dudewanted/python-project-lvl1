#!/usr/bin/env python
import random

TASK = 'What number is missing in the progression?'


def get_game_data():
    number = random.randint(1, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    index = random.randint(0, length - 1)
    progression = []
    correct_answer = 0
    for i in range(length):
        number += step
        if i != index:
            progression.append(number)
        else:
            progression.append('..')
            correct_answer = number
    convert_list = ' '.join(map(str, progression))
    question = '{}'.format(convert_list)
    return question, correct_answer
