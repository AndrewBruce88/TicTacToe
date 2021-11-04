THE_LINES = {'type1':'   |   |   ',
            'type2':'---+---+---'}
EMPTY_CHAR = " "
CURRENT_VALS = [EMPTY_CHAR]*9
VICTORY_TUPLE = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7})
# note clear_output only works in Jupyter Notebooks.
# from IPython.display import clear_output
# instead for CL runs, writing own clear_output function:
def clear_output():
    print("\n")

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
        if linenum == 4 or linenum == 8:
            outputstring = THE_LINES['type2']
        else:
            outputstring = THE_LINES['type1']
        
    print(outputstring)


# function to query whether player 1 wants to be "X" or "O".
# returns only "X" or "O"
def determine_player1_char():
    
    choice = ''
    
    while choice != 'X' and choice != 'O':
        choice = input("Player 1: Want to be X or O? ")
        
        if choice != 'X' and choice != 'O':
            print("Try again. (it's case sensitive)")
            
    return choice    

# function to ask for user input, updates and prints the new board, and
# determines victory status
# returns victory status, either "WINNER","CATSGAME","NOTOVER"
def player_turn(playernumber,char):
    
    global CURRENT_VALS
    
    CURRENT_VALS[get_user_value(playernumber)-1] = char
    
    return is_winner(char)
    
# function to get user value
# returns user value from 1-9
def get_user_value(playernumber):
    
    choice = ''
    spot_taken = True
    within_range = False
    acceptable_range = range(0,10)
    
    while spot_taken == True or within_range == False:
        choice = int(input(f'Player {playernumber}: Which spot will you take? (1-9): '))
        
        # check if within acceptable range now
        if choice in acceptable_range:
            within_range = True
        else:
            print("Try a value within the range!")
            within_range = False
        
        # check if that spot was already taken
        if CURRENT_VALS[choice - 1] != EMPTY_CHAR:
            spot_taken = True
            print("Try a different spot that's not already taken!")
        else:
            spot_taken = False
    
    return choice
        

# function to determine if there is a winning condition for the letter passed in
# returns string with either "WINNER", "CATSGAME", or "NOTOVER"
def is_winner(c):
    
    agnosticlist=[]
    allcharlist=[]
    
    for index, value in enumerate(CURRENT_VALS):
        if value != EMPTY_CHAR:
            allcharlist.append(index+1)
        if value == c:
            agnosticlist.append(index+1)
    
    # check for victory conditions and return as makes sense
    for entry in VICTORY_TUPLE:
        if set(agnosticlist).issuperset(entry):
            return "WINNER"
    else:
        if set(allcharlist) == {1,2,3,4,5,6,7,8,9}:
            return "CATSGAME"
        else:
            return "NOTOVER"
        
    # victory conditions that exist are: 1-2-3, 4-5-6, 7-8-9, 1-4-7, 2-5-8, 3-6-9, 1-5-9, 3-5-7
    
    
# function to query whether the players want to play again.
# returns either True or False
def want_to_play_again():
    
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input("Want to play again? Y or N: ")
        
        if choice != 'Y' and choice != 'N':
            print("Try again.")
    
    if choice == "Y":
        return True
    else:
        return False

    
# function to query who goes first, and set up all needed initial parameters
# returns tuple with (player1char, player2char, playertogo, chartogo)
def ask_who_goes_first():
    
    quickdict={'X':'first','O':'second'}
    
    clear_output()
    
    print("In this game we play with two players, and the spaces are defined as:")
    print_board([1,2,3,4,5,6,7,8,9])
    
    # Query whether player 1 wants to be "X" or "O"
    if(determine_player1_char() == 'X'):
        player1char = 'X'
        player2char = 'O'
    else:
        player1char = 'O'
        player2char = 'X'
    
    print("Alright, player 1 is {} and goes {}".format(player1char,quickdict[player1char]))
    
    # set up initial turn parameters
    chartogo = 'X'
    if player1char == 'X':
        playertogo = 1
    else:
        playertogo = 2
    
    return (player1char, player2char, playertogo, chartogo)

# function to clear all game data and reset everything to defaults
def clear_game_data():
    global CURRENT_VALS
    CURRENT_VALS = [EMPTY_CHAR]*9


# main game function
# calls other functions as needed
# does not return anything
def tictactoe_2player():
    
    # variable definitions:
    clear_game_data()
    victory_status = ""
    
    # Introduction
    print("Welcome to Tic Tac Toe... press any key to continue")
    input("")
    
    # Put out intro message and gather player1char info
    player1char, player2char, playertogo, chartogo = ask_who_goes_first()
    
    # Begin while loop that will last until game ends
    while True:
        
        clear_output()
        print_board(CURRENT_VALS)
        
        # Player makes move, we check victory conditions 
        victory_status = player_turn(playertogo,chartogo)
        
        if victory_status == "WINNER":
            clear_output()
            print_board(CURRENT_VALS)
            print("Congratulations on your glorious victory, player {}!".format(playertogo))
            
            # check if we want to play again.
            if(want_to_play_again()):
                
                clear_game_data()
                player1char, player2char, playertogo, chartogo = ask_who_goes_first()
                continue
            else:
                break
        
        elif victory_status == "CATSGAME":
            clear_output()
            print_board(CURRENT_VALS)
            print("Good try, but nobody wins!")
            
            # check if we want to play again
            if(want_to_play_again()):
                
                clear_game_data()
                player1char, player2char, playertogo, chartogo = ask_who_goes_first()
                continue
            else:
                break
                
        else:
            # game not over, set up parameters for next turn
            if chartogo == 'X':
                chartogo = 'O'
            else:
                chartogo = 'X'
            
            if playertogo == 1:
                playertogo = 2
            else:
                playertogo = 1
    
    print("Thanks for playing!")

if __name__ == "__main__":
    tictactoe_2player()