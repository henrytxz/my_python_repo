class Factorial(object):
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if not isinstance(n, int):
            return 'Factorial expects a non-negative integer argument'
        if n < 0:
            return 'Factorial expects a non-negative integer argument, got {}'\
                .format(n)
        if n not in self.cache:
            if n == 0:
                return 1
            else:
                self.cache[n] = n * self.__call__(n-1)
        return self.cache[n]

fact = Factorial()

for i in xrange(6):
    print '{}! yields {}'.format(i, fact(i))
