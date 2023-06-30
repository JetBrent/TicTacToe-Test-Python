board = [[1,2,3],[4,5,6],[7,8,9]]
wincondition = 0

def ChangeBoard(answer):
            if answer == 1 & board[0][0] == 1:
                board[0][0] = 0
            elif answer == 2 & board[0][1] == 2:
                board[0][1] = 0
            elif answer == 3 & board[0][2] == 3:
                board[0][2] = 0
            elif answer == 4 & board[1][0] == 4:
                board[1][0] = 0
            elif answer == 5 & board[1][1] == 5:
                board[1][1] = 0
            elif answer == 6 & board[1][2] == 6:
                board[1][2] = 0
            elif answer == 7 & board[2][0] == 7:
                board[2][0] = 0
            elif answer == 8 & board[2][1] == 8:
                board[2][1] = 0
            elif answer == 9 & board[2][2] == 9:
                board[2][2] = 0
            else:
                 print("Please input a valid answer!")

def PrintBoard():
    print(board[0])
    print(board[1])
    print(board[2])

def CheckWinCondition():
    if board[0][0] == board[1][0] & board[1][0] == board[2][0]: #First Column Checking
        return 1
    elif board[0][1] == board[1][1] & board[1][1] == board[2][1]: #Second Column Checking
        return 1
    elif board[0][2] == board[1][2] & board[1][2] == board[2][2]: #Third Column Checking
        return 1    
    elif board[0][0] == board[0][1] & board[0][1] == board[0][2]: #First Row Checking
        return 1
    elif board[1][0] == board[1][1] & board[1][1] == board[1][2]: #Second Row Checking
        return 1
    elif board[2][0] == board[2][1] & board[2][1] == board[2][2]: #Third Row Checking
        return 1   
    elif board[0][0] == board[1][1] & board[1][1] == board[2][2]: #Diagonal left to right Checking
        return 1    
    elif board[0][2] == board[1][1] & board[1][1] == board[2][0]: #Diagonal right to left Checking
        return 1 
    else:
        return 0

def main():
    wincondition = 0
    while wincondition == 0:
        PrintBoard()
        print("Please type your move.")
        try:
            useranswer = int(input())
        except:
            print("Please input a number!")
            continue
        ChangeBoard(useranswer)
        wincondition = CheckWinCondition()
    PrintBoard()
    print("You have won the game!")

if __name__ == '__main__':
    main()
     