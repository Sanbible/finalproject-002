from board import game_othello
import tkinter as tk
from tkinter import *
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def open_pvp():
    game_othello()

class window:
    def __init__(self,master):
        
        self.master=master
        self.root = tk.Tk()
        self.root.title("Othello")
        self.root.geometry("1000x600")
        
        self.left_frame = tk.Frame(master)
        self.left_frame.pack(side=LEFT, fill="pink")
        
        self.right_frame = tk.Frame(master)
        self.right_frame.pack(side=RIGHT)



        self.label = tk.Label(self.left_frame, text="WELCOME TO OTHELLO", fg = 'Black', font=('Comic Sans MS', 18))
        self.label.grid(row=5, column=2, pady=5, padx=5, sticky=tk.NS)
        self.label = tk.Label(self.left_frame, text="GAME MODE", fg = 'Black', font=('Comic Sans MS', 14))
        self.label.grid(row=10, column=2, pady=5, padx=5, sticky=tk.NS)
        
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        self.pvp_button = customtkinter.CTkButton(self.left_frame, text="PvP", font=('Comic Sans MS', 20),command=open_pvp)
        self.pvp_button.grid(row=15, column=2, padx=5, pady=20)
        
        customtkinter.set_default_color_theme("green")
        self.pva_button = customtkinter.CTkButton(self.left_frame, text="PvA", font=('Comic Sans MS', 20) )
        self.pva_button.grid(row=20, column=2, padx=20, pady=5)
        
        self.root.mainloop()
    
window(master)