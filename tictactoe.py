# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:49:53 2019

@author: JamieSK
"""

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('------------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    
test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# test_board = ['  '] * 10
display_board(test_board)

def runGame():
    gameConsole()

def showBoard(board):
    display_board(board)
    
def switchTurn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'
    
def isGameEnd(board):
    one = board[1]
    two = board[2]
    three = board[3]
    four = board[4]
    five = board[5]
    six = board[6]
    seven = board[7]
    eight = board[8]
    nine = board[9]
    if one == two and one == three and not one == ' ' and not two == ' ' and not three == ' ':
        return True
    elif four == five and four == six and not four == ' ' and not five == ' ' and not six == ' ':
        return True
    elif seven == eight and seven == nine and not seven == ' ' and not eight == ' ' and not nine == ' ':
        return True
    elif one == four and one == seven and not one == ' ' and not four == ' ' and not seven == ' ':
        return True
    elif two == five and two == eight and not two == ' ' and not five == ' ' and not eight == ' ':
        return True
    elif three == six and three == nine and not three == ' ' and not six == ' ' and not nine == ' ':
        return True
    elif one == five and one == nine and not one == ' ' and not five == ' ' and not nine == ' ':
        return True
    elif three == five and three == seven and not three == ' ' and not five == ' ' and not seven == ' ':
        return True
    elif not one == ' ' and not two == ' ' and not three == ' ' and not four == ' ' and not five == ' ' and not six == ' ' and not seven == ' ' and not eight == ' ' and not nine == ' ':
        return True
    else:
        return False
        
def isGameDraw(board):
    one = board[1]
    two = board[2]
    three = board[3]
    four = board[4]
    five = board[5]
    six = board[6]
    seven = board[7]
    eight = board[8]
    nine = board[9]
    if one == two and one == three and not one == ' ' and not two == ' ' and not three == ' ':
        return False
    elif four == five and four == six and not four == ' ' and not five == ' ' and not six == ' ':
        return False
    elif seven == eight and seven == nine and not seven == ' ' and not eight == ' ' and not nine == ' ':
        return False
    elif one == four and one == seven and not one == ' ' and not four == ' ' and not seven == ' ':
        return False
    elif two == five and two == eight and not two == ' ' and not five == ' ' and not eight == ' ':
        return False
    elif three == six and three == nine and not three == ' ' and not six == ' ' and not nine == ' ':
        return False
    elif one == five and one == nine and not one == ' ' and not five == ' ' and not nine == ' ':
        return False
    elif three == five and three == seven and not three == ' ' and not five == ' ' and not seven == ' ':
        return False
    else:
        return True
        
def gameConsole():
    
    isEnd = False
    board = [' '] * 10
    turn = ''
    
    # Ask for which one wants to go first
    while turn == '':
        userTurnChoice = input('Which one wants to go first X : O ? ')
        if userTurnChoice.lower() == 'x':
            turn = 'X'
            print('X goes first')
        elif userTurnChoice.lower() == 'o':
            turn = 'O'
            print('O goes first')
        else:
            print('Please try again ...')
    
    while not isEnd:
        
        # Ask for the fill in position
        controlLoop = True
        while controlLoop:
            userInputPosition = int(input(turn + ' turns, Which position do you want to fill-in ? '))
            if userInputPosition in range(1, 11, 1):
                if board[userInputPosition] == ' ':
                    board[userInputPosition] = turn
                    showBoard(board)
                    controlLoop = False
                else:
                    print('That position has already filled , try new position ...')
            else:
                print('Invalid input , please try again ...')
        
        # Check is the game end
        controlLoop = True
        isEnd = isGameEnd(board)
        if not isEnd:
            turn = switchTurn(turn)
        else:
            if isGameDraw(board):
                print('Draw, no one wins ...')
            else:
                print('\nCongratulations! The Winner is ' + turn +' .')
                
runGame()