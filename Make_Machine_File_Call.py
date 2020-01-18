import tic_tac_object_4
import csv
import statistics

# USE THIS FILE TO BUILD NEW FILES OF GAMES- TO DO THE MACHINE LEARNING THING
# Currently ONLY LEVEL ZERO AND ONE ARE OPTIMIZED. RAN ZERO LIKE A MILLION TIMES, AND THEN ONE A THOUSAND TIMES OFF OF THAT

level = 1

while level < 2:
    GDL_File = open('File_Machine_Level_' + str(level) + '.csv', 'w')
    writer = csv.writer(GDL_File)
    player_1_count = 0
    player_2_count = 0
    player_draw_count = 0

    game_id = 0
    while game_id < 1000:
        list_for_file = []
        Game_Temp = tic_tac_object_4.Game('random', level, 'machine', level)
        Game_Temp.play_game()
        if Game_Temp.winner_id == 'Player_1':
            player_1_count += 1
        if Game_Temp.winner_id == 'Player_2':
            player_2_count += 1
        if Game_Temp.winner_id == 'Null':
            player_draw_count += 1
        # if game_id % 1000 == 0:
        print('>', sep=' ', end='', flush=True)

        for move in Game_Temp.move_list:
            list_for_file.append(int(move))
        list_for_file.append(Game_Temp.winner_id)
        writer.writerow(list_for_file)
        game_id += 1
    GDL_File.close()
    win_ratio = player_1_count/game_id
    print('\n'"Player 1 win ratio at level " + str(level) + " is " + str(win_ratio))
    level += 1
