"""
https://en.wikipedia.org/wiki/Subsequence
for example
a,b,d is a subseq of a,b,c,d,e,f
=> chars in the subseq don't have to be consecutive in order
"""

from core.decorators.timer import timed_call

class Subseqs(object):
    # @timed_call
    def subseqs(self):
        resulting_list = self.__subseqs()
        return [x for x in resulting_list if x]

    def __subseqs(self, beg=0):
        """
        Args:
            S: the string to find subsequences for

        Returns: a set that contains all subsequences of S
        """
        if beg == self.first_invalid_index:
            return ['']

        resulting_list = []
        solution_to_problem_size_n_minus_1 = self.__subseqs(beg+1)

        # the following line same effect as
        # resulting_list.extend(set([''+x for x in self.cache[(S, beg+1)] ]))
        # but faster. '' + a_str is still a_str
        resulting_list.extend(solution_to_problem_size_n_minus_1)
        resulting_list.extend([self.S[beg] + x for x in solution_to_problem_size_n_minus_1])
        return resulting_list

    def __call__(self, full_string):
        self.S = full_string
        self.first_invalid_index = len(self.S)
        return self.subseqs()

def tests():
    subseqs = Subseqs()
    assert subseqs('a') == ['a']
    assert sorted(subseqs('ab')) == ['a', 'ab', 'b']

    x = subseqs('abcdef')
    assert len(x) == 63  # 6 chars, 2**6 combinations - 1 (the '') so 63
    assert 'abd' in x

    assert subseqs('aa') == ['a', 'a', 'aa']

if __name__ == '__main__':
    tests()