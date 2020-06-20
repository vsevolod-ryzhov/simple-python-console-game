import os
import copy
import random

CONST_EMPTY_FIELD = '_';
CONST_BARRIER_FIELD = '|';
CONST_HERO_FIELD = 'X';
CONST_EXIT_FIELD = '@';

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_game_location(game_dictionary):
    for item in game_dictionary['game_location']:
        print(item, end="")

    print("\n")


def check_move(game_dictionary, direction):
    if direction > 0 and game_dictionary['position_user'] == len(game_dictionary['game_location']) - 1:
        print("Error! Out of location.")
        return False;
    if direction < 0 and game_dictionary['position_user'] == 0:
        print("Error! Out of location.")
        return False
    if game_dictionary['game_location'][game_dictionary['position_user'] + direction] == CONST_BARRIER_FIELD:
        return False
    return True


def check_exit(game_dictionary):
    return game_dictionary['position_user'] == game_dictionary['position_exit']


def game_over():
    clear()
    print("###############################")
    print("##### GAME OVER! YOU WIN! #####")
    print("###############################")


def move(game_dictionary, direction):
    # TODO: check that hero can do move in direction
    location = copy.deepcopy(game_dictionary['game_location'])
    location[game_dictionary['position_user']] = CONST_EMPTY_FIELD
    game_dictionary['position_user'] += direction
    location[game_dictionary['position_user']] = CONST_HERO_FIELD
    game_dictionary['game_location'] = location
    return game_dictionary


def attack(game_dictionary, direction):
    if game_dictionary['game_location'][game_dictionary['position_user'] + direction] == CONST_BARRIER_FIELD:
        game_dictionary['game_location'][game_dictionary['position_user'] + direction] = CONST_EMPTY_FIELD;
    return game_dictionary


def after_move(game_dictionary):
    if check_exit(game_dictionary):
        game_over()
        return True
    else:
        print_game_location(game_dictionary)
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
    dict = {
        'game_location': list(CONST_EMPTY_FIELD * command),
        'position_user': position_user,
        'position_exit': position_exit
    }
    dict['game_location'][position_user] = CONST_HERO_FIELD
    dict['game_location'][position_exit] = CONST_EXIT_FIELD
    return dict


def make_barrier(game_dictionary):
    command = -1
    while command < 0 or command > count_free_fields(game_dictionary):
        clear()
        command = input("Enter barrier count: ")
        try:
            command = int(command)
        except ValueError:
            print("Count must be an integer")
            command = -1

    if command == 0:
        return game_dictionary

    generated_barrier = 0
    while command > generated_barrier:
        pos = random.randint(0, len(game_dictionary['game_location']) - 1)
        if game_dictionary['game_location'][pos] == CONST_EMPTY_FIELD:
            game_dictionary['game_location'][pos] = CONST_BARRIER_FIELD
            generated_barrier += 1

    return game_dictionary


def count_free_fields(game_dictionary):
    return sum(1 for i in game_dictionary['game_location'] if i == CONST_EMPTY_FIELD)