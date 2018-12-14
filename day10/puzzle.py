from collections import defaultdict

def coord_at(t, c):
    return (c[0] + (c[2] * t), c[1] + (c[3] * t), c[2], c[3])


def parse(lines):
    coords = []
    for line in lines:
        line = line.replace("position=<", "").replace("> velocity=<", ", ").replace(">", "").split(",")
        coords.append((int(line[0]), int(line[1]), int(line[2]), int(line[3])))
    return coords


def render(coords, t):
    display = defaultdict()
    minx, miny = 9999, 99999
    maxx, maxy = 0, 0
    for c in coords:
        dx, dy, _, _ = coord_at(t, c)
        maxx, maxy = max(maxx, dx), max(maxy, dy)
        minx, miny = min(minx, dx), min(miny, dy)
        display[(dx, dy)] = True
    r = ""
    for y in range(miny, maxy+1):
        l = []
        for x in range(minx, maxx+1):
            if display.get((x, y), False):
                l.append("#")
            else:
                l.append(".")
        r += "".join(l) + "\n"
    return r

def find_height(coords, t):
    miny = 99999
    maxy = -99999
    for c in coords:
        dx, dy, _, _ = coord_at(t, c)
        maxy = max(maxy, dy)
        miny = min(miny, dy)
    return maxy - miny

def solve(data):
    size = 999999
    for t in range(50000):
        newsize = find_height(data, t)
        if newsize > size:
            print "Got bigger at time ", t
            print render(data, t-1)
            return t
        else:
            size = newsize
