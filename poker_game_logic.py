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
        self.rotation = ["Button","Small Blind","Big Blind","Under the Gun", "Under the Gun+1","other 1","other 2","other 3","other 4"]
        self.players_chip_count = {player:0 for player in self.players}

    def play(self):

        def round():
            import random as r
            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
            print("NEW ROUND")
            ## Generate all possible cards
            # all possible suites
            suites = ("spades","hearts","clubs","diamonds")

            # all numbers, 14 is ace which is 1 and 14
            numbers = (2,3,4,5,6,7,8,9,10,11,12,13,14)
            deck = []
            deck = []
            deck = [card(suite, num) for suite in suites for num in numbers]

            # create a dictionary for play cards
            player_cards = {player:[] for player in self.players}

            # distribute the cards to players, as well as flop, turn and river
            for player in self.players:
                
                # select and remove two random cards for each player from the deck
                random_card1 = r.choice(deck)
                deck.remove(random_card1)
                random_card2 = r.choice(deck)
                deck.remove(random_card2)

                # add cards to player card dictionary
                player_cards[player] += [random_card1,random_card2]

            ### SHOW PLAYERS THEIR CARDS in better way
            print(player_cards)

            # create a variable to track the pot size
            pot = {"size":0}

            # create a dictionary to track active stack size and bets per round
            bet_stack = {player:{'stack size':self.players_chip_count[player],'bet':0} for player in self.players}

            # create a function to make a bet
            def bet(player,size):
                # find smallest amount possible to bet, in case bet size is over current stack size
                bet_size = min(size, bet_stack[player]['stack size'])
                # add betsize to current bet and subtract it from stack size
                bet_stack[player]['bet'] += bet_size
                bet_stack[player]['stack size'] -= bet_size
                pot["size"] += bet_size
                # if player has no more chips, player is all in
                if bet_stack[player]['stack size'] == 0:
                    print(f'{player} is all in for {bet_size}')
                else:
                    print(f"Bet tracked: {player} bet {bet_size}")
            # create active players list
            active_players = self.players[:]

            # initial big bling and small blind bets
            big_blind_size = 100
            small_blind_size = 50
            print(active_players)
            bet(active_players[2],big_blind_size)
            bet(active_players[1],small_blind_size)

            ## Start betting rounds

            # print codes for betting
            print("Actions Pins\nCheck: CH, Bet: BE, Call: CA, Fold: FO")

            ## Opening round action
            # create index for betting, action_indicator, round_action, highest bet
            open_index = 3 % len(active_players) # in case there are 3 players, so not out of index
            action_indicator = True
            round_action = [False for player in active_players]
            highest_bet = big_blind_size

            # opening bets until folded to 1 player or action closes
            while active_players != 1 or action_indicator == True:
                ## show some variables for debugging
                print(bet_stack)
                print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
                print(pot)

                # find player for the turn and signal for players action
                current_player = active_players[open_index]
                print(f"{current_player}'s turn")

                while True:
                    try:
                        # ask player what action they would like to take
                        pin = str(input("Enter an action pin: "))
                        if pin in ['CH','CA','FO','BE']:
                            break

                    except:
                        print("\nPlease enter a valid pin. ")

                print(f"Pin is: {pin}")

                # check to see if highest bet is already acheived to see if check is valid
                if pin == 'CH' and highest_bet == bet_stack[current_player]['bet']:
                    # change the action tracker
                    action_index = active_players.index(current_player)
                    round_action[action_index] = True
                # check is invalid
                elif pin == 'CH':
                        print("Please make a valid action")
                        # set tracker
                        open_index -= 1

                # actions for a call
                elif pin == 'CA':
                    # bet the highest amount - the amount already bet by the player
                    bet(current_player,highest_bet-bet_stack[current_player]['bet'])
                    # add to action indicator
                    action_index = active_players.index(current_player)
                    round_action[action_index] = True

                # actions for a fold
                elif pin == 'FO':
                    # remove signal from round_action
                    action_index = active_players.index(current_player)
                    round_action = round_action[:action_index] + round_action[action_index+1:]
                    # remove from active_player list
                    active_players.remove(current_player)
                    open_index = open_index % len(active_players)

                # actions for a bet
                elif pin == 'BE':
                    ### Need logic to deal with all ins
                    while True:
                        # ask for bet from the player
                        try:
                            bet_amount = int(input("Enter bet size: "))
                            if bet_amount >= highest_bet*2:
                                # update highest bet and call bet
                                highest_bet = bet_amount
                                bet(current_player,bet_amount-bet_stack[current_player]['bet']) 
                                # reset round action so player scan bet again
                                round_action = [False for player in active_players]
                                action_index = active_players.index(current_player)
                                round_action[action_index] = True
                                break
                        except:
                            print("Please enter a bet larger 2x the largest bet ")

                if len(active_players) == 1:
                    # add pot to winning players hand
                    print(f"{active_players[0]} wins {pot['size']}")
                    bet_stack[active_players[0]]['stack size'] += pot['size']
                    # add each player stacksize to global tracker
                    for player in self.players:
                        self.players_chip_count[player] = bet_stack[player]['stack size']
                    break

                # check to see if all values of round_action are true
                print(round_action)
                if False not in round_action:
                    print("Onto the flop, turn and river")
                    # reset necessary variables to continue
                    round_action = [False for player in active_players]
                    for player in active_players:
                        bet_stack[player]['bet'] = 0
                    highest_bet = 0
                    # create flop
                    flop_card1 = r.choice(deck)
                    deck.remove(flop_card1)
                    flop_card2 = r.choice(deck)
                    deck.remove(flop_card2)
                    flop_card3 = r.choice(deck)
                    deck.remove(flop_card3)
                    board = [flop_card1,flop_card2,flop_card3]
                    print(board)
                    ### Start betting with the small blind

                    ### move into the next round: flop, turn, river
                    ### reset all necessary trackers
                    # reset betstack count 
                    # bet_stack[player: for player in self.players]['bet'] = 0 
                    
                    break
                # progress tracker by 1 to continue to the next player unless a player folded
                elif pin != 'FO':
                    open_index = (open_index + 1) % len(self.players)

            ### Code for players to buy back in if they lose all their money
            ### Check for players to see if game cannot continue
            ### Option to add more players if only one player left and in general

            # switch players order for next round
            self.players.insert(0,self.players.pop())
            return

            ### for final return, change the chips stacks appropriately and possible include hand win counter
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

            # loop through all players and ask how many chips they would like to start with
            # for player in self.players:

            # while True:   

            #     try:
            #         #ask user for the amount of starting chips for each player
            #         num_chips = int(input(f"{player} starting chip stack: "))
            #         if 0 <= num_chips <= 100000:
            #             self.players_chip_count[player] = num_chips
            #             players_buy_ins[player] = num_chips
            #             break
            #         else:
            #             print("Please enter a chip stack between 0 and 100,000.")

            #     except ValueError:
            #         print("Please enter a chip stack between 0 and 100,000.")

            while True:   
                try:
                    #ask user for the amount of starting chips for each player
                    num_chips = int(input("Starting chip stacks: "))
                    if 0 <= num_chips <= 100000:
                        for player in self.players:
                            self.players_chip_count[player] = num_chips
                            players_buy_ins[player] = num_chips
                        break
                    else:
                        print("Please enter a chip stack between 0 and 100,000.")

                except ValueError:
                    print("Please enter a chip stack between 0 and 100,000.")

            ### keeping running through rounds until 1 player remains
            ### option to end game and get final tallies
            ### option to add new player to the game and what position 
            round()
            round()
            
        main()

poker_game().play()
