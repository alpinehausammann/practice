import curses, time
# from draw_map import *
# from curses_menu import *


screen = curses.initscr()
dims = screen.getmaxyx()
center = ((dims[0]//2),(dims[1]//2))
screen.keypad(1)
option = 0
menu_items = ["START", "INSTRUCTIONS", "OPTIONS", "EXIT"]
map_size = (18, 36)
boundries = []

###############################################################################
# curses_menu
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
            selection = 1

    return menu_items[option]



def menu_choice(choice):
    if choice.lower() == "start":
        screen.nodelay(0)
        screen.clear()

        # return screen.addstr(dims[0]//2, dims[1]//2, option)
#connect menu highlight to functions

################################################################

#draw_map
# import curses
#
# from main import *

def draw_map(screen, dims):

     #sets boundrys
                      ##TODO create corrective validation to check for even or odd boundries (make even)
    for y in range(map_size[0]):
        screen.addstr(center[0] - (map_size[0]//2)+y, center[1]-map_size[1]//2,"#") ##draws right boundry
        screen.addstr(center[0] - (map_size[0]//2)+y, center[1]+map_size[1]//2,"#") ##draws left boundry
        boundries.append((center[0] - (map_size[0]//2)+y,center[1]-map_size[1]//2))
        boundries.append((center[0] - (map_size[0]//2)+y, center[1]+map_size[1]//2))



        for x in range(map_size[1]):
            screen.addstr(center[0] - (map_size[0]//2), center[1]-(map_size[1]//2) + 1 + x,"#") ##draws top boundry
            screen.addstr(center[0] + (map_size[0]//2)-1, center[1]-(map_size[1]//2) + 1 + x,"#") ##draws bottom boundry
            boundries.append((center[0] - (map_size[0]//2),center[1]-(map_size[1]//2) + 1 + x))
            boundries.append((center[0] + (map_size[0]//2)-1,center[1]-(map_size[1]//2) + 1 + x))
class Snake:
    def __init__(self):
        self.position = (center[0],center[1])
        self.body_len = 1
        self.head = "X"
        self.body = "0"

    def draw_snake(self,):
        screen.addnstr(self.position[0],self.position[1],self.head)
        screen.refresh()
        # for count, piece in enumerate(self.body_len):
        #     if count == 0:
        #         screen.addstr(piece[0],piece[1], head)
        #     else:
        #         screen.addstr(piece[0],piece[1], body)

    def move_snake(self):
        action = screen.getch()
        if action == curses.KEY_DOWN:
            self.position = (self.position[0] + 1,self.position[1])
        elif action == curses.KEY_UP:
            self.position = (self.position[0] - 1,self.position[1])
        elif action == curses.KEY_RIGHT:
            self.position = (self.position[0],self.position[1] + 1 )
        elif action == curses.KEY_LEFT:
            self.position = (self.position[0],self.position[1] - 1 )
        self.draw_snake()




################################################################################

def choices(selection, snake):
    screen.refresh()
    selection = selection.upper()
    if selection == "START":
        screen.clear()
        draw_map(screen,dims)
        while True:
            if snake.position in boundries:
                break
            else:
                snake.move_snake()
                screen.refresh()


    # elif selection == "options":
    # elif selection == "instructions":


def main():
    snake = Snake()
    curses.curs_set(0)
    selection = menu()
    choices(selection,snake)



main()
