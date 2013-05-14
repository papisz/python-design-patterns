#!/usr/bin/python
# -*- coding: utf-8 -*-

"""An abstract factory according to GoF."""

from random import choice

from maze import Maze, Room, Door, Direction, Wall, Player
from enchanted_maze import EnchantedRoom, DoorNeedingSpell, Wizard
from basic_creator import play


class BasicMazeFactory(object):

    """Factory producing basic Maze."""

    @staticmethod
    def make_maze():
        return Maze()

    @staticmethod
    def make_wall():
        return Wall()

    @staticmethod
    def make_room(room_number):
        return Room(room_number)

    @staticmethod
    def make_door(room1, room2):
        return Door(room1, room2)


class EnchantedMazeFactory(BasicMazeFactory):

    """Factory producting Enchanted Maze."""

    SPELLS = ("Wingardium Leviosa", "Confundus", "Expelliarmus")

    @classmethod
    def make_room(cls, room_number):
        spell = choice(cls.SPELLS)
        return EnchantedRoom(room_number, spell)

    @staticmethod
    def make_door(room1, room2):
        return DoorNeedingSpell(room1, room2)


def create_maze(factory):
    """Series of operations which create our Maze."""

    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    thedoor = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, factory.make_wall())
    room1.set_side(Direction.EAST, thedoor)
    room1.set_side(Direction.SOUTH, factory.make_wall())
    room1.set_side(Direction.WEST, factory.make_wall())

    room2.set_side(Direction.NORTH, factory.make_wall())
    room2.set_side(Direction.EAST, factory.make_wall())
    room2.set_side(Direction.SOUTH, factory.make_wall())
    room2.set_side(Direction.WEST, thedoor)

    return maze


def play_enchanted(maze, player):
    print "\n---> Wizard {} enters the enchanted maze in room {}".format(player.player_id, player.current_room.room_number)
    room1 = player.current_room
    for side in Direction.ALL:
        print "\t{} SIDE: {}".format(side, room1.get_side(side))

    thedoor = room1.get_side(Direction.EAST)
    player.unlock_with_spell(thedoor)
    player = thedoor.enter(player)

    for side in Direction.ALL:
        print "\t{} SIDE: {}".format(side, room1.get_side(side))

if __name__ == "__main__":
    basic_maze = create_maze(BasicMazeFactory)
    enchanted_maze = create_maze(EnchantedMazeFactory)

    play(basic_maze, Player("Pinky", basic_maze.get_room_by_number(1)))
    play_enchanted(enchanted_maze, Wizard("Harry", enchanted_maze.get_room_by_number(1)))
