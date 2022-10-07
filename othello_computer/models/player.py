
import random
import numpy as np

from models.board import Board
from algorithm.algorithm import Algorithm

class Player():
    def __init__(self, color: int, name: str, algo: Algorithm) -> None:
        self.player_color = color
        self.name = name
        self.algo = algo
        self.hands = []
        self.computer_flag = self.is_computer

    
    def is_computer(self):
        if self.algo.pattern == 'R' or self.algo.pattern == 'S':
            return True
        else:
            return False



    def select_hand(self, board: Board, hands=[], ) -> list:
        #1 プレイヤーが人間の場合
        self.hands = hands
        if self.algo.pattern == 'H': 
            pass
        
        #2 プレイヤーがコンピューター（ランダムパターン）である場合
        elif self.algo.pattern == 'R': 
            if board.player_color == 1: # 白
                position = np.argwhere(board.white_position == True)
                self.hands = [str(i) for i in (random.choice(position))]
            elif board.player_color == -1: # 黒
                position = np.argwhere(board.black_position == True)
                self.hands = [str(i) for i in (random.choice(position))]

        #3 プレイヤーがコンピューター（ランダムパターン）である場合
        elif self.algo.pattern == 'S':
            if board.player_color == 1: # 白
                position = np.argwhere(board.white_position == True)
                positions_list = [list(i) for i in position]

                scores = []
                scores_pos = []
                index = 0
                for pos in positions_list:
                    p1 = pos[0] - 1
                    p2 = pos[1] - 1
                    scores.append(self.algo.eval_scores[p1][p2])
                    scores_pos.append(pos)
                max_score_indexes = [i for i, v in enumerate(scores) if v == max(scores)]

                if len(max_score_indexes) > 1:
                    index = random.choice(max_score_indexes)
                else:
                    index = max_score_indexes [0]
                self.hands = [str(i) for i in scores_pos[index]]

            elif board.player_color == -1: # 黒
                position = np.argwhere(board.black_position == True)
                positions_list = [list(i) for i in position]

                scores = []
                scores_pos = []
                index = 0
                for pos in positions_list:
                    p1 = pos[0] - 1
                    p2 = pos[1] - 1
                    scores.append(self.algo.eval_scores[p1][p2])
                    scores_pos.append(pos) 
                max_score_indexes = [i for i, v in enumerate(scores) if v == max(scores)]

                if len(max_score_indexes) > 1:
                    index = random.choice(max_score_indexes)
                else:
                    index = max_score_indexes [0]       
                self.hands = [str(i) for i in scores_pos[index]]
    
    def put_stone(self, board: Board) -> None:
        board.put_stone(self.hands)


