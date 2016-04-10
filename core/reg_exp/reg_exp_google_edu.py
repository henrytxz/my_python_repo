# https://developers.google.com/edu/python/regular-expressions?hl=en

# words of wisdom:
# I recommend that you always write pattern strings with 'r' just as a habit.

import re

str = 'an example word:ca_!!'
match = re.search(r'word:\w\w\w', str)
assert match.group() == 'word:ca_'   # match.group() is the matching text

match = re.search(r'iii', 'piiig')
assert match.group() == 'iii'

match = re.search(r'igs', 'piiig')
assert match is None

# repetition examples
match = re.search(r'pi+', 'piiig')
assert match.group() == 'piii'

match = re.search(r'i+', 'piigiiii')
assert match.group() == 'ii'

match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
assert match.group() == '1 2   3'

match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
assert match.group() == '12  3'

match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
assert match.group() == '123'

match = re.search(r'^b\w+', 'foobar')
assert match is None  # bc the 1st char isn't b

match = re.search(r'b\w+', 'foobar')
assert match.group() == 'bar'   # b is found then 2 more [a-zA-Z0-9_]

# examples of difference between
# 0 or more occurrences and 1 or more occurrences

match = re.search(r'i*', 'foobar')
assert match.group() == ''

match = re.search(r'i+', 'foobar')
assert match is None

##############################################################################

match = re.search('a*b*', 'foobar')
assert match.group() == ''

match = re.search('oba', 'foobar')
assert match.group() == 'oba'