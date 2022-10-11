"""Tests of view.py
"""
from unittest import TestCase
import numpy as np
from numpy.testing import assert_array_equal
from othello.views.view import View


# test用のBoardクラス
class TestBoard():
    def __init__(self):
        self.board_size = 8
        self.board = np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                         [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                         [2, 0, 0, 0, 0, -1, 0, 0, 0, 2],
                         [2, 0, 0, 0, 0, -1, 0, 0, 0, 2],
                         [2, 0, 0, 1, -1, -1, 0, 0, 0, 2],
                         [2, 0, 0, 0, 1, -1, 0, 0, 0, 2],
                         [2, 0, 0, 0, 1, 0, 0, 0, 0, 2],
                         [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                         [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                         ])
        self.player_color = -1 
        self.recent_hand = [6, 7]


class TestView(TestCase):
    def test_init(self):
        v = View(TestBoard())

        # test 1
        self.assertIsInstance(v.board, TestBoard)
        assert_array_equal(v.view_board, np.zeros((v.board.board_size + 2, v.board.board_size  + 2), dtype=str))


    def test_add_player(self):
        v = View(TestBoard())
        
        # test 2
        name = v.add_player()
        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)


    def test_input_hands(self):
        v = View(TestBoard())

        # test 3
        hands = v.input_hands()
        self.assertIsNotNone(hands)
        self.assertIsInstance(hands, list)

    
    def test_select_oppo(self):
        v = View(TestBoard())

        # test 4
        oppos = v.select_oppo()
        self.assertIsNotNone(oppos)
        self.assertIsInstance(oppos, str)

    
    def test_select_strength(self):
        v = View(TestBoard())

        # test 5
        strength = v.select_strength()
        self.assertIsNotNone(strength)
        self.assertIsInstance(strength, str)


    def test_display_board(self) -> None:
        v = View(TestBoard())

        # test 6
        v.display_board()
        assert_array_equal(v.view_board,
                    np.array(
                    [['■', '■', '■', '■', '■', '■', '■', '■', '■', '■'],
                     ['■', '-', '-', '-', '-', '-', '-', '-', '-', '■'],
                     ['■', '-', '-', '-', '-', '○', '-', '-', '-', '■'],
                     ['■', '-', '-', '-', '-', '○', '-', '-', '-', '■'],
                     ['■', '-', '-', '●', '○', '○', '-', '-', '-', '■'],
                     ['■', '-', '-', '-', '●', '○', '-', '-', '-', '■'],
                     ['■', '-', '-', '-', '●', '-', '-', '-', '-', '■'],
                     ['■', '-', '-', '-', '-', '-', '-', '-', '-', '■'],
                     ['■', '-', '-', '-', '-', '-', '-', '-', '-', '■'],
                     ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■'],]
                     )
                    )    
