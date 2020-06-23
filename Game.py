from controls import *


if __name__ == '__main__':
    game = Initializer.make_game()

    Game.clear()
    game.print_game_location()

    command_factory = CommandFactory()
    while True:
        input_command = input("Enter command: ")
        Game.clear()
        command_class = command_factory.create_command   (input_command)
        if command_class is not None:
            command = command_class(game)
        else:
            print("Wrong command. Use this commands:")
            command_factory.help()
            continue

        command.process()
        game.print_game_location()
