length = 0

with open('day9.input', 'r') as f:
    while True:
        char = f.read(1)

        # End of file
        if not char:
            break

        if char == '(':
            marker = []

            while True:
                char = f.read(1)

                # End of marker
                if char == ')':
                    break

                marker.append(char)

            markerSections = ''.join(marker).split('x')
            length += int(markerSections[0])*int(markerSections[1])

            f.seek(f.tell()+int(markerSections[0]))
        else:
            length += 1

print(length-1)
