import pydealer as pyd
import dealerhelper as pydh
import discord
import asyncio
import GameController as gc

deck = pyd.Deck()
deck.shuffle()
hand = deck.deal(13)
hand.spades_sort()

game = gc.GameTable()

p1 = gc.Player('p1', '1', game)
p2 = gc.Player('p2', '2', game)
p3 = gc.Player('p3', '3', game)
p4 = gc.Player('p4', '4', game)
game.add_player(p1)
game.add_player(p2)
game.add_player(p3)
game.add_player(p4)
game.start_game()

print(p1.hand)
