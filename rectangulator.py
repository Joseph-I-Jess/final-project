#!/usr/bin/env python3
"""
Create rectangles into which Xs and Os will appear.

Creates rectangles into which Xs and Os will appear at precise locations, as
determined by arguments.

Gareth Miller, Anthony Sierra, Srikar Valluri
"""

from tkinter import *


def rectize(canv, r_list, coord_list, des_tag):
    """
    Create rectangles into which Xs and Os will appear.

    Creates rectangles into which Xs and Os will be placed by the box_filler
    function, using standard tkinter functions which we got tired of typing
    over and over again.

    Parameters
    ----------
    canv : instance of tkinter canvas object
        The canvas upon which the rectangles are being created.
    r_list : list
        The blank list to which created rectangles will be appended.
    coord_list : list[tup]
        The list of tuples of x- and y-coordinates for the rectangles' corners.
    des_tag : str
        The desired tag, to which a number will be concatenated.

    Returns
    -------
    rectangle : instance of tkinter rectangle object
        The rectangle created.

    """
    for i in range(9):
        r_list.append(canv.create_rectangle(
            coord_list[i][0], coord_list[i][1], coord_list[i][2],
            coord_list[i][3], fill='white', outline='white',
            tags=des_tag + str(i + 1)
        ))
