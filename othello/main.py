from views.view import View
from models.board import Board
from models.player import Player
from models.computer import Computer
from algorithm.algorithm import Algorithm
from controller.game import Game

def main():
    # ボード
    board = Board()

    # ビュー
    view = View(board)

    # ゲーム
    game = Game(view,board)

    # プレイヤーの情報を確認し、players_infoリストに保存
    players_info = game.prepare_player()

    # players_infoリストをもとにゲームにプレイヤーを追加
    players = []
    for player_info in players_info:
        player_mode = player_info[0]
        player_name = player_info[1]

        if player_mode == 'C':
            computer_pattern = player_info[2]
            computer_player = Computer(board.player_color, Algorithm(computer_pattern), player_name)
            players.append(computer_player)
        else:
            human_player = Player(board.player_color, player_name, view)
            players.append(human_player)

    game.add_player(players)

    # ゲームを開始
    game.run()

    # 勝者を表示
    view.display_winner()

	# 棋譜を保存するか聞く
    # view.ask_record()

if __name__ == '__main__':
    main()
