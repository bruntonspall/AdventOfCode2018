def insert(marbles, position, value):
    if marbles == []:
        return [0], 0, 0
    if value % 23 == 0:
        pos = (position - 8) % len(marbles) + 1
        val = value + marbles[pos]
        del marbles[pos]
        return marbles, pos, val
    pos = (position + 1) % len(marbles) + 1
    marbles.insert(pos, value)
    return marbles, pos, 0

def parse(lines):
    return None


def solve(players, points):
    players = [0 for i in range(players)]
    marbles = []
    pos = 0
    for i in range(points):
        marbles, pos, score = insert(marbles, pos, i)
        players[i % len(players)] += score
    return max(players)
