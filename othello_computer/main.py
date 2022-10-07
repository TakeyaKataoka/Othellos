from game import Game

def main():
    winner_list = []

    for i in range(100):
        game = Game()
        winner_list.append(game.start())

    print(winner_list.count('黒'))
    print(winner_list.count('白'))
    
if __name__ == '__main__':
    main()
