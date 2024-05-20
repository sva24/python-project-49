from random import randint
import prompt


def gcd_game():
    """
    Функция для игры в НОД
    """

    print('Find the greatest common divisor of given numbers.')
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    print('Question:', number_a, number_b)
    answer = prompt.string('Your answer: ')
    while number_a != 0 and number_b != 0:
        if number_a >= number_b:
            number_a %= number_b
        else:
            number_b %= number_a
    correct = str(number_a or number_b)
    return answer, correct
