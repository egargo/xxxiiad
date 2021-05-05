# XXXII
# Copyright (C) 2021, Clint <github.com/clieg>
#
# This file is part of XXXII
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import tkinter as tk
from src.formatting import *
from src.game import Game


class Main(Game):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(TITLE)
        self.root.resizable(0, 0)
        self.root.geometry(WH)
        self.root.config(bg = BLACK)
        
        self.root.after(250, lambda:(self.splash_screen()))
        self.root.after(5000, lambda:(self.f_splash.destroy(), self.main_menu()))
        
        self.root.mainloop()
        
        
    # Display splash screen for 5 seconds.
    def splash_screen(self):
        self.f_splash = tk.Frame(self.root, bg = BLACK, width = 640,
            height = 400)
        self.f_splash.pack()
        
        self.i_splash = tk.PhotoImage(file = 'res/splash.png')
        Label = tk.Label(self.f_splash, image = self.i_splash, bd = 0)
        Label.pack()
        
        
    # Command function for the buttons.
    def commands_main(self, opts):
        if opts == 'PLAY GAME':
            self.frame.destroy(), self.prologue()
        else:
            self.root.destroy()
            
            
    # Prologue
    def prologue(self):
        self.f_prologue = tk.Frame(self.root, bg= BLACK, width = 540, height = 360)
        self.f_prologue.pack()
        
        f_buttons = tk.Frame(self.f_prologue, width=100, bg = BLACK, bd = 10)
        f_buttons.pack(side = tk.BOTTOM, fill = 'both')
        
        buttons = tk.Button(f_buttons, text = 'START CAMPAIGN', font = FONT,
            fg = WHITE, bg = BLACK, activeforeground = WHITE,
            activebackground = RED, width = 10, bd = 0,
            highlightthickness = 1, highlightbackground = RED,
            command=lambda:(self.f_prologue.destroy(), self.game()))
        buttons.pack(side = tk. LEFT, padx = 5, fill = 'both', expand = 'yes')
            
        self.i_prologue = tk.PhotoImage(file = 'res/prologue.png')
        l_prologue = tk.Label(self.f_prologue, image = self.i_prologue, bd = 0)
        l_prologue.pack()
        
        
    # Main menu
    def main_menu(self):
        self.frame = tk.Frame(self.root, bg= BLACK, width = 540, height = 360)
        self.frame.pack()
        
        f_menu = tk.Frame(self.frame, width=100, bg = BLACK, bd = 10)
        f_menu.pack(side = tk.BOTTOM, fill = 'both')
        
        
        # To save lines of codes, I stored their text values in a list named
        # `options`, made a `for` loop, and iterate the list.
        # Then I configured the command actions for each buttons.
        # This logic applies to my entire program.
        options = ['PLAY GAME', 'EXIT']
        
        for opts in options:
            buttons = tk.Button(f_menu, text = opts, font = FONT,
                fg = WHITE, bg = BLACK, activeforeground = WHITE,
                activebackground = RED, width = 10, bd = 0,
                highlightthickness = 1, highlightbackground = RED)
            action = lambda opts = opts: self.commands_main(opts)
            buttons.configure(command = action)
            buttons.pack(side = tk. LEFT, padx = 5, fill = 'both', expand = 'yes')
            
        self.i_cover = tk.PhotoImage(file = 'res/cover.png')
        l_cover = tk.Label(self.frame, image = self.i_cover, bd = 0)
        l_cover.pack()