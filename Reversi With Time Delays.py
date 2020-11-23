# NAME : BRYAN HOOI YU ERN
# STUDENT ID : 30221005
# TASK 2 : REVERSI

# 1 - Black Stone, 2 - White Stone # Black has first move

from copy import copy
from copy import deepcopy
from time import sleep

def new_board():
    new_board = []
    for i in range(8):
        rows = []
        for j in range(8):
            rows.append(0)
        new_board.append(rows)
    new_board[3][3], new_board[3][4] = 2,1
    new_board[4][3], new_board[4][4] = 1,2
    return new_board
#print(*new_board(), sep="\n")

def print_board(board):
    printed_board = deepcopy(board)
    row_labels = ["1|","2|","3|","4|","5|","6|","7|","8|"]
    col_labels = ["a","b","c","d","e","f","g","h"]
    row_index = 0
    for row in range(len(printed_board)):
        printed_board[row] = list(row_labels[row_index]) + printed_board[row]
        row_index += 1
    col_index = 0
    printed_board.append(["   ","-","-","-","-","-","-","-","-"])
    printed_board.append(["   ",0,0,0,0,0,0,0,0])
    for col in range(1, 9):
        printed_board[len(printed_board)-1][col] = col_labels[col_index]
        col_index += 1
    for element in printed_board:
        print(*element)
#print_board(new_board())

def score(board):
    p1_count = 0
    p2_count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                p1_count += 1
            elif board[i][j] == 2:
                p2_count += 1
    return (p1_count, p2_count)
#print(score(new_board()))

def enclosing(board, player, pos, direct):
    r, c = pos[0], pos[1]
    dr, dc = direct[0], direct[1]
    if board[r][c] != 0:
        return False
    if r + dr < 0 or r + dr > len(board) - 1 or c + dc < 0 or c + dc > len(board) - 1:
        return False
    if board[r + dr][c + dc] == 0:
        return False
    if board[r + dr][c + dc] != player:
        i = 1
        next_spot = board[r + (i*dr)][c + (i*dc)]
        while (0 <= (r + (i*dr)) and (r + (i*dr)) < len(board)) and (0 <= (c + (i*dc)) and (c + (i*dc)) < len(board)):
            if next_spot == player:
                return True
            i += 1
            if (0 <= (r + (i*dr)) and (r + (i*dr)) < len(board)) and (0 <= (c + (i*dc)) and (c + (i*dc)) < len(board)):
                next_spot = board[r + (i * dr)][c + (i * dc)]
                if next_spot == 0:
                    return False
            else:
                return False
    return False
#print(enclosing(new_board(), 1, (4,5), (0,-1)))
#print(enclosing(new_board(), 1, (4,5), (1,1)))

def position(string):
    row_dict = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
    col_dict = {"a": 0 , "b": 1 , "c": 2 , "d": 3 , "e": 4 , "f": 5 , "g": 6 , "h": 7}
    letter = list(string)[0]
    number = list(string)[1]
    if letter not in col_dict or number not in row_dict:
        return None
    row_coordinate = row_dict[number]
    col_coordinate = col_dict[letter]
    return (row_coordinate, col_coordinate)
#print(position("e3"))
#print(position("l1"))
#print(position("a0"))
#print(position("Genghis Khan"))

def reverse_position(coordinate):
    first_digit = {0:"1", 1:"2", 2:"3", 3:"4", 4:"5", 5:"6", 6:"7", 7:"8"}
    second_digit = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    letter = second_digit[coordinate[1]]
    number = first_digit[coordinate[0]]
    return letter+number
#print(reverse_position((4,5)))

directions = [(0,-1), (-1,0), (0,1), (1,0), (-1,-1), (-1,1), (1,1), (1,-1)]
def valid_moves(board, player):
    valid_moves_list = []
    for r in range(len(board)):
        for c in range(len(board)):
            for dir in directions:
                if enclosing(board, player, (r,c), dir) and (r,c) not in valid_moves_list:
                    valid_moves_list.append((r,c))
    return valid_moves_list
#print(valid_moves(new_board(),1))
#print(valid_moves(new_board(),2))

def convert_opponent(board, player, pos):
    r, c = pos[0], pos[1]
    i = 1
    for dir in directions:
        if enclosing(board, player, pos, dir):
            dr, dc = dir[0], dir[1]
            next_place = board[r + dr][c + dc]
            i = 1
            while next_place != player:
                board[r + (i * dr)][c + (i * dc)] = player
                i += 1
                if (0 <= (r + (i * dr)) and (r + (i * dr)) < len(board)) and (0 <= (c + (i * dc)) and (c + (i * dc)) < len(board)):
                    next_place = board[r + (i * dr)][c + (i * dc)]
    board[r][c] = player

def next_state(board, player, pos):
    next_board = board
    if player == 1:
        next_player = 2
        convert_opponent(next_board, player, pos)
        if len(valid_moves(next_board, next_player)) == 0:
            return (next_board, 0)
        else:
            return (next_board, next_player)
    else:
        next_player = 1
        convert_opponent(next_board, player, pos)
        if len(valid_moves(next_board, next_player)) == 0:
            return (next_board, 0)
        else:
            return (next_board, next_player)
