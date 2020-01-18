#This is the call file for the machine_move
import tic_tac_object_4

print("Hello! And welcome to Tic_Tac_Machine"'\n')

# UNHIGHLIGHT THE BELOW IN PRODUCTION
# player_1_ID = input("Who is Player 1: ")
# player_1_level = input("Enter player level /10: ")
# player_2_ID = input("Who is Player 2: ")
# player_2_level = input("Enter player level /10: ")
# level = input("Enter player level /10: ")
# number_of_games = input("How many games would you like to play: ")

# CHANGE THE BELOW AROUND TO PLAY THE GAME YOU WANT
# LEVEL ONLY MATTERS FOR MACHINE. LEVEL 1 IS THE HUGE FILE, LEVEL 2 IS CONDENSED
player_1_ID = 'machine'
player_1_level = 2
player_2_ID = 'stockfish'
player_2_level = 2
number_of_games = 1000


games_dictionary_library = {}
game_id = 0
while game_id < int(number_of_games):
    print('\n'"Game ID: " + str(game_id) +  ">>>>>")
    Game = tic_tac_object_4.Game(player_1_ID, player_1_level, player_2_ID, player_2_level)
    Game.play_game()
    games_dictionary_library[game_id] = Game.move_list, Game.winner_id
    game_id += 1
    Game.Game_Board.print_board_dict()
    print(Game.Game_Board.move_list)

player_1_count = 0
player_2_count = 0
player_draw_count = 0
for game in games_dictionary_library:
    if games_dictionary_library[game][1] == 'Player_1':
        player_1_count += 1
    if games_dictionary_library[game][1] == 'Player_2':
        player_2_count += 1
    if games_dictionary_library[game][1] == 'Null':
        player_draw_count += 1

win_ratio = player_1_count/game_id

print("Player_1 won: " + str(player_1_count) + " times.")
print("Player_2 won: " + str(player_2_count) + " times.")
print("Draws happened: " + str(player_draw_count) + " times.")
print("Player 1 win ratio: " + str(round(win_ratio, 2)))
