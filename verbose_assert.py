def verbose_assert(expected, actual):
    if expected != actual:
        print 'expected {} not equal to actual {}'.format(expected, actual)
    assert expected == actual
