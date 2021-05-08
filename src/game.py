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
import random

from src.formatting import *
from src.gameover import GameOver


class Game(GameOver):
    def commands(self, opts):
        # Generate pseudo-random numbers for the heal and damage points.
        heal = random.randrange(1, 10)
        dmg_punch = random.randrange(1, 5)
        dmg_kick = random.randrange(1, 10)
        
        
        # This will keep on running if the conditions are true.
        while self.h_player1 > 0 and self.h_player2 > 0:
            if self.turn == 1:
                if opts == 'PUNCH':
                    self.h_player2 = self.h_player2 - dmg_punch
                    
                    self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn + 1))
                    self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                    self.l_event.config(text = 'GAIUS OCTAVIUS DEALT {} DAMAGE!\nNEXT TURN: MARCUS ANTONIUS'.format(dmg_punch))
                    
                if opts == 'KICK':
                    self.h_player2 = self.h_player2 - dmg_kick
                    
                    self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn + 1))
                    self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                    self.l_event.config(text = 'GAIUS OCTAVIUS DEALT {} DAMAGE!\nNEXT TURN: MARCUS ANTONIUS'.format(dmg_kick))
                    
                if opts == 'HEAL':
                    if self.h_player1 < 100:
                        self.h_player1 = self.h_player1 + heal
                        
                        self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn + 1))
                        self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                        self.l_event.config(text = 'GAIUS OCTAVIUS RECOVERED {} HP!\nNEXT TURN: MARCUS ANTONIUS'.format(heal))
                    else:
                        self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn + 1))
                        self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                        self.l_event.config(text = 'GAIUS OCTAVIUS\'S HP IS FULL!\nNEXT TURN: MARCUS ANTONIUS'.format(heal))
                        
                if opts == 'SURRENDER':
                    self.frame.destroy(), self.w_player2()
                    
                self.turn = 2
                break
                
                
            if self.turn == 2:
                if opts == 'PUNCH':
                    self.h_player1 = self.h_player1 - dmg_punch
                    
                    self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn - 1))
                    self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                    self.l_event.config(text = 'MARCUS ANTONIUS DEALT {} DAMAGE!\nNEXT TURN: GAIUS OCTAVIUS'.format(dmg_punch))
                    
                if opts == 'KICK':
                    self.h_player1 = self.h_player1 - dmg_kick
                    
                    self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn - 1))
                    self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                    self.l_event.config(text = 'MARCUS ANTONIUS DEALT {} DAMAGE!\nNEXT TURN: GAIUS OCTAVIUS'.format(dmg_kick))
                    
                if opts == 'HEAL':
                    if self.h_player2 < 100:
                        self.h_player2 = self.h_player2 + heal
                        self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn - 1))
                        self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                        self.l_event.config(text = 'MARCUS ANTONIUS RECOVERED {} HP!\nNEXT TURN: GAIUS OCTAVIUS'.format(heal))
                    else:
                        self.l_turn.config(text = 'TURN:\nPLAYER {}'.format(self.turn - 1))
                        self.l_hp.config(text = '{} HP {}'.format(self.h_player1, self.h_player2))
                        self.l_event.config(text = 'MARCUS ANTONIUS\'S HP IS FULL!\nNEXT TURN: GAIUS OCTAVIUS'.format(heal))
                
                if opts == 'SURRENDER':
                    self.frame.destroy(), self.w_player1()
                
                self.turn = 1
                break
                
        # This will be called if the conditions in the `while` is False, i.e.,
        # `self.h_player1` and `self.h_player2` is equal or below zero (0).
        self.gameover()
            
            
    def game(self):
        # Players' initial health points.
        # Change these based on how long you want the game to last.
        self.h_player1 = 20
        self.h_player2 = 20
        
        
        # The main frame that contains the elements of the game.
        self.frame = tk.Frame(self.root, width = 640, height = 400, border = 15, bg = BLACK)
        self.frame.pack(fill = 'both')
        
        
        # Display the events during the game.
        # Events includes the health damage that a player has dealt, the
        # health points that a player has recovered, and who turns next.
        self.f_event = tk.LabelFrame(self.frame, text = 'EVENT:', font = BOLD,
            fg = WHITE, bg = BLACK, height = 50, width = 640, borderwidth = 1,
            highlightthickness = 10, highlightbackground = BLACK, relief = tk.FLAT)
        self.f_event.pack(side = tk.BOTTOM, fill = 'both')
        
        self.l_event = tk.Label(self.f_event, bg = BLACK, fg = WHITE,
            font = FONT, text = 'WELCOME TO \'XXXII\'\n(EVENTS WILL APPEAR HERE)')
        self.l_event.pack()
        
        
        # Buttons
        # To save lines of codes, I stored their text values in a list named
        # `options`, made a `for` loop, and iterate the list.
        # Then I configured the command actions for each buttons.
        f_buttons = tk.Frame(self.frame, bg = BLACK, width = 640)
        f_buttons.pack(side = tk.BOTTOM, fill = 'both')
        
        options = ['PUNCH', 'KICK', 'HEAL', 'SURRENDER']
        
        for opts in options:
            buttons = tk.Button(f_buttons, text = opts, font = FONT,
                fg = WHITE, bg = BLACK, activeforeground = WHITE,
                activebackground = RED, width = 10, bd = 0,
                highlightthickness = 1, highlightbackground = RED)
            action = lambda opts = opts: self.commands(opts)
            buttons.configure(command = action)
            buttons.pack(side = tk. LEFT, padx = 5, fill = 'both', expand = 'yes')
        
        
        # Player one
        # This displays the first player's avatar and name.
        f_player1 = tk.Frame(self.frame, bg = BLACK, width = 200, height = 200)
        f_player1.pack(side = tk.LEFT)
        
        l_player1 = tk.Label(f_player1, text = 'PLAYER 1', font = FONT,
            fg = WHITE, bg = BLACK).pack()
            
        self.a_player1 = tk.PhotoImage(file = 'res/player_1.png')
        Label = tk.Label(f_player1, image = self.a_player1, highlightthickness = 2,
            highlightbackground = WHITE, bd = 0)
        Label.pack()
        
        n_player1 = tk.Label(f_player1, text = 'GAIUS OCTAVIUS ', font = BITALIC,
            fg = WHITE, bg = BLACK).pack(side = tk.BOTTOM)
        
        
        # Display the players' HP count and turn.
        self.f_stats = tk.Frame(self.frame, bg = BLACK, width = 200, height = 400)
        self.f_stats.place(in_= self.frame, anchor = C, relx = 0.5, rely = 0.230)
        
        # Turn count.
        self.turn = 1
        self.l_turn = tk.Label(self.f_stats, text = 'TURN:\nPLAYER {}'.format(self.turn), font = BOLD,
            fg = WHITE, bg = BLACK)
        self.l_turn.pack()
            
        # Display the players' health points.
        self.l_hp = tk.Label(self.f_stats, bg = BLACK, fg = WHITE, font = BOLD,
            text = '{} HP {}'.format(self.h_player1, self.h_player2))
        self.l_hp.pack()
        
        # Display the 'VS' (versus) sign.
        l_vs = tk.Label(self.f_stats, bg = BLACK, text = 'VS',
            font = VS, fg = WHITE).pack(side = tk.BOTTOM)
        
        
        # Player two
        # This displays the first player's avatar and name.
        f_player2 = tk.Frame(self.frame, bg = BLACK, width = 200, height = 250)
        f_player2.pack(side = tk.RIGHT)
        
        l_player2 = tk.Label(f_player2, text = 'PLAYER 2', font = ('Silver', 15),
            fg = WHITE, bg = BLACK).pack()
            
        self.a_player2 = tk.PhotoImage(file = 'res/player_2.png')
        Label = tk.Label(f_player2, image = self.a_player2, highlightthickness = 2,
            highlightbackground = WHITE, bd = 0)
        Label.pack()
        
        n_player2 = tk.Label(f_player2, text = 'MARCUS ANTONIUS', font = BITALIC,
            fg = WHITE, bg = BLACK).pack(side = tk.BOTTOM)