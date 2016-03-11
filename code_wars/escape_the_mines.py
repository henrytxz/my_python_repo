# from unittest import TestCase
# from unittest.test.test_case import Test
import unittest

visited = set()

class Matrix:
  r = 'right'
  l = 'left'
  u = 'up'
  d = 'down'

  """
  a specific kind of graph where every node can have at most 4 neighbors
  """
  def __init__(self, mat):
    """
    :return: a dictionary, each key is a node, its value a set of (direction, node) pairs
    """
    self.m = {}
    self.m[(0,0)] = set()
    self.m[(0,0)].add((self.r, (1,0)))

    self.m[(1,0)] = set()
    self.m[(1,0)].add((self.l, (0,0)))
    self.m[(1,0)].add((self.d, (1,1)))

    self.m[(1,1)] = set()
    self.m[(1,1)].add((self.u, (1,0)))

  def __getitem__(self, tuple_representation_of_position):
    return self.m[tuple_representation_of_position]

  # class Neighbor:
  #   def __init__(self, mat, ):

# def build_graph(mat):

def data_translation(dict_representation_of_position):
  tuple_representation_of_position = (dict_representation_of_position['x'],
                                      dict_representation_of_position['y'])
  return tuple_representation_of_position

def solve(mat, s, e):
  if s == e:
    return []
  m = Matrix(mat)
  return dfs(graph=m, current_node=data_translation(s),
                      exit=data_translation(e))

def dfs(graph, current_node, exit):
  print 'current position: {0}'.format(current_node)
  if current_node == exit:
    return []
  visited.add(current_node)  # marked s as visited
  # For each neighbor, direction, pair
  #   If n not visited
  #   If dfs(mat, n, e), perpend direction to that list and return the resulting list
  for direction, neighbor in graph[current_node]:
    if neighbor not in visited:
      list_of_directions = dfs(graph, neighbor, exit)
      list_of_directions.insert(0, direction)
      return list_of_directions

"""
Escape(2 by 2,  0,0,  1,1): dfs(origin, exit), mark origin, say we go to (0,1) - 2nd row 1st column, it's not the exit, check,
"""

def describe(message):
  print message

def it(message):
  print message

describe('A trivial map (1x1)')
minemap = [[True]]
it('Should return an empty array, since we\'re already at the goal')
assert solve(minemap, {'x':0,'y':0}, {'x':0,'y':0}) == []

minemap = [[True, False], [True, True]]
it('Should return the only correct move')
assert solve(minemap, {'x':0,'y':0}, {'x':1,'y':0}) == ['right']

it('Should return the only moves necessary')
assert solve(minemap, {'x':0,'y':0}, {'x':1,'y':1}) == ['right', 'down']