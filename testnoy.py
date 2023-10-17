import tkinter as tk
window1=tk.Tk()
window1.title("Othello")
window1.geometry("800x500")


# Constants
GRID_SIZE = 8
CELL_SIZE = 50
MORE_SIZE = 20
CANVAS_SIZE = GRID_SIZE * CELL_SIZE + MORE_SIZE

# Initialize the board
board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
board[3][3] = 1
board[4][4] = 1 
board[3][4] = -1
board[4][3] = -1

title_row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
title_column = ['1', '2', '3', '4', '5', '6', '7', '8']

# Initialize the player (1 for white , -1 for black)
current_player = 1

class GAME_PLAY:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="gray79")
        self.canvas.pack(side="right",pady=10)
        for row in range(GRID_SIZE):
            self.canvas.create_text(row * CELL_SIZE + (MORE_SIZE + CELL_SIZE / 2), 10, text=f"{title_row[row]}")
            self.canvas.create_text(10, row * CELL_SIZE + (MORE_SIZE + CELL_SIZE / 2), text=f"{title_column[row]}")

    def draw_board(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1 = col * CELL_SIZE + MORE_SIZE
                y1 = row * CELL_SIZE + MORE_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="sea green", outline="black", width=2)

                if board[row][col] == 1:
                    self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="white")
                elif board[row][col] == -1:
                    self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="black")

    
    

    def is_valid_move(self,row, col):
        if board[row][col] != 0:
            return False
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if self.is_valid_direction(row, col, dr, dc):
                    return True
        return False

    def is_valid_direction(self,row, col, dr, dc):
        opponent = -current_player
        r, c = row + dr, col + dc
        if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE) or board[r][c] != opponent:
            return False
        r, c = r + dr, c + dc
        while 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            if board[r][c] == 0:
                return False
            elif board[r][c] == current_player:
                return True
            r, c = r + dr, c + dc
        return False

    def make_move(self,row, col):
        board[row][col] = current_player
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if self.is_valid_direction(row, col, dr, dc):
                    self.flip_direction(row, col, dr, dc)

    def flip_direction(self,row, col, dr, dc):
        r, c = row + dr, col + dc
        while board[r][c] == -current_player:
            board[r][c] = current_player
            r, c = r + dr, c + dc

    def toggle_player(self):
        global current_player
        current_player = -current_player

        if current_player == 1:
            print("Turn : white")
        else :
            print("Turn :  black")

    def make_guide_move(self):
        for r,c in self.find_index(board,current_player):
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr == 0 and dc == 0:
                        continue
                    row = r
                    col = c
                    
                    if self.is_valid_guid_move(row,col,dr,dc):
                        print(row,col)
                        row += dr
                        col += dc
                        while board[row][col] == -current_player:
                            row += dr
                            col += dc
                        # print(row,col)
                        FIXED_SIZE = 20
                        x1 = col * CELL_SIZE + MORE_SIZE
                        y1 = row * CELL_SIZE + MORE_SIZE
                        x2 = x1 + CELL_SIZE
                        y2 = y1 + CELL_SIZE
                        if current_player == 1:
                            self.canvas.create_oval(x1 + FIXED_SIZE, y1 + FIXED_SIZE, x2 - FIXED_SIZE, y2 - FIXED_SIZE, outline="white", width=2)
                        elif current_player == -1:
                            self.canvas.create_oval(x1 + FIXED_SIZE, y1 + FIXED_SIZE, x2 - FIXED_SIZE, y2 - FIXED_SIZE, outline="black", width=2)

    def is_valid_guid_move(self,r,c,dr,dc):
        # print(r,c,dr,dc)
        r += dr
        c += dc
        if not(0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            return False
        while board[r][c] == -current_player:
            r += dr
            c += dc
            if not(0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
                return False
        if board[r][c] == 0 and board[r-dr][c-dc] == -current_player:
            return True
        return False
    
    def find_index(self,all,need):
        import numpy as np
        arr = np.array(all)
        row,col = np.where(arr == need)
        return list(zip(row,col))
    
    def get_count(self, list, need):
        count = 0
        for i in list:
            count += i.count(need)
        return count

class pvp:
    def __init__(self,root):
        self.PVP=root
        self.CALL_GAME_PLAY = GAME_PLAY(self.PVP)
        self.CALL_GAME_PLAY.draw_board()
        self.CALL_GAME_PLAY.make_guide_move()
        self.CALL_GAME_PLAY.canvas.bind("<Button-1>", self.on_board_click)

    def on_board_click(self,event):
        row = (event.y - MORE_SIZE) // CELL_SIZE
        col = (event.x - MORE_SIZE) // CELL_SIZE
        # print(f"{row},{col}\t\t{event.x},{event.y}")
        if row < 0 or col < 0:
            return False
        if self.CALL_GAME_PLAY.is_valid_move(row, col):
            self.CALL_GAME_PLAY.make_move(row,col)
            self.CALL_GAME_PLAY.draw_board()
            self.CALL_GAME_PLAY.toggle_player()
            self.CALL_GAME_PLAY.make_guide_move()
    
    def restart(self):
        global board
        global current_player
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                board[row][col] = 0
        board[3][3] = 1
        board[4][4] = 1
        board[3][4] = -1
        board[4][3] = -1
        self.CALL_GAME_PLAY.draw_board()
        current_player = 1
        # current_player = -current_player
        self.CALL_GAME_PLAY.make_guide_move()

def menu1():
    window1.destroy()
        
    PVP = tk.Tk()
    PVP.geometry("800x500")
    pvp_game = pvp(PVP)
    def newgame():
        pvp_game.restart()
        
        print("new game")

    b_newgame = tk.Button(PVP,text="NEW GAME",bg="#292421",fg="white",font=10,relief=tk.RAISED,command=newgame)
    

    l_pointWhite = tk.Label(PVP, text=f"White : {pvp_game.CALL_GAME_PLAY.get_count(board, 1)}", font=20)
    l_pointBlack = tk.Label(PVP, text=f"Black : {pvp_game.CALL_GAME_PLAY.get_count(board, -1)}", font=20)
    # l_pointWhite.pack(anchor="nw",padx=10)
    # l_pointBlack.pack(anchor="nw",padx=10, pady=10)
    l_pointWhite.pack(side="bottom")
    l_pointBlack.pack(side="bottom")
    b_newgame.pack()
    PVP.mainloop()

l1=tk.Label(window1,text="Othello Game",font=("Helvetica", 40))
l1.pack()

b1=tk.Button(window1,text="player VS player",bg="#292421",fg="white",font=20,relief=tk.RAISED,command=menu1)
b1.pack()



window1.mainloop()

