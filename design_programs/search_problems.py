class Search(object):
    def bfs(self, start):
        frontier = [start]
        seen = set()
        while frontier:
            curr = frontier.pop(0)
            if curr not in seen:
                seen.add(curr)
                frontier.extend(self.get_neighboring_good_states(curr))

    def get_neighboring_good_states(self, curr_state):
        pass


