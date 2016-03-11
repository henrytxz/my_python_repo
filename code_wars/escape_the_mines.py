# from unittest import TestCase
# from unittest.test.test_case import Test
import unittest

visited = set()


def build_graph(mat):
  """
  :return: a dictionary, each key is a node, its value a set of neighbors
  """
  d = {}
  d[(0,0)] = set((1,0))
  d[(1,0)] = set((0,0))
  d[(1,0)].add((1,1))
  d[(1,1)] = set((1,0))
  return d

def solve(mat, s, e):
  if s == e:
    return []
  g = build_graph(mat)
  return dfs(graph=g, current_node=s, exit=e)

def dfs(graph, current_node, exit):
  if current_node == exit:
    return [exit]
  visited.add(current_node)  # marked s as visited
  # For each neighbor, direction, pair
  #   If n not visited
  #   If dfs(mat, n, e), perpend direction to that list and return the resulting list



"""
Escape(2 by 2,  0,0,  1,1): dfs(origin, exit), mark origin, say we go to (0,1) - 2nd row 1st column, it's not the exit, check,
"""

def describe(message):
  print message

def it(message):
  print message

class Test(unittest.TestCase):
  def assert_equals(self, x, y):
    return self.assertEqual(x, y)

# test_instance = TestCase()

describe('A trivial map (1x1)')
minemap = [[True]]
it('Should return an empty array, since we\'re already at the goal')
# test_instance.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':0,'y':0}), [])

assert solve(minemap, {'x':0,'y':0}, {'x':0,'y':0}) is []

minemap = [[True, False], [True, True]]
it('Should return the only correct move')
TestCase.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':1,'y':0}), ['right'])
it('Should return the only moves necessary')
TestCase.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':1,'y':1}), ['right', 'down'])