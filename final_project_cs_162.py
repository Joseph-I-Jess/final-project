#!/usr/bin/env python3
"""
Placeholder docstring
"""

import tkinter
from tkinter import *
import time
from PIL import ImageTk, Image
from board_class import Board
from rectangulator import rectize
from merge_sort import merge_sort
from the_tuple_izer import tuple_izer
from searcher import search_for
from save_file_reader import reader
from img_hider import hide_img


class GUI(Board):
    """
    Placeholder.
    """


    def __init__(self):
        """
        Placeholder
        """
        super().__init__()

        self.game = 0
        self.p1_wins = 0
        self.draws = 0
        self.p2_wins = 0
        self.tuple = 0
        self.list_games = []
        self.list_games = reader(self.list_games)

        self.master = Tk()
        self.master.geometry('800x600')
        self.master.title("Tic Tac Toe")

        self.board_image = ImageTk.PhotoImage(
            Image.open("./tic_tac_toe_board.png")
        )
        self.X_image = ImageTk.PhotoImage(
            Image.open("./tic_tac_toe_x.png")
        )
        self.O_image = ImageTk.PhotoImage(
            Image.open("./tic_tac_toe_o.png")
        )
        self.X_big = ImageTk.PhotoImage(
            Image.open("./x_big.png")
        )
        self.O_big = ImageTk.PhotoImage(
            Image.open("./o_big.png")
        )

        self.frame_up = Frame(self.master, width=400, height=100)
        self.frame_up.grid(row=0, column=0, sticky="nsew")
        self.frame_board = Frame(self.master, width=400, height=400)
        self.frame_board.grid(row=1, column=0, sticky="nsew")
        self.frame_down = Frame(self.master, width=400, height=100)
        self.frame_down.grid(row=2, column=0, sticky="nsew")
        self.frame_sidebar = Frame(self.master, width=400, height=600)
        self.frame_sidebar.grid(row=0, column=1, sticky="nsew")
        
        self.destroy_button = Button(
            self.frame_down, text="Destroy GUI.",
            background="red", foreground="white",
            highlightbackground="red", command=self.quit
            )
        self.destroy_button.pack()

        self.label_up = Label(
            self.frame_up, text="Tic Tac Toe", font=("Courier", 25)
            )
        self.label_up.pack()

        self.label_down = Label(
            self.frame_down, text="Player 1 Turn!", font=("Courier", 25)
            )
        self.label_down.pack()

        self.label_inst = Label(
            self.frame_sidebar,
            text="Please search for: (P1 Wins),(P2 Wins),(Draws)"
        )
        self.label_inst.pack()
        self.search_ = tkinter.Entry(self.frame_sidebar)
        self.search_.pack()
        self.search_bttn = tkinter.Button(
            self.frame_sidebar, text=" Find the Game! ",
            command=(
                lambda : search_for(
                    self.search_, self.list_games, self.label_sidebar
                )
            )
        )
        self.search_bttn.pack()
        self.label_sidebar = Label(self.frame_sidebar, text="")
        self.label_sidebar.pack()


        self.canvas_main = Canvas(
            self.frame_board, width=400, height=400, bg='white'
            )
        self.canvas_main.pack(expand=YES, fill=BOTH)
        
        self.canvas_main.create_image(3, 3, image=self.board_image, anchor=NW)

        self.r_coords = [
            (3, 3, 125, 130), (155, 3, 250, 130), (280, 3, 400, 130),
            (3, 160, 125, 255), (155, 160, 250, 255), (280, 160, 400, 255),
            (3, 285, 125, 399), (155, 285, 250, 399), (280, 285, 400, 399)
        ]

        self.rects = []

        rectize(self.canvas_main, self.rects, self.r_coords, "square")

        self.canvas_main.tag_bind(
            self.rects[0], "<Button-1>",
            (lambda event, square="square1": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[1], "<Button-1>",
            (lambda event, square="square2": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[2], "<Button-1>",
            (lambda event, square="square3": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[3], "<Button-1>",
            (lambda event, square="square4": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[4], "<Button-1>",
            (lambda event, square="square5": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[5], "<Button-1>",
            (lambda event, square="square6": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[6], "<Button-1>",
            (lambda event, square="square7": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[7], "<Button-1>",
            (lambda event, square="square8": self.box_filler(event, square))
            )
        self.canvas_main.tag_bind(
            self.rects[8], "<Button-1>",
            (lambda event, square="square9": self.box_filler(event, square))
            )

        self.dict_square = {
        "square1": (20, 20, 0, 0),
        "square2": (154, 20, 0, 1),
        "square3": (290, 20, 0, 2),
        "square4": (20, 155, 1, 0),
        "square5": (154, 155, 1, 1),
        "square6": (290, 155, 1, 2),
        "square7": (20, 290, 2, 0),
        "square8": (154, 290, 2, 1),
        "square9": (290, 290, 2, 2)
        }

        self.symbol = "X"

        self.turn = 0


    def box_filler(self, event, square):
        """
        Placeholder docstring.
        """
        if self.symbol == "X":
            self.canvas_main.create_image(
                self.dict_square[square][0], self.dict_square[square][1],
                image=self.X_image, anchor=NW
                )
            self.board[self.dict_square[square][2]][self.dict_square[square][3]] = self.symbol
            self.check_conditions()
            self.symbol = "O"
            self.label_down.configure(text="Player 2 Turn!")
            self.label_down.update()
        elif self.symbol == "O":
            self.canvas_main.create_image(
                self.dict_square[square][0], self.dict_square[square][1],
                image=self.O_image, anchor=NW
                )
            self.board[self.dict_square[square][2]][self.dict_square[square][3]] = self.symbol
            self.check_conditions()
            self.symbol = "X"
            self.label_down.configure(text="Player 1 Turn!")
            self.label_down.update()
        self.turn += 1

        self.print_board()
        print(self.board)

        if(self.done != False or self.turn >= 9):
            print(self.X, self.O)
            if(self.X == True):
                print("Player 1 Wins!\n")
                self.label_down.configure(text="Player 1 Wins!")
                self.label_down.update()
                time.sleep(0.2)
                self.p1_wins += 1
            elif(self.O == True):
                print("Player 2 Wins!\n")
                self.label_down.configure(text="Player 1 Wins!")
                self.label_down.update()
                time.sleep(0.2)
                self.p2_wins += 1
            else:
                print("It's a TIE!")
                self.label_down.configure(text="It's a TIE!")
                self.label_down.update()
                time.sleep(0.2)
                self.draws += 1
            
            self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            self.done = False
            self.O = False
            self.X = False
            self.symbol = "X"
            self.turn = 0
            self.game += 1
            time.sleep(0.2)
            self.label_down.configure(text="Player 1 Turn!")
            self.label_down.update()
            self.canvas_main.delete("all")

            if self.game != 5:

                self.canvas_main.create_image(3, 3, image=self.board_image, anchor=NW)

                self.r_coords = [
                    (3, 3, 125, 130), (155, 3, 250, 130), (280, 3, 400, 130),
                    (3, 160, 125, 255), (155, 160, 250, 255), (280, 160, 400, 255),
                    (3, 285, 125, 399), (155, 285, 250, 399), (280, 285, 400, 399)
                ]

                self.rects = []

                rectize(self.canvas_main, self.rects, self.r_coords, "square")

                self.canvas_main.tag_bind(
                    self.rects[0], "<Button-1>", (
                        lambda event,
                        square="square1": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[1], "<Button-1>", (
                        lambda event,
                        square="square2": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[2], "<Button-1>", (
                        lambda event,
                        square="square3": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[3], "<Button-1>", (
                        lambda event,
                        square="square4": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[4], "<Button-1>", (
                        lambda event,
                        square="square5": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[5], "<Button-1>", (
                        lambda event,
                        square="square6": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[6], "<Button-1>", (
                        lambda event,
                        square="square7": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[7], "<Button-1>", (
                        lambda event,
                        square="square8": self.box_filler(event, square)
                        )
                    )
                self.canvas_main.tag_bind(
                    self.rects[8], "<Button-1>", (
                        lambda event,
                        square="square9": self.box_filler(event, square)
                        )
                    )
    
        if self.game == 5:
            self.tuple = (self.p1_wins, self.p2_wins, self.draws)
            self.list_games.append(self.tuple)
            print(self.list_games)
            merge_sort(self.list_games)
            self.list_games = self.list_games[::-1]
            print(self.list_games)
            with open("save_log.txt", "w+") as out_file:
                for item in self.list_games:
                    out_file.write(str(item))
                    out_file.write("\n")
            time.sleep(0.5)
            self.canvas_main.delete("all")
            self.win_screen = None
            if self.p1_wins > self.p2_wins:
                self.label_down.configure(
                    text=f"P1 Wins {self.p1_wins} to {self.p2_wins}!"
                )
                self.label_down.update()
                hide_img(self.win_screen, self.canvas_main, self.X_big)
                self.canvas_main.delete("all")
            elif self.p1_wins < self.p2_wins:
                self.label_down.configure(
                    text=f"P2 Wins {self.p2_wins} to {self.p1_wins}!"
                )
                self.label_down.update()
                hide_img(self.win_screen, self.canvas_main, self.O_big)
                self.canvas_main.delete("all")
            elif self.p1_wins == self.p2_wins:
                self.label_down.configure(text=f"It's a Tie!")
                self.label_down.update()


    def print_board(self):
        """
        Placeholder.
        """
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end = " ")
            print("")
        print("")


    def check_conditions(self):
        """
        Placeholder.
        """
        for i in range(3):
            if(self.board[i][0] == 'O' and self.board[i][1] == 'O' and self.board[i][2] == 'O'):
                self.done = True
                self.O = True
            if(self.board[i][0] == 'X' and self.board[i][1] == 'X' and self.board[i][2] == 'X'):
                self.done = True
                self.X = True
        for j in range(3):
            if(self.board[0][j] == 'O' and self.board[1][j] == 'O' and self.board[2][j] == 'O'):
                self.done = True
                self.O = True
            if(self.board[0][j] == 'X' and self.board[1][j] == 'X' and self.board[2][j] == 'X'):
                self.done = True
                self.X = True
        if(self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O'):
            self.done = True
            self.O = True
        if(self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O'):
            self.done = True
            self.O = True
        if(self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X'):
            self.done = True
            self.X = True
        if(self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X'):
            self.done = True
            self.X = True

    def run(self):
        """
        Placeholder.
        """
        self.master.mainloop()


    def quit(self):
        """
        Placeholder.
        """
        self.master.destroy()
        sys.exit(0)

if __name__ == "__main__":
    my_gui = GUI()
    while True:
        my_gui.run()
