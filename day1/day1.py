x = 0
y = 0

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

direction = NORTH

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
            y += distance
        elif (direction == EAST):
            x += distance
        elif (direction == SOUTH):
            y -= distance
        elif (direction == WEST):
            x -= distance
f.close()

print (abs(x)+abs(y))
