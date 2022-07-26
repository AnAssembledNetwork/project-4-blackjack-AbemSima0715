2
# shuffle(list) : returns a list of shuffle values. [1,2,4,5] -> [5,1,2,4]
from random import shuffle

# sleep(3): delays the program by 3 seconds
from time import sleep

SUITS = ['♠️','♥️','♣️','♦️']
VALUES = {'A': 11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 ,'10':10, 'J':10, 'Q':10 ,'K':10}

class Card:

    def __init__(self, suit, value):
        """Initializier for a Card object that contains a suit and a value."""

        self.suit = suit
        self.val = value
    
    def __str__(self):
        """Returns the string representation of a card."""

        return f"|--------|\n\
|   {self.val}{self.suit}   |\n\
|________|\n"
    
    def value(self):
        """Return the value that is on the card."""

        return self.val

class Deck:

    def __init__(self):
        """Initializer for a DECK object that holds each card."""

        self.cards = []
        self.shuffle_cards()
    
    def hit(self):
        """Removes the card from the top of the deck and returns the value."""

        if self.cards:
            return self.cards.pop()
        else:
            self.shuffle_cards()
            return self.cards.pop()
    
    def shuffle_cards(self):
        """Creates and shuffle the cards in a deck. If playing WAR leave the second black of code commented since
        blackjack uses 8 deck of cards. Leave the first deck uncommented if you are playing war."""

        # # UNCOMMENT this code if you are playing War
        # self.cards = []
        # for suit in SUITS:
        #     for value in VALUES.keys():
        #         self.cards.append(Card(suit, value))
        
        # shuffle(self.cards)

        # UNCOMMENT this code if you are playing blackjack
        self.cards = []
        for i in range(8):
            for suit in SUITS:
                for value in VALUES.keys():
                    self.cards.append(Card(suit, value))
        
        shuffle(self.cards)
    
    def empty(self):
        """Returns True or False depending on if the deck is empty."""

        return True if self.deck else False
        

def clear_screen():
    """Clear the contents of the console."""
    sleep(4)
    for i in range(100):
        print()

def print_hand(cards):
    """
    Prints each card in the list of cards.
        Keyword arguments:
        cards     --  A list of card objects
    """
    for card in cards:
        print(card)
##################DO NOT EDIT ABOVE THIS LINE################


def deal_cards(num_players, player_hands):
  """
  Setup for the game. Given the number of players and a dictionary of each of their hands,
  deals out the appropriate amount of cards to each player.
      Keyword arguments:
      num_players     --  an integer value of the total number of players that will be
                          playing the game.
      player_hands    --  an empty dictionary thtat contains the current player and each of their 
                          hands. Should be in the format {player: [cards]}
  
      Return Arguments:

      player_hands    -- a populated dictionary that has all the players and the cards they need.
  """



  # figure out dictionary whos keys are the player and whos value is an empty list
  for i in range(2):
    for j in range(1, num_players + 1):
      player_hands[j] = [deck.hit(), deck.hit()]
    # print_hand(player_hands[i])
      # print("Player" + str(j))
      # print("Card" + str(i))
      # for _ in range(3):
      #   c = deck.hit()
      #   print(c)
      # print
      # player_hands[players] += [deck.hit()]
  #     player_hands[card].append(deck.hit())
  # print_hand(player_hands[1])
  # print_hand(player_hands[2])
  # print_hand(player_hands[3])
  return player_hands

    

  pass


def calculate_hand(player, player_hands):
    """
    Calculates the players current hand point total.
        Keyword arguments:
        player          --  an integer value representing the current player that is 
                            making their turn.
        player_hands    --  a dictionary thtat contains the current player and each of their hands.
                            Should be in the format {player: [cards]}
    
        Return Arguments:

        point_total     -- an integer value representing the hand's point total.
    """
    
    point_total = 0
    for card in player_hands[player]:
      point_total += VALUES[card.value()]
    # print(player_hands)

    return point_total
    #print_hand(player_hands[player])
    # pass


