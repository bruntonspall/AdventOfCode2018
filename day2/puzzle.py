import collections


def parse(lines):
    return lines


def count_boxids(boxid):
    twos = 0
    threes = 0
    counter = collections.Counter(boxid)
    for k in counter:
        if counter[k] == 2:
            twos = 1
        if counter[k] == 3:
            threes = 1
    return twos, threes


def checksum(list_of_factors):
    total = reduce(lambda a, b: (a[0]+b[0], a[1]+b[1]), list_of_factors)
    return total[0]*total[1]


def solve(data):
    return checksum([count_boxids(x) for x in data])
