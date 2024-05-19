from random import randint
from random import choice
from random import randint
import prompt
from brain_games.scripts.brain_engine import play_game


def calc_number():
    """Функция для игры в калькулятор"""

    number_a = str(randint(1, 100))
    number_b = str(randint(1, 100))
    math_operation = choice(['+', '-', '*'])
    print('Question:', number_a, math_operation, number_b)
    answer = prompt.string('Your answer: ')
    correct = str(eval(number_a + math_operation + number_b))
    return answer, correct


def main():
    play_game(calc_number)


if __name__ == "__main__":
    main()
