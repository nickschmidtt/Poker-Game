# Nick Schmidt
# Hand Ranking Code

# Card variations and format
"""
suits = ("spades","hearts","clubs","diamonds")
numbers = (2,3,4,5,6,7,8,9,10,11,12,13,14)
"""
# define class card 
class card:

    #Used to track the suite and number of the card
    def __init__(self,suite,value):
        self.suite = suite
        self.value = value

    #Used to check if two cards are the same so duplicates cannot be used
    def __eq__(self,other):
        if self.value == other.value and self.suite == other.suite:
            return True
        else:
            return False

    #Used to show a card when printed in another object
    def __repr__(self):
        return str(self.value) + str(self.suite[0])

    #Used to show a card when printed alone
    def __str__(self):
        return str(self.value) + " of " + str(self.suite)

    #Overloading the greater than symbol to organize cards in the sorting algorith
    def  __gt__(self,other):
        vals = {"spades":4,"clubs":3,"hearts":2,"diamonds":1}
        if self.suite == other.suite:
            return self.value > other.value
        else:
            return vals[self.suite] > vals[other.suite]

#define a new class to determine the value of a poker hand
class poker_hand:

    #take 7 cards from the user
    def __init__(self,c1,c2,c3,c4,c5,c6,c7):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6
        self.c7 = c7
    
    #used to visualize a hand 
    def __str__(self):
        return f"{self.c1},{self.c2},{self.c3},{self.c4},{self.c5},{self.c6},{self.c7}"

    #main function to determine a hands value, producing a number and a list of extra cards
    def hand_value(self):

        #bubble sorting algorithm to organize lists of cards
        def b_sort(array):
            
            # take n as the list of the given array
            n = len(array)

            for i in range(n):
                
                already_sorted = True

                for j in range(n - i - 1):

                    if array[j] > array[j + 1]:

                        array[j], array[j + 1] = array[j + 1], array[j]

                        already_sorted = False

                if already_sorted:
                    break

            return array

        #use this function to reverse certain lists
        def list_reverse(array):

            new_array = []
            #for each element, starting at the end, add to a new list
            for num in range(len(array)-1,-1,-1):
                new_array += [array[num]]

            #returning a new list so there is no in place change
            return new_array

        #start by adding all the cards into a list
        list_cards = [self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7]

        #sort the list into increasing order and grouped in suites
        ord_cards = b_sort(list_cards)

        #make a new list where it only contains numbers and no duplicates, which will be used to find straights
        seq_cards = []
        for card in ord_cards:
            if card.value not in seq_cards:
                seq_cards += [card.value]
        seq_cards = b_sort(seq_cards)

        #if 14 is in the list, which is an ace, also add a 1 becuase an ace can be a 1 or 14
        if 14 in seq_cards:
            seq_cards = [1] + seq_cards

        # Make a new list of all values, containing duplicates, used for getting extra cards
        all_seq_cards = []
        for card in ord_cards:
            all_seq_cards += [card.value]

        #reverse the list so the highest cards are in the front
        all_seq_cards = list_reverse(b_sort(all_seq_cards))

        #counts the number of values and suites in the given cards
        sui_counts = {card.suite:0 for card in list_cards}

        #initilizes cards using all_seq_cards so the larger values are at the front of the dictionaries
        val_counts = {num:0 for num in all_seq_cards}
        for card in ord_cards:
            sui_counts[card.suite] += 1
        for num in all_seq_cards:
            val_counts[num] += 1

        #dictionary to track which hand types are satisfied and track extra cards
        hand_val = {"RF":False,"SF":False,"FK":False,"FH":False,"FL":False,"ST":False,"TK":False,"TK2":False, "TP":False,"OP":False,"HC":[]}
        
        #first test if any flush; royal flush, straight flush, and regular flush
        for key in sui_counts.keys():

            #Check if there are at least 5 of any one suite, otherwise skip
            if sui_counts[key] >= 5:
                
                #Check for straight flush by making a list of all cards of the suite with 5 or more cards
                sf_list = []
                for card in ord_cards:
                    if card.suite == key:
                        sf_list += [card.value]

                #Go one by one counting how many of the cards are consequtive
                sf_tracker = 1
                sf_last_num = sf_list[0]

                for num in range(1,len(sf_list)):

                    #if the current number equals the last, add one to the count of consequtive cards
                    if sf_list[num] == sf_last_num + 1:
                        sf_tracker += 1

                        #keep track of current number to use to compare next cycle
                        sf_last_num = sf_list[num]

                        #if the straight flush counter is 5 or more, mark straight flush and its highest card
                        if sf_tracker >= 5:
                            hand_val["SF"] = True
                            hand_val["SF-C"] = [sf_list[num]]

                    else:
                        #if the straight flush counter is 5 or more, mark straight flush and its highest card
                        if sf_tracker >= 5:
                            hand_val["SF"] = True
                            hand_val["SF-C"] = [sf_list[num-1]]

                        #reset tracker back down to 1 and use current number as the last number in the list
                        else:
                            sf_tracker = 1
                            sf_last_num = sf_list[num]

                #Check for royal flush by checking top card of straight fluhs
                if hand_val["SF"] == True and hand_val["SF-C"] == [14]:
                    hand_val["RF"] = True
                    hand_val["RF-C"] = [14]

                # Signal that there are enough cards to have a flush
                hand_val["FL"] = True
                
                flush_extra_cards = []

                #find five highest cards for a flush and add them to the dictionary
                for card in ord_cards:
                    if card.suite == key:
                        flush_extra_cards = [card.value] + flush_extra_cards
                flush_extra_cards = flush_extra_cards[0:5]
                hand_val["FL-C"] = flush_extra_cards
        
        # Second test for four of a kind

        #create 4 variables to track highest pairs and trips
        card_pair1 = 0
        card_pair2 = 0
        trips_one = 0
        trips_two = 0

        #loop through all the val counts for 4, 3 and 2 instances
        for key in val_counts.keys():

            #this checks for four of a kind
            if val_counts[key] == 4:
                hand_val["FK"] = True
                quads_extra_card = []
                quads_counter = 0

                #find the highest card that isn't in the four of a kind to add to dictionary
                while len(quads_extra_card) != 1:
                    if all_seq_cards[quads_counter] == key:
                        quads_counter += 1
                    else:
                        quads_extra_card += [all_seq_cards[quads_counter]]
                        
                hand_val["FK-C"] = [key] + quads_extra_card

        #third test for a three of a kind house and two pair - will not work if there is a four of a kind
            elif val_counts[key] == 3 and  hand_val["FK"] != True:

                #if three of a kind is already true, means there is a second three of a kind
                if hand_val["TK"] == True:

                    #mark in the dictionary and mark card in trips_two
                    hand_val["TK2"] = True
                    trips_two = key
                    #do not need to find extra cards becuase if two three of a kinds, there is a full house

                else:
                    #finds first three of a kind
                    hand_val["TK"] = True
                    trips_one = key
                    tk_extra_cards = []
                    counter_tk = 0

                    #loop through all_seq_cards to find highest cards that is not the value of the three of a kind
                    while len(tk_extra_cards) != 2:
                        if all_seq_cards[counter_tk] != key:
                            tk_extra_cards += [all_seq_cards[counter_tk]]
                            counter_tk += 1
                        else:
                            counter_tk += 1

                    #add these cards to the dictionary
                    hand_val["TK-C"] = [key] + tk_extra_cards
                    
        # Fourth Test for pair and two pair - does not work if four of a kind
            elif val_counts[key] == 2  and hand_val["FK"] != True:

                #if there is already a two pair, this means there is a third pair
                if hand_val["TP"] == True:

                    #mark third pair under card_pair3 variable
                    card_pair3 = key

                #if one pair is already satisfied, this means there is two pair
                elif hand_val["OP"] == True:

                    #add to dictionary and track second pair
                    hand_val["TP"] = True
                    card_pair2 = key

                else:

                    #first pair found, track in dictionary and track second pair
                    hand_val["OP"] = True
                    card_pair1 = key
            
        
        # Check for one, two and three pair
        if hand_val["OP"] == True and hand_val["TP"] == False:

            #this means there is only one pair, so find three next highest cards
            op_extra_cards = []
            counter_op = 0
            while len(op_extra_cards) != 3:

                #make sure the card isn't the value in the pair
                if all_seq_cards[counter_op] != card_pair1:
                    op_extra_cards += [all_seq_cards[counter_op]] 
                    counter_op += 1
                else:
                    counter_op += 1
            hand_val["OP-C"] = [card_pair1] + op_extra_cards

        elif hand_val["TP"] == True:

            #does not matter if there is a third pair, becuase it will be the lowest and not used in strongest hand
            tp_extra_cards = []
            counter_tp = 0
            while len(tp_extra_cards) != 1:

                #make sure the card isn't the value of either pair
                if all_seq_cards[counter_tp] != card_pair1 and all_seq_cards[counter_tp] != card_pair2:
                    tp_extra_cards = [all_seq_cards[counter_tp]] + tp_extra_cards
                else:
                    counter_tp += 1

            hand_val["TP-C"] = [card_pair1] + [card_pair2] + tp_extra_cards
        
        # Fifth test for a straight
        straight_tracker = 1
        latest_num = seq_cards[0]

        #loop through all card values
        for num in range(1,len(seq_cards)):
            if seq_cards[num] == latest_num + 1:

                #if the current number equals the last, add one to the count of consequtive cards
                straight_tracker += 1
                #keep track of current number to use to compare next cycle
                latest_num = seq_cards[num]
                
                #if the straight counter is 5 or more, mark straight flush and its highest card
                if straight_tracker >= 5:
                    hand_val["ST"] = True
                    hand_val["ST-C"] = [seq_cards[num]]
            else:
                #if the straight counter is 5 or more, mark straight flush and its highest card
                if straight_tracker >= 5:
                    hand_val["ST"] = True
                    hand_val["ST-C"] = [seq_cards[num-1]]
                #reset straight tracker to 1 and set card to compare as the current one
                else:
                    straight_tracker = 1
                    latest_num = seq_cards[num]
        
        #Sixth Test for full house
        if hand_val["TK"] == True and hand_val["TK2"] == True:

            #if there are three of a kinds, mark first as three of a kind and second as pair for full house
            hand_val["FH"] = True
            hand_val["FH-C"] = [trips_one,trips_two]
        
        elif hand_val["TK"] == True and hand_val["OP"] == True:

            #since first pair will always be the greatest, mark trips first and then first pair
            hand_val["FH"] = True
            hand_val["FH-C"] = [trips_one,card_pair1]

        # Final return of high card
        hand_val["HC"] = all_seq_cards[0:5]

        # Use the hand_val dictionary to find the value of the hand
        value_hand = {"RF":9,"SF":8,"FK":7,"FH":6,"FL":5,"ST":4,"TK":3,"TP":2,"OP":1,"HC":0}
        num_val_hand = -1
        val_hand_extra_cards = []

        #loop through keys in hand tracker dictionary to find first true, which would signal highest hand
        for key in hand_val.keys():

            #use that key to find value of hand from value hand dictionary
            if hand_val[key] == True:
                num_val_hand = value_hand[key]
                val_hand_extra_cards = hand_val[f"{key}-C"]
                break
        
        #if none are true, return high cards
        if num_val_hand == -1:
            num_val_hand = 0
            val_hand_extra_cards = hand_val["HC"]

        #return the number value of hand and the extra cards
        return num_val_hand,val_hand_extra_cards

    # Create an overload function to compare two hands
    def __or__(self,other):
        
        #take values and extra cards of each of the given hands
        self_val, self_cards = self.hand_value()
        other_val, other_cards = other.hand_value()

        #if values are diffent, one hand is greater than the other
        if self_val > other_val:
            print("hand 1")
            return self
        elif self_val < other_val:
            print("hand 2")
            return other
        
        
        else:

            #if values are the same, look through each card and compare them
            for ind_card  in range(len(self_cards)):

                #if one of them is different, one of the hands is greater than the other
                if self_cards[ind_card] > other_cards[ind_card]:
                    print("hand 1")
                    return self
                elif self_cards[ind_card] < other_cards[ind_card]:
                    print("hand 2")
                    return other

            #if all are the same, the hands are equal
            print("equal")
            return 0

