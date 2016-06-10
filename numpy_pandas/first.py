a = [[1,2],[3,4],[5,6]]

assert [row[1] for row in a] == [2,4,6]

import numpy as np

# Subway ridership for 5 stations on 10 different days
# row is day, column is station
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

assert np.argmax(ridership[0,:]) == 3
assert ridership[0,:].argmax() == 3