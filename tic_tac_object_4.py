import random
import statistics
import csv
import move_options

class Board():
    def __init__(self):
        self.board_dict = {1:".", 2:".", 3:".", 4:".", 5: ".", 6:".", 7:".", 8:".", 9:"."}
        self.move_list = []

    def update_board(self, user_move, player_piece):
        self.move_list.append(user_move)
        self.board_dict[int(user_move)] = player_piece

    def is_win(self, board_dict):
        self.board_dict = board_dict
        is_win = False
        count = 1
        while count <= 7:
            if board_dict[count] == board_dict[count + 1] == board_dict[count + 2] != '.':
                is_win = True
            count += 3
        count = 1
        while count <= 3:
            if board_dict[count] == board_dict[count + 3] == board_dict[count + 6] != '.':
                is_win = True
            count += 1
        count = 1
        if board_dict[1] == board_dict[5] == board_dict[9] != '.':
            is_win = True
        if board_dict[3] == board_dict[5] == board_dict[7] != '.':
            is_win = True

        return is_win

    def print_board_dict(self):
        i = 1
        while i < 10:
            print(self.board_dict[i], self.board_dict[i + 1], self.board_dict[i + 2])
            i += 3

class Player():
    def __init__(self, player_ID, player_piece, player_type, player_level):
        self.player_ID = player_ID
        self.player_piece = player_piece
        self.player_type = player_type
        self.player_level = player_level

    def make_move(self, move_list, board_dict):
        if self.player_type == 'random':
            user_move = move_options.make_move_random(move_list)
            return user_move
        elif self.player_type == 'machine':
            user_move = move_options.make_move_machine(move_list, self.player_ID, self.player_level)
            return user_move
        elif self.player_type == 'stockfish':
            user_move = move_options.make_move_stockfish(move_list, self.player_ID, board_dict)
            return user_move
        elif self.player_type == 'human':
            user_move = move_options.make_move_human(move_list, board_dict, self.player_piece)
            return user_move


class Game():
    def __init__(self, player_1_type, player_1_level, player_2_type, player_2_level):
        self.Game_Board = Board()
        self.Player_1 = Player('Player_1', 'x', player_1_type, player_1_level)
        self.Player_2 = Player('Player_2', 'o', player_2_type, player_2_level)
        self.move_list = []
        self.winner_id = ''

    def play_game(self):
        turn_counter = 0
        while self.Game_Board.is_win(self.Game_Board.board_dict) is False and turn_counter < 9:
            if (turn_counter % 2) == 0:
                user_move = self.Player_1.make_move(self.Game_Board.move_list, self.Game_Board.board_dict)
                self.Game_Board.update_board(user_move, self.Player_1.player_piece)
                self.move_list.append(user_move)
            if (turn_counter % 2) == 1:
                user_move = self.Player_2.make_move(self.Game_Board.move_list, self.Game_Board.board_dict)
                self.Game_Board.update_board(user_move, self.Player_2.player_piece)
                self.move_list.append(user_move)
            turn_counter +=1
        if self.Game_Board.is_win(self.Game_Board.board_dict) is False:
            self.winner_id = 'Null'
        elif (turn_counter % 2) == 0:
            self.winner_id = self.Player_2.player_ID
        elif (turn_counter % 2) == 1:
            self.winner_id = self.Player_1.player_ID
