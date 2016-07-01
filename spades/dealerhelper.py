import pydealer as pyd
def calc_trick_winner(trick):
	highest_card = pyd.Card()
	# for card in trick:
	# 	if card.suit == 'Spade':

def spades_sort(stack):
	stack.ranks = pyd.const.DEFAULT_RANKS
	stack.sort()
	stack.ranks = suits_rank
	stack.sort()

def custom_str(self):
	symbol = 'a'
	if self.suit == 'Diamond':
		symbol = '♦'
	elif self.suit == 'Spade':
		symbol = '♠'
	elif self.suit == 'Heart':
		symbol = '♥'
	elif self.suit == 'Club':
		symbol = '♣'
	return self.value + symbol

pyd.Card.__str__ = custom_str
pyd.Stack.spades_sort = spades_sort

suits_rank = {
	    "suits": {
        "Spades": 4,
        "Hearts": 3,
        "Clubs": 2,
        "Diamonds": 1
    }
}
