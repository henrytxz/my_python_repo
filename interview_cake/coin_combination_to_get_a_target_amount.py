from verbose_assert import verbose_assert
from copy import copy

def get_total(number_each_coin, coins):
    return sum([x*y for (x,y) in zip(number_each_coin, coins)])

def count(target, coins):
    result = 0
    target_states = set()
    seen_states = set() # precise definition of seen is "having been put on the queue before"
    n = len(coins)
    start = [0]*n

    q = [start]
    seen_states.add(tuple(start))

    while q:
        curr_state = q.pop(0)
        total = get_total(curr_state, coins)
        if total < target:
            for i in range(n):
                new_state = copy(curr_state)
                new_state[i] += 1
                if tuple(new_state) not in seen_states:
                    q.append(new_state)
                    seen_states.add(tuple(new_state))
        elif total == target:
            # print 'curr_state {}'.format(curr_state)
            curr_state = tuple(curr_state)
            if curr_state not in target_states:
                result += 1
                target_states.add(curr_state)

    return result


if __name__ == '__main__':
    verbose_assert(0, get_total([0,0], [1,2]))
    verbose_assert(3, get_total([1,1], [1,2]))
    verbose_assert(4, get_total([2,1], [1,2]))

    verbose_assert(4, count(4, [1,2,3]))
    verbose_assert(0, count(4, [5,10]))

    set_a = set()
    set_b = frozenset([1,2,3])
    set_a.add(set_b)