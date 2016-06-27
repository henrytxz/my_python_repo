def recoverSecret(triplets):
    G = {'e':{},
         'g':set('en'),
         'l':set('eg'),
         'n':{'e'},
         'a':set('engl')}
    nodes = ['e','g','l','n','a']
    return build_str(G, nodes)

def find_sink(G, curr, fs):
    precedents = G[curr]
    for p in precedents:
        if p in fs:
            continue
        return find_sink(G, p, fs)
    return curr

def build_str(G, nodes):
    fs = []
    while nodes:
        if len(nodes)==1:
            fs.append(nodes[0])
            return ''.join(fs)
        s = find_sink(G, nodes[0], fs)
        fs.append(s)
        nodes.remove(s)

if __name__ == '__main__':
    triplets = [
      ['e','g','l'],
      ['e','n','a'],
      ['n','g','a'],
      ['e','l','a']
    ]

    print recoverSecret(triplets)
