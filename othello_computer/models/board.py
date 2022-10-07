
import numpy as np

# 盤面のクラス
class Board():
    def __init__(self) -> None:

        # ボードを作成し、場所に応じて数値を割り振る
        self.board = np.zeros((10, 10), dtype=int)
        
        self.board[0, :] = 2 # 壁　：　２＝Wall
        self.board[:, 0] = 2
        self.board[9, :] = 2
        self.board[:, 9] = 2
        
        self.board[4, 4] = 1 # 初期配置　：　１＝White、−１＝Black 
        self.board[5, 5] = 1
        self.board[4, 5] = -1
        self.board[5, 4] = -1

        # リバース可能な石を記録する
        self.reverse_stones = []

        # 石が置ける場所を保持するボード（黒、白）を作成し、場所に応じてbool値を割り振る
        self.black_position = np.zeros((10, 10), dtype=bool)
        self.white_position = np.zeros((10, 10), dtype=bool)
        for y in range(1,9):
            for x in range(1, 9):
                self.black_position[y, x] = self.is_reversible([y, x], -1)
                self.white_position[y, x] = self.is_reversible([y, x], 1)
        
        # 現在のプレイヤーの色　：　黒スタート
        self.player_color = -1

        # 直前の手を記録する
        self.recent_hand = []

        # 全ての手を記録する
        self.record_hands = ''

        # 勝者を記録する
        self.winner = ''


    def put_stone(self, hands: list) -> None:
        h1 = int(hands[0])
        h2 = int(hands[1])

        # 石を置く
        self.board[h1, h2] = self.player_color

        # 直前に置かれた手を記録する
        self.recent_hand = hands

        # 置かれた手を記録していく
        self.record_hands += hands[0]
        self.record_hands += hands[1]



    def is_put_stone(self, hands: list) -> bool:

        #1 数字（int）以外が入力された場合
        for hand in hands:
            if not str.isdigit(hand):
                print("有効な入力ではありません。")
                return False

        # 数字に変換する
        h1 = int(hands[0])
        h2 = int(hands[1])

        #2 有効なマスを洗濯していない場合
        if (h1 < 1 or 8 < h1) or (h2 < 1 or 8 < h2):
            print("有効なマスではありません。")
            return False

        #3 すでに駒がある場合
        if self.board[h1, h2] != 0:
            print("既に石が存在します。")
            return False

        #4 1方向もリバースできない場合
        if not self.is_reversible(hands, self.player_color):
            print("リバースできる石がありません。")
            return False
                
        return True


    def is_reversible(self, hands: list, color: int):
        h1 = int(hands[0])
        h2 = int(hands[1])

        # すでに石が設置されている場合はFalse
        if self.board[h1, h2] != 0:
            return False

        # 石を返すことができるかを確認する
        direction_bools = [] # 8方向全ての真偽を記録する

        for v in (-1, 0, 1):
            for h in (-1, 0, 1):
                if v == 0 and h == 0:
                    direction_bools.append(False)
                else:
                    # 置いた石のすぐ隣の石が違う色の場合
                    if self.board[h1 + v, h2 + h] == -color:
                        h1_temp = h1 + v
                        h2_temp = h2 + h

                        reverse_stones_temp = [] # リバース可能性がある石を記録する

                        #1 上記の判定の遠さを広げる（置いた石と違う色の石がなくなるまで）
                        while self.board[h1_temp, h2_temp] == -color:
                            reverse_stones_temp.append([h1_temp, h2_temp])

                            h1_temp += v
                            h2_temp += h
                            
                        #2 上記を通過し置いた石と同じ色の石が見つかった場合
                        if self.board[h1_temp, h2_temp] == color:
                            direction_bools.append(True)
                            self.reverse_stones.extend(reverse_stones_temp)
                        else:
                            direction_bools.append(False)

        return True in direction_bools


    def reverse(self) -> None:
        for reverse_stone in self.reverse_stones:
            s1 = reverse_stone[0]
            s2 = reverse_stone[1]

            self.board[s1, s2] *= -1

        # リバースできるポジションを更新
        for y in range(1,9):
            for x in range(1, 9):
                self.black_position[y, x] = self.is_reversible([y, x], -1)
                self.white_position[y, x] = self.is_reversible([y, x], 1)
        
        # リバースできる石のリストを空にする
        self.reverse_stones = []


    def is_gameover(self):
        # 全てのますが埋まった場合
        if 0 not in self.board:
            return True
        
        # 置いていお石が全て同じ色になった場合
        if 1 not in self.board or 2 not in self.board:
            return True

        #プレイヤーが置ける場所がある
        if self.black_position[:, :].any() or self.white_position[:, :].any():
            return False

        return True


    def next(self):
        # プレイヤーを変更する
        self.player_color = - self.player_color


    def set_winner(self):
        if np.count_nonzero(self.board == -1) > np.count_nonzero(self.board == 1):
            self.winner = '黒'
        else:
            self.winner = '白'