import sys
import collections

target = 'northpole-object-storage'

def decrypt(letter, shiftValue):
    value = ord(letter)-97
    newValue = (value+shiftValue)%26
    return chr(newValue+97)

with open('day4.input', 'r') as f:
    for line in f:
        # Extract string
        string = line[:-8]

        # Split string into sections and extract shift
        data = string.split('-')
        shift = int(data[-1])

        decryptedWords = [''.join([decrypt(letter, shift) for letter in word]) for word in data[:-1]]
        if '-'.join(decryptedWords) == target:
            print(shift)
