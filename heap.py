#!/usr/bin/python2

class Heap(object):
    """A heap array object with base 1 index"""

    def __init__(self, arr):
        self._heap = arr
        
    
    def __len__(self):
        return len(self._heap)

    
    def __getitem__(self, key):
        if type(key) is not int:
            raise TypeError
        if key < 0 or key > len(self._heap):
            raise IndexError
        return self._heap[key - 1]

    
    def __setitem__(self, key, value):
        if type(key) is not int or type(value) is not int:
            raise TypeError
        if key < 0 or key > len(self._heap):
            raise IndexError
        self._heap[key - 1] = value


    def __repr__(self):
        return repr(self._heap)


    def __str__(self):
        return str(self._heap)


def max_heapify(A, i):
    """Float down A[i] so subtree rooted at index i is a max heap"""
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left <= len(A) and A[left] > A[i]:
        largest = left
    if right <= len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        return max_heapify(A, largest) 
    else:
        return A


def build_max_heap(A):
    """Build a sorted max heap from unordered array"""
    for i in reversed(range(1, len(A) / 2 + 1)):   # Adjust for the range offset
        A = max_heapify(A, i)
    return A


if __name__ == "__main__":
    heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    max_heap = build_max_heap(heap)
    print "Max heap %r" % max_heap

