#!/usr/bin/env python3
"""
Search for a list element and print it.

Searches for a list element and prints it.
This is the code that Tony was debugging w/ Joseph Jess on 10 Dec 2019.

Anthony Sierra
"""

import tkinter as tk
from the_tuple_izer import tuple_izer
root = tk.Tk()
list_games = [(3,3,3), (2,2,2)]
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
search_1 = tk.Entry(root)
canvas1.create_window(200, 140, window=search_1)


def search_for(list_1):
    tup_ish = search_1.get()
    print(tup_ish)
    tup_ish = tuple_izer(tup_ish)
    print(tup_ish)
   
    for i in range(len(list_1)):
        if tup_ish == list_1[i]:
            print (list_1[i])
        else:
            print ("N/A")
            print(type(tup_ish))
            print(type(list_1[i]))

button_1 = tk.Button(text=" find the game!", command=(lambda : search_for(list_games)))
#a = 5
#b = 10
#button_1 = tk.Button(text=" find the game!", command=(lambda : print(f"{a + b}")))
button_1.pack()
canvas1.create_window(200,180,window= button_1)
