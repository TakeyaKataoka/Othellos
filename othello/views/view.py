import numpy as np

# （コンソール）ビューをユーザーに提供するクラス
class View():
	def __init__(self, board) -> None:
		self.board = board
		self.view_board = np.zeros((self.board.board_size + 2, self.board.board_size  + 2), dtype=str)


	def deco(f):
		def plus_row(*args, **keywords):
			print('-------------------')
			result = f(*args, **keywords)
			print('-------------------')
			return result
		return plus_row


	def color_convert(self, color: int) -> str:
		if color == -1:
			return "黒"
		elif color == 1:
			return "白"
		else:
			return None


	def add_player(self) -> str:
		name = input("名前を入力してください：")
		return  name


	def input_hands(self) -> list:
		return [(input("次の手を入力する(縦 1-8):")),
				(input("次の手を入力する(横 1-8):")),]

	
	def select_oppo(self) -> str:
		return input(self.color_convert(self.board.player_color) + \
					 "のプレイヤーを選択してください（H : 人間　/ C : コンピューター）:")

	
	def select_strength(self):
		print(self.color_convert(self.board.player_color) + "のプレイヤーについて")
		return input("コンピューターの強さを洗濯してください（R : ★ \ S : ★★）")


	def announce_color(self, name):
		print(name + "さんが参加しました！あなたの手番は" + self.color_convert(self.board.player_color))


	def announce_pass(self):
		color_str = self.color_convert(self.board.player_color)
		print(color_str + "がパスしました")


	def announce_newinput(self, reason):
		print(reason + "\nもう一度入力してください")


	@deco
	def display_record(self):
		print("今回の棋譜は以下の通りです！")
		print(self.board.record_hands)

		# （未）記録する場合の処理を書く
		# input("今回の棋譜を保存しますか？（Y/n）:")
	

	@deco
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
	

	@deco
	def display_hand(self):
		print(str(self.board.recent_hand) + "に石が置かれました")


	@deco
	def display_player(self) -> None:
		color_str = self.color_convert(self.board.player_color)
		print(color_str + "の手番です")


	@deco
	def display_winner(self):
		print("勝者は「" + self.color_convert(self.board.winner) +"」です！")


	

	
	

