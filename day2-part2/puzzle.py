import collections


def parse(lines):
    return [line.strip() for line in lines]


def distance(a, b):
    count = 0
    for x in a:
        if x not in b:
            count += 1
    return count


def differs_by_one(a, b):
    count = 0
    for p in zip(a, b):
        if p[0] != p[1]:
            count += 1
        if count > 1:
            return False
    return count == 1


def sameletters(a, b):
    letters = []
    for p in zip(a, b):
        if p[0] == p[1]:
            letters.append(p[0])
    return "".join(letters)


def solve(data):
    for x in data:
        for y in data:
            if differs_by_one(x, y):
                print x, "\n", y
                return sameletters(x, y)
