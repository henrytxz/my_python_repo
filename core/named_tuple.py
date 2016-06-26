from collections import namedtuple

State = namedtuple('State', 'p me you pending')
s = State(0, 15, 12, 2) # from Design of Computer Programs, play pig

assert s.p == 0
assert s.me == 15
assert s.you == 12
assert s.pending == 2

