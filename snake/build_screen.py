#!/bin/bash/python

import curses


def build_screen():
    screen = curses.initscr()
    dims = screen.getmaxyx()
    screen.keypad(1)

    return screen, dims
