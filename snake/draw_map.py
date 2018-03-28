#
import curses

from main import *

def draw_map(screen, dims):

     #sets boundrys
                      ##TODO create corrective validation to check for even or odd boundries (make even)

    for i in range(map_size[0]):
        screen.addstr(center[0] - (map_size[0]//2)+i, center[1]-map_size[1]//2,"#") ##draws right boundry
        screen.addstr(center[0] - (map_size[0]//2)+i, center[1]+map_size[1]//2,"#") ##draws left boundry

        for a in range(map_size[1]):
            screen.addstr(center[0] - (map_size[0]//2), center[1]-(map_size[1]//2)+1+a,"#") ##draws top boundry
            screen.addstr(center[0] + (map_size[0]//2)-1, center[1]-(map_size[1]//2)+a+1,"#") ##draws bottom boundry

class Snake:
    def __init__(self, position, body_len):
        self.position = position
        self.body_len = body_len
        head = "X"
        body = "0"

    def move_snake(self):
        for count, piece in enumerate(self.body_len):
            if count == 0:
                screen.addstr(piece[0],piece[1], head)
            else:
                screen.addstr(piece[0],piece[1], body)

        screen.refresh()





if __name__ == "__main__":
    while True:
        draw_snake(screen,dims)
        screen.border()
        screen.refresh()