class poker_game:

    #some variables to use
    players = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9"]
    rotation = ["Button","Small Blind","Big Blind","Under the Gun", "Under the Gun+1","other1","other2","other3","other4"]
    
    def play(self):
        
        def __init__(self):
            pot = {"pot":0,"bets":0}

        def bet(self, amount):
            return 

        def round(self):
            #the goal of this program is run a round of poker. I can use this in a while group to run the whole game by runnin
            #a round over and over again. What do I want to happen in this function? I want the function to rotate through the players 
            #to switch the blinds. I want to ask certain players if they want to buy in again if they lose all their money. I need to
            #check each turn how many players are in in case people fold down to one player. I need to go round by round of betting, 
            #from preflop to the last card, if it even gets there. The function will need to walk through all the players bets and 
            return

        def main():

            print("----------------------------------")
            print("\n\n\n\n\nWelcome to Poker!")
            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")

            while True:   

                try:
                    #ask user to input number of players and only allow for a number between 2 and 9
                    num_players = int(input("How many players will be playing? "))
                    if 2 <= num_players <= 9:
                        players = players[0:num_players]
                        break
                    else:
                        print("Please enter a number between 2 and 9.")

                except ValueError:
                    print("Please enter a number between 2 and 9.")

            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
    
            #create dictionary to keep track of all player chip counts and total buy ins
            players_chip_count = {player:0 for player in players}
            players_buy_ins = {player:0 for player in players}

            #loop through all players and ask how many chips they would like to start with
            for player in players:

                    while True:   

                        try:
                            #ask user for the amount of starting chips for each player
                            num_chips = int(input(f"{player} starting chip stack: "))
                            if 0 <= num_chips <= 100000:
                                players_chip_count[player] = num_chips
                                players_buy_ins[player] = num_chips
                                break
                            else:
                                print("Please enter a chip stack between 0 and 100,000.")

                        except ValueError:
                            print("Please enter a chip stack between 0 and 100,000.")

        main()

                

#poker_game().play()
