#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Simple representation of a maze."""

from random import choice


class Player(object):

    """Represents position of a certain player."""

    def __init__(self, player_id, start_room):

        self.player_id = player_id
        self.current_room = start_room


class Direction(object):

    """Simple structure representing 4 directions.

    Might as well be an enum with ints - I've' put strs here for simplicity.

    """

    NORTH, SOUTH, EAST, WEST = ('NORTH', 'SOUTH', 'EAST', 'WEST')
    ALL = {NORTH, SOUTH, EAST, WEST}


class MapSite(object):

    """Just an abstract for maze elements."""

    def enter(self, player):
        """Entering this abstract site can't be good..."""
        print player.player_id, "says: Ouch!"


class Room(MapSite):

    """Represents a room with four sides - north, south, east and west - and a room number."""

    def __init__(self, room_number):
        super(Room, self).__init__()
        self._sides = {
            Direction.NORTH: None,
            Direction.SOUTH: None,
            Direction.EAST: None,
            Direction.WEST: None
        }
        self.room_number = room_number

    def get_side(self, direction):
        """Return a MapSite object for given direction."""
        return self._sides[direction]

    def set_side(self, direction, mapsite_object):
        """Set a MapSite object for given direction."""
        self._sides[direction] = mapsite_object

    def enter(self, player):
        """Entering a room changes player's location."""
        print "--> {} enters room: {}".format(player.player_id, self.room_number)
        player.current_room = self


class Wall(MapSite):

    """Represents a Wall - you can't do anything with it."""

    pass


class Door(MapSite):

    """A door joins two rooms and it's got two states: open and closed."""

    def __init__(self, room1, room2, is_open=None):
        super(Door, self).__init__()
        self._open = choice((True, False)) if is_open is None else is_open
        self._rooms = {
            room2.room_number: room1,  # from room 2 we can get to the room 1
            room1.room_number: room2   # from room 1 we can get to the room 2
        }

    def other_side_from(self, room):
        """Return the Room object from the other side of the door."""
        return self._rooms[room.room_number]

    @property
    def is_open(self):
        """Returns True if the door is opened, False otherwise."""
        return self._open

    def enter(self, player):
        """Entering the door means going to room on the other side.

        A player can enter the door only if it's opened.

        """
        if self.is_open:
            other_room = self.other_side_from(player.current_room)
            other_room.enter(player)
        else:
            super(Door, self).enter(player)

    def unlock(self):
        self._open = True
        print "The door is now unlocked!"


class Maze(object):

    """Maze is a container for rooms."""

    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        """Add a room."""
        self.rooms[room.room_number] = room

    def get_room_by_number(self, room_number):
        """Get room by its number."""
        return self.rooms[room_number]
