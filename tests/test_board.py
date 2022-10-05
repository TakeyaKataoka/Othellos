"""Tests of board.py
"""
import unittest
from othello.models.board import Board
from othello.models.player import Player

from othello.models.board import Board

class TestBoard(unittest.TestCase):
    def test_board_add_player(self):
        board = Board()
        board.add_player(Player(-1, "kataoka"), Player(1, "takeya"))
        self.assertIsInstance(board.player_black, Player)
        self.assertIsInstance(board.player_white, Player)


    def test_board_put_stone(self):
        # 範囲内の数字の場合(0-9)
        hands = [1, 2]
        h1 = hands[0]
        h2 = hands[1]

        board = Board()
        board.put_stone(hands)

        self.assertEqual(board.board[h1, h2], board.player_color)


    def test_board_is_put_stone(self):
        testcase = [['String', 'Strings'], ['10', '10'], ['4', '4'], ['3', '3'], ['3', '4']]
        answer = [False, False, False, False, True]
        for i in range(len(testcase)):
            board = Board()
            self.assertEqual(board.is_put_stone(testcase[i]), answer[i])

    
    def test_board_reverse(self):
        board = Board()
        board.reverse_stones = [[4,4]]
        board.reverse()

        self.assertEqual(board.board[4, 4], -1)
        self.assertEqual(board.reverse_stones, [])

