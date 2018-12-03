def parse(lines):
    ans = []
    for line in lines:
        if line:
            ans.append(int(line))
    return ans


def solve(data):
    found = set([0])
    total = 0
    while True:
        for num in data:
            total = total + num
            if total in found:
                return total
            else:
                found.add(total)
