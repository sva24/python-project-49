#!/usr/bin/env python3
from brain_games.brain_engine import play_game
from brain_games.games.gcd import gcd_game, get_game_rules


def main():
    play_game(gcd_game, get_game_rules)


if __name__ == "__main__":
    main()
