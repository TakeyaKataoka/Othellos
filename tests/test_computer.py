"""Tests of computer.py
"""

import unittest

from othello.models.computer import Computer


class TestBoard():
    def __init__(self):
        self.recent_hand = []

    def set_stone(self, hands) ->  None:
        self.recent_hand = hands


class TestAlgorithm():
    def __init__(self):
        self.pattern = 'R'

    def select_random(self, board):
        return ['7', '8']

    def select_simopl_eval(self, board):
        return ['3', '4']


class TestComputer(unittest.TestCase):
    def setUp(self):
        self.testboard = TestBoard()
        self.testalgo = TestAlgorithm()


    def test_init(self):
        self.assertIsInstance(Computer(-1, self.testalgo).player_color, int)
        self.assertIsInstance(Computer(-1, self.testalgo, 'test').name, str)
        self.assertIsInstance(Computer(1, self.testalgo).algo, TestAlgorithm)
        self.assertEqual(Computer(1, self.testalgo).hands, [])


    def test_select_hand(self):
        p = Computer(1, self.testalgo, 'test')
        p.select_hand(self.testboard)
        self.assertEqual(p.hands, self.testalgo.select_random(self.testboard))

        self.testalgo.pattern = 'S'
        p.select_hand(self.testboard)
        self.assertEqual(p.hands, self.testalgo.select_simopl_eval(self.testboard))


    def test_put_stone(self):
        p = Computer(1, self.testalgo, 'test')
        p.select_hand(self.testboard)
        p.put_stone(self.testboard)
        self.assertEqual(p.hands, ['7', '8'])

        self.testalgo.pattern = 'S'
        p.select_hand(self.testboard)
        p.put_stone(self.testboard)
        self.assertEqual(p.hands, ['3', '4'])
                