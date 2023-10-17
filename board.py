import tkinter as tk
from tkinter import *
from tkinter import PhotoImage

#create board and main
class game_othello:

    def  __init__(self):
        self.root = tk.Tk()
        self.root.title("Othello")
        self.bg=PhotoImage(file="bg.png")
        self.tb=PhotoImage(file="blackbg.png")
        self.tw=PhotoImage(file="whitebg.png")
        self.ck=PhotoImage(file="mark.png")
        self.table = self.board()
        self.mark1()
        self.root.mainloop()
    
    def board(self):
        boardall = []
        for row0 in range(8):
            board = [] 
            for column0 in range(8):
                button = tk.Button(self.root, image=self.bg)
                board.append(button)
                button.grid(row=row0+1,column=column0+1)
            boardall.append(board)
            #chr = คาเรคเตอร์ โดยที่65 = A 
            Label(self.root ,text=chr(65+row0)).grid(row=0,column=row0+1)
            # ทำตัวเลขเรียน
            Label(self.root ,text=(row0+1)).grid(row=row0+1,column=0)
        return boardall

    #เปลี่ยนสีให้เป็นเริ่มต้น
    #ตำแหนง[1][2];1=row,2=column
    def mark1(self):
        self.table[3][3]["image"]=self.tb
        self.table[3][4]["image"]=self.tw
        self.table[4][3]["image"]=self.tw
        self.table[4][4]["image"]=self.tb
    

    # def check(self)
game_othello()
    

