#!/usr/bin/env python3
#
#
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


import argparse
from src.formatting import *
from src.main import Main


if __name__ == '__main__':
    # Using the `argparse` library, I added command line options to the game.
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-a', '--author', action = 'store_true', help = 'show author')
    parser.add_argument('-v', '--version', action = 'store_true', help = 'show version')
    parser.add_argument('-l', '--license', action = 'store_true', help = 'show license')
    parser.add_argument('-V', '--Verbose', action = 'store_true', help = 'show verbose')
    
    args = parser.parse_args()
    
    if args.author:
        print('Made by Clint E. <https://github.com/clieg> | BSIT - 1R1')
    elif args.version:
        print('Version 0.0.1')
    elif args.license:
        print('This program is provided under the GPL-3.0 License. See LICENSE for more details.')
    elif args.Verbose:
        print('Disk Version [September 27, 1986]\nHow many files (0-15)?\nNEC PC-8001 BASIC Version 2.8\nPublished by Clint\n56810 Bytes free\nOk')
    else:
        Main()