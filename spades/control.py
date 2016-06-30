import pydealer as pyd
import dealerhelper as pydh
import discord
import asyncio
import GameController as gc

deck = pyd.Deck()
deck.shuffle()
hand = deck.deal(13)
hand.spades_sort()
print(hand)

