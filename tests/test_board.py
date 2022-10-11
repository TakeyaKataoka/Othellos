"""Tests of board.py
"""
from unittest import TestCase
import numpy as np
from numpy.testing import assert_array_equal

from othello.models.board import Board


class TestBoard(TestCase):
    def test_init(self):
        # test 1
        b = Board(8)
        self.assertEqual(b.board_size, 8)
        assert_array_equal(b.board,
                           np.array([
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 1, -1, 0, 0, 0, 2],
                            [2, 0, 0, 0, -1, 1, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            ])
                        )
        assert_array_equal(b.can_rev_pos_b,
                           np.array([
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, True, False, False, False, False, False],
                            [False, False, False, True, False, False, False, False, False, False],
                            [False, False, False, False, False, False, True, False, False, False],
                            [False, False, False, False, False, True, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            ])
                        )
        assert_array_equal(b.can_rev_pos_w,
                           np.array([
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, True, False, False, False, False],
                            [False, False, False, False, False, False, True, False, False, False],
                            [False, False, False, True, False, False, False, False, False, False],
                            [False, False, False, False, True, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            [False, False, False, False, False, False, False, False, False, False],
                            ])
                        )
        self.assertEqual(b.reversible_stones, [])
        self.assertEqual(b.player_color, -1)
        self.assertEqual(b.recent_hand, [])
        self.assertEqual(b.record_hands, '')
        self.assertEqual(b.winner, 0)                        


    def test_set_stone(self):
        b = Board(8)

        # test 2
        b.set_stone(['7', '8'])
        self.assertEqual(b.board[7, 8], b.player_color)
        self.assertEqual(b.recent_hand, ['7', '8'])
        self.assertEqual(b.record_hands, '78')


    def test_set_winner(self):
        # test 3-1
        b = Board(8)
        b.board = np.array([
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, -1, 1, 1, 1, 2],
                        [2, 1, 1, 1, -1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    ])
        b.set_winner()
        self.assertEqual(b.winner, 1)

        # test 3-2
        b = Board(8)
        b.board = np.array([
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, 1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, 1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    ])
        b.set_winner()
        self.assertEqual(b.winner, -1)

        # test 3-3 引き分け
        b = Board(8)
        b.board = np.array([
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    ])
        b.set_winner()
        self.assertEqual(b.winner, 0)


    def test_can_put_stone(self):
        b = Board(8)

        # test 4-1
        result = b.can_set_stone(['abc', 'frs'])
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "有効な入力ではありません。")

        # test 4-2
        result = b.can_set_stone(['1', '10'])
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "有効なマスではありません。")

        # test 4-3
        result = b.can_set_stone(['4', '5'])
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "既に石が存在します。")

        # test 4-4
        result = b.can_set_stone(['1', '1'])
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "リバースできる石がありません。")

        # test 4-5
        result = b.can_set_stone(['3', '4'])
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "")


    def test_is_reversible(self):
        b = Board(8)

        # test 5
        is_reversible = b.is_reversible(['4', '3'], -1)
        self.assertEqual(is_reversible, True)


    def test_reverse(self):
        b = Board(8)
        b.board = np.array([
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, -1, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, -1, -1, 0, 0, 0, 2],
                            [2, 0, 0, 1, -1, 1, 0, 0, 0, 2],
                            [2, 0, 0, 1, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 1, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            ])

        # test 6
        b.set_stone(['6', '5'])
        b.reversible_stones = [[5, 5]]
        for y in range(1,9):
            for x in range(1, 9):
                b.can_rev_pos_b[y, x] = b.is_reversible([y, x], -1)
                b.can_rev_pos_w[y, x] = b.is_reversible([y, x], 1)
        b.reverse()
        self.assertEqual(b.board[5, 5], -1)
        self.assertEqual(b.reversible_stones, [])

    
    def test_gameover(self):
        b = Board(8)

        # test 7-1
        b.board = np.array([
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                            [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                            [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                            [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                            [2, -1, -1, 1, -1, 1, -1, -1, -1, 2],
                            [2, -1, -1, 1, -1, -1, -1, -1, -1, 2],
                            [2, -1, -1, 1, -1, -1, -1, -1, -1, 2],
                            [2, -1, -1, -1, -1, -1, -1, -1, -1, 2],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            ])
        result = b.is_gameover()
        self.assertEqual(result, True)

        # test 7-2
        b.board = np.array([
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                            [2, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            ])
        result = b.is_gameover()
        self.assertEqual(result, True)

        # test 7-3
        b.board = np.array([
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, -1, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, -1, -1, 0, 0, 0, 2],
                            [2, 0, 0, 1, -1, 1, 0, 0, 0, 2],
                            [2, 0, 0, 1, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 1, 0, 0, 0, 0, 0, 2],
                            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            ])
        for y in range(1,9):
            for x in range(1, 9):
                b.can_rev_pos_b[y, x] = b.is_reversible([y, x], -1)
                b.can_rev_pos_w[y, x] = b.is_reversible([y, x], 1)
        result = b.is_gameover()
        self.assertEqual(result, False)


    def test_next(self):
        b = Board(8)

        # test 8
        b.next()
        self.assertEqual(b.player_color, 1)
