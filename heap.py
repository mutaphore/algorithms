#!/usr/bin/python2

class Heap(object):
    """A heap array object with base 1 index"""

    def __init__(self, arr):
        self._heap = arr
        self.heap_size = len(self._heap)
        self.length = len(self._heap)
    

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
        return repr(self._heap[:self.heap_size])


    def __str__(self):
        return str(self._heap[:self.heap_size])


    def to_arr(self):
        return self._heap


def max_heapify(A, i):
    """Float down A[i] so subtree rooted at index i is a max heap"""
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left <= A.heap_size and A[left] > A[i]:
        largest = left
    if right <= A.heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest) 


def build_max_heap(A):
    """Build a sorted max heap from unordered array"""
    for i in reversed(range(1, len(A) / 2 + 1)):   # Adjust for the range offset
        max_heapify(A, i)


def heap_sort(A):
    """Sorts an array into increasing order by using the heap data structure"""
    A = Heap(A)
    build_max_heap(A)
    for i in reversed(range(2, len(A) + 1)):
        A[1], A[i] = A[i], A[1]
        A.heap_size -= 1
        max_heapify(A, 1)
    return A.to_arr()


def heap_max(A):
    """Return maximum element of a max heap"""
    return A[1]


def heap_extract_max(A):
    """Extracts the max element from a max heap and also return it"""
    if A.heap_size < 1:
        raise IndexError
    heap_max = A[1]
    A[1] = A[A.heap_size]
    A.heap_size -= 1
    max_heapify(A, 1)
    return heap_max


def heap_increase_key(A, i, key):
    """Increase the value of element at index i to key"""
    if A[i] > key:
        return        
    A[i] = key 
    while i / 2 > 1 and A[i/2] < A[i]:
        A[i/2], A[i] = A[i], A[i/2]
        i /= 2


if __name__ == "__main__":
    heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    build_max_heap(heap)
    print "Max heap %r" % heap
    print "Extract heap max %r" % heap_extract_max(heap) 
    print "Max heap %r" % heap
    heap_increase_key(heap, 8, 11)
    print "Heap increase key %r" % heap

    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    sorted_arr = heap_sort(arr)
    print "Sorted array %r" % sorted_arr


