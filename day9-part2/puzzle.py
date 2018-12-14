from collections import deque

def create():
    return deque([0])


def insert(marbles, value):
    if value % 23 == 0 and value != 0:
        marbles.rotate(7)
        removed = marbles.pop()
        marbles.rotate(-1)
        return marbles, removed + value
    marbles.rotate(-1)
    marbles.append(value)
    return marbles, 0

def parse(lines):
    return None


def solve(players, points):
    players = [0 for i in range(players)]
    marbles = deque()
    for i in range(points):
        marbles, score = insert(marbles, i)
        players[i % len(players)] += score
    return max(players)
