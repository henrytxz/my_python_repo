from math import pow
from verbose_assert import verbose_assert


def power(base, exponent):
    if exponent==0:
        return 1
    if exponent==1:
        return base
    if exponent<0:
        raise ValueError('not expecting negative exponent, '
                         'but got {}'.format(exponent))
    '''
    find power_of_2, y such that power_of_2 + y = e and power_of_2 is
    the last power of 2 <= the exponent

    the benefit is runtime complexity, rather than O(exponent) multiplications
    it will be O(log(exponent)^2) multiplications


    '''
    power_of_2 = 2
    result = base
    while power_of_2<=exponent:
        result *= result
        power_of_2 *= 2
    # after the while, power_of_2 > exponent,
    # divide by 2 to have power_of_2 just <= exponent
    power_of_2 /= 2
    y = exponent - power_of_2
    result *= power(base, y)
    return result

assert power(3, 0) == 1
assert power(5, 1) == 5
verbose_assert(expected=pow(2, 10), actual=power(2, 10))