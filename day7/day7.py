import re

count = 0

def hasAbba(string):
    for i in range(0, len(string)-3):
        substr = string[i:i+4]
        if substr == ''.join(reversed(substr)):
            if substr.count(substr[0]) is not 4: # No same 4 chars
                return True
    return False

def tryList(list):
    for item in list:
        if hasAbba(item):
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

        if tryList(regular):
            if not tryList(hypernet):
                count += 1

print(count)
