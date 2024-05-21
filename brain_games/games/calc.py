from random import choice
from random import randint


def calc_number(a: int, operation: str, b: int) -> str:
    """
    Функция вычисления
    """
    return str(eval(str(a) + operation + str(b)))


def get_game_rules():
    """Правила игры"""
    return 'What is the result of the expression?'


def calc_game():
    """
    Функция для игры в калькулятор
    """

    number_a = randint(1, 100)
    number_b = randint(1, 100)
    math_operation = choice(['+', '-', '*'])
    question = str(number_a) + ' ' + math_operation + ' ' + str(number_b)
    correct = calc_number(number_a, math_operation, number_b)
    return correct, question
