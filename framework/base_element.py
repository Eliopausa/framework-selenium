# coding: utf-8

class BaseElement:
    """ Родительский класс для элементов веб-страницы. """

    def __init__(self, name, locator):
        self.name = name
        self.locator = locator
