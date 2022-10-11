"""Tests of algorithm.py
"""
from unittest import TestCase
from unittest.mock import patch
import numpy as np
from numpy.testing import assert_array_equal

from othello.algorithm.algorithm import Algorithm


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

        self.can_rev_pos_b = np.array([
        				 [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         [False, False, True, False, False, False, False, False, False, False],
                         [False, False, False, True, False, False, False, False, False, False],
                         [False, False, False, True, False, False, False, False, False, False],
                         [False, False, False, False, True, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         ])

        self.can_rev_pos_w = np.array([
        				 [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, True, False, False, False, False],
                         [False, False, True, False, False, False, True, False, False, False],
                         [False, False, False, True, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, True, False, False, False, False, False],
                         [False, False, False, False, False, False, True, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False],
                         ])



# Algorithmクラスのユニットテスト
class TestAlgorithm(TestCase):
    def test_init(self):
    	# test 1-1
    	a = Algorithm('R')
    	self.assertEqual(a.pattern, 'R')
    	assert_array_equal(a.base_scores,
    						np.array([
					            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
					            [0, 30, -10, 2,  1,  1, 2, -10, 30, 0],
					            [0, -10, -20, -3, -3, -3, -3, -20, -10, 0],
					            [0, 2, -3, 2, 0, 0, 2, -3, 2, 0],
					            [0, 1, -3, 0, 0, 0, 0, -3, 1, 0],
					            [0, 1, -3, 0, 0, 0, 0, -3, 1, 0],
					            [0, 2, -3, 2, 0, 0, 2, -3, 2, 0],
					            [0, -10, -20, -3, -3, -3, -3, -20, -10, 0],
					            [0, 30, -10, 2,  1,  1, 2, -10, 30, 0],
					            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
					        ])
					    )

    	# test 1-2
    	a = Algorithm('S')
    	self.assertEqual(a.pattern, 'S')
    	assert_array_equal(a.eval_scores,
    						np.array([
    							[70, -9, 37, 7, 7, 37, -9, 70], 
						        [-9, -30, 28, -3, -3, 28, -30, -9], 
						        [37, 28, 34, 7, 7, 34, 28, 37], 
						        [7, -3, 7, -2, -2, 7, -3, 7], 
						        [7, -3, 7, -2, -2, 7, -3, 7], 
						        [37, 28, 34, 7, 7, 34, 28, 37], 
						        [-9, -30, 28, -3, -3, 28, -30, -9], 
						        [70, -9, 37, 7, 7, 37, -9, 70]
						    ])
					    )


    @patch('random.choice')
    def test_select_random(self, mock):
    	# test 2
    	a = Algorithm('R')
    	mock.return_value = [6, 4]
    	hands = a.select_random(TestBoard())
    	self.assertEqual(hands, ['6', '4'])


    def test_select_simple_eval(self):
    	# test 3
    	a = Algorithm('S')
    	testboard = TestBoard()
    	testboard.player_color = 1
    	hands = a.select_simopl_eval(testboard)
    	self.assertEqual(hands, ['8', '6'])

