def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def find_closest_point(points, target):
    min = 99999
    closest = None
    for i, point in enumerate(points):
        dist = distance(target, point)
        # print "From ", target, " to ", point, " is ", dist
        if dist == min:
            # print "Equal to existing minimum"
            closest = None
        if dist < min:
            # print "New minimum"
            min = dist
            closest = i
    # print "Closest point to ",target," is point ",closest," ",points.get(closest, "None")
    return closest


def draw(points):
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    maxx = max([p[0] for p in points])
    maxy = max([p[1] for p in points])
    print "************"
    for y in range(maxy+1):
        line = ""
        for x in range(maxx+1):
            point = find_closest_point(points, (x, y))
            if (x, y) in points:
                line += BOLD+RED
            if point is None:
                line += "."
            else:
                line += str(point)
            if (x, y) in points:
                line += ENDC
        print line
    print "************"



def find_valid_points(points):
    valid = {}
    for i, _ in enumerate(points):
        valid[i] = True
    maxx = max([p[0] for p in points])
    maxy = max([p[1] for p in points])
    for x in range(maxx):
        point = find_closest_point(points, (x, 0))
        if point != None:
            valid[point] = False
        point = find_closest_point(points, (x, maxy))
        if point != None:
            valid[point] = False
    for y in range(maxy):
        point = find_closest_point(points, (0, y))
        if point != None:
            valid[point] = False
        point = find_closest_point(points, (maxx, y))
        if point != None:
            valid[point] = False
    return valid


def count(points):
    valid = find_valid_points(points)
    count = {}
    maxx = max([p[0] for p in points])
    maxy = max([p[1] for p in points])
    for y in range(maxy+1):
        for x in range(maxx+1):
            point = find_closest_point(points, (x, y))
            if point is not None and valid[point]:
                count[point] = count.get(point, 0) + 1
    return count


def parse(lines):
    ans = []
    for line in lines:
        x, y = line.split(",")
        ans.append((int(x.strip()), int(y.strip())))
    return ans


def solve(data):
    counts = count(data)
    return max(counts.values())
