class Graph(object):
    """
    dfs works as follows
    at the beginning, s is the only node that's seen
    while we've not yet seen all the nodes
    visit the 1st unseen neighbor of u
    backtrack when all neighbors have been seen
    """

    def __init__(self, G):
        self.G = G
        self.seen = set()

    def dfs(self, s):
        print 'dfs on {0}'.format(s)
        self.seen.add(s)
        for v in self.G[s]:
            if v not in self.seen:
                self.dfs(v)

    def dfs_stack(self, s):
        self.seen.add(s)
        st = []
        st.append(s)
        while st:
            v = st.pop()
            print 'stack dfs on {0}'.format(v)
            for w in G[v]:
                if w not in self.seen:
                    self.seen.add(w)
                    st.append(w)

    def bfs(self, s):
        self.seen.add(s)
        q = [s]
        while q:
            v = q.pop(0)
            print 'bfs on {0}'.format(v)
            for w in G[v]:
                if w not in self.seen:
                    self.seen.add(w)
                    q.append(w)

        """
        the above is better than what I did earlier 9/21/2016
        q = [s]
        while q:
            v = q.pop(0)
            if v not in self.seen:
                print 'bfs on {0}'.format(v)
                self.seen.add(v)
                q.extend(G[v])
        """

if __name__ == '__main__':
    [a,b,c,d,e] = [x for x in 'abcde']
    G = {}
    G[a] = [b,d,e]
    G[b] = [a,c]
    G[c] = [b,d,e]
    G[d] = [a,c]
    G[e] = [a,c]
    # g = Graph(G)
    # g.dfs(a)

    g = Graph(G)
    g.dfs_stack(a)

    # g = Graph(G)
    # g.bfs(a)