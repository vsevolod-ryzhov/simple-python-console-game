import copy


def print_game_location(location):
    for item in location:
        print(item, end=" ")

    print("\n")


def check_move(location, pos, direction):
    if direction > 0 and pos == len(location) - 1:
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
    commands = ['left', 'l', 'right', 'r', 'help', 'h', 'quit', 'q']
    game_location = list('__________________X')
    position = game_location.index('X')

    command = None;
    is_quit = False
    while not is_quit:
        command = input("Enter command:\n")
        try:
            commands.index(command)
        except ValueError:
            print("Commands list: (h)elp, (l)eft, (r)ight, (q)uit")

        if command == "left" or command == "l":
            if check_move(game_location, position, -1):
                game_location, position = move(game_location, position, -1)
                print_game_location(game_location)
        if command == "right" or command == "r":
            if check_move(game_location, position, 1):
                game_location, position = move(game_location, position, 1)
                print_game_location(game_location)
        if command == "quit" or command == "q":
            is_quit = True
