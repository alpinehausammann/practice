#!/usr/bin/python

#curses_menu.py
import curses, time
from main import *

def menu_gen(menu_items):
    vertical_location = dims[0]//2
    graphics = [0] * len(menu_items)
    graphics[option] = curses.A_REVERSE
    menu_dict = {}

    for item in menu_items:
        menu_dict[item] = screen.addstr(vertical_location, (dims[1]-len(item))//2, item, graphics[menu_items.index(item)])
        vertical_location += 1

    return menu_dict

def menu():
    global option

    screen.nodelay(0)
    screen.clear()
    title = "MAIN MENU"
    selection = -1



    while selection < 0:
        screen.addstr(0, (dims[1]-len(title))//2, title)
        menu_gen(menu_items)
        action = screen.getch()

        if action == curses.KEY_DOWN:
            option = (option +1) % len(menu_items)

        elif action == curses.KEY_UP:
            option = (option -1) % len(menu_items)

        elif action == curses.KEY_RIGHT:
            return menu_items[option]


def menu_choice(choice):
    if choice.lower() == "start":
        screen.nodelay(0)
        screen.clear()

        # return screen.addstr(dims[0]//2, dims[1]//2, option)
#connect menu highlight to functions

if __name__ == "__main__":
    selection = menu()
    screen.addstr(selection)
    screen.refresh()
    menu_choice(selection)

    #end of file
    curses.endwin()
