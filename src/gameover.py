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


class GameOver():
    def gameover(self):
        if self.h_player1 <= 0 or self.h_player2 <= 0:
            if self.h_player1 > self.h_player2:
                self.frame.destroy(), self.w_player1()
            elif self.h_player2 > self.h_player1:
                self.frame.destroy(), self.w_player2()
                
                
    def commands_over(self, opts):
        if opts == 'PLAY AGAIN':
            self.frame.destroy(), self.main_menu()
        else:
            self.root.destroy()
            
            
    def w_player1(self):
        self.frame = tk.Frame(self.root, bg= BLACK, width = 540, height = 360)
        self.frame.pack()
        
        f_menu = tk.Frame(self.frame, width=100, bg = BLACK, bd = 10)
        f_menu.pack(side = tk.BOTTOM, fill = 'both')
        
        options = ['PLAY AGAIN', 'EXIT']
        
        for opts in options:
            buttons = tk.Button(f_menu, text = opts, font = FONT,
                fg = WHITE, bg = BLACK, activeforeground = WHITE,
                activebackground = RED, width = 10, bd = 0,
                highlightthickness = 1, highlightbackground = RED)
            action = lambda opts = opts: self.commands_over(opts)
            buttons.configure(command = action)
            buttons.pack(side = tk. LEFT, padx = 5, fill = 'both', expand = 'yes')
            
        self.i_wplayer1 = tk.PhotoImage(file = 'res/w_player1.png')
        l_cover = tk.Label(self.frame, image = self.i_wplayer1, bd = 0)
        l_cover.pack()
        
        
    def w_player2(self):
        self.frame = tk.Frame(self.root, bg= BLACK, width = 540, height = 360)
        self.frame.pack()
        
        f_menu = tk.Frame(self.frame, width=100, bg = BLACK, bd = 10)
        f_menu.pack(side = tk.BOTTOM, fill = 'both')
        
        options = ['PLAY AGAIN', 'EXIT']
        
        for opts in options:
            buttons = tk.Button(f_menu, text = opts, font = FONT,
                fg = WHITE, bg = BLACK, activeforeground = WHITE,
                activebackground = RED, width = 10, bd = 0,
                highlightthickness = 1, highlightbackground = RED)
            action = lambda opts = opts: self.commands_over(opts)
            buttons.configure(command = action)
            buttons.pack(side = tk. LEFT, padx = 5, fill = 'both', expand = 'yes')
            
        self.i_wplayer2 = tk.PhotoImage(file = 'res/w_player2.png')
        l_cover = tk.Label(self.frame, image = self.i_wplayer2, bd = 0)
        l_cover.pack()