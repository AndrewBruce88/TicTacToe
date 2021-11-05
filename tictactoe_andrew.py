'''
This is a simple tictactoe game
Playable by 2 players
Written by AN for his intro python course in 2021
pylint score of 7.58 / 10
'''

import os

THE_LINES = {'type1':'   |   |   ',
            'type2':'---+---+---'}
EMPTY_CHAR = " "
VICTORY_TUPLE = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7})
CHAR_PLAY_SEQUENCE={'X':'first','O':'second'}

def clear_output():

    # for Windows:
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux, os.name is "posix"
    else:
        _ = os.system('clear')

# function to print out the board
def print_board(gamevals = [0,0,0,0,0,0,0,0,0]):
    for i in range(1,12):
        print_line(i,gamevals)

# function to print single line. Note linenum is 1-indexed.
def print_line(linenum,gamevals):
    outputlist = ['']*11
    # modify line if necessary
    # could reduce size of thelines dict, and make it "linetype"
    if linenum == 2:
        outputlist = list(THE_LINES['type1'])
        # insert character from eg gamevals[0] into pos 1
        outputlist[1] = gamevals[0]
        outputlist[5] = gamevals[1]
        outputlist[9] = gamevals[2]
        # convert ints into lists and save into outputstring
        outputstring = ''.join(map(str,outputlist))
    elif linenum == 6:
        outputlist = list(THE_LINES['type1'])
        # insert character from eg gamevals[0] into pos 1
        outputlist[1] = gamevals[3]
        outputlist[5] = gamevals[4]
        outputlist[9] = gamevals[5]
        # convert ints into lists and save into outputstring
        outputstring = ''.join(map(str,outputlist))
    elif linenum == 10:
        outputlist = list(THE_LINES['type1'])
        # insert character from eg gamevals[0] into pos 1
        outputlist[1] = gamevals[6]
        outputlist[5] = gamevals[7]
        outputlist[9] = gamevals[8]
        # convert ints into lists and save into outputstring
        outputstring = ''.join(map(str,outputlist))
    else:
        if linenum in (4,8):
            outputstring = THE_LINES['type2']
        else:
            outputstring = THE_LINES['type1']
        
    print(outputstring)

# function to query whether player 1 wants to be "X" or "O".
# returns only "X" or "O"
def determine_player1_char():
    choice = ''
    
    while choice not in ('X','O'):
        choice = input("Player 1: Want to be X or O? ")
        if choice not in ('X','O'):
            print("Try again. (it's case sensitive)")
            
    return choice

# function to ask for user input, updates and prints the new board, and
# determines victory status
# returns victory status, either "WINNER","CATSGAME","NOTOVER" and updated board values
def player_turn(playernumber,char,vals):
    vals[get_user_value(playernumber,char,vals)-1] = char
    return (is_winner(char,vals), vals)
    
# function to get user value
# returns user value from 1-9
def get_user_value(playernumber,char,vals):
    choice = ''
    spot_taken = True
    within_range = False
    acceptable_range = range(0,10)
    
    while spot_taken is True or within_range is False:
        choice = int(input(f'Player {playernumber} ({char}): Which spot will you take? (1-9): '))
        
        # check if within acceptable range now
        if choice in acceptable_range:
            within_range = True
        else:
            print("Try a value within the range!")
            within_range = False
        
        # check if that spot was already taken
        if vals[choice - 1] != EMPTY_CHAR:
            spot_taken = True
            print("Try a different spot that's not already taken!")
        else:
            spot_taken = False
    
    return choice
        
# function to determine if there is a winning condition for the letter passed in
# and taking into account the existing values on the board
# returns string with either "WINNER", "CATSGAME", or "NOTOVER"
def is_winner(char,vals):
    agnosticlist=[]
    allcharlist=[]
    
    for index, value in enumerate(vals):
        if value != EMPTY_CHAR:
            allcharlist.append(index+1)
        if value == char:
            agnosticlist.append(index+1)
    
    # check for victory conditions and return as makes sense
    for entry in VICTORY_TUPLE:
        if set(agnosticlist).issuperset(entry):
            return "WINNER"
    else:
        if set(allcharlist) == {1,2,3,4,5,6,7,8,9}:
            return "CATSGAME"

    return "NOTOVER"
    
# function to query whether the players want to play again.
# returns either True or False
def want_to_play_again():
    choice = ''
    while choice not in ('Y','N'):
        choice = input("Want to play again? Y or N: ")
        if choice not in ('Y','N'):
            print("Try again.")

    return choice == "Y"
    
# function to query who goes first, and set up all needed initial parameters
# returns dictionary with (player1char, player2char, playertogo, chartogo)
def ask_who_goes_first():
    clear_output()
    print("In this game we play with two players, and the spaces are defined as:")
    print_board([1,2,3,4,5,6,7,8,9])
    
    # Query whether player 1 wants to be "X" or "O"
    if determine_player1_char() == 'X':
        player_order = {'player1char':'X','player2char':'O','playertogo':1,'chartogo':'X'}
    else:
        player_order = {'player1char':'O','player2char':'X','playertogo':2,'chartogo':'X'}
    
    print(f"Alright, player 1 is {player_order['player1char']} and \
            goes {CHAR_PLAY_SEQUENCE[player_order['player1char']]}")
    return player_order

# main game function
# calls other functions as needed
# does not return anything
def tictactoe_2player():
    # variable definitions:
    current_vals = [EMPTY_CHAR]*9
    victory_status = ""
    # Introduction
    print("Welcome to Tic Tac Toe... press any key to continue")
    input("")
    # Put out intro message and gather player order info
    player_order = ask_who_goes_first()
    # Begin while loop that will last until game ends:
    while True:
        clear_output()
        print_board(current_vals)
        # Player makes move, we check victory conditions
        victory_status,current_vals = player_turn(player_order['playertogo'], \
            player_order['chartogo'],current_vals)

        if victory_status == "WINNER":
            clear_output()
            print_board(current_vals)
            print(f"Congratulations on your glorious victory, player {player_order['playertogo']}!")
            # check if we want to play again.
            if want_to_play_again():
                current_vals = [EMPTY_CHAR]*9
                player_order = ask_who_goes_first()
                continue
            else:
                break
        elif victory_status == "CATSGAME":
            clear_output()
            print_board(current_vals)
            print("Good try, but nobody wins!")
            
            # check if we want to play again
            if want_to_play_again():
                current_vals = [EMPTY_CHAR]*9
                player_order = ask_who_goes_first()
                continue
            else:
                break     
        else:
            # game not over, set up parameters for next turn
            if player_order['playertogo'] == 1:
                player_order['playertogo'] = 2
                player_order['chartogo'] = player_order['player2char']
            else:
                player_order['playertogo'] = 1
                player_order['chartogo'] = player_order['player1char']
    print("Thanks for playing!")

if __name__ == "__main__":
    tictactoe_2player()
