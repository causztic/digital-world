import re


def binary_to_decimal(s):
    """parses a binary number as a string into a decimal integer."""
    val = 0
    for idx, item in enumerate(s[::-1]):
        i = int(item)
        if i:
            if idx == 0:
                val += 1
            else:
                val += 2**(idx)
    return val


def uncompressed(compressed_string):
    """takes a compressed string as input and outputs an uncompress string, 
    where each alphabetic character is preceded by a single digit indicating the number of times 
    that the character should be entered in the uncompress version of the string"""
    uncompressed_string = ""
    twos = re.findall('..', compressed_string)
    for num, letter in twos:
        uncompressed_string += letter * int(num)
    return uncompressed_string


def get_base_counts2(DNA):
    invalid = 'The input DNA string is invalid'
    d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in DNA:
        if i.islower():
            return invalid
        for item in ['A', 'T', 'C', 'G']:
            if i == item:
                d[item] += 1
                break
    return d

f = open('week6/constants.txt', 'r')


def get_fundamental_constants(file_item):
    """ takes a file object as an argument, reads and interprets the text in the file, and returns
the dictionary """
    constants = {}
    for line in file_item.readlines()[2:]:
        items = line.strip().split()
        constants[items[0]] = float(items[1])
    return constants

f = open('week6/scores.txt', 'r')
def process_scores(file_item):
    total = 0.0
    count = 0
    lines = file_item.readlines()
    file_item.seek(0)
    for line in lines:
        total += float(line)
        count += 1
    return total, total/count

def process_scores2(f):
    scores = f.readlines()
    scores = scores.strip()
    scores = scores.split()
    num = len(scores)
    total = 0
    for score in scores:
        total += float(score)
    ave = float(total) / num
    return total, ave

print process_scores(f)
print process_scores2(f)