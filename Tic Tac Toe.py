#Tic Tac Toe

"""
For tic-tac-toe game:
- need to create board for the player 
- Need to store the place for each grid in a dictionary 
- The dict key will be the number of the place in the grid and the value will be empty but will change to X or O
- need if else statements  to check if player has won
"""
#Creating the game board
board = {'1': '1', '2': '2', '3': '3',
         '4': '4', '5': '5', '6': '6',
         '7': '7', '8': '8', '9': '9'}

#showing game board to user with space for each place
def printBoard(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print(f"- - -")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print(f"- - -")
    print(board['7'] + "|" + board['8'] + "|" + board['9'])
    
    
"""
8 possible winning combos:
- 1,2,3
- 4,5,6
- 7,8,9
- 1,5,9
- 3,5,7
- 1,4,7
- 2,5,8
- 3,6,9
"""
def gameWinner(board):
    if board[1] == "X" and board[2] == "X" and board[3] == "X":
        print("Player X is the winner!")
    elif board[1] == "O" and board[2] == "O" and board[3] == "O":
        print("Player O is the winner!")

    if board[4] == "X" and board[5] == "X" and board[6] == "X":
        print("Player X is the winner!")
    elif board[4] == "O" and board[5] == "O" and board[6] == "O":
        print("Player O is the winner!")
        
    if board[7] == "X" and board[8] == "X" and board[9] == "X":
        print("Player X is the winner!")
    elif board[7] == "O" and board[8] == "O" and board[9] == "O":
        print("Player O is the winner!")

    if board[1] == "X" and board[5] == "X" and board[9] == "X":
        print("Player X is the winner!")
    elif board[1] == "O" and board[5] == "O" and board[9] == "O":
        print("Player O is the winner!")

    if board[3] == "X" and board[5] == "X" and board[7]== "X":
        print("Player X is the winner!")
    elif board[3] == "O" and board[5] == "O" and board[7]== "O":
        print("Player O is the winner!")

    if board[1] == "X" and board[4] == "X" and board[7]== "X":
        print("Player X is the winner!")
    elif board[1] == "O" and board[4] == "O" and board[7]== "O":
        print("Player O is the winner!")

    if board[2] == "X" and board[5] == "X" and board[8]== "X":
        print("Player X is the winner!")
    elif board[2] == "O" and board[5] == "O" and board[8]== "O":
        print("Player O is the winner!")

    if board[3] == "X" and board[6] == "X" and board[9]== "X":
        print("Player X is the winner!")
    elif board[3] == "O" and board[6] == "O" and board[9]== "O":
        print("Player O is the winner!")


def playMove():
    
    players = ['X','O']
    player_index = 0 #for changing player 
    count = 0 #keep track of number of moves

    while count < len(board) - 1:
        move = input("Please make your move [1-9]: ")
        try:
            if board[move] == move:
                board[move] = players[player_index % len(players)] #0 % 2 = 0, 1 % 2 = 1. therefore player will be swapped
                print(f"You have moved to square {move}.")
                player_index += 1 #increment player so it keeps swapping from 0 to 1
                count += 1
            else:
                print("that place has been taken, please try again")
                continue
            for square in board:
                if board[square] != 'X' or board[square] != 'O':
                    print("The result is a draw!")
        except KeyError:
            print("That is an invalid move. Please pick 1-9")
            pass
        finally:
            printBoard(board)
            print(f"Number of moves: {count}")

    return board


def playGame():
    print("Here is your starting board for Tic Tac Toe!")
    printBoard(board)
    playMove()

playGame()