import copy


def print_game_location(location):
    for item in location:
        print(item, end=" ")

    print("\n")


def check_move(pos, direction):
    if direction > 0 and pos == 9:
        print("Error! Out of location.")
        return False;
    if direction < 0 and pos == 0:
        print("Error! Out of location.")
        return False
    return True


def move(location, pos, direction):
    location = copy.deepcopy(location)
    location[pos] = "_"
    pos += direction
    location[pos] = "X"
    return location, pos


if __name__ == '__main__':
    game_location = list('X_________')
    position = 0

    command = None;
    while command != "done":
        command = input("Enter command:\n")
        if command == "left":
            if check_move(position, -1):
                game_location, position = move(game_location, position, -1)
                print_game_location(game_location)
            pass
        if command == "right":
            if check_move(position, 1):
                game_location, position = move(game_location, position, 1)
                print_game_location(game_location)
            pass
        if command == "help" or (command != "left" and command != "right" and command != "help" and command != "done"):
            print("Commands list: help, left, right, done")
