import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [rank + ' of ' + suit for suit in suits for rank in ranks]

# Function to deal a hand of cards
def deal_hand(deck, hand_size=5):
    hand = random.sample(deck, hand_size)
    for card in hand:
        deck.remove(card)
    return hand

# Function to determine the highest card in a hand
def get_high_card(hand):
    rank_order = {rank: index for index, rank in enumerate(ranks)}
    hand_ranks = [rank_order[card.split()[0]] for card in hand]
    high_card_index = max(hand_ranks)
    return ranks[high_card_index]

# Deal hands to two players
player1_hand = deal_hand(deck)
player2_hand = deal_hand(deck)

print("Player 1's hand:", player1_hand)
print("Player 2's hand:", player2_hand)

# Determine the winner based on the highest card
player1_high_card = get_high_card(player1_hand)
player2_high_card = get_high_card(player2_hand)

print("Player 1's highest card:", player1_high_card)
print("Player 2's highest card:", player2_high_card)

if ranks.index(player1_high_card) > ranks.index(player2_high_card):
    print("Player 1 wins!")
elif ranks.index(player1_high_card) < ranks.index(player2_high_card):
    print("Player 2 wins!")
else:
    print("It's a tie!")
