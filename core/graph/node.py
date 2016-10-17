class Node:
    def __init__(self, key):
        self.key = key
        self.adj = []

    def add_adj(self, neighbors):
        self.adj.extend(neighbors)

    def get_adj(self):
        return self.adj

    def __str__(self):
        return self.key

if __name__ == '__main__':
    [a,b,c,d,e] = [Node(x) for x in 'abcde']
    a.add_adj([b,d,e])
    b.add_adj([a,c])
    c.add_adj([b,d,e])
    d.add_adj([a,c])
    e.add_adj([a,c])

    assert len(a.get_adj())==3

    for n in a.get_adj():
        print '%s is a neighbor of node a' %n
