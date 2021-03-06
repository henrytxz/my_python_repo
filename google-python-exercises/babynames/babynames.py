#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from collections import OrderedDict

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  file = open(filename, 'r')
  file_content = file.read()
  year = re.search(r'Popularity in (\d\d\d\d)', file_content).group(1)
  list = []
  list.append('Popularity in '+str(year))
  rows_of_names = re.findall(r'(\d+)</td><td>(\w*)</td><td>(\w*)', file_content)
  # print rows_of_names

  male_names = {}
  female_names = {}

  for row in rows_of_names:
      rank, name1, name2 = row
      male_names[name1] = rank
      female_names[name2] = rank

  # print sorted(male_names.items())
  # print sorted(female_names.items())
  all_names = male_names.items()
  all_names.extend(female_names.items())
  all_names = sorted(all_names)
  for name, rank in all_names:
    list.append(name+' '+rank)
  return list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for arg in args:
    list = extract_names(arg)
    if summary:
      summary_file = open(arg+'.summary', 'w')
      summary_file.write('\n'.join(list))
    else:
      print '\n'.join(list)
      print '='*88

if __name__ == '__main__':
  main()
