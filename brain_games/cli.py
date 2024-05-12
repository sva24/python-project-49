import prompt


def welcome_user():
    """Функция для приветствия пользователя"""

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
