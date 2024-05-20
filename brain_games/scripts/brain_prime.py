#!/usr/bin/env python3
from brain_games.scripts.brain_engine import play_game
from brain_games.games.prime import prime_game


def main():
    play_game(prime_game)


if __name__ == "__main__":
    main()
