from random import randint
import prompt
from brain_games.scripts.brain_engine import play_game


def even_game():
    """Функция для игры в чёт-нечёт"""

    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = randint(1, 100)
    print('Question:', number)
    answer = prompt.string('Your answer: ')
    correct = 'yes' if number % 2 == 0 else 'no'
    return answer, correct


def main():
    play_game(even_game)


if __name__ == "__main__":
    main()
