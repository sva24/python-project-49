#!/usr/bin/env python3
from brain_games.scripts.brain_engine import play_game
from brain_games.games.gcd import gcd_game


def main():
    play_game(gcd_game)


if __name__ == "__main__":
    main()
