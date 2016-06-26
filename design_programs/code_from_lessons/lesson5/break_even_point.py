import math

mil = 1000000

def Q(state, action, U):
    if action == 'gamble':
        return U(state + 3*mil)*0.5 + U(state)*0.5
    if action == 'hold':
        return U(state + 1*mil)

U = math.log10

c = 1*mil

print Q(c, 'gamble', U) - Q(c, 'hold', U)
