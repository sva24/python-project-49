#!/usr/bin/env python3
from random import randint
import prompt


def main():
    """Функция для игры в чёт-нечёт"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('What is the result of the expression?')
    attempt = 3
    while attempt > 0:

        number_a = randint(1, 100)
        number_b = randint(1, 100)
        print('Question:', number_a, ' + ', number_b)
        answer = prompt.string('Your answer: ')
        correct = str(number_a + number_b)
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return None
        attempt -= 1
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
