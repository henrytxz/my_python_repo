from design_programs.search_problems import Search

class GenerateParentheses(Search):
    def __init__(self, total_pair_parentheses):
        self.n = total_pair_parentheses
        self.result = []

    def get_neighboring_good_states(self, curr_state):
        """
        state will be represented by a tuple (string_so_far, open, close)
         open is the number of open parentheses in the current state
         close is the number of close parentheses in the current state
        """
        string, open, close = curr_state
        if open == self.n and close == self.n:
            self.result.append(string)
            return []
        if open == close:
            return [ (string+'(', open+1, close) ]
        elif open > close:
            new_states = []
            if open < self.n:
                new_states.append( (string+'(', open+1, close) )
            new_states.append( (string+')', open, close+1) )
            return new_states


def test1(starting_state, debug=False):
    instance = GenerateParentheses(1)
    instance.bfs(starting_state)
    if debug:
        print instance.result
    assert len(instance.result) == 1
    assert instance.result[0] == '()'

def test2(starting_state, debug=False):
    instance = GenerateParentheses(2)
    instance.bfs(starting_state)
    if debug:
        print instance.result
    assert len(instance.result) == 2
    assert instance.result[0] == '(())'
    assert instance.result[1] == '()()'

def test3(starting_state, debug=False):
    instance = GenerateParentheses(3)
    instance.bfs(starting_state)
    assert len(instance.result) == 5
    if debug:
        print instance.result
    assert instance.result[0] == '((()))'
    assert instance.result[1] == '(()())'
    assert instance.result[2] == '(())()'
    assert instance.result[3] == '()(())'
    assert instance.result[4] == '()()()'


if __name__ == '__main__':
    starting_state = ('(', 1,0)
    test1(starting_state)
    test2(starting_state)
    test3(starting_state, True)