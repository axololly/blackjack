# Classes:
# - Player class
# - Game class
# - Card class
# - Deck class

import random
from enum import Enum

class Suit(Enum):
    spades = 1
    hearts = 2
    diamonds = 3
    clubs = 4

class Rank(Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

class Options:
    HOLD = 0
    DRAW = 1
    BUST = -1

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.name.capitalize()} of {self.suit.name.capitalize()}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def draw(self) -> Card:
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = 0

        self.has_held = False
        self.gone_bust = False

    def draw(self, deck: Deck) -> Card:
        "Draws a card from the deck instance supplied and adds it to the player's hand."
        self.hand.append(drawn_card := deck.draw())
        self.update_score()
        return drawn_card

    def show_hand(self) -> None:
        "Prints the cards in the player's hand. Rarely ever used outside of debugging."
        [print(card) for card in self.hand]
    
    def hold(self) -> None:
        "Function for when a player decides to hold."
        self.has_held = True
    
    def update_score(self):
        "Updates a player's score based on the cards in their hand."
        self.score = sum([card.rank.value for card in self.hand])

    def is_bust(self) -> bool:
        """
        Returns True if the player's score is over 21, False otherwise.
        Requires updating the player's score before calling.
        """
        return self.score > 21
    
    ...

class Game:
    def __init__(self, *players: Player):
        self.players = list(players)
        
        random.shuffle(players)

        self.turn = 0
        
        self.deck = Deck()

    def start(self) -> None:
        "Starts the game."
        self.deck.shuffle()
        self.deal()
        self.play_round()
    
    def deal(self) -> None:
        "Deals two cards to each player."
        [
            player.draw(self.deck)
            for player in self.players
            for _ in range(2)
        ]
    
    def play_round(self) -> None:
        "Plays a round of the game."
        
        ...

        self.turn += 1
        self.turn %= len(self.players)