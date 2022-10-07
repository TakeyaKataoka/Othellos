
from models.board import Board
from models.player import Player
from algorithm.algorithm import Algorithm


class Game():
	def __init__(self, view) -> None:
		self.view = view

	def start(self):
		# ビュー（ユーザーインターフェース）を作成する
		# view = View()

		# ゲームを開始する場合、ボードを作成する
		if self.view.start_game():
			board = Board()

		# 対戦相手を選ぶ
		algo1 = Algorithm('H')
		algo2 = Algorithm('H')
		flags = view.select_oppo()

		if flags[0] == 'C':
			print("プレイヤー１について")
			algo1 = Algorithm(view.select_strength())
		else:
			pass

		if flags[1] == 'C':
			print("プレイヤー2について")
			algo2 = Algorithm(view.select_strength())
		else:
			pass

		# プレイヤーの名前を聞く
		player1_name = view.add_player(board)
		board.player_color = - board.player_color

		player2_name = view.add_player(board) 
		board.player_color = - board.player_color

		# ゲームにプレイヤーを追加する
		player_black = Player(-1, player1_name, algo1)
		player_white = Player(1, player2_name, algo2)

		# ゲームを進める
		while True:
			# 石の置ける場所があるか判定し、もし置けなければパスする
			if board.player_color == -1 and not board.black_position[:, :].any():
				view.plus_row()
				print("黒がパスしました")
				board.next()
				continue
			elif board.player_color == 1 and not board.white_position[:, :].any():
				view.plus_row()
				print("白がパスしました")
				board.next()
				continue

			# 石を置くプレイヤーを表示
			view.display_player(board.player_color)

			# 各プレイヤーが手を選択する
			hands = []

			if board.player_color == -1: # 黒
				if player_black.computer_flag: # コンピューター
					player_black.select_hand(board)
					hands = player_black.hands
				else:
					player_black.select_hand(board, view.input_hands())
					hands = player_black.hands
			elif board.player_color == 1: # 白
				if player_white.computer_flag: # コンピューター
					player_white.select_hand(board)
					hands = player_white.hands
				else:
					player_white.select_hand(board, view.input_hands())
					hands = player_white.hands
			
			# 石を置こうとする場所が有効化どうかを確認する
			print(hands)
			if not board.is_put_stone(hands):
				print("もう一度入力してください")
				continue

			# 石を置く
			if board.player_color == -1:
				player_black.put_stone(board)
			else:
				player_white.put_stone(board)
			
			# 全てのリバース可能な石をリバースする
			board.reverse()

			# 置いた結果を表示する
			view.display_board(board)
			view.display_hand(board)

			# 勝敗を判定する
			if board.is_gameover():
				board.set_winner()
				print("終わり！")
				break

			# 次のプレイヤーへ
			board.next()

			print('')
		
		# 勝者を表示する
		view.display_winner(board.winner)

		# 棋譜を保存するか聞く
		view.ask_record(board)
	
		return board.winner
