import random

playing = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self, suits, ranks):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def __len__(self):
        return len(self.cards)


class Chips:
    def __init__(self, total=0, bet=0):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = bet

    def win_bet(self):
        self.total += (self.bet)*2

    def lose_bet(self):
        self.total -= self.bet

    def __str__(self):
        return f'{self.total}'


def take_bet(total, bet=0):
    while bet not in range(1, total+1):
        try:
            bet = int(input('Enter bet amount:'))
        except:
            print('please enter a valid bet amount.')
    return bet


def hit(deck, hand):

    card = deck.deal()
    hand.add_card(card)


def hit_or_stand(deck, hand):

    status = input('do u want to hit or stand??')
    if status[0].lower() == 'h':
        hit(deck, hand)
        return True
    elif status[0].lower() == 's':
        print("Player stands. Dealer is playing.")
        return False


def show_some(player, dealer):
    print('-----------------------------------------')
    print('--|  Dealer  |--')
    for i in range(len(dealer)):
        if i == 0:
            print("Hidden card")
        else:
            print(dealer.cards[i])

    print('\n\n--|  Player  |--')
    for i in range(len(player)):
        print(player.cards[i])
    print('Hand value: ', player.value)
    print('-----------------------------------------')
    print('\n')


def show_all(player, dealer):
    print('-----------------------------------------')
    print('--|  Dealer  |--')
    for i in range(len(dealer)):
        print(dealer.cards[i])
    print('Dealer hand value: ', dealer.value)

    print('\n\n--|  Player  |--')
    for i in range(len(player)):
        print(player.cards[i])
    print('Hand value: ', player.value)
    print('-----------------------------------------')
    print('\n')


def player_busts(player_value):
    return player_value > 21


def player_wins(player_value, dealer_value):
    if player_busts(player_value):
        return False
    if player_value <= dealer_value <= 21:
        return False
    return True


def dealer_busts(dealer_value):
    return dealer_value > 21


def dealer_wins(player_value, dealer_value):
    if dealer_busts(dealer_value):
        return False
    if dealer_value <= player_value <= 21:
        return False
    return True


def play_again():
    p = input('do u want to play again??')
    if p[0].lower() == 'y':
        return True
    return False
