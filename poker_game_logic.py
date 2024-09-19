# Nick Schmidt
# September 18, 2024
# Poker Game Logic

from card_ranking_logic import poker_hand
from card_ranking_logic import card

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
