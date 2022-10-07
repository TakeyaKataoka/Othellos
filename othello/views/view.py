import numpy as np

# （コンソール）ビューをユーザーに提供するクラス
class View():
	def __init__(self, board) -> None:
		self.board = board
		self.view_board = np.zeros((self.board.board_size + 2, self.board.board_size  + 2), dtype=str)


	def add_player(self) -> str:
		name = input("名前を入力してください：")
		print(name + "さんが参加しました！あなたの手番は" + self.color_convert(self.board.player_color))
		return  name


	def input_hands(self) -> list:
		return [(input("次の手を入力する(縦 1-8):")),
				(input("次の手を入力する(横 1-8):")),]

	
	def select_oppo(self):
		return [input("プレイヤー1を選択してください（H : 人間　/ C : コンピューター）:"),
				input("プレイヤー2を選択してください（H : 人間　/ C : コンピューター）:"),]

	
	def select_strength(self):
		return input("コンピューターの強さを洗濯してください（R : ★ \ S : ★★）")


	def display_board(self) -> None:
		# 文字へ変換
		# -1 = black, 1 = white, 2 = wall
		for y in range(10):
			for x in range(10):
				if self.board.board[x, y] == 1:
					self.view_board[x, y]= '●'
				elif self.board.board[x, y] == -1:
					self.view_board[x, y] = '○'
				elif self.board.board[x, y] == 2:
					self.view_board[x, y] = '■'
				else:
					self.view_board[x, y] = '-'

		# 表示する
		for stone in self.view_board:
			print(*stone)
	

	def display_hand(self):
		print(str(self.board.recent_hand) + "に石が置かれました")

	
	def ask_record(self):
		self.plus_row()
		print("今回の棋譜は以下の通りです！")
		print(self.board.record_hands)
		input("今回の棋譜を保存しますか？（Y/n）:")
		# （未）記録する場合の処理を書く


	def display_player(self) -> None:
		self.plus_row()
		color_str = self.color_convert(self.board.player_color)
		print(color_str + "の手番です")


	def display_winner(self):
		self.plus_row()
		print("勝者は「" + self.board.winner +"」です！")


	def color_convert(self, color: int) -> str:
		if color == -1:
			return "黒"
		elif color == 1:
			return "白"
		else:
			return None

	
	def plus_row(self):
		print('-------------------')

