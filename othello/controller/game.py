# ゲームを実行するクラス
class Game():
	def __init__(self, view, board, player_black, player_white) -> None:

		self.view = view
		self.board = board
		self.player_black = player_black
		self.player_white = player_white

	def run(self) -> None:
		# ゲームを実行する
		while True:
			# 石の置ける場所があるか判定し、もし置けなければパスする
			if self.board.player_color == -1 and not self.board.can_rev_pos_b[:, :].any():
				self.view.plus_row()
				print("黒がパスしました")
				self.board.next()
				continue
			elif self.board.player_color == 1 and not self.board.can_rev_pos_w[:, :].any():
				self.view.plus_row()
				print("白がパスしました")
				self.board.next()
				continue
			
			# 石を置くプレイヤーを表示
			self.view.display_player()

			# 各プレイヤーが手を選択する
			hands = []

			if self.board.player_color == -1: # 黒
				self.player_black.select_hand(self.board)
				hands = self.player_black.hands

			elif self.board.player_color == 1: # 白
				self.player_white.select_hand(self.board)
				hands = self.player_white.hands
			
			# 石を置こうとする場所が有効化どうかを確認する
			print(hands)
			if not self.board.is_put_stone(hands):
				print("もう一度入力してください")
				continue

			# 石を置く
			if self.board.player_color == -1:
				self.player_black.put_stone(self.board)
			else:
				self.player_white.put_stone(self.board)
			
			# 全てのリバース可能な石をリバースする
			self.board.reverse()

			# 置いた結果を表示する
			self.view.display_board()
			self.view.display_hand()

			# 勝敗を判定する
			if self.board.is_gameover():
				self.board.set_winner()
				print("終わり！")
				break

			# 次のプレイヤーへ
			self.board.next()

			print('')
