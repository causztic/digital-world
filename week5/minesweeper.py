#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:15:50 2017

@author: yaojie
"""
import random
from copy import deepcopy

class Minesweeper:
    
    # just for readability
    WIN = True
    IS_A_BOMB = True
    NOT_A_BOMB = False
    
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def __init__(self, height, width, mines):
        """initializes the Minesweeper instance with a width, height, and the number of mines.
        Sets up a default game table, generates random mine locations and updates another table for the solution."""
        self.x = int(width)
        self.y = int(height)
        self.table_state = [['-' for i in xrange(0, self.x)] for j in xrange(0, self.y)]
        self.mine_locations = self.generate_mines(int(mines))
        self.final_table = self.generate_answer()

    @staticmethod
    def print_table(table):
        """prints the table, regardless whether it's a game state table or the answer table."""
        width = len(table[0])
        height = len(table)
        s = '\t'
        
        # print number headers along x-axis
        for i in range(0, width):
            s += str(i) + "\t"

        s += "\n"

        # print letters for y-axis, + the relevant values in each coordinate depending on table.
        for y in range(0, height):
            s += (Minesweeper.letters[y] + "\t")
            for x in range(0, width): 
                s += table[y][x] + "\t"
            s += "\n"
        
        # use tabbing to space them nicely
        print s.expandtabs(3)

    def generate_mines(self, number):
        """generate a list of viable coordinates for mines, and randomly choose them."""
        mine_locations = []
        available_places = [[j, i] for i in xrange(0, self.x) for j in xrange(0, self.y)]
        while number > 0:
            # the chosen coordinate for a mine is appended into the list and is 
            # removed from the list of choices to prevent duplicates.
            choice = random.choice(available_places)
            available_places.remove(choice)
            mine_locations.append(choice)
            number -= 1
        return mine_locations
    
    def generate_answer(self):
        ft = deepcopy(self.table_state)
        for x in range(0, self.x):
            for y in range(0, self.y):
                # get the number or mine with neighbours
                ft[y][x] = self.get_neighbour(y,x)
        return ft
    
    def get_neighbour(self, y, x):
        """populate answer table with numbers and mines"""
        if [y, x] in self.mine_locations:
            return "*"
        count = 0
        # (x-1, y-1), (x, y-1), (x+1, y-1), 
        #  (x-1, y),  (x, y),   (x+1, y),
        # (x-1, y+1), (x, y+1), (x+1, y+1) 
        for xe in range(x-1, x+2):
            for ye in range(y-1, y+2):
                if [ye, xe] in self.mine_locations:
                    count += 1
        return str(count)
    
    def open_neighbours(self, y, x):
        """Open neighbours if the current coordinates are 0 and neighbours are untouched. 
        Recursively opens if the neighbours are also 0."""
        
        # generate neighbours with positive indexes
        l = [[ye, xe] for xe in range(x-1,x+2) if xe >= 0 for ye in range(y-1, y+2) if ye >= 0]       
        for ye,xe in l:
            # if the indexes are out of the game table, skip
            if xe >= self.x or ye >= self.y:
                continue
            # if the current coordinates are still untouched, update their values
            if self.table_state[ye][xe] == '-':
                self.table_state[ye][xe] = self.final_table[ye][xe]
                # if the coordinate has a value of 0, recursively open it's neighbours.
                if self.final_table[ye][xe] == '0':
                    self.open_neighbours(ye,xe)
                
    def check_status(self):
        count = 0
        flag_count = 0
        for i in [item for sublist in self.table_state for item in sublist]:
            if i == '-':
                count += 1
            if i == '?':
                count += 1
                flag_count += 1
        print "%d tiles remaining. (%d flagged)" % (count - flag_count, flag_count)
        return count == len(self.mine_locations)
    
    def flag(self, y, x):
        """set a flag to the desired coordinates."""
        self.table_state[Minesweeper.letters.index(y)][x] = "?"
        Minesweeper.print_table(self.table_state)

    def tease_user(self,y, x):
        """come here when the coordinates do not have a bomb.
        update the table_state with the selected coordinate."""
        self.table_state[y][x] = self.final_table[y][x]

        # if there are no neighbouring 0s, open neighbours
        if self.table_state[y][x] == '0':
            self.open_neighbours(y,x)

        self.print_table(self.table_state)
        
    def show_answer_board(self):
        """prints the answer table with print_table."""
        Minesweeper.print_table(self.final_table)
    
    def open_tile(self, y, x):
        """opens a tile at the respective coordinates on the table_state list."""
        y = Minesweeper.letters.index(y)
        # Find the letter index and convert into a y-coordinate.
        # Checks if it is a mine
        if [y,x] in self.mine_locations:
            # explode
            self.show_answer_board()
            print "Boomz."
            return Minesweeper.IS_A_BOMB
        else:
            # strip(?)tease to the user (oh damn sexy numbers)
            self.tease_user(y,x)
            return Minesweeper.NOT_A_BOMB

# initialize options

print "Options: "
print "* = letter from A to P, # = number from 0 to 29"
print "Opening a tile: o*#"
print "Flag a tile:    f*#"
print "exit: exit"

height = raw_input("Height (1 to 26), defaults to 10: ") or 10
width  = raw_input("Width (1 to 100), defaults to 30: ") or 30
mines  = raw_input("Number of mines, defaults to 20: ") or 20

ms = Minesweeper(height, width, mines)
Minesweeper.print_table(ms.table_state)

# listen to commands by user.
while True:
    command = raw_input("Command: ")
    if command == "exit":
        break
    elif 'o' == command[0]:
        # open a tile
        # ms.open_tile checks whether it's a bomb
        if ms.open_tile(command[1], int(command[2:])) == Minesweeper.IS_A_BOMB:
            break
    elif 'f' == command[0]:
        ms.flag(command[1], int(command[2:]))
    if ms.check_status() == Minesweeper.WIN:
        print "You win!"
        break