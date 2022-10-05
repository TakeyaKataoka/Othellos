
from board import Board
from player import Player
from view import View



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
	while True:
		# 各プレイヤーごとに場面を進める
		for player in players:
			# ハンドを入力し、有効であれば次のプレイヤーに進める
			while True:
				hands = view.input_hands(player.name)

				# 有効な場所に石を置く場合
				if board.is_put_stone(hands):
					board.put_stone(hands)

					# 置いた結果を表示する
					view.display(board)

					# 次のプレイヤーへ
					break

				# 有効ではない場所に石を置く場合
				else:
					print("もう一度入力してください")


if __name__ == '__main__':
    main()