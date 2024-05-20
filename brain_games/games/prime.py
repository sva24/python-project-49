from random import randint
import prompt


def is_prime(a: int) -> bool:
    """
    Функция определения простое ли число
    """
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def prime_game():
    """
    Функция для игры в простое число
    """
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = randint(2, 15)
    print('Question:', n)
    answer = prompt.string('Your answer: ')
    correct = 'yes' if is_prime(n) else 'no'
    return answer, correct
