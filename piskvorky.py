result = "-"
board = "-" * 20
from random import randrange

def evaluate_result(board):
    #function has to evaluate result of game and print it - wom, lost or not finished
    if "-" not in board:
        result != "-"
        if "xxx" in board:
            print("Player X won")
        elif "ooo" in board:
            print("Player O won")
        else:
            print("no winner, friendship won")
    else:
        result = "-"
        print("game continues")

while True:
    #game continues while there are free
    def turn_playerX(board, field, symbol):
        field = int(input("which field do you want to play in? Insert number from 0 to" + str(len(board)-1)))
        symbol = "x"
        while field < 0 or field > 19:
            print("Not valid. Insert number from 0 to" + str(len(board)-1))
            field = int(input("which field do you want to play in?Insert number from 0 to" + str(len(board)-1)))
        while board[field] != '-':
            print("It is taken")
            field = int(input("which field do you want to play in?Insert number from 0 to" + str(len(board)-1)))
            if evaluate_result(board):
                result != "-"
                print(evaluate_result(board))
                break

            board1 = board[0:field]
            board2 = board[field+1:]
            board = board1 + symbol + board2
            return board

            board=turn_playerX(board, field, symbol)
            print(board)

    def turn_playerO(board, field, symbol):
        field = randrange(0,len(board))
        symbol= "o"
        while board[field] != '-':
            field = randrange(0,len(board))
            if evaluate_result(board):
                result != "-"
                print(evaluate_result(board))
                break

            board1 = board[0:field]
            board2 = board[field+1:]
            board = board1 + symbol + board2
            return board
