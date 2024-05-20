from random import randint
from random import choice
import prompt


def progression_game():
    """
    Функция для игры в арифметическую прогрессию
    """

    print('What number is missing in the progression?')
    range_progression = randint(5, 10)
    start = randint(1, 20)
    step = randint(1, 20)
    progression = [start + i * step for i in range(range_progression)]
    correct = choice(progression)
    print('Question:', end=' ')
    for n in progression:
        if n == correct:
            print('..', end=' ')
        else:
            print(n, end=' ')

    answer = prompt.string('\nYour answer: ')
    return answer, str(correct)
