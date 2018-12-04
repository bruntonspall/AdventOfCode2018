def parse_line(line):
    d = {}
    id, addr = line.split(' @ ')
    coord, size = addr.split(': ')
    d['id'] = id
    d['x'], d['y'] = map(int, coord.split(','))
    d['width'], d['height'] = map(int, size.split('x'))
    print line, d
    return id, d


def parse(lines):
    data = {}
    for line in lines:
        i, d = parse_line(line.strip())
        data[i] = d
    return data


def apply(map, data):
    for cut in data:
        for x in range(cut['x'], cut['x']+cut['width']):
            for y in range(cut['y'], cut['y']+cut['height']):
                l = map.get((x, y), [])
                l.append(cut['id'])
                map[(x, y)] = l
    return map


def solve(data):
    map = {}
    map = apply(map, data)
    count = 0
    for k, v in map.items():
        if len(v) > 1:
            count += 1
    return count
