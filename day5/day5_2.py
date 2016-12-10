import hashlib

count = 0

result = [None]*8

def getHash(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

with open('day5.input', 'r') as f:
    for line in f:
        currentString = line[:-1] + str(count) # Get rid of string terminator and add first

        while None in result:
            count += 1
            currentString = (currentString[:-len(str(count-1))] + str(count))
            currentHash = getHash(currentString)
            while currentHash[0:5].count('0') != 5:
                currentString = (currentString[:-len(str(count-1))] + str(count))
                count += 1
                currentHash = getHash(currentString)
            pos = int(currentHash[5], 16)
            val = currentHash[6]
            if pos < 8 and result[pos] is None:
                result[pos] = val
        print(''.join(result))
