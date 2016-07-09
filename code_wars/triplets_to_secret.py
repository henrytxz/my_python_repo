from collections import defaultdict

def recoverSecret(triplets):
    G, nodes = build_graph(triplets)
    return build_str(G, list(nodes))

def build_graph(triplets):
    G = defaultdict(set)
    nodes = set()
    for triplet in triplets:
        a,b,c = triplet
        G[b].add(a)
        G[c].add(a)
        G[c].add(b)
        nodes.add(a)
        nodes.add(b)
        nodes.add(c)
    return G, nodes

def build_str(G, nodes):
    fs = []
    while nodes:
        if len(nodes)==1:
            fs.append(nodes[0])
            return ''.join(fs)
        s = find_sink(G, nodes[0], fs)
        fs.append(s)
        nodes.remove(s)

def find_sink(G, curr, fs):
    precedents = G[curr]
    for p in precedents:
        if p in fs:
            continue
        return find_sink(G, p, fs)
    return curr


if __name__ == '__main__':
    triplets = [
      ['e','g','l'],
      ['e','n','a'],
      ['n','g','a'],
      ['e','l','a']
    ]
    # print build_graph(triplets)
    assert recoverSecret(triplets) == 'engla'
