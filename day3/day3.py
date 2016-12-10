count = 0

f = open('day3.input', 'r')
for line in f:
    sides = line.split()
    sides = [int(x) for x in sides]
    if ((sides[0]+sides[1] > sides[2]) and (sides[0]+sides[2] > sides[1]) and (sides[1]+sides[2] > sides[0])):
        count += 1
f.close()

print(count)
