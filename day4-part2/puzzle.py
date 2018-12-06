# Data structure
# key: (1, 10, 31) -> Guard 1, on 31st of 10th,
# value: minutes asleep
from pprint import pprint
from collections import Counter


def asleep_at(data, id, day):
    retval = []
    for key in data:
        if key[0] == id and key[2] == day:
            retval.extend([x for x in range(key[3], key[3]+data[key])])
    return retval


def asleep_minutes(data):
    sleepchart = {}
    for key in data:
        if key[0] not in sleepchart:
            sleepchart[key[0]] = []
        sleepchart[key[0]].extend([x for x in range(key[3], key[3]+data[key])])
    return sleepchart


def most_asleep_minute(data):
    most = (0, 0)
    chart = asleep_minutes(data)
    for guard in chart:
        c = Counter(chart[guard]).most_common(1)[0][0]
        if c > most[1]:
            most = (guard, c)
    return most


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
    guard, minute = most_asleep_minute(data)
    print "Guard", guard, " was most asleep at minute", minute

    return guard * minute
