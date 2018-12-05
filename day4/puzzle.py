# Data structure
# key: (1, 10, 31) -> Guard 1, on 31st of 10th,
# value: minutes asleep
from pprint import pprint


def most_asleep(times):
    totals = {}
    for key, sleeptime in times.items():
        id, _, _, _ = key
        totals[id] = totals.get(id, 0) + sleeptime
    maxsleep = 0
    maxid = None
    for id, time in totals.items():
        if time > maxsleep:
            maxsleep = time
            maxid = id
    return maxid


def most_asleep_during(data, id):
    minute_asleep = {}
    max = [0, 0]
    for key in data:
        if key[0] == id:
            for x in range(key[3], key[3]+data[key]):
                minute_asleep[x] = minute_asleep.get(x, 0) + 1
    for x in minute_asleep:
        if minute_asleep[x] > max[1]:
            max[1] = minute_asleep[x]
            max[0] = x
    # pprint(minute_asleep)
    # pprint(max)
    return max[0]


def parse(lines):
    data = {}
    guardid = None
    starttime = None
    for line in sorted(lines):
        if line.find("begins shift") != -1:
            guardid = int(line[26:].split(' ')[0])
        if line.find("falls asleep") != -1:
            starttime = int(line[6:8]), int(line[9:11]), int(line[15:17])
        if line.find("wakes up") != -1:
            endtime = int(line[6:8]), int(line[9:11]), int(line[15:17])
            duration = endtime[2] - starttime[2]
            data[(guardid, starttime[0], starttime[1], starttime[2])] = duration
    return data


def solve(data):
    id = most_asleep(data)

    minute = most_asleep_during(data, id)
    print "Guard ", id, " was most asleep during minute", minute

    return id * minute
