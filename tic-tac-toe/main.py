from classes.Player import Player
from classes.Board import Board

print(16*"*")
print("  Tic-Tac-Toe!  ")
print(16*"*")

board = Board()
player = Player()
computer = Player(False)

board.print_board()

while True:
    #ask human user move
    move = player.get_player_move()
    #submit move
    board.submit_move(move, player)
    #print boards
    board.print_board()
    if board.check_tie():
        print("the game is tie")
        break 

    if board.is_move_valid(move) and board.is_winner(player, move[0], move[1]):
        print("you win!")
        break

    #ask computer move
    comp_move = computer.get_computer_move()
    #submit move
    board.submit_move(comp_move, computer)
    #print boards
    board.print_board()

    if board.is_winner(computer, comp_move[0], comp_move[1]): #as the computer generates a random move
        print("the computer won and you lost !")
        break
    