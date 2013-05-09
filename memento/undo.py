#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Sample Memento pattern LITERALLY rewritten from Java example (see references in README).

For more Pythonic approach see undo_prettier.py."""


class Originator(object):

    def __init__(self, initial_state=None):
        self.state = initial_state

    def set(self, state):
        self.state = state

    def save_to_memento(self):
        return Memento(self.state)

    def restore_from_memento(self, memento):
        self.state = memento.get_saved_state()

    def __repr__(self):
        return "Originator: \t({})".format(self.state)


class Memento(object):

    def __init__(self, state_to_save):
        self.__state = state_to_save

    def get_saved_state(self):
        return self.__state

    def __repr__(self):
        return "Memento: \t({})".format(self.__state)


class Caretaker(object):

    def __init__(self):
        self.saved_states = []

    def add_memento(self, memento):
        self.saved_states.append(memento)

    def get_memento(self, index):
        return self.saved_states[index]

if __name__ == "__main__":

    # Creating Caretaker
    caretaker = Caretaker()

    # Creating Originator
    originator = Originator("State1")
    # Let's set some states
    originator.set("State2")
    # Saving this one for later...
    caretaker.add_memento(originator.save_to_memento())
    originator.set("State3")
    # ...and this one too
    caretaker.add_memento(originator.save_to_memento())
    originator.set("State4")

    # Restore the first saved state
    originator.restore_from_memento(caretaker.get_memento(0))

    # We can also get the other one
    originator.restore_from_memento(caretaker.get_memento(1))
