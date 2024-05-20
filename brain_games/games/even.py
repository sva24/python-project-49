from random import randint
import prompt


def even_game():
    """
    Функция для игры в чёт-нечёт
    """

    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = randint(1, 100)
    print('Question:', number)
    answer = prompt.string('Your answer: ')
    correct = 'yes' if number % 2 == 0 else 'no'
    return answer, correct
