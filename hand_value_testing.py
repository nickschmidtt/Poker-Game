# Nick Schmidt
# Hand Value Testing

from Card_Ranking_B24 import poker_hand
from Card_Ranking_B24 import card

#Royal flush and one pair
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",8)
c5 = card("clubs",8)
c6 = card("spades",11)
c7 = card("spades",10)

poker1 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker1.hand_value() == (9,[14])

#Royal flush
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",3)
c5 = card("clubs",8)
c6 = card("spades",11)
c7 = card("spades",10)

poker2 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker2.hand_value() == (9,[14])

#Royal flush with three of a kind
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",10)
c5 = card("clubs",10)
c6 = card("spades",11)
c7 = card("spades",10)

poker3 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker3.hand_value() == (9,[14])

#Royal flush full 7 cards flush
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("spades",8)
c5 = card("spades",9)
c6 = card("spades",11)
c7 = card("spades",10)

poker4 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker4.hand_value() == (9,[14])

#Royal flush full 7 cards straight
c1 = card("spades",14)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",9)
c5 = card("clubs",8)
c6 = card("spades",11)
c7 = card("spades",10)

poker5 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker5.hand_value() == (9,[14])

#Straight flush
c1 = card("spades",7)
c2 = card("spades",8)
c3 = card("spades",6)
c4 = card("clubs",2)
c5 = card("spades",9)
c6 = card("spades",5)
c7 = card("diamonds",3)

poker6 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker6.hand_value() == (8,[9])

#Straight flush with 7 cards
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("spades",8)
c5 = card("spades",7)
c6 = card("spades",11)
c7 = card("spades",10)

poker7 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker7.hand_value() == (8,[13])

#Straight flush with trips
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",12)
c5 = card("clubs",12)
c6 = card("spades",11)
c7 = card("spades",10)

poker8 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker8.hand_value() == (8,[13])

#Straight flush with two pair
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",9)
c5 = card("clubs",12)
c6 = card("spades",11)
c7 = card("spades",10)

poker9 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker9.hand_value() == (8,[13])

#Straight flush with one pair
c1 = card("spades",9)
c2 = card("spades",13)
c3 = card("spades",12)
c4 = card("diamonds",5)
c5 = card("clubs",5)
c6 = card("spades",11)
c7 = card("spades",10)

poker10 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker10.hand_value() == (8,[13])

#Quads
c1 = card("spades",9)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",12)
c6 = card("spades",11)
c7 = card("spades",10)

poker11 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker11.hand_value() == (7,[12,11])

#Quads with pair
c1 = card("spades",9)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",12)
c6 = card("hearts",10)
c7 = card("spades",10)

poker12 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker12.hand_value() == (7,[12,10])

#Quads with trips
c1 = card("diamonds",10)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",12)
c6 = card("hearts",10)
c7 = card("spades",10)

poker13 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker13.hand_value() == (7,[12,10])

#full house two trips
c1 = card("diamonds",11)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",11)
c6 = card("hearts",11)
c7 = card("spades",6)

poker14 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker14.hand_value() == (6,[12,11])

#full house
c1 = card("diamonds",11)
c2 = card("hearts",12)
c3 = card("clubs",12)
c4 = card("diamonds",12)
c5 = card("spades",11)
c6 = card("hearts",5)
c7 = card("spades",7)

poker15 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker15.hand_value() == (6,[12,11])

#full house low trips
c1 = card("diamonds",11)
c2 = card("hearts",4)
c3 = card("clubs",4)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("hearts",5)
c7 = card("spades",7)

poker16 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker16.hand_value() == (6,[4,11])


#full house trips and two pair
c1 = card("diamonds",11)
c2 = card("hearts",4)
c3 = card("clubs",4)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("hearts",9)
c7 = card("spades",9)

poker17 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker17.hand_value() == (6,[4,11])

#flush
c1 = card("diamonds",11)
c2 = card("hearts",7)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",10)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker18 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker18.hand_value() == (5,[11,9,5,4,2])

#flush with pair
c1 = card("diamonds",11)
c2 = card("hearts",7)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker19 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker19.hand_value() == (5,[11,9,5,4,2])

#flush with trips
c1 = card("diamonds",11)
c2 = card("hearts",11)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",11)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker20 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker20.hand_value() == (5,[11,9,5,4,2])

#flush with two pair
c1 = card("diamonds",11)
c2 = card("hearts",11)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",9)
c6 = card("diamonds",9)
c7 = card("diamonds",2)

poker21 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker21.hand_value() == (5,[11,9,5,4,2])

#flush with two pair
c1 = card("diamonds",11)
c2 = card("hearts",10)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("spades",9)
c6 = card("diamonds",8)
c7 = card("diamonds",7)

poker22 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker22.hand_value() == (5,[11,8,7,5,4])

