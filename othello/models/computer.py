# コンピュータープレイヤーのクラス
class Computer():
    def __init__(self, color: int, algo, name='computer') -> None:
        self.player_color = color
        self.name = name
        self.algo = algo
        self.hands = []

    def select_hand(self, board) -> list:        
        #1 ランダムパターンである場合
        if self.algo.pattern == 'R': 
            self.hands = self.algo.select_random(board)

        #2 簡単な評価関数アルゴリズムである場合
        elif self.algo.pattern == 'S':
            self.hands = self.algo.select_simopl_eval(board)
    
    def put_stone(self, board) -> None:
        board.set_stone(self.hands)
