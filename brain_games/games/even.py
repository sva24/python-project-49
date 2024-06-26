from random import randint
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n: int) -> bool:
    """
    Функция вычисления четного числа
    """
    return n % 2 == 0


def even_game():
    """
    Функция для игры в чёт-нечёт
    """

    question = randint(1, 100)
    correct = 'yes' if is_even(question) else 'no'
    return correct, question
