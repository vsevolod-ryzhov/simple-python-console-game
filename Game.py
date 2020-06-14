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
    if location[pos + direction] == '|':
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
    command = 0
    while command < 3:
        clear()
        command = input("Enter location size (size must be an integer > 2): ")
        try:
            command = int(command)
        except ValueError:
            print("Location size must be an integer")
            command = 0

    position_user, position_exit = random.sample(range(0, command), 2)
    game_location = list('_' * command)
    game_location[position_user] = 'X'
    game_location[position_exit] = '@'
    return game_location, position_user, position_exit


def make_barrier(game_location, pos_user, pos_exit):
    command = -1
    while command < 0 or command > count_free_fields(game_location):
        clear()
        command = input("Enter barrier count: ")
        try:
            command = int(command)
        except ValueError:
            print("Count must be an integer")
            command = -1

    if command == 0:
        return game_location

    generated_barrier = 0
    while command > generated_barrier:
        pos = random.randint(0, len(game_location) - 1)
        if game_location[pos] == '_':
            game_location[pos] = '|'
            generated_barrier += 1

    return game_location


def count_free_fields(game_location):
    return sum(1 for i in game_location if i == '_')


if __name__ == '__main__':
    commands = ['left', 'l', 'right', 'r', 'help', 'h', 'quit', 'q', 'attack left', 'al', 'attack right', 'ar']
    game_location, position_user, position_exit = init()
    game_location = make_barrier(game_location, position_user, position_exit)

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
            print("Incorrect command. Commands list: (h)elp, (l)eft, (r)ight, (al) attack left, (ar) attack right, (q)uit")
            print_game_location(game_location)

        if command == "left" or command == "l":
            if check_move(game_location, position_user, -1):
                game_location, position_user = move(game_location, position_user, -1)
                is_quit = after_move(game_location, position_user, position_exit)
        if command == "right" or command == "r":
            if check_move(game_location, position_user, 1):
                game_location, position_user = move(game_location, position_user, 1)
                is_quit = after_move(game_location, position_user, position_exit)
        if command == "attack left" or command == "al":
            if game_location[position_user - 1] == '|':
                game_location[position_user - 1] = '_';
                print_game_location(game_location)
        if command == "attack right" or command == "ar":
            if game_location[position_user + 1] == '|':
                game_location[position_user + 1] = '_';
                print_game_location(game_location)
        if command == "quit" or command == "q":
            is_quit = True
