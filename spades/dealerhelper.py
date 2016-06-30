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

pyd.Stack.spades_sort = spades_sort

suits_rank = {
	    "suits": {
        "Spades": 4,
        "Hearts": 3,
        "Clubs": 2,
        "Diamonds": 1
    }
}