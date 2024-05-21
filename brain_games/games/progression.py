from random import randint
from random import choice


def generate_progression(start: int, step: int, range_progression: int) -> list:
    """
    Функция генерации арифметической прогрессии
    """
    progression = [start + i * step for i in range(range_progression)]
    return progression


def get_game_rules():
    """Правила игры"""
    return 'What number is missing in the progression?.'


def progression_game():
    """
    Функция для игры в арифметическую прогрессию
    """

    progression = generate_progression(randint(1, 20), randint(1, 20), randint(5, 10))
    correct = str(choice(progression))
    question = '' + ' '.join(['..' if n == correct else str(n) for n in progression])
    return correct, question
