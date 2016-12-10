count = 0

linecount = 0
current = []

f = open('day3.input', 'r')
for line in f:
    # Read 3 lines
    current.append(line.split())
    linecount = (linecount+1)%3
    # Then:
    if linecount == 0:
        # Transpose
        current = list(map(list, zip(*current)))
        for sides in current:
            # Same as part 1
            sides = [int(x) for x in sides]
            if ((sides[0]+sides[1] > sides[2]) and (sides[0]+sides[2] > sides[1]) and (sides[1]+sides[2] > sides[0])):
                count += 1
        current = []
f.close()

print(count)
