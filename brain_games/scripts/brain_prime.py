#!/usr/bin/env python3
from brain_games.brain_engine import play_game
from brain_games.games.prime import prime_game, GAME_RULES


def main():
    play_game(prime_game, GAME_RULES)


if __name__ == "__main__":
    main()
