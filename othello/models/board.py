import numpy as np

# 盤面のクラス
class Board():
    def __init__(self, board_size=8) -> None:
        # ボードのサイズ
        self.board_size = board_size

        # ボードを作成する
        self.board = np.zeros((board_size + 2, board_size + 2), dtype=int)

        # 石が置けるポジション（黒、白）を作成し、場所に応じてbool値を割り振る
        self.can_rev_pos_b = np.zeros((board_size + 2, board_size + 2), dtype=bool) # blackのリバースできるポジション
        self.can_rev_pos_w = np.zeros((board_size + 2, board_size + 2), dtype=bool) # whiteのリバースできるポジション

        # リバース可能な石を記録する
        self.reversible_stones = []

        # 現在のプレイヤーの色　：　黒スタート
        self.player_color = -1

        # 直前の手を記録する
        self.recent_hand = []

        # 全ての手を記録する
        self.record_hands = ''

        # 勝者を記録する
        self.winner = ''

        # 初期化
        self.set_initboard()
        self.set_initreversible()

    
    # ボードの初期配置を行う
    def set_initboard(self):
        self.board[0, :] = 2 # 壁　：　２＝Wall
        self.board[:, 0] = 2
        self.board[self.board_size + 1, :] = 2
        self.board[:, self.board_size + 1] = 2
        self.board[self.board_size // 2, self.board_size // 2] = 1 # 初期配置　：　１＝White、−１＝Black 
        self.board[self.board_size // 2 +1 , self.board_size // 2 +1] = 1
        self.board[self.board_size // 2, self.board_size // 2 + 1] = -1
        self.board[self.board_size // 2 + 1, self.board_size // 2] = -1


    # 石がおけるポジションの初期配置を行う
    def set_initreversible(self):
        for y in range(1,self.board_size + 1):
            for x in range(1, self.board_size + 1):
                self.can_rev_pos_b[y, x] = self.is_reversible([y, x], -1) # black
                self.can_rev_pos_w[y, x] = self.is_reversible([y, x], 1) # white


    # 場面に石を置く
    def set_stone(self, hands: list[str]) -> None:
        # handsを分解し、intへ変換する
        h1 = int(hands[0])
        h2 = int(hands[1])

        # ボード状況を更新
        self.board[h1, h2] = self.player_color#

        # 直前に置かれた手を記録する
        self.recent_hand = hands

        # 置かれた場所を記録していく
        self.record_hands += hands[0]
        self.record_hands += hands[1]

    
    # ボードの勝者を設定する
    def set_winner(self):
        if np.count_nonzero(self.board == -1) > np.count_nonzero(self.board == 1):
            self.winner = '黒'
        else:
            self.winner = '白'


    def is_put_stone(self, hands: list) -> bool:
        #1 数字（int）に変換できないhandsが入力された場合
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

        # 全て問題がない場合
        return True


    # リバースできるかの真偽を返し、返せる場所があれば属性(self.reversible_stones)で記録する
    def is_reversible(self, hands: list[str], color: int) -> bool:
        # handsを分解し、intへ変換する
        h1 = int(hands[0])
        h2 = int(hands[1])

        #1 すでに石が設置されている場合は
        if self.board[h1, h2] != 0:
            return False

        #2 石を返すことができるかを確認する
        direction_bools = [] # 9方向全ての真偽を記録する

        for v in (-1, 0, 1):
            for h in (-1, 0, 1):
                if v == 0 and h == 0: # 自分自身を選択した場合（０方向）
                    direction_bools.append(False)
                else:
                    # 置いた石のすぐ隣の石が違う色の場合
                    if self.board[h1 + v, h2 + h] == -color:
                        h1_temp = h1 + v
                        h2_temp = h2 + h

                        reversible_stones_temp = [] # リバース可能性がある石を記録する

                        #1 上記の判定の遠さを広げる（置いた石と違う色の石がなくなるまで）
                        while self.board[h1_temp, h2_temp] == -color:
                            reversible_stones_temp.append([h1_temp, h2_temp]) # 一時的に保存

                            h1_temp += v
                            h2_temp += h
                            
                        #2 上記を通過し置いた石と同じ色の石が見つかった場合
                        if self.board[h1_temp, h2_temp] == color:
                            direction_bools.append(True)
                            self.reversible_stones.extend(reversible_stones_temp) # 一時的に保存した石の場所を正式に記録
                        else:
                            direction_bools.append(False)

        # 9方向中一つでもリバース可能な方向があるかを返す
        return True in direction_bools


    # 石をリバースする
    def reverse(self) -> None:
        for reversible_stone in self.reversible_stones:
            s1 = reversible_stone[0]
            s2 = reversible_stone[1]

            self.board[s1, s2] *= -1 # ボードの対象の石をリバースする x(-1)

        # リバースできるポジションを更新
        for y in range(1,9):
            for x in range(1, 9):
                self.can_rev_pos_b[y, x] = self.is_reversible([y, x], -1)
                self.can_rev_pos_w[y, x] = self.is_reversible([y, x], 1)
                
        # リバースできる石のリストを初期化する
        self.reversible_stones = []


    # ゲームが終わったかを判定する
    def is_gameover(self):
        #1 勝利１　全てのますが埋まった場合
        if 0 not in self.board:
            return True
        
        #2 勝利２　置いていお石が全て同じ色になった場合
        if 1 not in self.board or 2 not in self.board:
            return True

        #1 継続１ 次のプレイヤーが置ける場所がある
        if  self.player_color == -1 and self.can_rev_pos_w[:, :].any():
            return False

        #2 継続２ 次のプレイヤーが置ける場所がある
        if self.player_color == 1 and self.can_rev_pos_b[:, :].any():
            return False

        return False


    # プレイヤーを入れ替える
    def next(self):
        # プレイヤーを変更する
        self.player_color = - self.player_color
    