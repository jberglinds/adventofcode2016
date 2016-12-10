current = 5

A = 10
B = 11
C = 12
D = 13

keypad = {
    #   U D L R
    1: [1,3,1,1],
    2: [2,6,2,3],
    3: [1,7,2,4],
    4: [4,8,3,4],
    5: [5,5,5,6],
    6: [2,A,5,7],
    7: [3,B,6,8],
    8: [4,C,7,9],
    9: [9,9,8,9],
    A: [6,A,A,B],
    B: [7,D,A,C],
    C: [8,C,B,C],
    D: [B,D,D,D]
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
    if current < 10:
        print(current, end="")
    else: #ABCD
        print(chr(55+current), end="")

f.close()
