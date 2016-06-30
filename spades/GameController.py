import pydealer as pyd
class GameController():
	players = []

	def is_players_empty():
		if len(players) == 0:
			return True
		else:
			return False

	def is_players_full():
		if len(players) == 4:
			return True
		else:
			return False

	def add_player(player):
		if len(players) <= 4:
			players.append(player)
			return player
		else:
			return False

	def start_game(playerlist):
		deck = pyd.Deck()
		deck.shuffle()
		for p in playerlist:
			p.hand = deck.deal(13)
		return playerlist

	def play_card(card, trick):
		if trick.count == 0:
			trick.leading_suit == card.suit
		trick.add(card)
		return trick

	def calc_trick_winner(trick):
		highest_card = pyd.Card()
		# for card in trick:
		# 	if card.suit == 'Spade':
	
	def suit_sort(self, stack):
		stack.ranks = pyd.const.DEFAULT_RANKS
		stack.sort()
		stack.ranks = pyd.const.SUITS
		stack.sort()
