
from cerberus import Validator

# ゲームを実行するクラス
class Game():
	def __init__(self, view, board) -> None:
		self.view = view
		self.board = board


		

	def prepare_player(self) -> list:
		# ゲーム開始に必要なmode, name, patternのバリデーションを行い、プレイヤー情報を返す
		schema = {
		    'player_mode': {
		        'type': 'string',
		        'allowed': ['H', 'C'],
		        'empty': False,
		    },

		    'player_name': {
		        'type': 'string',
		        'maxlength': 10,
		        'empty': False,
		    },

		    'computer_pattern': {
		        'type': 'string',
		        'allowed': ['R', 'S'],
		        'empty': False,
		    },
		}
		# バリデーションチェッククラスを作成する
		v = Validator(schema)

		players_info = [[],[]]

		for i in range(2):
			while True:
				player_mode = self.view.select_oppo()
				if not v.validate({'player_mode': player_mode}):
					self.view.announce_newinput('プレイヤーモードの入力が有効ではりません')
					continue
				players_info[i].append(player_mode)
				break

			while True:
				player_name = self.view.add_player()
				if not v.validate({'player_name': player_name}):
					self.view.announce_newinput('名前の入力が有効ではりません')
					continue
				players_info[i].append(player_name)
				break
			self.view.announce_color(player_name)

			if player_mode == 'C':
				while True:
					computer_pattern = self.view.select_strength()
					if not v.validate({'computer_pattern': computer_pattern}):
						self.view.annoussnce_newinput('強さの入力が有効ではりません')
						continue
					players_info[i].append(computer_pattern)
					break

			self.board.player_color = -self.board.player_color

		return players_info


	def add_player(self, players):
		self.player_black = players[0]
		self.player_white = players[1]


	def run(self) -> None:
		# ゲームを実行する
		while True:
			# 石の置ける場所があるか判定し、もし置けなければパスする
			if self.board.player_color == -1 and not self.board.can_rev_pos_b[:, :].any():
				self.view.announce_pass()
				self.board.next()
				continue
			elif self.board.player_color == 1 and not self.board.can_rev_pos_w[:, :].any():
				self.view.announce_pass()
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
			putable, reason = self.board.can_set_stone(hands)
			if not putable:
				self.view.announce_newinput(reason)
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
				break

			# 次のプレイヤーへ
			self.board.next()

			print('')
