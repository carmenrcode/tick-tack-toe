import random

def prettyprintgrid(grid):
    row = 0
    print "  0 1 2 3 4"
    for line in grid:
        print row,
        row += 1
        for point in line:
            print point,
        print ""
        
def straightdistance(r1, c1, r2, c2):
    rdiff = r1 - r2
    cdiff = c1 - c2
    cdiff = abs(cdiff)

    if rdiff > cdiff:
        return rdiff
    else:
        return cdiff
    
grid = []

mugr = random.randint(0,4)
mugc = random.randint(0,4)

lives = 5

#this will constuct this grid
for i in range(0,5):
    grid.append(['.','.','.','.','.',])

#game loop
while lives > 0:
    prettyprintgrid(grid)
    print "lives:",lives

    row = raw_input("Row: ")
    row = int(row)
    col = raw_input("Col: ")
    col = int(col)

    if row == mugr and col == mugc:
        grid[row][col] = 'O'
        prettyprintgrid(grid)
        print "You won! You found the distgusting Mugwump!"
        break

    else:
        grid[row][col] = 'x'
        print "You hear a strange creature grunting 'mugwump mugwump'", straightdistance(row, col, mugr, mugc), "tiles away."
        lives -= 1

        if lives == 0:
            grid[mugr][mugc] = 'O'
            prettyprintgrid(grid)
            print "You lose! The mugwump continues to terrify!"
keystroke = raw_input ("Press enter to exit")
