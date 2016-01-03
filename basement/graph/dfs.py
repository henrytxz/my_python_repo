from node import Node

class Graph:
    def __init__(self, list_of_nodes):
        self.visited = set()
        self.nodes = list_of_nodes
        # self.add_nodes([a,b,c,d,e])

    # def add_nodes(self, list_of_nodes):
    #     self.nodes.extend(list_of_nodes)

    def dfs(self, begin):
        print 'visiting %s' %begin
        self.visited.add(begin)
        for n in begin.get_adj():
            if n not in self.visited:
                self.dfs(n)

if __name__ == '__main__':
    print 'depth first search!'
    [a,b,c,d,e] = [Node(x) for x in 'abcde']
    a.add_adj([b,d,e])
    b.add_adj([a,c])
    c.add_adj([b,d,e])
    d.add_adj([a,c])
    e.add_adj([a,c])
    g = Graph([a,b,c,d,e])
    g.dfs(a)
