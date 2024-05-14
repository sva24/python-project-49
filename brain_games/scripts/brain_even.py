from random import randint
import prompt


def main():
    """Функция для игры в чёт-нечёт"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 3
    while attempt > 0:

        number = randint(1, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        correct = 'yes' if number % 2 == 0 else 'no'
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
