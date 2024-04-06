# CodeNerd
# This program is practice to code for the purposes of learning Python

# Amount_of_players = int(input("Welcome to Connect Four! How many people are playing: "))
# if Amount_of_players == 1:
#     print("Alright its a single player game! You will be playing the computer!")
# elif Amount_of_players == 2:
#     print("Alright its person vs person! You will be playing each other!")
# else: 
#     print("Else it seems you have enter to many or no players please try again.")
    
def create_board():
    """We will use this function to create the board"""
    return [["." for _ in range(6)] for _ in range(7)]



def print_board(board):
    """Print the board."""
    print(" 0 1 2 3 4 5 6")
    print("---------------")
    for row in range(6):
        print("|", end="")
        for col in range(7):
            print(board[col][5-row], end="|")  # Print the bottom row first
        print("\n---------------")

board = create_board()
print_board(board)