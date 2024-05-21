from random import randint
GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(a: int, b: int) -> str:
    """
    Функция вычисления НОД
    """
    while b != 0:
        a, b = b, a % b
    return str(abs(a))


def gcd_game():
    """
    Функция для игры в НОД
    """

    number_a = randint(1, 50)
    number_b = randint(1, 50)
    question = str(number_a) + ' ' + str(number_b)
    correct = get_gcd(number_a, number_b)
    return correct, question
