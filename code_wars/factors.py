def factors(x):
    if not isinstance(x, int) or x<1:
        return -1
    else:
        bigger_factors = []
        smaller_factors = []
        import math
        # bigger_factors.append(x)
        values_to_check = range(int(math.floor(math.sqrt(x))))  # for x = 54: 0 to 6
        for i in values_to_check:
            i += 1
            quotient = float(x)/i
            if quotient.is_integer():
                bigger_factors.append(int(quotient))
                smaller_factors.append(i)   # this is ascending order for now
        if bigger_factors[-1] == smaller_factors[-1]:
            bigger_factors.remove(bigger_factors[-1])
        smaller_factors.reverse()
        return bigger_factors+smaller_factors

factors(64)

def factors(x):
    if not isinstance(x, int) or x<1:
        return -1
    else:
        result = []
        result.append(x)
        values_to_check = range(x)
        values_to_check.reverse()
        # I explored only checking up to the sqrt of x, doing that, every time I find a legit quotient,
        # I append both i and quotient to result
        # that made it a little more complicated to have all factors in descending order
        # it could be done with 2 lists, let's call them bigger_factors and smaller_factors
        # one needs to pay attention to have them still in descending order before concatenating them
        # and also, if a number appears in both lists, that needs to be handled so it's more code to write
        # for a performance gain of checking for sqrt(x) numbers instead of x numbers... could be worth it
        # before writing code, ask the interviewer what (s)he wants
        for i in values_to_check:
            i += 1
            quotient = float(x)/i
            if quotient.is_integer():
                if len(result)>0 and i==result[-1]:
                    continue
                result.append(i)
        return result