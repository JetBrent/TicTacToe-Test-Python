import os

def clear_console():
    # Clear console screen for Windows
    if os.name == 'nt':
        _ = os.system('cls')

board = [['1','2','3'],['4','5','6'],['7','8','9']]

def ChangeBoard(answer, playermove):
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

def PrintBoard():
    print(board[0])
    print(board[1])
    print(board[2])

def CheckWinCondition():
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

def main():
    wincondition = 0
    player = 2
    while wincondition == 0:
        if player == '1':
            player = '2'
        else:
            player = '1'
        playermove = Playersign(player)
        inputcorrect = False
        while(inputcorrect == False):
            PrintBoard()
            print("It is  Player " + player  + "'s turn. Please type your move now.")
            try:
                useranswer = input()
            except:
                print("Unexpected error has occured. Please restart the game.")
                continue
            clear_console()
            inputcorrect = ChangeBoard(useranswer, playermove)
        wincondition = CheckWinCondition()
    PrintBoard()
    print("Player " + player + " has won the game!")
    input()

if __name__ == '__main__':
    main()
     