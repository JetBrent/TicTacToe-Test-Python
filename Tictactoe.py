import os

def clear_console():
    # Clear console screen for Windows
    if os.name == 'nt':
        _ = os.system('cls')


def ChangeBoard(board, answer, playermove):
            if answer == '1' and board[0][0] == '1':
                board[0][0] = playermove
                return True
            elif answer == '2' and board[0][1] == '2':
                board[0][1] = playermove
                return True
            elif answer == '3' and board[0][2] == '3':
                board[0][2] = playermove
                return True
            elif answer == '4' and board[1][0] == '4':
                board[1][0] = playermove
                return True
            elif answer == '5' and board[1][1] == '5':
                board[1][1] = playermove
                return True
            elif answer == '6' and board[1][2] == '6':
                board[1][2] = playermove
                return True
            elif answer == '7' and board[2][0] == '7':
                board[2][0] = playermove
                return True
            elif answer == '8' and board[2][1] == '8':
                board[2][1] = playermove
                return True
            elif answer == '9' and board[2][2] == '9':
                board[2][2] = playermove
                return True
            else:
                print("Answer not found in board. Please input a valid answer!")
                return False

def PrintBoard(board):
    print("{0} | {1} | {2}".format(board[0][0], board[0][1], board[0][2]))
    print("----------")
    print("{0} | {1} | {2}".format(board[1][0], board[1][1], board[1][2]))
    print("----------")
    print("{0} | {1} | {2}".format(board[2][0], board[2][1], board[2][2]))

def CheckWinCondition(board):
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]: #First Column Checking
        return 1
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]: #Second Column Checking
        return 1
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]: #Third Column Checking
        return 1    
    elif board[0][0] == board[0][1] and board[0][1] == board[0][2]: #First Row Checking
        return 1
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]: #Second Row Checking
        return 1
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]: #Third Row Checking
        return 1   
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]: #Diagonal left to right Checking
        return 1    
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]: #Diagonal right to left Checking
        return 1 
    else:
        return 0
    
def Playersign(player):
    if player == '1':
        return 'X'
    else:
        return 'O'

def maingame(board, player):
    resetgame = 0
    wincondition = 0
    while(resetgame == 0):            
            while wincondition == 0:
                breakcondition = 0
                if player == '1':
                    player = '2'
                else:
                    player = '1'
                playermove = Playersign(player)
                inputcorrect = False
                while(inputcorrect == False):
                    PrintBoard(board)
                    print("It is  Player " + player  + "'s turn. Please type your move now.")
                    useranswer = input()
                    if useranswer.lower() == 'q':
                        breakcondition = 1
                        wincondition = 1
                        break
                    else:
                        clear_console()
                        inputcorrect = ChangeBoard(board, useranswer, playermove)
                        wincondition = CheckWinCondition(board)
            if breakcondition == 1:
                resetgame = 1
                break
            else:
                PrintBoard(board)
                print("\nPlayer " + player + " has won the game!")
                resetgame = 1

def resetboard():
    return [['1','2','3'],['4','5','6'],['7','8','9']]

def main():
    board = [['1','2','3'],['4','5','6'],['7','8','9']]
    player = 2
    endgame = 0
    while(endgame == 0):
        maingame(board, player)
        if player == '1':
            player = '2'
        else:
            player = '1'
        print("\nDo you want to quit? Press 'Q' to quit. Press any key to play a new game.")
        userquit = input()
        if userquit.lower() == "q":
            endgame = 1
            break
        else:
            clear_console()
            board = resetboard()
            continue
    print("Exiting the game... ")
    input()

if __name__ == '__main__':
    main()
     