"""
Create Tony's tic-tac-toe board.

Creates Tony's tic-tac-toe board.
"""

import tkinter as tk
root = tk.Tk()
win = tk.Canvas(root ,width = 320, height = 320)
root.title = ("tic tac toe")
win.pack()
win.create_line(10,110,310,110,fill="black",width = 2)
win.create_line(10,210,310,210,fil ="black", width =2)
win.create_line(110,10,110,310,fill="black",width = 2)
win.create_line(210,10,210,310,fil ="black", width =2)

class player_base:
    def __init__(self):
        self.pos_x = pos_x
        self.pos_y = pos_y
       
    def click(self,event):
        self.pos_x = event.x
        self.pos_y = event.y
        print(self.pos_x,self.pos_y)

       
    def create_symbol(self,symbol):
        if self.x != None and self.y != None:
            if symbol == "x":
                win.create_line(self.x[0],self.y[0],self.x[1],self.y[1],fill= "black")
                win.create_line(self.x[1],self.y[0],self.x[0],self.y[1],fill= "black")
            elif symbol =="0":
                win.create_oval(self.x[0],self.y[0], self.x[1],self.y[1])
                #win.create_oval(self.y[1],self.y[0], self.x[0],self.y[1])

   
       
         
    def get_pos(self):
   
        if self.pos_x>10 and self.pos_x<110: #  left
            x = [10,110]
        elif self.pos_x>110 and self.pos_x <210:# middle
            x = [110,210]
        elif self.pos_x <310 and self.pos_x >210: #right
            x = [210,310]
        else:
            x=None
       
        if self.pos_y <110 and self.pos_y >10: # top
            y= [10,110]
        elif self.pos_y <210 and self.pos_y >110: #middle
            y= [110,210]
       

        elif self.pos_y <310 and self.pos_y > 210: # bottom
            y= [210,310]
        else:
            y= None

        self.x = x
        self.y = y
           
class player(player_base):
    def __init__(self,symbol):
        self.symbol = symbol
    def click(self,event):
        self.pos_x = event.x
        self.pos_y = event.y
        self.get_pos()
        self.create_symbol(self.symbol)
       


p1= player("x")
p2= player("0")
win.bind("<Button-1>", p1.click)
win.bind("<Button-3>", p2.click)
