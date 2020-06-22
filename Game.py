from core import *
from abc import ABC, abstractmethod


class abstractstatic(staticmethod):
    __slots__ = ()
    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    __isabstractmethod__ = True


class CommandFactory():
    def __init__(self):
        self.commands = [LeftCommand, RightCommand, QuitCommand, AttackLeftCommand, AttackRightCommand]

    def create_command(self, command):
        for command_class in self.commands:
            if any(command in i for i in command_class.aliases()):
                return command_class
        return None

    def help(self):
        for command_class in self.commands:
            print(command_class.aliases())


class Command(ABC):
    @abstractmethod
    def __init__(self, game):
        self.game = game

    @abstractstatic
    def aliases(self):
        pass

    @abstractmethod
    def process(self):
        pass


class LeftCommand(Command):
    def __init__(self, game):
        super().__init__(game)

    @staticmethod
    def aliases():
        return 'left', 'l'

    def process(self):
        game.move(-1)


class RightCommand(Command):
    def __init__(self, game):
        super().__init__(game)

    @staticmethod
    def aliases():
        return 'right', 'r'

    def process(self):
        game.move(1)


class QuitCommand(Command):
    def __init__(self, game):
        super().__init__(game)

    @staticmethod
    def aliases():
        return 'quit', 'q'

    def process(self):
        Game.quit()


class AttackLeftCommand(Command):
    def __init__(self, game):
        super().__init__(game)

    @staticmethod
    def aliases():
        return 'attack left', 'al'

    def process(self):
        game.attack(-1)


class AttackRightCommand(Command):
    def __init__(self, game):
        super().__init__(game)

    @staticmethod
    def aliases():
        return 'attack right', 'ar'

    def process(self):
        game.attack(1)


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
