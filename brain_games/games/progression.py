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
    start_prog = randint(1, 20)
    step_prog = randint(1, 20)
    range_prog = randint(5, 10)
    progression = generate_progression(start_prog, step_prog, range_prog)
    correct = choice(progression)
    question = ' '.join(['..' if n == correct else str(n) for n in progression])
    return str(correct), question
