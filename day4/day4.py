import sys
import collections

sectorSum = 0

with open('day4.input', 'r') as f:
    for line in f:
        # Split into string and checksum
        string = line[:-8]
        checksum = line[-7:-2]

        # Split string into sections and extract id
        data = string.split('-')
        id = data[-1]

        # All words without separator
        words = ''.join(data[:-1])
        # Count letter frequency
        counter = collections.Counter(words)

        # Sort on frequency and then by letter and take 5 first
        top = sorted(counter.items(), key=lambda x: (-x[1],x[0]), reverse=False)[:5]
        
        topString = ''.join([x[0] for x in top])
        if checksum == topString:
            sectorSum += int(id)

print(sectorSum)
