#!/usr/bin/env python3
"""
Search for saved scores and report the number of matching saves.

Searches for saved scores based upon user input and then returns the number of
saved scores that match the user input.
"""

from tkinter import *
from the_tuple_izer import tuple_izer

def search_for(tup_ish, list_, label):
    """
    Placeholder.
    """
    tup_ish = tup_ish.get()
    # print(tup_ish)
    tup_ish = tuple_izer(tup_ish)
    # print(str(tup_ish) + "\n")
    number = 0

    for i in range(len(list_)):
        if tup_ish == list_[i]:
            number += 1
 
    label.configure(
        text = f"There are {number} games with the result {tup_ish}."
    )
    label.update()
