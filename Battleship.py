from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

print "Welcome to Battleship."
print "You have four guesses to hit the enemy ship."
print "Good Luck."
print "DEBUG MODE: ENABLED"

ship_row = random_row(board)
ship_col = random_col(board)
guesses = 0
while guesses < 6:
    guesses = guesses + 1
    if guesses == 5:
        print "You ran out of guesses, Game Over"
        break
    
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    print "Ship location:"
    print ship_row
    print ship_col
    print "---------------------------------------------------------"
    
    
    if guess_col == ship_col and guess_row == ship_row:
        print "Congratulations! You sank the enemy battleship!"
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
            guesses = guesses - 1
            print "Try Again."
            
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
            guesses = guesses - 1
            
        else:
            print "You missed the enemy battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    print "Guesses remaining:" + str(4 - guesses)
