import curses

curses.initscr()
dims = curses.newwin(100,100,50,50)
dims.addstr(50,50,"hi")
dims.refresh()
