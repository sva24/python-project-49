# from brain_games.games.even import even_number
import prompt


def play_game(game_name):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    attempt = 3
    while attempt > 0:
        answer, correct = game_name()
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return None
        attempt -= 1
    print(f'Congratulations, {name}!')
