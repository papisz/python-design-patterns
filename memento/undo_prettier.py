#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Sample Memento pattern rewritten from Java example, in a more Pythonic way."""

class Originator(object):

    def __init__(self, initial_state=None):
        self.__state = initial_state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        # TODO: (to think of): combine state setter with restore_from_memento using Strategy Pattern
        self.__state = state

    def save_to_memento(self):
        return Memento(self.state)

    def restore_from_memento(self, memento):
        self.__state = memento.saved_state

    def __repr__(self):
        return "Originator: \t({})".format(self.state)

class Memento(object):

    def __init__(self, state_to_save):
        self.__state = state_to_save

    @property
    def saved_state(self):
        return self.__state

    def __repr__(self):
        return "Memento: \t({})".format(self.__state)

if __name__ == "__main__":

    saved_states = []

    # Creating Originator
    originator = Originator("State1")
    # Let's set some states
    originator.state = "State2"
    # Saving this one for later...
    saved_states.append(originator.save_to_memento())
    originator.state = "State3"
    # ...and this one too
    saved_states.append(originator.save_to_memento())
    originator.state = "State4"

    # Restore the first saved state
    originator.restore_from_memento(saved_states[0])

    # We can also get the other one
    originator.restore_from_memento(saved_states[1])

