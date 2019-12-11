#!/usr/bin/env python3
"""
Placeholder.
"""


class Board:
    """
    Create the board upon which the GUI is based.

    Creates the board upon which the GUI is based.
    """


    def __init__(self):
        """
        Instantiate the Board class.

        Instantiates the Board class.
        """
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.O = False
        self.X = False
        self.done = False
