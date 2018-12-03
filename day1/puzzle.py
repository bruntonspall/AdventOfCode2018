def parse(lines):
    ans = []
    for line in lines:
        line = line.strip()
        line = line.replace('+', '')
        if line:
            ans.append(int(line))
    return ans


def solve(data):
    total = 0
    for num in data:
        total += num
    return total
