#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:15:50 2017

@author: yaojie
"""
import random
import sys
from copy import deepcopy

class Minesweeper(object):

    # just for readability
    WIN = True
    IS_A_BOMB = True
    NOT_A_BOMB = False
    
    # Unicode just to look pretty
    FLAG = u'\u2691'
    BOMB = u'\U0001F4A3'
    EXPLOSION = u'\U0001F4A5'

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, height, width, mines):
        """initializes the Minesweeper instance with a width, height, and the number of mines.
        Sets up a default game table, generates random mine locations and updates another table for the solution."""
        self.x = int(width)
        self.y = int(height)
        self.table_state = [
            ['-' for i in xrange(0, self.x)] for j in xrange(0, self.y)]
        self.mine_locations = self.generate_mines(int(mines))
        self.final_table = self.generate_answer()

    @staticmethod
    def print_table(table, exploded_at=[-1, -1]):
        """prints the table, regardless whether it's a game state table or the answer table."""

        # color codes just to look pretty
        NORMAL = '\33[10m'
        BLUE_START = '\33[104m'
        RED_START = '\33[31m'
        PURPLE_START = '\33[35m'
        GREEN_START = '\33[92m'
        ORANGE_START = '\33[93m'
        END = '\033[0m'
        s = '    %s' % BLUE_START

        # print number headers along x-axis
        for i in range(0, width):
            s += " %s" % i
            if i < 10:
                s += " " * 2
            else:
                s += " "

        s += "%s\n" % END
        # print letters for y-axis, + the relevant values in each coordinate
        # depending on table.
        for y in range(0, height):
            s += "%s %s %s \t" % (BLUE_START, Minesweeper.letters[y], END)
            for x in range(0, width):
                value = table[y][x]
                if value == "0":
                    s += "%s%s%s" % (NORMAL, value, END)
                elif value == "1":
                    s += "%s%s%s" % (GREEN_START, value, END)
                elif value == "2":
                    s += "%s%s%s" % (ORANGE_START, value, END)
                elif value == "3":
                    s += "%s%s%s" % (RED_START, value, END)
                elif value == "4" or value == "5" or value == "6" or value == "7" or value == "8":
                    s += "%s%s%s" % (PURPLE_START, value, END)
                # special
                elif value == "-":
                    s += "%s%s%s" % (NORMAL, value, END)
                elif value == Minesweeper.BOMB:
                    if y == exploded_at[0] and x == exploded_at[1]:
                        # Make the bomb at the casualty site explode!
                        s += "%s%s%s" % (RED_START, Minesweeper.EXPLOSION, END)
                    else:
                        # show normal bomb
                        s += "%s%s%s" % (RED_START, value, END)
                elif value == Minesweeper.FLAG:
                    s += "%s%s%s" % (RED_START, value, END)
                s += " " * 3
            s += "\n"

        # use tabbing to space them nicely
        print s.expandtabs(3)

    def generate_mines(self, number):
        """generate a list of viable coordinates for mines, and randomly choose them."""
        mine_locations = []
        available_places = [[j, i]
                            for i in xrange(0, self.x) for j in xrange(0, self.y)]
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
                ft[y][x] = self.get_neighbour(y, x)
        return ft

    def get_neighbour(self, y, x):
        """populate answer table with numbers and mines"""
        if [y, x] in self.mine_locations:
            return Minesweeper.BOMB
        count = 0
        # (x-1, y-1), (x, y-1), (x+1, y-1),
        #  (x-1, y),  (x, y),   (x+1, y),
        # (x-1, y+1), (x, y+1), (x+1, y+1)
        for xe in range(x - 1, x + 2):
            for ye in range(y - 1, y + 2):
                if [ye, xe] in self.mine_locations:
                    count += 1
        return str(count)

    def flags_nearby(self, y, x):
        """ gets number of flags nearby """
        count = 0
        l = [[ye, xe] for xe in range(
            x - 1, x + 2) if xe >= 0 for ye in range(y - 1, y + 2) if ye >= 0]
        for ye, xe in l:
            if xe >= self.x or ye >= self.y:
                continue
            if self.table_state[ye][xe] == Minesweeper.FLAG:
                count += 1
        return str(count)

    def special_open_neighbours(self, y, x):
        """Open neighbours if the flag number matches the count."""
        if self.table_state[y][x] != "-" and self.table_state[y][x] == self.flags_nearby(y, x):
            l = [[ye, xe] for xe in range(
                x - 1, x + 2) if xe >= 0 for ye in range(y - 1, y + 2) if ye >= 0]
            for ye, xe in l:
                if xe >= self.x or ye >= self.y:  # do not open out of bounds
                    continue
                # if it is a bomb but not flagged
                if self.final_table[ye][xe] == Minesweeper.BOMB and self.table_state[ye][xe] != Minesweeper.FLAG:
                    self.show_answer_board([ye, xe])
                    print "KABOOM!"
                    return Minesweeper.IS_A_BOMB
            self.open_neighbours(y, x)
        self.print_table(self.table_state)
        return Minesweeper.NOT_A_BOMB

    def open_neighbours(self, y, x):
        """Open neighbours if the current coordinates are 0 and neighbours are untouched.
        Recursively opens if the neighbours are also 0."""
        if [y, x] in self.mine_locations:
            return [y, x]
        # generate neighbours with positive indexes
        l = [[ye, xe] for xe in range(
            x - 1, x + 2) if xe >= 0 for ye in range(y - 1, y + 2) if ye >= 0]
        for ye, xe in l:
            # if the indexes are out of the game table, skip
            if xe >= self.x or ye >= self.y:
                continue
            # if the current coordinates are still untouched, update their values
            if self.table_state[ye][xe] == '-':
                self.table_state[ye][xe] = self.final_table[ye][xe]
                # if the coordinate has a value of 0, recursively open it's neighbours.
                if self.final_table[ye][xe] == '0':
                    self.open_neighbours(ye, xe)

    def check_status(self):
        count = 0
        flag_count = 0
        for i in [item for sublist in self.table_state for item in sublist]:
            if i == '-':
                count += 1
            if i == Minesweeper.FLAG:
                count += 1
                flag_count += 1
        print "%d tiles remaining. (%d flagged)" % (count - flag_count, flag_count)
        return count == len(self.mine_locations)

    def flag(self, y, x):
        """set a flag to the desired coordinates."""
        if self.table_state[y][x] == '-':
            self.table_state[y][x] = Minesweeper.FLAG
        Minesweeper.print_table(self.table_state)

    def tease_user(self, y, x):
        """come here when the coordinates do not have a bomb.
        update the table_state with the selected coordinate."""
        self.table_state[y][x] = self.final_table[y][x]

        # if there are no neighbouring 0s, open neighbours
        if self.table_state[y][x] == '0':
            self.open_neighbours(y, x)

        self.print_table(self.table_state)

    def show_answer_board(self, coords):
        """prints the answer table with print_table."""
        Minesweeper.print_table(self.final_table, coords)

    def open_tile(self, y, x):
        """opens a tile at the respective coordinates on the table_state list."""
        # Find the letter index and convert into a y-coordinate.
        # Checks if it is a mine
        if [y, x] in self.mine_locations:
            # explode
            self.show_answer_board([y, x])
            print "Boomz."
            return Minesweeper.IS_A_BOMB
        else:
            # strip(?)tease to the user (oh damn sexy numbers)
            self.tease_user(y, x)
            return Minesweeper.NOT_A_BOMB

