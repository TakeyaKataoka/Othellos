class Player():
    def __init__(self, color: int, name: str, is_computer=False) -> None:
        self.player_color = color
        self.name = name
        self.is_computer = is_computer
        self.hands = []
 

    def put_stone(self, hands) -> None:
        self.hands = hands
        