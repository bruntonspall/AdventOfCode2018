def solve(data):
    while True:
        old = len(data)
        for c in "abcdefghijkklmnopqrstuvwxyz":
            data = data.replace(c+c.upper(), "").replace(c.upper()+c, "")
        if len(data) == old:
            return data
