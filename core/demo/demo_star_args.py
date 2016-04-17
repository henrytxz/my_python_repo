def f(x, *args):
    assert x==1
    assert args==(2,3)
    return g(x, *args)

def g(*args):
    assert args==(1,2,3)

f(1,2,3)