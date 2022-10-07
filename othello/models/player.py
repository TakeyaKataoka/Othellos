# 人間プレイヤーのクラス
class Player():
    def __init__(self, color: int, name: str, view) -> None:
        self.player_color = color
        self.name = name
        self.hands = []
        self.view = view


    def select_hand(self, board) -> list:
        self.hands = self.view.input_hands()

    
    def put_stone(self, board) -> None:
        board.set_stone(self.hands)
