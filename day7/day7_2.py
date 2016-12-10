import re

count = 0

def getAbas(string):
    abas = []
    for i in range(0, len(string)-2):
        substr = string[i:i+3]
        if substr == ''.join(reversed(substr)):
            if substr.count(substr[0]) is not 3: # No same 3 chars
                abas.append(substr)
    return abas

def getAbasOfList(list):
    abas = []
    for item in list:
        res = getAbas(item)
        if res:
            abas.extend(res)
    return abas

def checkForBabs(string, babs):
    for bab in babs:
        if bab in string:
            return True
    return False

def hasBabsInList(list, babs):
    for item in list:
        if checkForBabs(item, babs):
            return True
    return False

with open('day7.input', 'r') as f:
    for line in f:
        splitted = re.split(r'(\[|\])', line)

        hypernet = []
        regular = []

        hyper = False

        # Split in hypernet and regular and look for ABBAs separately
        for section in splitted:
            if section == '[' or section == ']':
                hyper = not hyper
            else:
                if hyper:
                    hypernet.append(section)
                else:
                    regular.append(section)

        abas = getAbasOfList(regular)
        babs = [''.join([aba[1],aba[0],aba[1]]) for aba in abas]
        if hasBabsInList(hypernet, babs):
            count += 1

print(count)
