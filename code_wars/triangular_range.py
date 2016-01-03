# d maps the length of a side to the triangular number
#d = {1:1}

# list of triangular numbers, starting with the 1st triangular number which is 1
l = [0,1]

def triangular_number(n):
    global l
    if n < len(l):
        return l[n]
    else:
        while len(l)<=n:
            next_triangular_number = l[-1] + len(l)
            l.append(next_triangular_number)
        return l[-1]

def triangular_range(start, stop):
    #print l.index(1)
    global l
    """
        given start, i want the 1st triangular number that's >= start
        to achieve this, i can scan l till i either find one or reach the end of l
        when either occurs, i keep going till the triangular number is larger than stop
        if found:
            keep inserting l.index(triangular_number) : triangular_number into result_dict
        else:
            generate the next triangular number then do the above
    """
    result_dict = {}
    i = 1
    while l[i] < start:
        i+=1
        if i==len(l):
            triangular_number(i)
    while l[i] <= stop:
        result_dict[i] = l[i]
        i+=1
        if i==len(l):
            triangular_number(i)
    return result_dict

# assert triangular_number(1) == 1
# assert triangular_number(2) == 3
# assert triangular_number(3) == 6
# assert triangular_number(4) == 10
# assert triangular_number(5) == 15
print triangular_range(1, 3)
print triangular_range(5, 16)