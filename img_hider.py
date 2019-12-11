#!/usr/bin/env python3
"""
Hide and reveal an image file in quick succession.

Hides and reveals an image file in quick succession, causing it to blink three
times before disappearing.
"""

from tkinter import *


def hide_img(var, widget, img):
    """
    Placeholder
    """
    import time
    var = widget.create_image(
        200, 200, image=img
    )
    widget.update()
    time.sleep(0.3)
    for i in range(4):
        if i % 2 == 0:
            #widget["state"] = "normal"
            widget.itemconfig(var, state=HIDDEN)
        else:
            #widget["state"] = "disabled"
            widget.itemconfig(var, state=NORMAL)
        widget.update()
        time.sleep(0.3)
    time.sleep(0.7)
    
    # for i in range(4):
    #     if (i % 2) == 0 and i < 3:
    #         #widget.itemconfig(var, state=HIDDEN)
    #         widget["state"] = "disabled"
    #         widget.update()
    #         time.sleep(0.3)
    #     elif (i % 2) != 0 and i < 3:
    #         #widget.itemconfig(var, state=NORMAL)
    #         widget["state"] = "active"
    #         widget.update()
    #         time.sleep(0.3)
    #     elif i == 3:
    #         #widget.itemconfig(var, state=NORMAL)
    #         widget["state"] = "active"
    #         widget.update()
    #         time.sleep(1)
