import csv
import operator
import random
import tic_tac_object_4


def make_move_human(move_list, board_dict, player_piece):
    Temp_Board = tic_tac_object_4.Board()
    Temp_Board.board_dict = board_dict
    Temp_Board.print_board_dict()
    user_move = input("Please enter your move: ")
    while user_move in move_list:
        user_move = input("That move was already made, please enter a new move: ")

    Temp_Board.board_dict[int(user_move)] = player_piece
    if Temp_Board.is_win(Temp_Board.board_dict) == True:
        # BUG- SAYING YOU WON IS NOT WORKING
        print("Congratulations, you have won!")
    return int(user_move)

def make_move_random(move_list):
    user_move = random.randint(1, 9)
    while user_move in move_list:
        user_move = random.randint(1, 9)
    return user_move

def make_move_stockfish(move_list, player_id, board_dict):
    possible_move_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # HAVE TO TURN THE MOVE LIST INTO STRINGS FOR SOME REASON
    new_move_list = []
    for move in move_list:
        new_move_list.append(str(move))
    move_list = new_move_list

    for move in possible_move_list:
        if move in move_list:
            continue
        if player_id == 'Player_1':
            board_dict[int(move)] = 'x'
        elif player_id == 'Player_2':
            board_dict[int(move)] = 'o'

        temp_Board = tic_tac_object_4.Board()
        temp_Board.board_dict = board_dict
        if temp_Board.is_win(board_dict) == True:
            user_move = move
            return int(user_move)
        # RETURNS THE BOARD TO BEING NORMAL AFTER TESTING IF A MOVE WOULD MAKE A WIN
        board_dict[int(move)] = '.'

    if '5' not in move_list:
        user_move = 5
    else:
        user_move = random.randint(1, 9)
        while board_dict[int(user_move)] != ".":
            user_move = random.randint(1, 9)

    return user_move

def make_move_machine(move_list, player_ID, level):
    possible_move_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_1_win_dict = {}
    player_2_win_dict = {}

    # HAVE TO TURN THE MOVE LIST INTO STRINGS FOR SOME REASON
    new_move_list = []
    for move in move_list:
        new_move_list.append(str(move))
    move_list = new_move_list

    for move in possible_move_list:
        if move in move_list:
            continue

        win_player_1_count = 0
        win_player_2_count = 0
        win_player_draw_count = 0
        temp_move_list = []
        move = [move]
        temp_move_list = move_list + move

        # DECIDE LEVEL OF MACHINE PLAY HERE
        f = open('File_Machine_Level_' + str(level-1) + '.csv')
        reader = csv.reader(f)
        for row in reader:
            if temp_move_list[:len(temp_move_list)] == row[:len(temp_move_list)]:
                if row[-1] == 'Player_1':
                    win_player_1_count += 1
                if row[-1] == 'Player_2':
                    win_player_2_count += 1
                if row[-1] == 'Null':
                    win_player_draw_count += 1
        try:
            player_1_win_percentage = win_player_1_count/(win_player_2_count + win_player_1_count + win_player_draw_count)
        except ZeroDivisionError:
            # print("ZeroDivisionError")
            player_1_win_percentage = 0.6
        player_1_win_dict[int(move[0])] = player_1_win_percentage
        try:
            player_2_win_percentage = win_player_2_count/(win_player_1_count + win_player_2_count + win_player_draw_count)
        except ZeroDivisionError:
            # print("ZeroDivisionError")
            player_2_win_percentage = 0.4
        player_2_win_dict[int(move[0])] = player_2_win_percentage

    # PICKS OUT THE MOVE WITH THE HIGHEST WIN RATE OF ANY POSSIBLE MOVE
    if player_ID == 'Player_1':
        user_move = max(player_1_win_dict.items(), key=operator.itemgetter(1))[0]
    if player_ID == 'Player_2':
        user_move = max(player_2_win_dict.items(), key=operator.itemgetter(1))[0]

    # print(move_list)
    # print(player_2_win_dict)
    # print("User move = " + str(user_move))
    # print("New Move")
    return user_move
