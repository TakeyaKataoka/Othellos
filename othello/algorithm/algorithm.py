# コンピューターの選択手アルゴリズムのクラス
import random
import numpy as np

class Algorithm():
    def __init__(self, pattern) -> None:
        # アルゴリズムの種類
        self.pattern = pattern

        # 場面の得点
        self.base_scores = np.array([
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

        # 評価関数（固定値）
        if self.pattern == 'S':
            self.eval_scores = self.eval_hand()
        """
        [[70, -9, 37, 7, 7, 37, -9, 70], 
        [-9, -30, 28, -3, -3, 28, -30, -9], 
        [37, 28, 34, 7, 7, 34, 28, 37], 
        [7, -3, 7, -2, -2, 7, -3, 7], 
        [7, -3, 7, -2, -2, 7, -3, 7], 
        [37, 28, 34, 7, 7, 34, 28, 37], 
        [-9, -30, 28, -3, -3, 28, -30, -9], 
        [70, -9, 37, 7, 7, 37, -9, 70]]
        """


    # ランダムに選択可能な手から選択する
    def selcet_random(self, board):
        if board.player_color == -1: # 黒
                position = np.argwhere(board.can_rev_pos_b == True)
                return [str(i) for i in (random.choice(position))]
        elif board.player_color == 1: # 白
                position = np.argwhere(board.can_rev_pos_w == True)
                return [str(i) for i in (random.choice(position))]


    # 簡単な評価関数アルゴリズムで得た得点が高く、選択可能な手から選択する
    def select_simopl_eval(self, board):
        if board.player_color == -1: # 黒
            position = np.argwhere(board.can_rev_pos_b == True)
            positions_list = [list(i) for i in position]

            scores = []
            scores_pos = []
            index = 0
            for pos in positions_list:
                p1 = pos[0] - 1
                p2 = pos[1] - 1
                scores.append(self.eval_scores[p1][p2])
                scores_pos.append(pos)
            max_score_indexes = [i for i, v in enumerate(scores) if v == max(scores)]

            if len(max_score_indexes) > 1:
                index = random.choice(max_score_indexes)
            else:
                index = max_score_indexes [0]
            return [str(i) for i in scores_pos[index]]

        elif board.player_color == 1: # 白
            position = np.argwhere(board.can_rev_pos_w == True)
            positions_list = [list(i) for i in position]

            scores = []
            scores_pos = []
            index = 0
            for pos in positions_list:
                p1 = pos[0] - 1
                p2 = pos[1] - 1
                scores.append(self.eval_scores[p1][p2])
                scores_pos.append(pos) 
            max_score_indexes = [i for i, v in enumerate(scores) if v == max(scores)]

            if len(max_score_indexes) > 1:
                index = random.choice(max_score_indexes)
            else:
                index = max_score_indexes [0]       
            return [str(i) for i in scores_pos[index]]


    # 簡単な評価関数のアルゴリズム
    def eval_hand(self):
        w = -2
        point = 0
        points =[]
        points_s = []

        for y in range(1, 9):
            for x in range(1, 9):
                if x == 0 or x == 9 or y == 0 or y == 9:
                    points.append(point)
                for v in [-1, 0, 1]:
                    for h in [-1, 0, 1]:
                        if v == 0 and h == 0:
                            point += self.base_scores[y + v,  x + h]
                        else:
                            point += w * self.base_scores[y + v,  x + h]
                points.append(point)
                point = 0
            points_s.append(points) 
            points =[]
        
        return points_s
