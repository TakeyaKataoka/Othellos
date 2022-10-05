
import numpy as np

from othello.models.board import Board

class View():
	def __init__(self) -> None:
		self.view_board = np.zeros((8 + 2, 8 + 2), dtype=str)


	def start_game(self) -> bool:
		return input("ゲームを開始しますか（Y/n）:") == "Y"


	def add_player(self, board: Board) -> str:
		name = input("名前を入力してください：")
		print(name + "さんが参加しました！あなたの手番は" + self.color_convert(board.player_color))
		return  name


	def input_hands(self) -> list:
		return [(input("次の手を入力する(縦 1-8):")),
				(input("次の手を入力する(横 1-8):")),]


	def display_board(self, board: Board) -> None:
		# 文字へ変換
		# -1 = black, 1 = white, 2 = wall
		for y in range(10):
			for x in range(10):
				if board.board[x, y] == 1:
					self.view_board[x, y]= '●'
				elif board.board[x, y] == -1:
					self.view_board[x, y] = '○'
				elif board.board[x, y] == 2:
					self.view_board[x, y] = '■'
				else:
					self.view_board[x, y] = '-'

		# 表示する
		for stone in self.view_board:
			print(*stone)
	

	def display_player(self, color: int) -> None:
		color_str = self.color_convert(color)
		print(color_str + "の手番です")


	def color_convert(self, color: int) -> str:
		if color == -1:
			return "黒"
		elif color == 1:
			return "白"
		else:
			return None

