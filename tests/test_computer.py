"""Tests of computer.py
"""
from unittest import TestCase
from othello.models.computer import Computer


# test用のBoardクラス
class TestBoard():
    def __init__(self):
        self.recent_hand = []

    def set_stone(self, hands) ->  None:
        self.recent_hand = hands


# test用のAlgorithhmクラス
class TestAlgorithm():
    def __init__(self):
        self.pattern = 'R'

    def select_random(self, board):
        return ['7', '8']

    def select_simopl_eval(self, board):
        return ['3', '4']


# Unittestクラス
class TestComputer(TestCase):
    def setUp(self):
        self.testboard = TestBoard()
        self.testalgo = TestAlgorithm()


    def test_init(self):
        c = Computer(-1, self.testalgo)

        # test 1
        self.assertIsInstance(c.player_color, int)
        self.assertIsInstance(c.name, str)
        self.assertIsInstance(c.algo, TestAlgorithm)
        self.assertEqual(c.hands, [])


    def test_select_hand(self):
        c = Computer(1, self.testalgo, 'test')

        # test 2-1
        c.select_hand(self.testboard)
        self.assertEqual(c.hands, self.testalgo.select_random(self.testboard))

        # test 2-2
        self.testalgo.pattern = 'S'
        c.select_hand(self.testboard)
        self.assertEqual(c.hands, self.testalgo.select_simopl_eval(self.testboard))


    def test_put_stone(self):
        c = Computer(1, self.testalgo, 'test')

        # test 3-1
        c.select_hand(self.testboard)
        c.put_stone(self.testboard)
        self.assertEqual(c.hands, ['7', '8'])

        # test 3-2
        self.testalgo.pattern = 'S'
        c.select_hand(self.testboard)
        c.put_stone(self.testboard)
        self.assertEqual(c.hands, ['3', '4'])
                