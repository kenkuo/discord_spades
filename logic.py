from pydealer import pydealer 

class Player:
	score = 0
	bid = 0
	bags = 0

class Trick(Stack):
	leading_suit = ''
	suit_broken = False


def init(players):
	playerlist = []
	for p in players:
		player = Player(p)
		playerlist.append()
	startgame(playerlist)

def start_game(playerlist):
	deck = Deck()
	deck.shuffle()
	deck.ranks = 
	for p in playerlist:
		p.hand = deck.deal(13)
	return playerlist

def play_card(card, trick):
	if trick.count == 0:
		trick.leading_suit == card.suit
	trick.add(card)
	return trick

def calc_trick_winner(trick)
	highest_card = Card()
	for card in trick:
		if card.suit == 'Spade'

