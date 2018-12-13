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


def sum_node(node):
    if not node["children"]:
        return sum(node["metadata"])
    else:
        total = 0
        for i in node["metadata"]:
            if i <= len(node["children"]):
                total += sum_node(node["children"][i-1])
        return total


def solve(data):
    return sum_node(data)
