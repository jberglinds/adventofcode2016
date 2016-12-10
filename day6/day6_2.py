import collections

inputForIndex = ['']*8

with open('day6.input', 'r') as f:
    for line in f:
        for i in range(0,8):
            inputForIndex[i] += line[i]
            freqForIndex = [collections.Counter(x) for x in inputForIndex]

    topForIndex = [sorted(x.items(), key=lambda x: (x[1],x[0]))[0] for x in freqForIndex]
    print(''.join([x[0] for x in topForIndex]))
