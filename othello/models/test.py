from models.board import Board
from models.player import Player
from views.view import View


def main():
    board = Board()
    board.test()

    print(dir(board))


if __name__ == '__main__':
    main()
