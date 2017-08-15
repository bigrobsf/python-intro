"""python homework - oop exercises"""

from __future__ import print_function

# What is a class?

# A class is a blueprint for objects that can contain properties and methods.
# They are commonly used to reduce code duplication and maintenance.

# What is an instance?

# An instance is an object created by a class. Instances of a class will all
# have the same structure because they were created from the same blueprint.

# What is encapsulation?

# Encapsulation refers to the idea that the data and processes relating to a
# class are controlled by the class. Outside code should not be able to
# directly change it.

# What is abstraction?

# Abstraction allows us to think about classes at a higher level. Methods that
# are made available by the class are all that we need to use the class and
# access its data without having to worry about the details of how it is
# implemented.

# What is inheritance?

# Inheritance is the idea that a class can inherit the properties and methods
# of a parent class. This saves us from having to implement the same logic in
# our new class.

# What is polymorphism?

# Polymorphism is the idea that an object can take many forms. It is a key
# concept in OOP. A common example is when a parent class's method is
# overridden by a sub class - each sub class will have a difference
# implementation of the method.

# What is method resolution order?

# MRO determines the order in which Python will look for methods on instances
# of a class that inherits from multiple classes that have the same method.
# This can be determined by looking at the __mro___ attribute for the class or
# the mro() method.


import random


class Deck:
    """defines a standard deck of cards"""
    def __init__(self):
        self.cards = []
        self.suite = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                      'Jack', 'Queen', 'King']

    def fill_deck(self):
        self.cards.clear()
        for suite in self.suite:
            for value in self.value:
                card = Card(suite, value)
                self.cards.append(card)
        return 'New deck has {} cards.'.format(len(self.cards))

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return 'All cards have been dealt.'

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
            return self
        else:
            return 'Deck must be full to be shuffled.'

    def __repr__(self):
        return 'The deck has {} cards.'.format(len(self.cards))

    def list_cards(self):
        return [card for card in self.cards]


class Card:
    """represents a standard playing card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit)





# end
