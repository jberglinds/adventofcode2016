length = 0

def readInScope(file, start, end, multiplier):
    global length

    file.seek(start)
    while file.tell() < end:
        char = file.read(1)

        if char == '(':
            marker = []
            while True:
                char = file.read(1)
                if char == ')':
                    # End of marker
                    break
                marker.append(char)
            markerSections = ''.join(marker).split('x')

            savedPos = file.tell()
            readInScope(file, savedPos, savedPos+int(markerSections[0]), multiplier*int(markerSections[1]))
            file.seek(savedPos+int(markerSections[0]))
        else:
            length += 1*multiplier

with open('day9.input', 'r') as f:
    f.seek(0, 2)
    size = f.tell()
    readInScope(f, 0, size-1, 1)

print(length)
