import numpy as np

from models.board import Board

class View():
	def __init__(self) -> None:
		self.view_board = np.zeros((8 + 2, 8 + 2), dtype=str)


	def start_game(self) -> bool:
		return input("ゲームを開始しますか（Y/n）:") == "Y"


	def add_player(self) -> str:
		name = input("名前を入力してください：")
		print(name + "さんが参加しました！")
		return  name


	def input_hands(self, name: str) -> list:
		print(name + "さんの番です")
		return [int(input("次の手を入力する(縦 1-8):")),
				int(input("次の手を入力する(横 1-8):")),]


	def display(self, board: Board) -> None:
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
