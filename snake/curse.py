#!/usr/bin/python

import curses


stdscr = curses.initscr()
dim = stdscr.getmaxyx()

def menu():
	global stdscr
	global dim
	menu_items = ["MAIN MENU", "NEW FILE", "EDIT FILE", "MANAGE FILES", "EXIT"]
    
## Create display ##
    
	menu_location = 2
	stdscr.addstr(0,dim[1]//2-len(menu_items[0]), menu_items[0])
	stdscr.refresh()
	for i in range(len(menu_items)):
		while i <= len(menu_items)-1:
			stdscr.addstr(menu_location,dim[1]//2-len(menu_items[i]), menu_items[i])
			
			menu_location += 1
		

## Select list item ##
    #selection = 0 
    #if selection is "NEW FILE":
    #    new_file()
    #elif selection is "EDIT FILE":
    #    edit_file()
    #elif selection is "MANAGE FILES":
    #    manage_files()
    #elif selection is "EXIT":
     #   curses.endwin()
    
#def new_file():
    #null
#def edit_file():
 #   null
#def manage_files():
 #   null

menu()
curses.endwin()
