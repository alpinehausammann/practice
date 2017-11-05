#!/usr/bin/python

#curses_menu.py

import curses
import time

screen = curses.initscr()
dims = screen.getmaxyx()
screen.keypad(1)
option = 0
menu_items = ["START", "INSTRUCTIONS", "OPTIONS", "EXIT"]

def menu_gen(menu_items):
	vertical_location = dims[0]//2
	graphics = [0] * len(menu_items)
	graphics[option] = curses.A_REVERSE
	menu_dict = {}
	
	for item in menu_items:
		menu_dict[item] = screen.addstr( vertical_location, dims[1]//2-len(item), item, graphics[menu_items.index(item)])		
		vertical_location += 1
		
	return menu_dict
	
def menu():
	global option

	screen.nodelay(0)
	screen.clear()
	title = "MAIN MENU"
	selection = -1
	
	
	
	while selection < 0:	
		screen.addstr(0,dims[1]//2-len(title), title)
		
		menu_gen(menu_items)
		
		action = screen.getch()
		if action == curses.KEY_DOWN:
			option = (option +1) %len(menu_items)
	
		elif action == curses.KEY_UP:
			option = (option -1) %len(menu_items)
		
#Calls
menu()
#end of file
curses.endwin()
