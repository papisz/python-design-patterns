#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Creates a basic maze and a play."""

from maze import Maze, Room, Door, Direction, Wall, Player


def create_maze():
    """Series of operations which create our Maze."""
    maze = Maze()
    room1 = Room(1)
    room2 = Room(2)
    thedoor = Door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.EAST, thedoor)
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.WEST, Wall())

    room2.set_side(Direction.NORTH, Wall())
    room2.set_side(Direction.EAST, Wall())
    room2.set_side(Direction.SOUTH, Wall())
    room2.set_side(Direction.WEST, thedoor)

    return maze


def play(maze, player):
    print "\n--> Player", player.player_id, "enters the maze in room", player.current_room.room_number
    room1 = player.current_room
    for side in Direction.ALL:
        print "\t{} SIDE: {}".format(side, room1.get_side(side))

    thedoor = room1.get_side(Direction.EAST)
    if not thedoor.is_open:
        thedoor.unlock()
    player = thedoor.enter(player)

    for side in Direction.ALL:
        print "\t{} SIDE: {}".format(side, room1.get_side(side))

if __name__ == "__main__":
    maze = create_maze()
    play(maze, Player("Pinky", maze.get_room_by_number(1)))
