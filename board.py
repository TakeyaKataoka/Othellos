import numpy as np

# 盤面のクラス
class Board():
    def __init__(self, board_size=8) -> None:
        # ボードのサイズを指定
        self.board_size = board_size

        # ボードを作成
        self.board = np.zeros((self.board_size + 2, self.board_size + 2), dtype=int)
        ### print("オセロボードが生成されました"

        # 場所に応じて数値を割り振る
        # 壁　：　２＝Wall
        self.board[0, :] = 2
        self.board[:, 0] = 2
        self.board[board_size + 1, :] = 2
        self.board[:, board_size + 1] = 2
        # 初期配置　：　１＝White、−１＝Black 
        self.board[4, 4] = 1
        self.board[5, 5] = 1
        self.board[4, 5] = -1
        self.board[5, 4] = -1

        # 現在のプレイヤーの色　：　黒スタート
        self.player_color = -1


    def put_stone(self, hands: list) -> None:
        h1 = hands[0]
        h2 = hands[1]

        # 石を置く
        self.board[h1, h2] = self.player_color

        # プレイヤーを変更する
        self.player_color = - self.player_color


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

        # 石を返すことができるかを確認する
        # [vertical, horizontal]
        # vertical = {'down':-1, 'none':0, 'up':1]
        # horizontal = {'left':-1, 'none':0, 'right':1]

        # 置いた石から8方向の石を見ていく

        direction_bools = [] # 8方向全ての真偽を記録する
        reverse_stones = [] # リバース可能な石を記録する


        for v in (-1, 0, 1):
            for h in (-1, 0, 1):
                if v == 0 and h == 0:
                    pass
                else:
                    # 置いた石のすぐ隣の石が違う色の場合
                    if self.board[h1 + v, h2 + h] == -self.player_color:
                        h1_temp = h1 + v
                        h2_temp = h2 + h

                        pre_reverse_stones = [] # リバース可能性がある石を記録する

                        #1 上記の判定の遠さを広げる（置いた石と違う色の石がなくなるまで）
                        while self.board[h1_temp, h2_temp] == -self.player_color:
                            pre_reverse_stones.append([h1_temp, h2_temp])

                            h1_temp += v
                            h2_temp += h

                        #2 上記を通過し置いた石と同じ色の石が見つかった場合
                        if self.board[h1_temp, h2_temp] == self.player_color:
                            direction_bools.append(True)
                            reverse_stones.extend(pre_reverse_stones)
                        else:
                            direction_bools.append(False)

        #3 1方向でもTrueである場合
        if True in direction_bools:

            # 全てのリバース可能な石をリバースする
            self.reverse(reverse_stones)

            return True
                
        # 置けない場所に石がない場合
        return False


    def reverse(self, reverse_stones: list) -> None:
        print(reverse_stones)
        for reverse_stone in reverse_stones:
            s1 = reverse_stone[0]
            s2 = reverse_stone[1]

            self.board[s1, s2] *= -1
