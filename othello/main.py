
from models.board import Board
from models.player import Player
from views.view import View


def main():
	# viewを作成する
	view = View()

	# ゲームを開始するかを尋ねる
	start_flag = view.start_game()

	# ゲームを開始する場合、ボードを作成する
	if start_flag:
		board = Board()

	# 最初のボードを表示
	view.display(board)

	# プレイヤーの名前を聞く
	player_black = view.add_player()
	player_white = view.add_player() 

	# ゲームにプレイヤーを追加する
	players = [Player(-1, player_black),
			   Player(1, player_white),]

	# ゲームを進める
	while not board.is_gameover():
		# 各プレイヤーごとに場面を進める
		for player in players:
			# ハンドを入力し、有効であれば次のプレイヤーに進める
			while True:
				hands = view.input_hands(player.name)

				# 有効な場所に石を置く
				if board.is_put_stone(hands):

					# 石を置く
					board.put_stone(hands)

					# 全てのリバース可能な石をリバースする
					board.reverse()

					# 置いた結果を表示する
					view.display(board)

					# 次のプレイヤーへ
					break

				# 有効ではない場所に石を置く場合
				else:
					print("もう一度入力してください")
			
			# 勝敗を判定する
			if board.is_gameover():
				print("終わり！")
				break


if __name__ == '__main__':
    main()
