#Define a deck of cards

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


class Card():

    def __init__(self,suits,rank):
        self.suits=suits
        self.rank=rank
        self.value=values[self.rank]

    def __str__(self):
        return F"{self.rank} of {self.suits}"


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r))

    def __str__(self):
        return F"first card in the deck is: {self.deck[0]}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value=self.value + card.value
        if card.rank=="Ace":
            self.aces=1+self.aces

    def adjust_for_ace(self):
        if self.value>21:
            while self.value > 10 and self.aces>=1:
                self.value=self.value-self.aces*(11-1)
                self.aces=self.aces-1

    def blackjack(self):
        self.value = 21


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet=0


    def new_bet(self):

        bet=True

        while bet:
            self.bet = int(input(f"Please place your bet 0 to {self.total} "))

            if self.bet>self.total:
                print(f"Ups - you can max bet your balance of {self.total} ")

            else:
                bet=False
                break

    def win_bet(self):
        self.total=self.total+self.bet

    def lose_bet(self):
        self.total=self.total-self.bet



def hit(deck,hand):

    #Add new card to players hand and remove it from deck
    hand.add_card(deck.deal())

    #check hand for aces
    hand.adjust_for_ace()

    #check for blackjack
    if hand.value<=21 and len(hand.cards)==5:
        hand.blackjack()


def hit_or_stand(deck,hand):
    global hit_stand
    hit_stand = "empty"
    player_input = "empty"

    while player_input in ("empty"):
        player_input=input("Hit or Stand?")
        if player_input not in ("Hit","Stand"):
            print("Invalid value - please wirte Hit or Stand")

    if player_input in ("Hit"):
        hit(deck,hand)
        hit_stand ="Hit"
        print(hit_stand)
    elif:
        hit_stand ="Stand"
        print(hit_stand)

def hit_dealer(deck,hand):

    while hand.value<=17:
        #add to hand
        hand.add_card(deck.deal())

        #check hand for aces
        hand.adjust_for_ace()

        if hand.value<=21 and len(hand.cards)==5:
            hand.blackjack()


def show_some(player,dealer):

    #show first card for dealer, all cards for player
    print("")
    print(f"Dealer's first card:\n{dealer.cards[0]}")

    print("")
    print("Player's card:")
    for i in range(len(player.cards)):
        print(player.cards[i])
    print(f"Value of Player's cards: {player.value}")



def show_all(player,dealer):

    print("")
    print("Dealers's card:")
    for i in range(len(dealer.cards)):
        print(dealer.cards[i])

    print(f"Value of Dealers's cards: {dealer.value}")

    print("")
    print("Player's card:")
    for i in range(len(player.cards)):
        print(player.cards[i])
    print(f"Value of Player's cards: {player.value}")



def player_busts(player):
    if player.value>21:
        return True

def player_wins(dealer,player):
    if player.value>dealer.value:
        return True

def dealer_busts(dealer):
    if dealer.value>21:
        return True

def dealer_wins(dealer,player):
    if dealer.value>player.value:
        return True


#if dealer reach 17 PUSH!
def push(dealer,player):
    if dealer.value == player.value:
        return True


def replay():

    user_input="empty"

    while user_input not in ("Yes", "No"):
        user_input=input("Would you like to play again? Yes/No ")
        if user_input not in ("Yes", "No"):
            print("Wrong input, please answer Yes or No ")

    if user_input=="Yes":
        return True
    else:
        return False

#initiate deck and shuffle
new_deck=Deck()
new_deck.shuffle()

#setup hands
player=Hand()
dealer=Hand()

#Allocate two cards to both dealer and player
for i in range(2):
    dealer.add_card(new_deck.deal())
    player.add_card(new_deck.deal())

#Hand out chips to player
player_chips=Chips()

# Set up the Player's chips
player_chips.new_bet()


# Show cards (but keep one dealer card hidden)
show_some(player,dealer)


#And game is on!

from IPython.display import clear_output
play=True
playing=True
player_playing=True

#Set players chips (should not be part of a loop!):
player_chips=Chips()

while play:

    #reset loops
    playing=True
    player_playing=True

    #clear the board
    clear_output()

    # Print an opening statement
    print("Welcome to Blackjack")
    print("--------------------")

    # Create & shuffle the deck
    new_deck=Deck()
    new_deck.shuffle()

    # Setup hands
    player=Hand()
    dealer=Hand()

    # Deal two cards to dealer and player:
    for i in range(2):
        dealer.add_card(new_deck.deal())
        player.add_card(new_deck.deal())


    # Prompt the Player for their bet
    player_chips.new_bet()

    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)


    while playing:

        while player_playing:
            # Prompt for Player to Hit or Stand
            hit_or_stand(new_deck,player)

            # Show cards (but keep one dealer card hidden)
            if hit_stand == "Hit":
                show_some(player,dealer)
            else:
                break


            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_busts(player):
                player_chips.lose_bet()
                print("Busted - you went over 21")
                player_playing=False
                playing=False



        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if not player_busts(player):
            hit_dealer(new_deck,dealer)

            # Show all cards
            print ("--------------------")
            show_all(player,dealer)
            print ("--------------------")

            # Dealer bust Run different winning scenarios
            if dealer_busts(dealer):
                player_chips.win_bet()
                print("Player wins")
                break

            elif dealer_wins(dealer,player):
                player_chips.lose_bet()
                print("Dealer wins")
                break

            elif player_wins(dealer,player):
                player_chips.win_bet()
                print("Player wins")
                break

            elif push(dealer,player):
                print("Draw - nobody wins")
                break

    # Inform Player of their chips total
    print(f"Player's total chips: {player_chips.total} ")

    # Ask to play again
    if replay()!=True:
        play=False
        break
    else:
        continue
