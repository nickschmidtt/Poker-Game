# Nick Schmidt
# September 18, 2024
# Poker Game Logic

 # import neccesary classes from other files
from card_ranking_logic import poker_hand
from card_ranking_logic import card

class poker_game:

    def __init__(self):
        # create variables used throughout the class
        self.players = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9"]
        self.rotation = ["Button","Small Blind","Big Blind","UTG", "UTG+1","other 1","other 2","other 3","other 4"]

        # create variables to use throughout the code
        self.pot = {"size": 0} # track pot size
        self.bet_stack = {} # track player bets and stacks
        self.player_cards = {} # track a players cards
        self.active_players = [] # track active players in round
        self.board_cards = [] # track all cards on the board

    def play(self):

        def round():
            import random as r
            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
            print("New Round")
            ## Generate all possible cards
            # all possible suites
            suites = ("hearts","clubs","diamonds")

            # all numbers, 14 is ace which is 1 and 14
            numbers = (2,3,4,5,6,7,8,9,10,11,12,13,14)
            deck = []
            deck = []
            deck = [card(suite, num) for suite in suites for num in numbers]

            # create a dictionary for play cards
            self.player_cards = {player:[] for player in self.players}

            # distribute the cards to players, as well as flop, turn and river
            for player in self.players:
                
                # select and remove two random cards for each player from the deck
                random_card1 = r.choice(deck)
                deck.remove(random_card1)
                random_card2 = r.choice(deck)
                deck.remove(random_card2)

                # add cards to player card dictionary
                self.player_cards[player] += [random_card1,random_card2]

            # create a function to make a bet
            def bet(player,size):
                # find smallest amount possible to bet, in case bet size is over current chips
                bet_size = min(size, self.bet_stack[player]['chips'])
                # add betsize to current bet and subtract it from chips
                self.bet_stack[player]['bet'] += bet_size
                self.bet_stack[player]['chips'] -= bet_size
                self.pot["size"] += bet_size
                # if player has no more chips, player is all in
                if self.bet_stack[player]['chips'] == 0:
                    print(f'{player} is all in for {bet_size}')
                else:
                    #print(f"Bet tracked: {player} bet {bet_size}")
                    pass
            # create active players list
            self.active_players = self.players[:]

            # initial big bling and small blind bets
            big_blind_size = 100
            small_blind_size = big_blind_size / 2
            # print(self.active_players)
            bet(self.active_players[2],big_blind_size)
            bet(self.active_players[1],small_blind_size)

            ## Start betting rounds

            # print codes for betting
            print("Actions Pins -- CHECK, CALL, FOLD, BET, CARDS")

            # create a function for the logic of each round of betting
            def betting_round_logic(highest_bet,starting_index):
                # create variables for function
                open_index = starting_index % len(self.active_players) # in case there are 3 players, so not out of index
                round_action = [False for player in self.active_players]
                while True:
                    ## show some variables for debugging
                    print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
                    print(self.bet_stack)
                    print(f"Pot size: {self.pot['size']}")

                    # find player for the turn and signal for players action
                    current_player = self.active_players[open_index]

                    # prints for debugging
                    print(round_action)
                    print(self.active_players)
                    print(self.player_cards)
                    print(self.board_cards)
                    print(f"{current_player}'s turn")

                    while True:
                        try:
                            # ask player what action they would like to take
                            pin = str(input("Enter an action pin: ")).upper()
                            if pin in ['CHECK','C','FOLD','BET','CARDS']: ### change back to CALL after debugging
                                break

                        except:
                            print("\nPlease enter a valid pin. ")

                    # check to see if highest bet is already acheived to see if check is valid
                    if pin == 'CHECK' and highest_bet == self.bet_stack[current_player]['bet']:
                        # change the action tracker
                        action_index = self.active_players.index(current_player)
                        round_action[action_index] = True
                    # check is invalid
                    elif pin == 'CHECK':
                            print("Please make a valid action")
                            # set tracker back one
                            open_index -= 1

                    # actions for a call
                    elif pin == 'C':
                        # bet the highest amount - the amount already bet by the player
                        bet(current_player,highest_bet-self.bet_stack[current_player]['bet'])
                        # add to action indicator
                        action_index = self.active_players.index(current_player)
                        round_action[action_index] = True

                    # actions for a fold
                    elif pin == 'FOLD':
                        # remove signal from round_action
                        action_index = self.active_players.index(current_player)
                        round_action = round_action[:action_index] + round_action[action_index+1:]
                        # remove from active_player list
                        self.active_players.remove(current_player)
                        open_index = open_index % len(self.active_players)

                    # actions for a bet
                    elif pin == 'BET':
                        ### Need logic to deal with all ins
                        while True:
                            # ask for bet from the player
                            try:
                                bet_amount = int(input("Enter bet size: "))
                                if bet_amount >= highest_bet*2:
                                    # update highest bet and call bet
                                    highest_bet = bet_amount
                                    bet(current_player,bet_amount-self.bet_stack[current_player]['bet']) 
                                    # reset round action so player scan bet again
                                    round_action = [False for player in self.active_players]
                                    action_index = self.active_players.index(current_player)
                                    round_action[action_index] = True
                                    break
                            except:
                                print("Please enter a bet larger 2x the largest bet ")
                    # show player cards
                    elif pin == "CARDS":
                        print("\n\n\n----------------------------------\n\n\n")
                        print(self.player_cards[current_player])
                        # set tracker back one
                        open_index -= 1
                        

                    if len(self.active_players) == 1:
                        # add pot to winning players hand
                        print(f"{self.active_players[0]} wins {self.pot['size']}")
                        self.bet_stack[self.active_players[0]]['chips'] += self.pot['size']
                        # switch players order for next round
                        self.players.insert(0,self.players.pop())
                        # reset pot size
                        self.pot['size'] = 0
                        # reset player bets
                        for player in self.players:
                            self.bet_stack[player]['bet'] = 0
                        # reset board
                        self.board_cards = []
                        return True

                    # check to see if all values of round_action are true
                    if False not in round_action:
                        return False

                    # increase progress tracker by 1 to continue to the next player unless a player folded
                    elif pin != 'FOLD':
                        open_index = (open_index + 1) % len(self.active_players)

            # opening bets until folded to 1 player or action closes
            opening_round_over = betting_round_logic(big_blind_size,3)
            # signal round was won
            if opening_round_over == True:
                return
            # signal move onto flop
            elif opening_round_over == False:
                print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
                print("Onto the flop")
                # reset necessary variables to continue
                for player in self.players:
                    self.bet_stack[player]['bet'] = 0
                # create flop
                flop_card1 = r.choice(deck)
                deck.remove(flop_card1)
                flop_card2 = r.choice(deck)
                deck.remove(flop_card2)
                flop_card3 = r.choice(deck)
                deck.remove(flop_card3)
                self.board_cards = [flop_card1,flop_card2,flop_card3]
                # start betting with the small blind and max bet is 0
                flop_round_over = betting_round_logic(0,1)
                # signal round was won
                if flop_round_over == True:
                    return
                elif flop_round_over == False:
                    print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
                    print('Onto the turn')

                    # reset necessary variables to continue
                    for player in self.players:
                        self.bet_stack[player]['bet'] = 0
                    # create turn
                    turn_card = r.choice(deck)
                    deck.remove(turn_card)
                    self.board_cards+= [turn_card]

                    turn_round_over = betting_round_logic(0,1)
                    # signal round was won
                    if turn_round_over == True:
                        return
                    elif turn_round_over == False:
                        print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
                        print('Onto the river')

                        # reset necessary variables to continue
                        for player in self.players:
                            self.bet_stack[player]['bet'] = 0

                        # create turn
                        river_card = r.choice(deck)
                        deck.remove(river_card)
                        self.board_cards+= [river_card]
                        river_round_over = betting_round_logic(0,1)

                        # signal round was won
                        if river_round_over == True:
                            return
                        elif river_round_over == False:
                            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
                            print('Finding winner of the hand')
                            print(self.active_players)
                            tie = False
                            tie_tracker = [False for player in self.active_players]

                            # find the strongest hand
                            while len(self.active_players) != 1:
                                
                                player1,player2 = self.active_players[0], self.active_players[1]
                                # player one hand 
                                p1_hand = poker_hand(self.board_cards[0],self.board_cards[1],self.board_cards[2],
                                self.board_cards[3],self.board_cards[4],self.player_cards[player1][0],self.player_cards[player1][1])
                                # player two hand
                                p2_hand = poker_hand(self.board_cards[0],self.board_cards[1],self.board_cards[2],
                                self.board_cards[3],self.board_cards[4],self.player_cards[player2][0],self.player_cards[player2][1])
                                
                                # find winning hand
                                #print(self.player_cards)
                                #print(f'p1h= {p1_hand}\np2h= {p2_hand}')
                                if p1_hand | p2_hand == p1_hand:
                                    self.active_players.remove(player2)
                                    tie_tracker = tie_tracker[:1]+tie_tracker[2:]
                                elif p1_hand | p2_hand == p2_hand:
                                    self.active_players.remove(player1)
                                    tie_tracker = tie_tracker[1:]
                                # if player tie will need to split the pot between the two
                                else:
                                    # update tie tracker
                                    tie_tracker[0] = True
                                    tie_tracker[1] = True
                                    if False not in tie_tracker:
                                        # divide up the pot to whoever ties
                                        split_winnings = self.pot['size'] // len(self.active_players)
                                        extra_winnings = self.pot['size'] % len(self.active_players)
                                        print(f'{self.active_players} split the pot, each winning {split_winnings}')
                                        for player in self.active_players:
                                            self.bet_stack[player]['chips'] += split_winnings
                                        print(self.active_players[0])
                                        self.bet_stack[self.active_players[0]]['chips'] += extra_winnings
                                        break
                                    # shift player who tied to the back of the list
                                    self.active_players = [self.active_players[0]] + self.active_players[2:]+ [self.active_players[1]]
                                    tie_tracker = [tie_tracker[0]] + tie_tracker[2:] + [tie_tracker[1]]

                            if len(self.active_players) == 1:
                                # add pot to winning players hand
                                print(f"{self.active_players[0]} wins {self.pot['size']}")
                                self.bet_stack[self.active_players[0]]['chips'] += self.pot['size']

                            # reset player bets
                            for player in self.players:
                                self.bet_stack[player]['bet'] = 0

                            # reset board
                            self.board_cards = []

                            # reset pot to 0
                            self.pot['size'] = 0

                            # switch players order for next round
                            self.players.insert(0,self.players.pop())

                            return
            
        def main():
        
            print("----------------------------------")
            print("\n\n\n\n\nWelcome to Poker!")
            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")

            while True:   
                ### Adjust so possible to play with 2 players
                try:
                    # ask user to input number of players and only allow for a number between 2 and 9
                    num_players = int(input("How many players will be playing? "))
                    if 3 <= num_players <= 9:
                        self.players = self.players[0:num_players]
                        break
                    else:
                        print("Please enter a number between 3 and 9.")

                except ValueError:
                    print("Please enter a integer between 3 and 9.")

            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")

            # create dictionary to keep track total buy ins
            players_buy_ins = {player:0 for player in self.players}
            self.bet_stack = {player: {"chips":0,"bet": 0} for player in self.players}

            while True:   
                try:
                    #ask user for the amount of starting chips for each player
                    num_chips = int(input("Starting chip stacks: "))
                    if 0 <= num_chips <= 100000:
                        for player in self.players:
                            self.bet_stack[player]['chips'] = num_chips
                            players_buy_ins[player] = num_chips
                        break
                    else:
                        print("Please enter a chip stack between 0 and 100,000.")

                except ValueError:
                    print("Please enter a chip stack between 0 and 100,000.")

            while True:
                # run round of betting
                round()
                # players to buy back in if they lose all their money
                for player in self.players:
                    if self.bet_stack[player]['chips'] == 0:
                        while True:
                            try:
                                add_chips = str(input(f"{player}, would you like to buy back in"))
                                if add_chips == 'YES':
                                    while True:
                                        try:
                                            num_new_chips = int(input(f'How many chips would you like to add? '))
                                            if num_new_chips > 0:
                                                self.bet_stack[player]['chips'] = num_new_chips
                                                players_buy_ins[player] += num_new_chips
                                                break
                                            else:
                                                print('Please enter a valid amount of chips')
                                        except:
                                            print('Please enter a valid amount of chips')

                            except:
                                # show amount lost (buy in amount)
                                amount_left = self.bet_stack[player]['chips']-players_buy_ins[player]
                                print(f'{player} ended with {amount_left}')
                                # remove player from player list
                                self.player.remove(player)
                                break

                # actions in between round
                while True:
                    print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
                    try:
                        between_rounds = str(input("Please enter to continue, or enter code: "))
                        if between_rounds in ['ADD','INCREASE', 'END']:
                            # add players into the game and where
                            if between_rounds == 'ADD':
                                while True:
                                    try:
                                        # get name of player, starting stack size and where they would like to be added
                                        player = str(input("Name of player: "))
                                        amount = int(input(f'{player} starting chips: '))
                                        location = str(input("Which player are they sitting in front of? "))
                                        if amount > 0 and location in self.players and player not in self.players:
                                            index = self.players.index(location) + 1
                                            self.players = self.players[:index] + [player] + self.players[index:]
                                            self.bet_stack[player] = {'chips':amount,'bet':0}
                                            break
                                        else:
                                            print("Please add valid information")
                                    except:
                                        print("Please add valid information")
                                
                            # increase players chips stack 
                            elif between_rounds == 'INCREASE':
                                while True:
                                    try:
                                        player = str(input("For which player would you like to add chips? "))
                                        amount = int(input('How many chips would you like to add? '))
                                        if player in self.players and amount > 0: 
                                            # add new chips into players stack
                                            self.bet_stack[player]['chips'] += amount
                                            players_buy_ins[player] += amount
                                            print(self.bet_stack)
                                            break

                                    except:
                                        print("Please enter valid player and amount of chips.")

                                
                            # end game and get final tallies
                            elif between_rounds == 'END':

                                for player in self.players:
                                    ending_balance = self.bet_stack[player]['chips'] - players_buy_ins[player]
                                    if ending_balance >= 0:
                                        print(f'{player} ended up {ending_balance}')
                                    else:
                                        print(f'{player} ended down {ending_balance}')
                                return
                            
                        else: break
                            
                    except: 
                        # check to see if only one or two players are in the game, if so, end the game
                        if self.players == 1:
                            for players in self.players:
                                    ending_balance = self.bet_stack[player]['chips'] - players_buy_ins[player]
                                    if ending_balance >= 0:
                                        print(f'{player} ended up {ending_balance}')
                                    else:
                                        print(f'{player} ended down {ending_balance}') ### Fix this to show non negative
                            return
                        break
                            
  
        main()

poker_game().play()