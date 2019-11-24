class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.O = False
        self.X = False
        self.done = False


from tkinter import * 
from PIL import ImageTk, Image


class GUI():
    def __init__(self):
        self.board = Board()

        for i in range(3):
            for j in range(3):
                self.board.board[i][j] = '.'
                print(self.board.board[i][j], end = " ")
            print("")
        print("")

        self.master = Tk()
        self.master.geometry('400x600')
        self.master.title("GUI")

        self.board_image = ImageTk.PhotoImage(Image.open("./tic_tac_toe_board.png"))
        self.X_image = ImageTk.PhotoImage(Image.open("./tic_tac_toe_x.png"))
        self.O_image = ImageTk.PhotoImage(Image.open("./tic_tac_toe_o.png"))

        self.frame_up = Frame(self.master, width=400, height=100)
        self.frame_up.grid(row=0, column=0, sticky="nsew")
        self.frame_board = Frame(self.master, width=400, height=400)
        self.frame_board.grid(row=1, column=0, sticky="nsew")
        self.frame_down = Frame(self.master, width=400, height=100)
        self.frame_down.grid(row=2, column=0, sticky="nsew")

        self.destroy_button = Button(self.frame_down, text="Destroy GUI.", background="red", foreground="white", highlightbackground="red", command=self.quit)
        self.destroy_button.pack()

        self.label_up = Label(self.frame_up, text="Tic Tac Toe", font=("Courier", 25))
        self.label_up.pack()

        self.label_down = Label(self.frame_down, text="Player 1 Turn!", font=("Courier", 25))
        self.label_down.pack()

        self.canvas = Canvas(self.frame_board, width=400, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        
        self.canvas.create_image(3, 3, image=self.board_image, anchor=NW)

        self.rect1 = self.canvas.create_rectangle(3, 3, 125, 130, fill='white', outline='white', tags="square1")
        self.rect2 = self.canvas.create_rectangle(155, 3, 250, 130, fill='white', outline='white', tags="square2")
        self.rect3 = self.canvas.create_rectangle(280, 3, 400, 130, fill='white', outline='white', tags="square3")
        self.rect4 = self.canvas.create_rectangle(3, 160, 125, 255, fill='white', outline='white', tags="square4")
        self.rect5 = self.canvas.create_rectangle(155, 160, 250, 255, fill='white', outline='white', tags="square5")
        self.rect6 = self.canvas.create_rectangle(280, 160, 400, 255, fill='white', outline='white', tags="square6")
        self.rect7 = self.canvas.create_rectangle(3, 285, 125, 399, fill='white', outline='white', tags="square7")
        self.rect8 = self.canvas.create_rectangle(155, 285, 250, 399, fill='white', outline='white', tags="square8")
        self.rect9 = self.canvas.create_rectangle(280, 285, 400, 399, fill='white', outline='white', tags="square9")

        self.canvas.tag_bind(self.rect1, "<Button-1>", (lambda event, square="square1": self.hi(event, square)))
        self.canvas.tag_bind(self.rect2, "<Button-1>", (lambda event, square="square2": self.hi(event, square)))
        self.canvas.tag_bind(self.rect3, "<Button-1>", (lambda event, square="square3": self.hi(event, square)))
        self.canvas.tag_bind(self.rect4, "<Button-1>", (lambda event, square="square4": self.hi(event, square)))
        self.canvas.tag_bind(self.rect5, "<Button-1>", (lambda event, square="square5": self.hi(event, square)))
        self.canvas.tag_bind(self.rect6, "<Button-1>", (lambda event, square="square6": self.hi(event, square)))
        self.canvas.tag_bind(self.rect7, "<Button-1>", (lambda event, square="square7": self.hi(event, square)))
        self.canvas.tag_bind(self.rect8, "<Button-1>", (lambda event, square="square8": self.hi(event, square)))
        self.canvas.tag_bind(self.rect9, "<Button-1>", (lambda event, square="square9": self.hi(event, square)))

        self.dict = {
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
    
    def hi(self, event, square):
        if self.symbol == "X":
            self.canvas.create_image(self.dict[square][0], self.dict[square][1], image=self.X_image, anchor=NW)
            self.board.board[self.dict[square][2]][self.dict[square][3]] = self.symbol
            self.checkConditions()
            self.symbol = "O"
            self.label_down.configure(text="Player 2 Turn!")
            self.label_down.update()
        elif self.symbol == "O":
            self.canvas.create_image(self.dict[square][0], self.dict[square][1], image=self.O_image, anchor=NW)
            self.board.board[self.dict[square][2]][self.dict[square][3]] = self.symbol
            self.checkConditions()
            self.symbol = "X"
            self.label_down.configure(text="Player 1 Turn!")
            self.label_down.update()
        self.turn += 1

        self.printBoard()
        print(self.board.board)

        if(self.board.done != False or self.turn >= 9):
            print(self.board.X, self.board.O)
            if(self.board.X == True):
                print("Player 1 Wins!\n")
            elif(self.board.O == True):
                print("Player 2 Wins!\n")
            else:
                print("It's a TIE!")
            
            self.quit()

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board.board[i][j], end = " ")
            print("")
        print("")

    def checkConditions(self):
        for i in range(3):
            if(self.board.board[i][0] == 'O' and self.board.board[i][1] == 'O' and self.board.board[i][2] == 'O'):
                self.board.done = True
                self.board.O = True
            if(self.board.board[i][0] == 'X' and self.board.board[i][1] == 'X' and self.board.board[i][2] == 'X'):
                self.board.done = True
                self.board.X = True
        for j in range(3):
            if(self.board.board[0][j] == 'O' and self.board.board[1][j] == 'O' and self.board.board[2][j] == 'O'):
                self.board.done = True
                self.board.O = True
            if(self.board.board[0][j] == 'X' and self.board.board[1][j] == 'X' and self.board.board[2][j] == 'X'):
                self.board.done = True
                self.board.X = True
        if(self.board.board[0][0] == 'O' and self.board.board[1][1] == 'O' and self.board.board[2][2] == 'O'):
            self.board.done = True
            self.board.O = True
        if(self.board.board[0][2] == 'O' and self.board.board[1][1] == 'O' and self.board.board[2][0] == 'O'):
            self.board.done = True
            self.board.O = True
        if(self.board.board[0][0] == 'X' and self.board.board[1][1] == 'X' and self.board.board[2][2] == 'X'):
            self.board.done = True
            self.board.X = True
        if(self.board.board[0][2] == 'X' and self.board.board[1][1] == 'X' and self.board.board[2][0] == 'X'):
            self.board.done = True
            self.board.X = True

    def run(self):
        self.master.mainloop()

    def quit(self):
        self.master.destroy()
        sys.exit(0)

my_gui = GUI()
while True:
    my_gui.run()
