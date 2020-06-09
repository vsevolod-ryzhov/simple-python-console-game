import os
import copy
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_game_location(location):
    for item in location:
        print(item, end="")

    print("\n")


def check_move(location, pos, direction):
    if direction > 0 and pos == len(location) - 1:
        print("Error! Out of location.")
        return False;
    if direction < 0 and pos == 0:
        print("Error! Out of location.")
        return False
    return True


def check_exit(pos_user, pos_exit):
    return pos_user == pos_exit


def game_over():
    clear()
    print("###############################")
    print("##### GAME OVER! YOU WIN! #####")
    print("###############################")


def move(location, pos, direction):
    location = copy.deepcopy(location)
    location[pos] = "_"
    pos += direction
    location[pos] = "X"
    return location, pos


def after_move(location, pos_user, pos_exit):
    if check_exit(pos_user, pos_exit):
        game_over()
        return True
    else:
        print_game_location(location)
    return False


def init():
    command = input("Enter location size: ")
    command = int(command)

    position_user, position_exit = random.sample(range(0, command), 2)
    game_location = list('_' * command)
    game_location[position_user] = 'X'
    game_location[position_exit] = '@'
    return game_location, position_user, position_exit


if __name__ == '__main__':
    commands = ['left', 'l', 'right', 'r', 'help', 'h', 'quit', 'q']
    game_location, position_user, position_exit = init()

    clear()
    print_game_location(game_location)

    command = None;
    is_quit = False
    while not is_quit:
        command = input("Enter command: ")
        clear()
        try:
            commands.index(command)
        except ValueError:
            print("Incorrect command. Commands list: (h)elp, (l)eft, (r)ight, (q)uit")
            print_game_location(game_location)

        if command == "left" or command == "l":
            if check_move(game_location, position_user, -1):
                game_location, position_user = move(game_location, position_user, -1)
                is_quit = after_move(game_location, position_user, position_exit)
        if command == "right" or command == "r":
            if check_move(game_location, position_user, 1):
                game_location, position_user = move(game_location, position_user, 1)
                is_quit = after_move(game_location, position_user, position_exit)
        if command == "quit" or command == "q":
            is_quit = True
