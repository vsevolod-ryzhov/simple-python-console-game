from core import *


if __name__ == '__main__':
    commands = ['left', 'l', 'right', 'r', 'help', 'h', 'quit', 'q', 'attack left', 'al', 'attack right', 'ar']
    game_dictionary = init()
    game_dictionary = make_barrier(game_dictionary)

    clear()
    print_game_location(game_dictionary)

    command = None;
    is_quit = False
    while not is_quit:
        command = input("Enter command: ")
        clear()
        try:
            commands.index(command)
        except ValueError:
            print("Incorrect command. Commands list: (h)elp, (l)eft, (r)ight, (al) attack left, (ar) attack right, (q)uit")
            print_game_location(game_dictionary)

        if command == "left" or command == "l":
            if check_move(game_dictionary, -1):
                game_dictionary = move(game_dictionary, -1)
                is_quit = after_move(game_dictionary)
        if command == "right" or command == "r":
            if check_move(game_dictionary, 1):
                game_dictionary = move(game_dictionary, 1)
                is_quit = after_move(game_dictionary)
        if command == "attack left" or command == "al":
            game_dictionary = attack(game_dictionary, -1)
            print_game_location(game_dictionary)
        if command == "attack right" or command == "ar":
            game_dictionary = attack(game_dictionary, 1)
            print_game_location(game_dictionary)
        if command == "quit" or command == "q":
            is_quit = True
