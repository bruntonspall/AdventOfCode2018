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


def find_next(graph, done, use=set()):
    minlen = 99999
    nextnode = None
    for node in graph:
        if node not in done and graph[node].issubset(done) and node not in use:
            return node
    return None


def traverse(graph, numworkers, duration):
    worker_times = [0 for i in range(numworkers)]
    worker_jobs = [None for i in range(numworkers)]
    done = []
    allocated = set()
    next = find_next(graph, set())
    t = 0
    while t < 10000:
        for i, time in enumerate(worker_times):
            if time < 1:
                print t, ": Worker ", i, " finished job ", worker_jobs[i]
                if worker_jobs[i]:
                    done.append(worker_jobs[i])
                next = find_next(graph, set(done), allocated)
                if next:
                    allocated.add(next)
                    print t, ": Worker ", i, " starts job ", next
                    worker_jobs[i] = next
                    worker_times[i] = ord(next)+duration-ord('A')
                else:
                    worker_jobs[i] = None
                if len(done) == len(graph):
                    return done, t
            else:
                worker_times[i] -= 1
        t += 1
        print t, allocated, done

def solve(data):
    return -1
