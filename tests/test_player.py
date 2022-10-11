"""Tests of player.py
"""
from unittest import TestCase
import numpy as np
from othello.models.player import Player

# test用のViewクラス
class TestView():
    def __init__(self):
        pass

    def input_hands(self) -> list:
        return ['3', '4']


# test用のBoardクラス
class TestBoard():
    def __init__(self):
        self.recent_hand = []

    def set_stone(self, hands) ->  None:
        self.recent_hand = hands


# Unittestクラス
class TestPlayer(TestCase):
    def setUp(self):
        self.testview = TestView()
        self.testboard = TestBoard()


    def test_init(self):
        p = Player(-1, 'test', self.testview)

        # test 1
        self.assertIsInstance(p.player_color, int)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.view, TestView)
        self.assertEqual(p.hands, [])


    def test_select_hand(self):
        p = Player(1, 'test', self.testview)

        # test 2
        p.select_hand(self.testboard)
        self.assertEqual(p.hands, self.testview.input_hands())


    def test_put_stone(self):
        p = Player(1, 'test', self.testview)

        # test 3
        p.select_hand(self.testboard)
        p.put_stone(self.testboard)
        self.assertEqual(p.hands, ['3', '4'])
                