#!/usr/bin/env python
import random


TASK = 'What number is missing in the progression?'


def game_data():
    num = random.randint(1, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    mas = []
    for i in range(length):
        num += step
        mas.append(num)
    correct_answer = random.choice(mas)
    convertList = ' '.join(map(str,mas))
    hidden_mas = convertList.replace(str(correct_answer), '..')
    question = 'Question: {}'.format(hidden_mas)
    return question, correct_answer