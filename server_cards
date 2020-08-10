import socket
import random
import pygame
from _thread import *
import sys

server = "192.168.0.106"
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connections.")

def client(conn):

    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                conn.send(data.encode())

            conn.sendall(str.encode(reply))

        except:
            break



# Card class definition
class Card:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value

# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
# The type of card
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
# The card value
cards_values = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": 11, "12": 12, "13": 13}
# The deck of cards - List of Objects
deck = []
# Adding each card to the deck
for suit in suits:
    for card in cards:
        deck.append(Card(suit, card))

players = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(client, (conn,))
    players += 1

    # Game starts
    for i in range(3, 0, -1):
        conn.send("The game started!".encode())

        if i>2:

            # Choosing a random card as the pot card to start the game
            pot_card = random.choice(deck)
            deck.remove(pot_card)

            pot_card_send = pot_card.value + pot_card.suit_type[0]
            conn.send(pot_card_send.encode())

        # Dealing 3 cards to each of the clients
        for j in range(3, 0, -1):
            dealt_card = random.choice(deck)
            deck.remove(dealt_card)

            dealt_card_send = dealt_card.value + dealt_card.suit_type[0]
            conn.send(dealt_card_send.encode())



