from time import time

def timed_call(f):
    def timed_f(*args):
        begin = time()
        output = f(*args)
        print 'took {0:.3f} seconds'.format(time()-begin, '')
        return output
    return timed_f