#show_board = next_state(new_board(), 1, (4,5))[0]
#player_turn = next_state(new_board(), 1, (4,5))[1]
#print_board(show_board)
#print(player_turn)
#print(valid_moves(next_state(new_board(),1,(4,5))[0],2))

def run_two_players():
    print("Lets play a game of Reversi. Type \"q\" to quit. Player with highest score at the end wins. Good Luck!")
    game_board = new_board()
    print_board(game_board)
    player = 1
    while len(valid_moves(game_board, 1)) > 0 or len(valid_moves(game_board, 2)) > 0:
        if player == 1:
            if len(valid_moves(game_board, player)) == 0:
                print("Player " + str(player) + " has no moves left.")
                player = 2
            else:
                print("Its player 1's turn")
                user_choice = input("Select a location to place your piece:")
                if user_choice == "q":
                    print("Player " + str(player) + " quits.")
                    break
                pos = position(user_choice)
                if pos in valid_moves(game_board, player):
                    game_board = next_state(game_board, player, pos)[0]
                    print_board(game_board)
                    player = 2
                else:
                    print("Invalid move")
                    print("You have other valid moves. Try again")
        else:
            if len(valid_moves(game_board, player)) == 0:
                print("Player " + str(player) + " has no moves left.")
                player = 1
            else:
                print("Its player 2's turn")
                user_choice = input("Select a location to place your piece:")
                if user_choice == "q":
                    print("Player " + str(player) + " quits.")
                    break
                pos = position(user_choice)
                if pos in valid_moves(game_board, player):
                    game_board = next_state(game_board, player, pos)[0]
                    print_board(game_board)
                    player = 1
                else:
                    print("Invalid move")
                    print("You have other valid moves. Try again")
    print("Game over. Either a player quit or both players have no moves left.")
    print_board(game_board)
    print("Final score is... " + "Player 1:" + str(score(game_board)[0]) + " and Player 2:" + str(score(game_board)[1]))
    return None
#run_two_players()

def best_move(board, lst, player):
    best_move = lst[0]
    most_converted = 0
    for pos in lst:
        num_pieces_converted = 0
        r, c = pos[0], pos[1]
        for dir in directions:
            if enclosing(board, player, pos, dir):
                dr, dc = dir[0], dir[1]
                next_place = board[r + dr][c + dc]
                i = 1
                while next_place != player and next_place != 0:
                    num_pieces_converted += 1
                    i += 1
                    if (0 <= (r + (i * dr)) and (r + (i * dr)) < len(board)) and (0 <= (c + (i * dc)) and (c + (i * dc)) < len(board)):
                        next_place = board[r + (i * dr)][c + (i * dc)]
        if num_pieces_converted > most_converted:
            best_move, most_converted = pos, num_pieces_converted
    return best_move
#print(best_move(test_board, valid_moves(test_board,2), 2))

def run_single_player():
    print("Lets play a game of Reversi.")
    print("You as Player 1 will be going up against the computer(player 2). Type \"q\" to quit. Good Luck!")
    game_board = new_board()
    print_board(game_board)
    print("Current score is Player 1:" + str(score(game_board)[0]) + " and Computer:" + str(score(game_board)[1]))
    player = 1
    while len(valid_moves(game_board, 1)) > 0 or len(valid_moves(game_board, 2)) > 0:
        if player == 1:
            if len(valid_moves(game_board, player)) == 0:
                print("Player " + str(player) + " has no moves left.")
                player = 2
            else:
                print("Its player 1's turn")
                user_choice = input("Select a location to place your piece:")
                sleep(2)
                if user_choice == "q":
                    print("Player " + str(player) + " quits.")
                    break
                pos = position(user_choice)
                if pos in valid_moves(game_board, player):
                    game_board = next_state(game_board, player, pos)[0]
                    print_board(game_board)
                    sleep(2)
                    print("Current score is Player 1:" + str(score(game_board)[0]) + " and Computer:" + str(score(game_board)[1]))
                    sleep(2)
                    player = 2
                else:
                    print("Invalid move")
                    print("You have other valid moves. Try again")
        else:
            if len(valid_moves(game_board, player)) == 0:
                print("Player " + str(player) + " has no moves left.")
                player = 1
            else:
                print("Its the Computer's turn")
                sleep(2)
                print("The computer is deciding.......")
                sleep(5)
                pos = best_move(game_board, valid_moves(game_board, player), player)
                print("The computer picked " + reverse_position(pos))
                sleep(2)
                game_board = next_state(game_board, player, pos)[0]
                print_board(game_board)
                sleep(2)
                print("Current score is Player 1:" + str(score(game_board)[0]) + " and Computer:" + str(score(game_board)[1]))
                player = 1
    print("Game over. Either a player quit or both players have no moves left.")
    print_board(game_board)
    print("Final score is... " + "Player 1:" + str(score(game_board)[0]) + " and Computer:" + str(score(game_board)[1]))
    return None
run_single_player()
