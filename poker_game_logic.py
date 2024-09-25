# Nick Schmidt
# September 18, 2024
# Poker Game Logic

from card_ranking_logic import poker_hand
from card_ranking_logic import card

class poker_game:

    # import neccesary classes from other files
    from card_ranking_logic import poker_hand
    from card_ranking_logic import card
    import random as r

    def __init__(self):
        # create variables used throughout the class
        self.players = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9"]
        self.rotation = ["Button","Small Blind","Big Blind","Under the Gun", "Under the Gun+1","other 1","other 2","other 3","other 4"]
        
    def play(self):
        
        # create a function for all possible in round actions
        def action(self,player,pin):

            # actions for a check
            if pin == 'CH':
                pass
            # actions for a call
            elif pin == 'CA':
                pass
            # actions for a fold
            elif pin == 'FO':
                pass
            # actions for a bet
            elif pin == 'BE':
                pass
            

        def round(self):

            ## Generate all possible cards
            # all possible suites
            suites = ("spades","hearts","clubs","diamonds")

            # all numbers, 14 is ace which is 1 and 14
            numbers = (2,3,4,5,6,7,8,9,10,11,12,13,14)
            deck = []
            for suite in suites:
                for num in numbers:
                    cards += [card(suite,num)]

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

            ### SHOW PLAYERS THEIR CARDS
            
            # create a dictionary to track active stack size and bets per round
            bet_stack = {player:{'stack size':players_chip_count[player],'bet':0} for player in self.player}

            # create a function to make a bet
            def bet(player,size):
                if size > bet_stack[player]['stack size']:

                    # if bet size is greater than the players stack, player moves all in
                    bet_stack[player]['bet'] += bet_stack[player]['stack size']
                    bet_stack[player]['stack size'] = 0
                    print(f'{player} is all in')

                else:

                    # subtract away bet from stack size and add bet to total bet
                    bet_stack[player]['stack size'] -= size
                    bet_stack[player]['bet'] += size
            
            # initial big bling and small blind bets
            big_blind_size = 100
            small_blind_size = 50
            bet(self.players[2],big_blind_size)
            bet(self.players[1],small_blind_size)

            ## Start betting rounds

            # print codes for betting
            print("Actions Pins:\nCheck: CH, Bet: BE, Call: CA, Fold: FO")

            # create index for betting
            open_index = 3

            # opening bets
            while True:
                
                # find player for the turn
                current_player = self.players[open_index]

                # ask player if they would like to bet
                pin = float(input("Enter an action pin: "))
                action(current_player,pin)

                # progress to the next player
                
                
            ### Code for players to buy back in if they lose all their money

            ### Check for players to see if game cannot continue
            if len(self.players) == 1:
                pass

            # switch players order
            self.players = self.players[-1] + self.players[:-1]

        def main():

            print("----------------------------------")
            print("\n\n\n\n\nWelcome to Poker!")
            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")

            while True:   

                try:
                    # ask user to input number of players and only allow for a number between 2 and 9
                    num_players = int(input("How many players will be playing? "))
                    if 2 <= num_players <= 9:
                        self.players = self.players[0:num_players]
                        break
                    else:
                        print("Please enter a number between 2 and 9.")

                except ValueError:
                    print("Please enter a integer between 2 and 9.")

            print("\n\n\n\n\n----------------------------------\n\n\n\n\n")
    
            # create dictionary to keep track of all player chip counts and total buy ins
            players_chip_count = {player:0 for player in self.players}
            players_buy_ins = {player:0 for player in self.players}

            # loop through all players and ask how many chips they would like to start with
            for player in self.players:

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

            # start round 1
            round()

        main()

poker_game().play()
