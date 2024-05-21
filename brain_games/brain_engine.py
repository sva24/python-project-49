import prompt
ATTEMPT = 3


def play_game(game_name, get_game_rules):
    """
    Основной движок для игр.
    Сюда вынесено всё взаимодействие с игроком
    """
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    rules = get_game_rules
    print(rules)
    attempt = ATTEMPT
    while attempt > 0:
        correct, question = game_name()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return None
        attempt -= 1
    print(f'Congratulations, {name}!')
