"""
# Problem 54: Poker Hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in 
the following way:

0 - High Card: Highest value card.
1 - One Pair: Two cards of the same value.
2 - Two Pairs: Two different pairs.
3 - Three of a Kind: Three cards of the same value.
4 - Straight: All cards are consecutive values.
5 - Flush: All cards of the same suit.
6 - Full House: Three of a kind and a pair.
7 - Four of a Kind: Four cards of the same value.
8 - Straight Flush: All cards are consecutive values of same suit.
9 - Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for 
example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
for example, both players have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1        Player 2            Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
        Pair of Fives       Pair of Eights

2       5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
        Highest card Ace    Highest card Queen

3       2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds

4       4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from os import path

# OOOOOOOOH THIS IS FUN!

file_name = 'p_054_poker.txt'
file_path = path.join('Files', file_name)

with open(file_path, 'r') as poker_hand_file:
    poker_hands = [line.split() for line in poker_hand_file.readlines()]
    poker_hands = [{1: cards[:5], 2: cards[5:]} for cards in poker_hands]
    # Wow I wish I had the := syntax available so that I could do this all in one thing!


value = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7,
         "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}


def assess_hand(hand):
    cards = sorted([value[card[0]] for card in hand])
    types_cards = list(set(cards))
    if len(types_cards) == 5:
        straight = ([cards[index+1] - face_value for index, face_value in enumerate(cards[:-1])]
                    == [1, 1, 1, 1])
    else:
        straight = False
    suits = list(set([card[1] for card in hand]))

    if len(suits) == 1:
        if cards == [10, 11, 12, 13, 14]:
            return 9, 14
        elif straight:
            return 8, cards[-1]
        else:
            return 5, cards[-1]
    elif straight:
        return 4, cards[-1]
    elif len(types_cards) == 2:
        # either full house or four of a kind
        if (cards[0] == cards[1] == cards[2] == cards[3]
                or cards[1] == cards[2] == cards[3] == cards[4]):
            return 7, cards[3]  # cards[3] is always in the set of cards
        else:
            if cards[1] == cards[2]:
                return 6, cards[2]  # the three of a kind is [t, t, t, p, p]
            else:
                return 6, cards[-1]  # the three of a kind is [p, p, t, t, t]
    elif len(types_cards) == 3:
        if cards[0] == cards[1] and cards[2] == cards[3]:  # two pair, high card
            return 2, cards[3], cards[1], cards[-1]
        elif cards[1] == cards[2] and cards[3] == cards[4]:  #two pair, low card
            return 2, cards[4], cards[2], cards[0]
        else:
            # possibilities: [t, t, t, x, y], [x, t, t, t, y], [x, y, t, t, t]
            if cards[0] == cards[1] == cards[2]:
                return 3, cards[0], cards[-1], cards[-2]
            elif cards[1] == cards[2] == cards[3]:
                return 3, cards[1], cards[-1], cards[0]
            else:
                return 3, cards[2], cards[1], cards[0]
    elif len(types_cards) == 4:  # pair
        for index, card in enumerate(cards[:-1]):
            if card == cards[index + 1]:
                return 1, card, cards[-1]
    else:
        return 0, cards[-1], cards[-2], cards[-3], cards[-4], cards[-5]


def compare_hands(hand1, hand2):
    hand1_score = assess_hand(hand1)
    hand2_score = assess_hand(hand2)

    if len(hand1_score) == len(hand2_score):
        for index, score in enumerate(hand1_score):
            if score != hand2_score[index]:
                return 1 + score > hand2_score[index]
    else:
        return 1 + hand1_score[0] > hand2_score[0]


count = 0
for player_hands in poker_hands:
    if compare_hands(player_hands[1], player_hands[2]) == 1:
        count += 1
print(count)