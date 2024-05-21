from random import randint


def get_gcd(a: int, b: int) -> str:
    """
    Функция вычисления НОД
    """
    while b != 0:
        a, b = b, a % b
    return str(abs(a))


def get_game_rules():
    """Правила игры"""
    return 'Find the greatest common divisor of given numbers.'


def gcd_game():
    """
    Функция для игры в НОД
    """

    number_a = randint(1, 50)
    number_b = randint(1, 50)
    question = str(number_a) + ' ' + str(number_b)
    correct = get_gcd(number_a, number_b)
    return correct, question
