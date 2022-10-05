
import numpy as np

# 盤面のクラス
class Board():
    def __init__(self, board_size=8) -> None:
        # ボードのサイズを指定
        self.board_size = board_size

        # ボードを作成し、場所に応じて数値を割り振る
        self.board = np.zeros((self.board_size + 2, self.board_size + 2), dtype=int)
        
        self.board[0, :] = 2 # 壁　：　２＝Wall
        self.board[:, 0] = 2
        self.board[board_size + 1, :] = 2
        self.board[:, board_size + 1] = 2
        
        self.board[4, 4] = 1 # 初期配置　：　１＝White、−１＝Black 
        self.board[5, 5] = 1
        self.board[4, 5] = -1
        self.board[5, 4] = -1

        # リバース可能な石を記録する
        self.reverse_stones = []

        # 石が置ける場所を保持するボード（黒、白）を作成し、場所に応じてbool値を割り振る
        self.black_position = np.zeros((self.board_size + 2, self.board_size + 2), dtype=bool)
        self.white_position = np.zeros((self.board_size + 2, self.board_size + 2), dtype=bool)
        for y in range(1,9):
            for x in range(1, 9):
                self.black_position[y, x] = self.is_reversed([y, x], -1)
                self.white_position[y, x] = self.is_reversed([y, x], 1)

        # 現在のプレイヤーの色　：　黒スタßßート
        self.player_color = -1

        



    def put_stone(self, hands: list) -> None:
        h1 = hands[0]
        h2 = hands[1]

        # 石を置く
        self.board[h1, h2] = self.player_color


    def is_put_stone(self, hands: list) -> bool:
        h1 = hands[0]
        h2 = hands[1]

        #1 有効なマスを洗濯していない場合
        if (h1 < 1 or 8 < h1) or (h2 < 1 or 8 < h2):
            print("有効なマスではありません。")
            return False

        #2 すでに駒がある場合
        if self.board[h1, h2] != 0:
            print("既に石が存在します。")
            return False

        #3 1方向でもTrueである場合
        if self.is_reversed(hands, self.player_color):
            return True
                
        # 置けない場所に石がない場合
        print("そこには石が置けません")
        return False


    def is_reversed(self, hands: list, color: int):
        h1 = hands[0]
        h2 = hands[1]

        # 石を返すことができるかを確認する
        # [vertical, horizontal]
        # vertical = {'down':-1, 'none':0, 'up':1]
        # horizontal = {'left':-1, 'none':0, 'right':1]

        # 置いた石から8方向の石を見ていく

        direction_bools = [] # 8方向全ての真偽を記録する

        for v in (-1, 0, 1):
            for h in (-1, 0, 1):
                if v == 0 and h == 0:
                    pass
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
        
        for y in range(1,9):
            for x in range(1, 9):
                self.black_position[y, x] = self.is_reversed([y, x], -1)
                self.white_position[y, x] = self.is_reversed([y, x], 1)
        
        # プレイヤーを変更する
        self.player_color = - self.player_color
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
    

    def test(self):
        pass
        # print(self.black_position)
        # print(self.white_position)

