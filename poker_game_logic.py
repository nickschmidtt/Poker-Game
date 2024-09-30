# Nick Schmidt
# September 18, 2024
# Poker Game Logic

from card_ranking_logic import poker_hand
from card_ranking_logic import card

class poker_game:

    # import neccesary classes from other files
    from card_ranking_logic import poker_hand
    from card_ranking_logic import card

    def __init__(self):
        # create variables used throughout the class
        self.players = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9"]
        self.rotation = ["Button","Small Blind","Big Blind","Under the Gun", "Under the Gun+1","other 1","other 2","other 3","other 4"]
        self.players_chip_count = {player:0 for player in self.players}

    def play(self):

        def round():
            import random as r
            ## Generate all possible cards
            # all possible suites
            suites = ("spades","hearts","clubs","diamonds")

            # all numbers, 14 is ace which is 1 and 14
            numbers = (2,3,4,5,6,7,8,9,10,11,12,13,14)
            deck = []
            deck = []
            for suite in suites:
                for num in numbers:
                    deck += [card(suite,num)]

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
                if size >= bet_stack[player]['stack size']:

                    # if bet size is greater than the players stack, player moves all in
                    bet_size = bet_stack[player]['stack size']
                    bet_stack[player]['bet'] += bet_size # might not need this?
                    bet_stack[player]['stack size'] = 0
                    print(f'{player} is all in for {bet_size}')

                    #increase pot by the bet size
                    pot["size"] += bet_size

                    return
                else:
                    # subtract away bet from stack size and add bet to total bet
                    bet_size = size
                    bet_stack[player]['stack size'] -= size 
                    bet_stack[player]['bet'] += size # might not need this?

                    #increase pot by the bet size
                    pot["size"] += bet_size

                    return
            
            # initial big bling and small blind bets
            big_blind_size = 100
            small_blind_size = 50
            bet(self.players[2],big_blind_size)
            bet(self.players[1],small_blind_size)

            ## Start betting rounds

            # print codes for betting
            print("Actions Pins\nCheck: CH, Bet: BE, Call: CA, Fold: FO")

            # create active players list
            active_players = self.players

            ## Opening round action
            # create index for betting, action_indicator, round_action, highest bet
            open_index = 3 % len(self.players) # in case there are 3 players, so not out of index
            action_indicator = True
            round_action = [False for player in self.players]
            round_action[2] = True
            highest_bet = big_blind_size

            # opening bets until folded to 1 player or action closes
            while active_players != 1 or action_indicator == True:
                
                while True:

                    # find player for the turn and signal for players action
                    current_player = self.players[open_index]
                    print(self.players)
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

                    # actions for a check
                    if pin == 'CH':
                        ### check if check is valid, aka no other bets, and continue
                        pass

                    # actions for a call
                    elif pin == 'CA':
                        ### find highest bet value and bet it
                        ### add to action indicator
                        pass

                    # actions for a fold
                    elif pin == 'FO':
                        # remove player from active player list
                        active_players = active_players.remove(current_player)
                        # remove signal from round_action
                        round_action = round_action[:open_index] + round_action[open_index:]
                        open_index = open_index % len(self.players)

                    # actions for a bet
                    elif pin == 'BE':
                        ### ask for bet amount
                        while True:
                            # ask for bet from the player
                            try:
                                bet_amount = int(input("Enter bet size: "))
                                if bet_amount >= highest_bet:
                                    # update highest bet
                                    highest_bet = bet_amount
                                    pass
                            except:
                                print("Please enter a bet larger than the big blind ")

                        bet(current_player,bet_amount)
                    
                    # check to see if all values of round_action are true
                    if False not in round_action:
                        ### move into the next round: flop, turn, river
                        ### reset all necessary trackers
                        break
                    # progress tracker by 1 to continue to the next player unless a player folded
                    elif pin != 'FO':
                        open_index = (open_index + 1) % len(self.players)
                
            
                ### Code for players to buy back in if they lose all their money
                ### Check for players to see if game cannot continue
                ### Option to add more players
                if len(self.players) == 1:
                    pass

                # switch players order for next round
                self.players = self.players[-1] + self.players[:-1]

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
            for player in self.players:

                    while True:   

                        try:
                            #ask user for the amount of starting chips for each player
                            num_chips = int(input(f"{player} starting chip stack: "))
                            if 0 <= num_chips <= 100000:
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
            
        main()

poker_game().play()
