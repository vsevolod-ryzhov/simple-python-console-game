import os
import sys
import copy
import random
from abc import ABC, abstractmethod


class Position(ABC):
    @abstractmethod
    def __init__(self, position):
        self.position = position


class Initializer:
    @staticmethod
    def make_game():
        command = 0
        while command < 3:
            Game.clear()
            command = input("Enter location size (size must be an integer > 2): ")
            try:
                command = int(command)
            except ValueError:
                print("Location size must be an integer")
                command = 0

        position_user, position_exit = random.sample(range(0, command), 2)
        location = list(Game.empty_field() * command)
        location[position_user] = Game.hero_field()
        location[position_exit] = Game.exit_field()

        game = Game(location, Hero(position_user), Exit(position_exit))
        return Initializer.make_barrier(game)

    @staticmethod
    def make_barrier(game):
        command = -1
        while command < 0 or command > game.count_free_fields():
            Game.clear()
            command = input("Enter barrier count: ")
            try:
                command = int(command)
            except ValueError:
                print("Count must be an integer")
                command = -1

        if command == 0:
            return game

        generated_barrier = 0
        while command > generated_barrier:
            pos = random.randint(0, len(game.location) - 1)
            if game.location[pos] == Game.empty_field():
                game.location[pos] = Game.barrier_field()
                generated_barrier += 1

        return game


class Game:
    @staticmethod
    def empty_field():
        return '_'

    @staticmethod
    def barrier_field():
        return '|'

    @staticmethod
    def hero_field():
        return 'X'

    @staticmethod
    def exit_field():
        return '@'

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def game_over():
        Game.clear()
        print("###############################")
        print("##### GAME OVER! YOU WIN! #####")
        print("###############################")
        Game.quit()

    @staticmethod
    def quit():
        Game.clear()
        sys.exit()

    def __init__(self, location, hero, exit):
        self.location = location
        self.hero = hero
        self.exit = exit

    def print_game_location(self):
        for item in self.location:
            print(item, end="")
        print("\n")

    def check_move(self, direction):
        if direction > 0 and self.hero.position == len(self.location) - 1:
            print("Error! Out of location.")
            return False;
        if direction < 0 and self.hero.position == 0:
            print("Error! Out of location.")
            return False
        if self.location[self.hero.position + direction] == self.barrier_field():
            return False
        return True

    def check_exit(self):
        return self.hero.position == self.exit.position

    def count_free_fields(self):
        return sum(1 for i in self.location if i == self.empty_field())

    def move(self, direction):
        if not self.check_move(direction):
            return False
        location = copy.deepcopy(self.location)
        location[self.hero.position] = self.empty_field()
        self.hero.position += direction
        location[self.hero.position] = self.hero_field()
        self.location = location

        self.after_move()
        return True

    def after_move(self):
        if self.check_exit():
            self.game_over()

    def attack(self, direction):
        if self.location[self.hero.position + direction] == self.barrier_field():
            self.location[self.hero.position + direction] = self.empty_field();


class Hero(Position):
    def __init__(self, position):
        super().__init__(position)


class Exit(Position):
    def __init__(self, position):
        super().__init__(position)
