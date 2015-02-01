#!/usr/bin/python2


def max_heapify(A, i):
    """Float down A[i] so subtree rooted at index i is a max heap"""
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left < len(A) and A[left] > A[i]:
        A[left], A[i] = A[i], A[left]
        largest = left
    if right < len(A) and A[right] > A[i]:
        A[right], A[i] = A[i], A[right]
        largest = right
    if largest != i:
        return max_heapify(A, largest) 
    else:
        return A


if __name__ == "__main__":
    heap = [None, 5, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    heap2 = max_heapify(heap, 1)
    print "Heap 2 is %r" % heap2

