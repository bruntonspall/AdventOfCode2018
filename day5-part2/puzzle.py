def solve(data):
    min_length = len(data)+1
    for x in "abcdefghijkklmnopqrstuvwxyz":
        chain = data.replace(x, "").replace(x.upper(), "")
        while True:
            old = len(chain)
            for c in "abcdefghijkklmnopqrstuvwxyz":
                chain = chain.replace(c+c.upper(), "").replace(c.upper()+c, "")
            if len(chain) == old:
                if old < min_length:
                    min_length = old
                break
    return min_length
