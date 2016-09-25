def firstn(n):
    i = 0
    while i<n:
        yield i
        i+=1

for i in firstn(5):
    print i
