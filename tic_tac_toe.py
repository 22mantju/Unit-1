#!/usr/bin/env python3

board = [0,1,2,
         3,4,5,
         6,7,8]
win_con = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]

def show():
    print("===============================")
    print()
    print()
    print("+---+---+---+")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("+---+---+---+")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("+---+---+---+")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("+---+---+---+")

def check():
    if move > 8:
        print("ERROR: Invalid space")
        if xnum == 1:
            del board[i]
            board.insert(i,"X")
        
            
def x_move(i):
    if board[i] == "X" or board[i] == "O":
        print("===============================")
        return print("ERROR: Spot already taken!")
        print("===============================")
    else:
        del board[i]
        board.insert(i,"X")
def o_move(i):
    if board[i] == "X" or board[i] == "O":
        print("===============================")
        return print("ERROR: Spot already taken!")
        print("===============================")
    else:
        del board[i]
        board.insert(i,"O")
  
    
while True:
    turn_num = 1
    board = [0,1,2,3,4,5,6,7,8]
    print("===============================")
    print("Welcome to Tic-Tac-Toe")
    #check for win, or how we now how many rounds have passed with the "xnum / onum" variables 
    while True:
        for list in win_con:
            xnum = 0
            onum = 0
            for num in list:
                if board[num] == "X":
                    xnum += 1
                elif board[num] == "O":
                    onum += 1
                else:
                    pass
            if xnum == 3 or onum == 3:
                break
        if xnum == 3 or onum == 3:
            break

        show()
        if turn_num % 2 == 1:
            print()
            print("X's turn")
            print()
        else:
            print()
            print("O's turn")
            print()
        #input for space choice
        move = int(input("Choose a space. "))
        if move < 0 or move > 8:
            print("===============================")
            print("ERROR: Invalid space")
            continue
        else:
            if turn_num % 2 == 1:
                x_move(move)
            else:
                o_move(move)
            turn_num += 1
    if xnum == 3:
        show()
        print()
        print("X Wins!")
        print()
        print("Game over!")
        break
    elif onum == 3:
        show()
        print()
        print("O Wins!")
        print()
        print("Game over!")
        break
    else:
        show()
        print()
        print("Draw!")
        print()
        print("Game over!")
        break