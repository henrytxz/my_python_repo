"""
this module contains the main logic to implementing the auto-completion feature
using a prefix tree

every node in the prefix tree can have any of the lower case alphabet or *
* marks the end of a word
"""

class Node(object):
    def __init__(self, key, children=[]):
        self.key = key
        self.children = children


def make_branch(keys):
    """ assumes len(keys)>0 """
    child = Node(keys[-1])
    for i in range(len(keys)-2, -1, -1):
        parent = Node(keys[i], [child])
        child = parent
    return child

def print_branch(branch_begin):
    """ assumes it's a branch, i.e. no forking, every node has 1 child """
    branch = branch_begin.key
    curr_node = branch_begin.children[0]
    while curr_node:
        if curr_node.key != '*':
            branch += '-' + curr_node.key
        curr_node = curr_node.children[0] if len(curr_node.children) else None
    return branch

def print_tree(root):
    tree_depth = {}
    depth = 0
    tree_depth.setdefault(depth, []).append(root)
    while tree_depth[depth]:
        new_depth = depth+1
        for node in tree_depth[depth]:
            tree_depth.setdefault(new_depth, []).extend(node.children)
        depth = new_depth
    for _, nodes_at_that_depth in tree_depth.iteritems():
        print ' '.join([node.key for node in nodes_at_that_depth])

def return_branch(node):
    if node.key == '*':
        return ['']
    else:
        result = []
        for c in node.children:
            result.extend([node.key+x for x in return_branch(c)])
        return result

def return_suggestions(root, prefix, matched=0):
    for c in root.children:
        if c.key == prefix[matched]:
            result = []
            if matched+1 == len(prefix):
                for cc in c.children:
                    result.extend([prefix + x for x in return_branch(cc)])
                return result
            else:
                return return_suggestions(c, prefix, matched+1)

def test(debug=False):
    """
    'an' prefix should output ['and', 'an', 'annoy'] from this tree

                prefix_tree_root
                /        \      \
             a            b      c
           / | \
         c   n   p
       /    /|\   \
      e    d * n    p
    /     /     \    \
   *    *        o    l
                  \    \
                   y    e
                    \    \
                     *    *
    """
    d = make_branch('d *'.split())
    assert print_branch(d) == 'd'
    noy = make_branch('n o y *'.split())
    assert print_branch(noy) == 'n-o-y'
    node_star = Node('*')
    node_n = Node('n', [d, node_star, noy])
    if debug:
        print_tree(node_n)

    ce = make_branch('c e *'.split())
    assert print_branch(ce) == 'c-e'
    pple = make_branch('p p l e *'.split())
    assert print_branch(pple) == 'p-p-l-e'
    node_a = Node('a', [ce, node_n, pple])
    if debug:
        print_tree(node_a)

    root = Node('prefix_tree_root', [node_a, Node('b'), Node('c')])
    assert return_suggestions(root, 'an') == ['and', 'an', 'annoy']

if __name__ == '__main__':
    test()