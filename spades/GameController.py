import pydealer as pyd

class GameTable():
	def __init__(self):
		self.players = []
		self.current_trick = pyd.Stack()

	def is_players_empty(self):
		if len(self.players) == 0:
			return True
		else:
			return False

	def is_players_full(self):
		if len(self.players) == 4:
			return True
		else:
			return False

	def add_player(self, player):
		if len(self.players) <= 4:
			self.players.append(player)
			return player
		else:
			return False

	def start_game(self):
		deck = pyd.Deck()
		deck.shuffle()
		for p in self.players:
			p.hand = deck.deal(13)
			p.hand.spades_sort()
		return self.players

	def play_card(self, card, trick):
		if trick.count == 0:
			trick.leading_suit == card.suit
		trick.add(card)
		return trick


class Player():

	def __init__(self, name, uid, table):
		self.name = name
		self.uid = uid
		self.table = table
		self.hand = pyd.Stack()
		self.team = 0
		self.bid = 0
		self.points = 0
		self.bags = 0
		self.tricks = 0

	def play_card(self, card):
		self.table.play_card(card)