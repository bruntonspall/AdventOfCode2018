# Data structure
# key: (1, 10, 31) -> Guard 1, on 31st of 10th,
# value: minutes asleep
from collections import Counter


def most_asleep_minute(data):
    c = Counter(data)
    return c.most_common(1)[0][0]


def parse(lines):
    data = []
    guardid = None
    starttime = None
    for line in sorted(lines):
        if line.find("begins shift") != -1:
            guardid = int(line[26:].split(' ')[0])
        if line.find("falls asleep") != -1:
            starttime = int(line[15:17])
        if line.find("wakes up") != -1:
            endtime = int(line[15:17])
            for minute in range(starttime, endtime):
                data.append((guardid, minute))
    return data


def solve(data):
    guard, minute = most_asleep_minute(data)
    return guard * minute
