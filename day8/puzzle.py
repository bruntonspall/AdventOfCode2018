def parse_node(data):
    children = []
    metadata = []
    childnum, _, s = data.partition(" ")
    metadatanum, _, s = s.partition(" ")
    for i in range(int(childnum)):
        child, s = parse_node(s)
        children.append(child)
    for i in range(int(metadatanum)):
        md, _, s = s.partition(" ")
        metadata.append(int(md))
    return {"metadata": metadata, "children": children}, s

def parse(data):
    ret, _ = parse_node(data)
    return ret


def solve(data):
    return sum(data["metadata"]) + sum([solve(child) for child in data["children"]])
