#!/usr/bin/env python
import prompt

ROUNDS = 3


def engine_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.TASK)
    for i in range(ROUNDS):
        question, correct_answer = game.get_game_data()
        print(question)
        answer = prompt.string('Your answer: ')
        if str(correct_answer) == answer.lower():
            print('Correct!')
        else:
            return print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\n"
                         "Let's try again, {2}!"
                         .format(answer, correct_answer, name))
    print('Congratulations, {}!'.format(name))
