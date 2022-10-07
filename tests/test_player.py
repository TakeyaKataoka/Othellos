"""Tests of player.py
"""

import unittest

from othello.models.player import Player

class TestView():
    def __init__(self):
        pass

    def input_hands(self) -> list:
        return ['3', '4']


class TestBoard():
    def __init__(self):
        self.recent_hand = []

    def set_stone(self, hands) ->  None:
        self.recent_hand = hands


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.testview = TestView()
        self.testboard = TestBoard()


    def test_init(self):
        self.assertIsInstance(Player(-1, 'test', self.testview).player_color, int)
        self.assertIsInstance(Player(-1, 'test', self.testview).name, str)
        self.assertIsInstance(Player(1, 'test', self.testview).view, TestView)
        self.assertEqual(Player(1, 'test', self.testview).hands, [])


    def test_select_hand(self):
        p = Player(1, 'test', self.testview)
        p.select_hand(self.testboard)
        self.assertEqual(p.hands, self.testview.input_hands())


    def test_put_stone(self):
        p = Player(1, 'test', self.testview)
        p.select_hand(self.testboard)
        p.put_stone(self.testboard)
        self.assertEqual(p.hands, ['3', '4'])
                