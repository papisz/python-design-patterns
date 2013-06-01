# -*- coding: utf-8 -*-


class Target(object):

    def request(self):
        return "I'm a target"


class Adaptee(object):

    def specific_request(self):
        return "I'm an adaptee"


class Adapter(Target, Adaptee):

    def request(self):
        return self.specific_request()

if __name__ == "__main__":
    adapt = Adapter()
    print adapt.request()
