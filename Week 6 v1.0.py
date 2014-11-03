import simplegui as s
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = s.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = s.load_image("http://i.imgur.com/17mUfmL.jpg")    

# initialize some useful global variables
in_play = False
money = 500
outcome = "Hit or Stand?"
string_message = ""
bet = 0
felt_colors = ('Green', 'Aqua', 'Brown', 'Orange')

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], 
                           pos[1] + CARD_CENTER[1]], 
                          CARD_SIZE)
        
    def drawBack(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0] + 1, 
                           pos[1] + CARD_BACK_CENTER[1] + 1], 
                          CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        st_cards = ""
        for card in self.cards:
            st_cards = st_cards + str(card) + " "
        return "Hand contains " + st_cards.strip()

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        hand_value = 0
        has_ace = False
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True
        if has_ace and hand_value < 12:
            hand_value += 10
        return hand_value
   
    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            card.draw(canvas, pos)
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        st_cards = ""
        for card in self.cards:
            st_cards = st_cards + str(card) + " "
        return "Deck contains " + st_cards.strip()

#define event handlers for buttons
def deal():
    global in_play, my_deck, player_hand, dealer_hand, outcome, \
    money, st_player, st_dealer, string_message
    if in_play:
        money -= bet
        in_play = False
        deal()
    else:    
        my_deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
        my_deck.shuffle()
        player_hand.add_card(my_deck.deal_card())
        player_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        outcome = "Hit or Stand?"
        st_player = "Player"
        st_dealer = "Dealer"
        string_message = ""
        in_play = True

def hit():
    global in_play, my_deck, player_hand, money, outcome, st_player, string_message
    if in_play:
        if player_hand.get_value() < 22:
            player_hand.add_card(my_deck.deal_card())
            if player_hand.get_value() > 21:
                st_player = "Busted!"
                string_message = "Player Busts!"
                money -= bet
                outcome = "New game?"
                in_play = False
       
def stand():
    global in_play, dealer_hand, player_hand, money, outcome, st_dealer, string_message
    if in_play:
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(my_deck.deal_card())
        if dealer_hand.get_value() > 21:
            st_dealer = "Busted!"
            string_message = "Dealer busted! You win!"
            money += bet
            outcome = "Play again?"
            in_play = False
        elif player_hand.get_value() > dealer_hand.get_value():
            string_message = "Player wins!"
            money += bet
            outcome = "Play again?"
            in_play = False
        else:
            string_message = "Dealer wins!"
            money -= bet
            outcome = "Play again?"
            in_play = False

#Betting
def increase_bet():
    global bet, money
    if bet < money:
        bet += 5

def decrease_bet():
    global bet, money
    if bet > money:
        pass
    else:
        if (bet - 5) >= 0:
            bet -= 5
            
            
# draw handler    
def draw(canvas):
    canvas.draw_text("Dealer Stands on 17", (250, 385), 33, "Red")
    lDealer = canvas.draw_text(st_dealer, (60, 185), 33, "Black")
    lPlayer = canvas.draw_text(st_player, (60, 385), 33, "Black")
    lOutcome = canvas.draw_text(outcome, (250, 350), 33, "Black")
    lMessage = canvas.draw_text(string_message, (250, 185), 33, "Black")
    lmoney = canvas.draw_text("Money: $" + str(money), (455, 25), 24, "Black")
    lbet = canvas.draw_text("Bet: $" + str(bet), (455, 50), 24, "Black")
    lBlackjack = canvas.draw_text("Blackjack...", (60, 100), 40, "Black")
    dealer_hand.draw(canvas, [-65, 200])
    player_hand.draw(canvas, [-65, 400])
    if in_play:
        dealer_hand.cards[0].drawBack(canvas, [28, 200])
        

# initialization frame
frame = s.create_frame("Blackjack", 600, 600)
frame.set_canvas_background(random.choice(felt_colors))

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_label("")
frame.add_label("Betting controls: ")
frame.add_button("Increase Bet $5", increase_bet, 200)
frame.add_button("Decrease Bet $5", decrease_bet, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
deal()
