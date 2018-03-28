import os

counter = 3
grid = []
block = 0
def buildGrid(counter,grid):
    for r in range(10):
        for c in range(10):
            if r < counter and c < counter:
                block = 1
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))

            if r < counter and counter <= c < counter*2:
                block = 2
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))

            if r < counter and counter*2 <= c < counter*3:
                block = 3
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))


            if counter <= r < counter*2 and c < counter:
                block = 4
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))

            if counter <= r < counter*2 and counter <= c < counter*2:
                block = 5
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))

            if counter <= r < counter*2 and counter*2 <= c < counter *3:
                block = 6
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))
            if counter*2 <= r < counter*3 and c < counter:
                block = 7
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))
            if counter*2 <= r < counter*3 and counter <= c < counter *2:
                block = 8
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))
            if counter*2 <= r < counter*3 and counter*2 <= c < counter *3:
                block = 9
                grid.append(('blk-{}'.format(str(block)),'row-{}'.format(str(r+1)),'col-{}'.format(str(r+1))))

if __name__ =="__main__":
    buildGrid(counter, grid)
    os.remove('grid.txt')
    f = open('grid.txt','w')

    for i in grid:
        f.write(str(i)+"\n")
    f.close()
    print(grid)
