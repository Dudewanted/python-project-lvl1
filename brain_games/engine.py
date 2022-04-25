#!/usr/bin/env python
import prompt


def engine_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.TASK)
    for i in range(3):
        question, correct_answer = game.game_data()
        print(question)
        answer = prompt.string('Your answer: ')
        if str(correct_answer) == answer.lower():
            print('Correct!')
        else:
            return print(game.WRONG.format(answer, correct_answer, name))
    print('Congratulations, {}!'.format(name))