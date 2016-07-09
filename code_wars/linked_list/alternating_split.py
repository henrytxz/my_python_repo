from unittest import test


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def prepend(head, data):
    if head is None:
        return Node(data)
    else:
        new_head = Node(data)
        new_head.next = head
        return new_head

def list_to_linked_list(list, curr):
    while list:
      curr = prepend(curr, list.pop())
        # curr.next = Node(list.pop())
        # curr = curr.next
    return curr

def build_one_two_three():
    return prepend(prepend(Node(3), 2), 1)

def alternating_split(head):
    # Remember to return the context.
    if head is None or head.next is None: raise ValueError
    f, s = [], []
    append_to_f = True
    while head:
        if append_to_f:
            f.append(head.data)
        else:
            s.append(head.data)
        head = head.next
        append_to_f = not append_to_f
    assert f == [1,3]
    assert s == [2]
    first, second = Node(f.pop()), Node(s.pop())
    assert first.data == 3
    first  = list_to_linked_list(f, first)
    second = list_to_linked_list(s, second)
    return Context(first, second)

if __name__ == '__main__':
  print "should be able to handle a list of length 3"
  assert alternating_split(build_one_two_three()).first.data == 1
