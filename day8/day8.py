import re

xMax = 6
yMax = 50
display = [[False for y in range(yMax)] for x in range(xMax)]

def rotateRow(row, amount):
    for i in range(amount):
        temp = display[row][yMax-1]
        for y in range(yMax-1, 0, -1):
            display[row][y] = display[row][(y-1)%yMax]
        display[row][0] = temp

def rotateColumn(column, amount):
    for i in range(amount):
        temp = display[xMax-1][column]
        for x in range(xMax-1, 0, -1):
            display[x][column] = display[(x-1)%xMax][column]
        display[0][column] = temp

with open('day8.input', 'r') as f:
    for line in f:
        tokens = re.split(r'\sx\=|\sy\=|\sby\s|x|\s', line)
        op = tokens[0]

        if op == 'rect':
            for x in range(int(tokens[1])):
                for y in range(int(tokens[2])):
                    display[y][x] = True
        elif op == 'rotate':
            rc = tokens[1]
            if rc == 'column':
                rotateColumn(int(tokens[2]), int(tokens[3]))
            elif rc == 'row':
                rotateRow(int(tokens[2]), int(tokens[3]))

count = 0
for row in display:
    count += row.count(True)

print(count)
