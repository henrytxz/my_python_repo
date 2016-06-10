def count(combination_of_passengers):
    return combination_of_passengers.count('M'), \
           combination_of_passengers.count('C')

def generate_passengers(m, c):
    combinations = {'M','C','MC','MM','CC'}
    if m<2: combinations.remove('MM')
    if c<2: combinations.remove('CC')
    if m<1: combinations.remove('M', 'MC')
    if c<1: combinations.remove('C', 'MC')
    return combinations

def csuccessors(state):
    m1,c1,b1,m2,c2,b2 = state
    d = dict()
    if m1<c1 or m2<c2: return dict()
    if b1>0 and (m1>0 or c1>0):
        arrow = '->'
        combinations = generate_passengers(m1,c1)
        for c in combinations:
            mcount, ccount = count(c)
            d[(m1-mcount, c1-ccount, b1-1, m2+mcount, c2+ccount, b2+1)] = c+arrow
    if b2>0 and (m2>0 or c2>0):
        arrow = '<-'
        combinations = generate_passengers(m2,c2)
        for c in combinations:
            mcount, ccount = count(c)
            d[(m1+mcount, c1+ccount, b1+1, m2-mcount, c2-ccount, b2-1)] = arrow+c
    return d

def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                               (2, 1, 1, 3, 3, 0): '<-M',
                                               (3, 1, 1, 2, 3, 0): '<-MM',
                                               (1, 3, 1, 4, 1, 0): '<-CC',
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print test()