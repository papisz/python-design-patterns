# -*- coding: utf-8 -*-


class Target(object):

    def request(self):
        return "I'm a target"


class Adaptee(object):

    def specific_request(self):
        return "I'm an adaptee"


class Adapter(Target):

    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request()

if __name__ == "__main__":
    adapt = Adapter(Adaptee())
    print adapt.request()
