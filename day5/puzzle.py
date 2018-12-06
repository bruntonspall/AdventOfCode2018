def parse(lines):
    return list(lines)


def has_pair(str):
    for i in range(len(str)-1):
        l = str[i].lower(), str[i+1].lower()
        if l[0] == l[1]:
            if (str[i].isupper() and str[i+1].islower()) or (str[i+1].isupper() and str[i].islower()):
                return i+1
    return 0


def do_reduce(str):
    i = has_pair(str)
    if not i:
        return str
    return str[:i-1]+str[i+1:]


def solve(data):
    while True:
        new = do_reduce(data)
        if new == data:
            return new
        data = new
