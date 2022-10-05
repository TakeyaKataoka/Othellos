
from othello.models.board import Board
from othello.models.player import Player
from othello.views.view import View


def Main():
	# viewを作成する
	view = View()

	# ゲームを開始するかを尋ねる
	start_flag = view.start_game()

	# ゲームを開始する場合、ボードを作成する
	if start_flag:
		board = Board()

	# 最初のボードを表示
	view.display_board(board)

	# プレイヤーの名前を聞く
	player_black = view.add_player(board)
	board.player_color = - board.player_color

	player_white = view.add_player(board) 
	board.player_color = - board.player_color

	# ゲームにプレイヤーを追加する
	board.add_player(Player(-1, player_black),
					Player(1, player_white))

	# ゲームを進める
	while True:
		# 石を置くプレイヤーを表示
		view.display_player(board.player_color)

		# 各プレイヤーごとに場面を進める
		hands = view.input_hands()

		# 有効な場所に石を置けるかを確認する
		if not board.is_put_stone(hands):
			print("もう一度入力してください")
			continue

		# 石を置く
		board.put_stone(hands)

		# 全てのリバース可能な石をリバースする
		board.reverse()

		# 置いた結果を表示する
		view.display_board(board)

		# 勝敗を判定する
		if board.is_gameover():
			print("終わり！")
			break

		# 次のプイレイヤーが石を置けない場合、もう一度同じプレイヤーが石を置く
		if board.player_color == -1 and not board.black_position[:, :].any():
			print("黒がパスしました")
			continue
		elif board.player_color == 0 and not board.white_position[:, :].any():
			print("白がパスしました")
			continue

		# 次のプレイヤーへ
		board.next()

			

if __name__ == '__main__':
    Main()
