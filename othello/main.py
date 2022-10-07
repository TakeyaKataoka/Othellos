
from views.view import View
from models.board import Board
from models.player import Player
from models.compiter import Computer
from algorithm.algorithm import Algorithm
from controller.game import Game

def main():
    if input("コンピューター同士の戦いを監視しますか？（Y/n）")!= 'Y':
        # ビュー（ユーザーインターフェース）を作成する
        view = View()

        # ゲームを開始する場合、ボードを作成する
        if view.start_game():
            board = Board()
        
        # 対戦相手を選ぶ
        flags = view.select_oppo()

        # プレイヤーの名前を聞く
        player1_name = view.add_player(board)
        board.player_color = - board.player_color

        player2_name = view.add_player(board) 
        board.player_color = - board.player_color

        # ゲームにプレイヤーを追加する
        # ただし、コンピューターを選択したプレイヤーの強さを選ぶ
        if flags[0] == 'C':
            print("プレイヤー１について")
            algo1 = Algorithm(view.select_strength())
            player_black = Computer(-1, algo1, player1_name)
        else:
            player_black = Player(-1, player1_name, view)
            pass

        if flags[1] == 'C':
            print("プレイヤー2について")
            algo2 = Algorithm(view.select_strength())
            player_white = Computer(-1, algo2, player2_name)
        else:
            player_white = Player(1, player1_name, view)
            pass

        # ゲームを実行する
        game = Game(view,
                        board,
                        player_black,
                        player_white,
                        )
        game.run()

        # 勝者を表示する
        view.display_winner(board.winner)

		# 棋譜を保存するか聞く
        view.ask_record(board)

    # コンピュータ同士の勝敗を試す
    else:
        winner_list = []
        algo1 = Algorithm(input("コンピューター1の強さを洗濯してください（R : ★ \ S : ★★）"))
        player_black = Computer(-1, algo1)
        algo2 = Algorithm(input("コンピューター2の強さを洗濯してください（R : ★ \ S : ★★）"))
        player_white = Computer(-1, algo2)

        for i in range(int(input("何回試しますか？"))):
            view = View()
            board = Board()
            
            game = Game(view,
                        board,
                        player_black,
                        player_white,
                        )
            game.run()

            winner_list.append(board.winner)

        print(winner_list.count('黒'))
        print(winner_list.count('白'))

    
if __name__ == '__main__':
    main()
