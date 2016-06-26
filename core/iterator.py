import random

def die_rolls():
    while True:
        yield random.randint(1, 6)

results = []
for i in range(int(1e5)):
    results.append(next(die_rolls()))   # call next(generator)
print sum(results)/float(len(results))  # close to 3.5

print die_rolls()