def parse(lines):
    goals = {}
    for line in lines:
        words = line.split()
        prereq = words[1]
        if prereq not in goals:
            goals[prereq] = set()
        goal = goals.get(words[7], set())
        goal.add(prereq)
        goals[words[7]] = goal
    return goals


def find_next(graph, done):
    minlen = 99999
    nextnode = None
    for node in graph:
        newlen = len(graph[node] - done)
        if newlen < minlen and node not in done:
            minlen = newlen
            nextnode = node
        if newlen == minlen and node < nextnode and node not in done:
            nextnode = node
    return nextnode

def traverse(graph):
    done = []
    next = find_next(graph, set())
    while next:
        done.append(next)
        next = find_next(graph, set(done))
    return done

def solve(data):
    return -1
