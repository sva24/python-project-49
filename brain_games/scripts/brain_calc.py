#!/usr/bin/env python3
from brain_games.scripts.brain_engine import play_game
from brain_games.games.calc import calc_number


def main():
    play_game(calc_number)


if __name__ == "__main__":
    main()