#flush with all seven cards
c1 = card("diamonds",11)
c2 = card("diamonds",10)
c3 = card("diamonds",5)
c4 = card("diamonds",4)
c5 = card("diamonds",6)
c6 = card("diamonds",13)
c7 = card("diamonds",7)

poker23 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker23.hand_value() == (5,[13,11,10,7,6])

#straight
c1 = card("diamonds",11)
c2 = card("spades",10)
c3 = card("clubs",5)
c4 = card("hearts",9)
c5 = card("diamonds",6)
c6 = card("clubs",12)
c7 = card("diamonds",8)

poker24 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker24.hand_value() == (4,[12])

#straight with pair
c1 = card("diamonds",11)
c2 = card("spades",10)
c3 = card("clubs",5)
c4 = card("hearts",9)
c5 = card("diamonds",10)
c6 = card("clubs",12)
c7 = card("diamonds",8)

poker25 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker25.hand_value() == (4,[12])

#straight with two pair
c1 = card("diamonds",11)
c2 = card("spades",10)
c3 = card("clubs",8)
c4 = card("hearts",9)
c5 = card("diamonds",10)
c6 = card("clubs",12)
c7 = card("diamonds",8)

poker26 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker26.hand_value() == (4,[12])

#straight with trips
c1 = card("diamonds",11)
c2 = card("spades",10)
c3 = card("clubs",10)
c4 = card("hearts",9)
c5 = card("diamonds",10)
c6 = card("clubs",12)
c7 = card("diamonds",8)

poker27 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker27.hand_value() == (4,[12])

#three of a kind
c1 = card("clubs",10)
c2 = card("spades",11)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",7)
c6 = card("diamonds",7)
c7 = card("spades",7)

poker28 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker28.hand_value() == (3,[7,12,11])


#two pair
c1 = card("clubs",10)
c2 = card("spades",10)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",7)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker29 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker29.hand_value() == (2,[10,7,12])


#two pair three pairs
c1 = card("clubs",10)
c2 = card("spades",12)
c3 = card("hearts",12)
c4 = card("spades",3)
c5 = card("clubs",7)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker30 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker30.hand_value() == (2,[12,7,10])

#single pair
c1 = card("clubs",10)
c2 = card("spades",10)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",4)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker31 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker31.hand_value() == (1,[10,12,8,7])

#high card
c1 = card("clubs",10)
c2 = card("spades",2)
c3 = card("hearts",12)
c4 = card("spades",8)
c5 = card("clubs",4)
c6 = card("diamonds",7)
c7 = card("spades",3)

poker32 = poker_hand(c1,c2,c3,c4,c5,c6,c7)
assert poker32.hand_value() == (0,[12,10,8,7,4])

#print("....hand value check complete....")
"""
Royal flush -> 1-5
    with no pair
    with one pair 
    with three of a kind
    full 7 cards

Straight flush -> 6-10
    with no pair
    with one pair
    with three of a kind
    full 7 cards

Four of a kind -> 11-13
    regular
    with pair
    with three of a kind

Full house -> 14-17
    two three of a kinds, no pair
    two three of a kind, pair
    
flush -> 18-23
    regular
    with pair
    with two pair
    with straight
    with trips

straight -> 24-27
    regular
    with pair
    with two pair
    with trips

three of a kind -> 28
    regular

two pair -> 29-30
    regular
    three pairs

one pair -> 31
    regular

high card -> 32
"""
#print("....moving on to hand comparison....")

# random hand generator
import random as r
def hand():
    suites = ("spades","hearts","clubs","diamonds")
    numbers = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    cards = []
    while len(cards) < 7:
        suite = r.choice(suites)
        number = r.choice(numbers)
        newcard = card(suite,number)
        if newcard not in cards:
            cards += [newcard]
    print("\n\n",cards)
    poker_hand_test = poker_hand(cards[0],cards[1],cards[2],cards[3],cards[4],cards[5],cards[6]).hand_value()
    new_hand_val = []
    for item in poker_hand_test:
        new_hand_val += [item]
    hand_val_dict = {0:"High Card",1:"One Pair",2:"Two Pair",3:"Three of a Kind",4:"Straight",5:"Flush",6:"Full House",7:"Four of a Kind",
    8:"Straight Flush",9:"Royal Flush"}
    new_hand_val[0] = hand_val_dict[new_hand_val[0]]
    print(new_hand_val)
    print("\n\n")
    return poker_hand_test

#Monte Carlo-esque simulator to see what the average hand value would be based on many trials
def run_hand_test(n):
    counter = 0
    total_hand_val = 0
    while counter != n:
        hand_value = hand()
        total_hand_val += hand_value[0]
        counter += 1
    avg_hand_val = total_hand_val / n
    print(avg_hand_val)
    return avg_hand_val

hand()

#comparison tests
"""
assert poker5 | poker15 == poker5
assert poker16 | poker10 == poker10
"""