def play_turn(player, player_hands):
  """
  Simulates one turn for a player. Should allow a player to hit until they choose
  to stay. Should also alart a player if they go over the value of 21.
      Keyword arguments:
      player          --  an integer value representing the current player that is 
                          making their turn.
      player_hands    --  a dictionary thtat contains the current player and each of their hands.
                          Should be in the format {player: [cards]}
  """
  
  # if player point_total > 
  #   print("You went over 21 you lose")
  # elif:
  #   input("Would you like to hit or stay")
  # while player point_total < 21 and choose to Hit:
  #   give them a new card and then you want to calculate their hand again
  # and if that is less than 21 ask them to hit or stay again
  # calculate_hand(player, player_hands)
  point_total = calculate_hand(player, player_hands)
  print_hand(player_hands[player])
  move = "hit"
  
  while move == "hit" and point_total < 21:
    print(point_total)
    # print currrent playeres hands
    move = input("Would you like to hit or stay? ")
    if move == "hit":
      player_hands[player].append(deck.hit())
      point_total = calculate_hand(player, player_hands)
      print_hand(player_hands[player])
  if point_total > 21:
    print("Looks like player" ,player, "went over 21 they lost, imagine 🤣🤣")
  if point_total == 21:
    print("Player",player,"got a blackjack 👍")
  
    # if point_total > 21:
    #   print("You went over you lose")
    # if point_total == 21:
    #   print("BLACKJACK you win")
    
      
    # elif response == "stay":
    #   player_hands[player]
  # print(player_hands)  

    
      
      
      
      
    
      
  # if response = hit:


  return player_hands
    
  

    
def dealer_turn(player_hands):
    """
    After every player makes their turn, call this function to automate the dealer's
    turn. Remember, the dealer keeps hitting the deck until their hand value is greater than
    16. Once the dealer has collected their hand, determine who in the game did or did not win.
        Keyword arguments:
        player_hands    --  a populated dictionary thtat contains the current player and each of their hands.
                            Should be in the format {player: [cards]}
    
        Return Arguments:
        winners    -- a list of string representations of the winners
    """
    
    dealers_hand = [deck.hit(), deck.hit()]
    point_total = 0
    for card in dealers_hand:
      point_total += VALUES[card.value()]
    print("Dealer's first total", point_total)  
    while point_total <= 16:
      card = deck.hit()
      point_total += VALUES[card.value()]
      print("Dealer's next total", point_total)
    
    winners = []

    
    for player_num in player_hands:
      total_value = calculate_hand(player_num, player_hands)
      if ((total_value >= point_total) and (total_value <= 21)):
        winners.append(str(player_num))
      elif total_value <= 21 and point_total > 21:
        winners.append(str(player_num))

    return winners
        
        
      
      
    

def declare_winner(winners):
  """
  Given a list of winners goes through each winner and lets the users know
  which ones won.
      Keyword arguments:
      winners         --  a list of string representations of the winners
  """
  for player_num in winners:
    print(f"Congratulations Player {player_num} on winning this game, take this imaginary money 💵💵 ")
    print()
  if len(winners) == 0:
      print("Looks like dealer won this one, boohoo ")

def play_blackjack(num_players, player_hands):
    """
    Setup for the game. Given the number of players and a dictionary of each of their hands,
    deals out the appropriate amount of cards to each player.
        Keyword arguments:
        player_hands    --  a populated dictionary thtat contains the current player and each of their hands.
                            Should be in the format {player: [cards]}
    
    """
    player_hands = deal_cards(num_players, player_hands)
    for player in range(1, num_players + 1):
     play_turn(player, player_hands)
    winners = dealer_turn(player_hands)
    declare_winner(winners)
    keeplaying = input("Do you want to play again (Y/N) ")
    if keeplaying == "y":
      blackjack()
    
    # pass


def blackjack():
  """
  The initializer for the blackjack game. This function should ask the user how many
  players will be participating in the game. It should also create the empty dictionary that 
  is passed when the game starts. No other code should be in here but any code that is necessary
  prior to the first turn of the game.
  """
  players = int(input("how many people are playing? "))
  play_blackjack(players, {})
  pass

##################DO NOT EDIT BELOW THIS LINE################
def main():
    """The main function that starts the game of blackjack"""
    global deck
    deck = Deck()

    blackjack()

# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
    main()
