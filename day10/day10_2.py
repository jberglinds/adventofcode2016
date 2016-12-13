import sys

instructions = {}
bots = {}
outputs = {}

with open('day10.input', 'r') as f:
    for line in f:
        splitted = line.split()
        if splitted[0] == 'value':
            botNumber = int(splitted[5])
            value = int(splitted[1])
            if botNumber in bots:
                bots[botNumber].append(value)
            else:
                bots[botNumber] = [value]
        else:
            botNumber = int(splitted[1])
            lowOutput = splitted[5] == 'output'
            lowNumber = int(splitted[6])
            highOutput = splitted[10] == 'output'
            highNumber = int(splitted[11])

            if botNumber not in bots:
                bots[botNumber] = []
            if lowOutput:
                if lowNumber not in outputs:
                    outputs[lowNumber] = []
            else:
                if lowNumber not in bots:
                    bots[lowNumber] = []
            if highOutput:
                if highNumber not in outputs:
                    outputs[highNumber] = []
            else:
                if highNumber not in bots:
                    bots[highNumber] = []

            instructions[botNumber] = [lowOutput, lowNumber, highOutput, highNumber]

anythingToDo = True
while anythingToDo:
    anythingToDo = False
    for bot, chips in bots.items():
        if len(chips) == 2 and bot in instructions:
            anythingToDo = True

            instruction = instructions[bot]
            minChip = min(chips[0], chips[1])
            maxChip = max(chips[0], chips[1])
            if instruction[0]:
                outputs[instruction[1]].append(minChip)
            else:
                bots[instruction[1]].append(minChip)
            if instruction[2]:
                outputs[instruction[3]].append(maxChip)
            else:
                bots[instruction[3]].append(maxChip)
            bots[bot] = []

print(outputs[0][0]*outputs[1][0]*outputs[2][0])
