#!/usr/bin/python
# -*- coding: utf-8 -*-


""""Simple representation of an enchanted maze."""

from maze import Room, Door, Player


class Wizard(Player):

    """A Wizard can cast spells."""

    def unlock_with_spell(self, door):
        door.unlock(with_spell="Alohomora!")


class EnchantedRoom(Room):

    """When the room is enchanted, it casts the spell on the player."""

    def __init__(self, room_number, spell):
        super(EnchantedRoom, self).__init__(room_number)
        self.spell = spell

    def enter(self, player):
        super(EnchantedRoom, self).enter(player)
        print "{} is under the spell {}".format(player.player_id, self.spell)


class DoorNeedingSpell(Door):

    """This door can't be opened manually - a wizard has to cast a spell on it."""

    def __init__(self, room1, room2):
        super(DoorNeedingSpell, self).__init__(room1, room2, is_open=False)

    def enter(self, player):
        super(DoorNeedingSpell, self).enter(player)
        if not self.is_open:
            print "You need to cast a spell first."

    def unlock(self, with_spell=False):
        """Unlocking without a spell doesn't work."""

        if not with_spell:
            print "You need to cast a spell first."
        else:
            print with_spell
            super(DoorNeedingSpell, self).unlock()
