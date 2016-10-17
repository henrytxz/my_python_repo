import itertools

count_it = itertools.count(1)
assert count_it.next() == 1
assert count_it.next() == 2
assert count_it.next() == 3
assert next(count_it) == 4
assert next(count_it) == 5

cycle_it = itertools.cycle('abc')
assert cycle_it.next() == 'a'
assert cycle_it.next() == 'b'
assert cycle_it.next() == 'c'
assert next(cycle_it) == 'a'

repeat_it = itertools.repeat(5)
for i in range(10):
    assert repeat_it.next() == 5

chain_it = itertools.chain('abc','def')
assert chain_it.next() == 'a'
assert chain_it.next() == 'b'
assert chain_it.next() == 'c'
assert chain_it.next() == 'd'
assert chain_it.next() == 'e'

# print [''.join(pair) for pair
#        in itertools.combinations_with_replacement('abc', 2)]

print [''.join(i) for i in itertools.product('abc', 'xy')]
