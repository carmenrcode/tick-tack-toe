import random
def gameover(grid):
    if grid[0][0] == grid[0][1] == grid[0][2]:
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][0]

    if grid[0][0] == grid[1][0] == grid[2][0]:
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][1]
    if grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][2]

    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[1][1]
    if grid[2][0] == grid[1][1] == grid[0][2]:
        return grid[1][1]
def prettyprintgrid(grid):
    row = 0
    print "  0 1 2 "
    for line in grid:
        print row,
        row += 1
        for point in line:
            print point,
        print ""

grid = []

#this will constuct the grid
for i in range(0,3):
    grid.append(['.','.','.',])

#game loop
for j in range(0,5):
    prettyprintgrid(grid)
    while True:
        row = raw_input("Row: ")
        row = int(row)
        col = raw_input("Col: ")
        col = int(col)
        if grid[row][col] == '.':
            grid[row][col] = 'x'
            break
        else:
            print "Spot is already played!"
            grid

    if j == 4:
        break
    while True:
        randr = random.randint(0,2)
        randc = random.randint(0,2)
        if grid[randr][randc] == '.':
            grid[randr][randc] = 'O'
            break


keystroke = raw_input ("Press enter to exit")