# initialize options

print "Options: "
print "* = letter from A to P, # = number from 0 to 29"
print "Opening a tile: o*#"
print "Flag a tile:    f*#"
print "Left and right click a tile to open neighbouring tiles when the number matches the number of flags:   d*#"
print "exit: exit"

default_height = 15
default_width = 15
default_mines = 20
height = raw_input("Height (1 to 26), defaults to %d: " %
                   default_height) or default_height
width = raw_input("Width (1 to 26), defaults to %d: " %
                  default_width) or default_width
mines = raw_input("Number of mines, defaults to %d: " %
                  default_mines) or default_mines

print ''

ms = Minesweeper(height, width, mines)
Minesweeper.print_table(ms.table_state)

# listen to commands by user.
while True:
    command = raw_input("Command: ")
    try:
        if command == "exit":
            break
        elif 'd' == command[0]:
            # open neighbour of selected coordinate if flag count matches
            # number
            if ms.special_open_neighbours(Minesweeper.letters.index(command[1]), int(command[2:])) == Minesweeper.IS_A_BOMB:
                break
        elif 'o' == command[0]:
            # open a tile
            # ms.open_tile checks whether it's a bomb
            if ms.open_tile(Minesweeper.letters.index(command[1]), int(command[2:])) == Minesweeper.IS_A_BOMB:
                break
        elif 'f' == command[0]:
            ms.flag(Minesweeper.letters.index(command[1]), int(command[2:]))
        if ms.check_status() == Minesweeper.WIN:
            ms.show_answer_board([-1, -1])
            print "You win!"
            break
    except:
        print sys.exc_info()
        print "Whoops, try again!"
