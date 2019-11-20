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

        self.canvas = Canvas(self.frame_board, width=400, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        
        self.canvas.create_image(3, 3, image=self.board_image, anchor=NW)

        self.rect1 = self.canvas.create_rectangle(3, 3, 125, 130, fill='lightgrey', outline='white', tags="square1")
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
    
    def hi(self, event, square):
        if self.symbol == "X":
            self.canvas.create_image(self.dict[square][0], self.dict[square][1], image=self.X_image, anchor=NW)
            self.symbol = "O"
        elif self.symbol == "O":
            self.canvas.create_image(self.dict[square][0], self.dict[square][1], image=self.O_image, anchor=NW)
            self.symbol = "X"

    def setupBoard(self):
        board = Board()
        for i in range(3):
            for j in range(3):
                board.board[i][j] = '.'
                print(board.board[i][j], end = " ")
            print("")
        print("")
        return board

    def printBoard(self, board):
        for i in range(3):
            for j in range(3):
                print(board.board[i][j], end = " ")
            print("")
        print("")

    def checkConditions(self, board):
        for i in range(3):
            if(board.board[i][0] == 'O' and board.board[i][1] == 'O' and board.board[i][2] == 'O'):
                board.done = True
                board.O = True
            if(board.board[i][0] == 'X' and board.board[i][0] == 'X' and board.board[i][2] == 'X'):
                board.done = True
                board.X = True
        for j in range(3):
            if(board.board[0][j] == 'O' and board.board[1][j] == 'O' and board.board[2][j] == 'O'):
                board.done = True
                board.O = True
            if(board.board[0][j] == 'X' and board.board[1][j] == 'X' and board.board[2][j] == 'X'):
                board.done = True
                board.X = True
        if(board.board[0][0] == 'O' and board.board[1][1] == 'O' and board.board[2][2] == 'O'):
            board.done = True
            board.O = True
        if(board.board[0][2] == 'O' and board.board[1][1] == 'O' and board.board[2][0] == 'O'):
            board.done = True
            board.O = True
        if(board.board[0][0] == 'X' and board.board[1][1] == 'X' and board.board[2][2] == 'X'):
            board.done = True
            board.X = True
        if(board.board[0][2] == 'X' and board.board[1][1] == 'X' and board.board[2][0] == 'X'):
            board.done = True
            board.X = True
        return board

    def turnCycle(self, board):
        i = 0
        j = 0
        print("Player 1, enter the x-coordinate for the 'X' character: ")
        i = int(input())
        print("Player 1, enter the y-coordinate for the 'X' character: ")
        j = int(input())
        board.board[j][i] = 'X'
        self.printBoard(board)
        board = self.checkConditions(board)
        if(board.done == False):
            print("Great!\n\n")
            print("Player 2, enter the x-coordinate for the 'O' character: ")
            i = int(input())
            print("Player 2, enter the y-coordinate for the 'O' character: ")
            j = int(input())
            board.board[j][i] = 'O'
            self.printBoard(board)
            board = self.checkConditions(board)
        return board

    def main(self):
        print("Welcome to TicTacToe! Here's the Board: \n\n")
        board = self.setupBoard()
        board.done = False
        board.O = False
        board.X = False

        i = 0
        while(board.done == False and i < 9):
            board = self.turnCycle(board)
            i += 1
        if(board.O == True):
            print("Player 1 Wins!\n")
        elif(board.X == True):
            print("Player 2 Wins!\n")
        else:
            print("It's a TIE!")
        return 0

    def run(self):
        self.master.mainloop()

    def quit(self):
        self.master.destroy()
        sys.exit(0)

my_gui = GUI()
while True:
    my_gui.run()
