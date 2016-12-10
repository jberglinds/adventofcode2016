import hashlib

count = 0

def getHash(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

with open('day5.input', 'r') as f:
    for line in f:
        currentString = line[:-1] + str(count) # Get rid of string terminator and add first

        for i in range(0,8):
            count += 1
            currentString = (currentString[:-len(str(count-1))] + str(count))
            currentHash = getHash(currentString)
            while currentHash[0:5].count('0') != 5:
                currentString = (currentString[:-len(str(count-1))] + str(count))
                count += 1
                currentHash = getHash(currentString)
            print(currentHash[5], end="")
