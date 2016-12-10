current = 5

keypad = {
    #   U D L R
    1: [1,4,1,2],
    2: [2,5,1,3],
    3: [3,6,2,3],
    4: [1,7,4,5],
    5: [2,8,4,6],
    6: [3,9,5,6],
    7: [4,7,7,8],
    8: [5,8,7,9],
    9: [6,9,8,9],
}

f = open('day2.input', 'r')
for line in f:
    for move in line:
        if (move == 'U'):
            current = keypad[current][0]
        elif (move == 'D'):
            current = keypad[current][1]
        elif (move == 'L'):
            current = keypad[current][2]
        elif (move == 'R'):
            current = keypad[current][3]
    print(current, end="")
f.close()
