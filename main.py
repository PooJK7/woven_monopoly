import sys
from game.game import Game


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <rolls_file>")
        print("Example: python main.py rolls_1.json")
        sys.exit(1)

    rolls_path = sys.argv[1]

    game = Game()
    game.play(rolls_path)


if __name__ == "__main__":
    main()
