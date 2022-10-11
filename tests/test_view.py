"""Tests of view.py
"""
from unittest import TestCase
from unittest.mock import patch, call
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
        self.record_hands = '32324367813813784563487326478'
        self.winner = 0


# Viewクラスのユニットテスト
class TestView(TestCase):
    def test_init(self):
        # test 1
        v = View(TestBoard())
        self.assertIsInstance(v.board, TestBoard)
        assert_array_equal(v.view_board, np.zeros((v.board.board_size + 2, v.board.board_size  + 2), dtype=str))


    def test_color_convert(self):
        # test 2
        v = View(TestBoard())
        color_str = v.color_convert(-1)
        self.assertEqual(color_str, "黒")

        color_str = v.color_convert(1)
        self.assertEqual(color_str, "白")

        color_str = v.color_convert(0)
        self.assertIsNone(color_str)


    @patch('builtins.input')
    def test_add_player(self, mock):
        v = View(TestBoard())
        mock.return_value = 'testname'
        
        # test 3
        name = v.add_player()
        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual(name, 'testname')


    @patch('builtins.input')
    def test_input_hands(self, mock):
        v = View(TestBoard())
        mock.side_effect = ['5', '6']

        # test 4
        hands = v.input_hands()
        self.assertIsNotNone(hands)
        self.assertIsInstance(hands, list)
        self.assertEqual(hands, ['5', '6'])


    @patch('builtins.input')
    def test_select_oppo(self, mock):
        v = View(TestBoard())
        mock.return_value = 'C'

        # test 5
        oppo = v.select_oppo()
        self.assertIsNotNone(oppo)
        self.assertIsInstance(oppo, str)
        self.assertEqual(oppo, 'C')

    
    @patch('builtins.input')  
    def test_select_strength(self, mock):
        v = View(TestBoard())
        mock.return_value = 'R'

        # test 6
        strength = v.select_strength()
        self.assertIsNotNone(strength)
        self.assertIsInstance(strength, str)
        self.assertEqual(strength, 'R')


    @patch('builtins.print')
    def test_announce_color(self, mock):
        v = View(TestBoard())
        
        # test 7
        v.announce_color('Test')
        mock.assert_called_with('Testさんが参加しました！あなたの手番は黒')


    @patch('builtins.print')
    def test_announce_pass(self, mock):
        v = View(TestBoard())
        
        # test 8
        v.announce_pass()
        mock.assert_called_with('黒がパスしました')


    @patch('builtins.print')
    def test_announce_newinput(self, mock):
        v = View(TestBoard())
        
        # test 9
        v.announce_newinput('リバースできる石がありません')
        mock.assert_called_with('リバースできる石がありません\nもう一度入力してください')


    @patch('builtins.print')
    def test_display_records(self, mock):
        v = View(TestBoard())
        
        # test 10
        v.display_record()
        mock.assert_called_with('今回の棋譜は以下の通りです！\n32324367813813784563487326478')


    def test_display_board(self):
        v = View(TestBoard())

        # test 11
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
 
    @patch('builtins.print')
    def test_display_hand(self, mock):
        v = View(TestBoard())
        
        # test 12
        v.display_hand()
        mock.assert_called_with('[6, 7]に石が置かれました')


    @patch('builtins.print')
    def test_display_player(self, mock):
        v = View(TestBoard())
        
        # test 13
        v.display_player()
        mock.assert_called_with('黒の手番です')


    @patch('builtins.print')
    def test_display_winner(self, mock):
        b = TestBoard()
        v = View(b)
        
        # test 14-1
        v.display_winner()
        mock.assert_called_with('引き分けです！')

        # test 14-2
        b.winner = 1
        v.display_winner()
        mock.assert_called_with('勝者は「白」です！')
