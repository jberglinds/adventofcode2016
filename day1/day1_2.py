import sys

x = 0
y = 0

xSpeed = 0
ySpeed = 1

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

direction = NORTH

visited = [(0,0)]

f = open('day1.input', 'r')
for line in f:
    line = line.split(', ')
    for token in line:
        if (token[0] == 'R'):
            direction = (direction+1)%4
        elif (token[0] == 'L'):
            direction = (direction-1)%4
        distance = int(token[1:])

        if (direction == NORTH):
            xSpeed = 0
            ySpeed = 1
        elif (direction == EAST):
            xSpeed = 1
            ySpeed = 0
        elif (direction == SOUTH):
            xSpeed = 0
            ySpeed = -1
        elif (direction == WEST):
            xSpeed = -1
            ySpeed = 0

        newCoord = (x, y)
        for i in range(1, distance+1):
            newCoord = (x+(i*xSpeed), y+(i*ySpeed))
            if (newCoord in visited):
                print (abs(newCoord[0])+abs(newCoord[1]))
                sys.exit(0)
            else:
                visited.append(newCoord)

        x = newCoord[0]
        y = newCoord[1]
f.close()

print (abs(x)+abs(y))
