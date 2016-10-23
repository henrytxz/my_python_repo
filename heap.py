import heapq


class Heap(object):
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def peek(self):
        raise NotImplementedError()

    def pop(self, item):
        raise NotImplementedError()

    def push(self):
        raise NotImplementedError()

    def replace(self):
        raise NotImplementedError()


class MaxHeap(Heap):
    """
    to leverage the heapq module, I will store -item for every item
    so peek, returning -item being the smallest will be the largest item
    """
    def peek(self):
        return -self.heap[0]

    def pop(self):
        return -heapq.heappop(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, -item)


class MinHeap(Heap):
    def peek(self):
        return self.heap[0]

    def pop(self):
        return heapq.heappop(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, item)


class FixedSizeMixin(object):
    def __init__(self, fixed_size):
        super(FixedSizeMixin, self).__init__()
        self.fixed_size = fixed_size

    def push(self, item):
        if self.size() == self.fixed_size:
            heapq.heappushpop(self.heap, item)
        else:
            heapq.heappush(self.heap, item)


class FixedSizeMinHeap(FixedSizeMixin, MinHeap):
    pass


class FixedSizeMaxHeap(FixedSizeMixin, MaxHeap):
    def push(self, item):
        super(FixedSizeMaxHeap, self).push(-item)


def test_min_heap():
    min_heap = MinHeap()
    min_heap.push(2)
    min_heap.push(3)
    min_heap.push(1)
    assert min_heap.size() == 3
    assert min_heap.peek() == 1
    assert min_heap.pop() == 1
    assert min_heap.pop() == 2
    assert min_heap.pop() == 3


def test_max_heap():
    max_heap = MaxHeap()
    max_heap.push(2)
    max_heap.push(3)
    max_heap.push(1)
    assert max_heap.size() == 3
    assert max_heap.peek() == 3
    assert max_heap.pop() == 3
    assert max_heap.pop() == 2
    assert max_heap.pop() == 1


def test_fixed_min_heap():
    min_heap = FixedSizeMinHeap(3)
    min_heap.push(2)
    min_heap.push(3)
    min_heap.push(0)
    # heap: 0, 2 and 3 => at capacity
    assert min_heap.size() == 3
    min_heap.push(1)
    # 0 < 1 so get rid of 0 and keep 1: 1, 2 and 3
    assert min_heap.size() == 3
    assert min_heap.peek() == 1

    assert min_heap.pop() == 1
    assert min_heap.pop() == 2
    assert min_heap.pop() == 3


def test_fixed_max_heap():
    max_heap = FixedSizeMaxHeap(3)
    max_heap.push(2)
    max_heap.push(3)
    max_heap.push(0)
    # heap: 0, 2 and 3 => at capacity
    assert max_heap.size() == 3
    max_heap.push(1)
    # 1 < 3 so get rid of 3 and keep 1: 0, 1 and 2
    assert max_heap.size() == 3
    assert max_heap.peek() == 2

    assert max_heap.pop() == 2
    assert max_heap.pop() == 1
    assert max_heap.pop() == 0


if __name__ == '__main__':
    test_min_heap()
    test_max_heap()
    test_fixed_min_heap()
    test_fixed_max_heap()