#!/usr/bin/python2

import random

def partition(A, p, r, randomize):
    # If randomize is true, pick a random element as pivot
    if randomize:
        randint = random.randint(0, r - 1)
        A[randint], A[r] = A[r], A[randint]
    pivot = A[r]
    i = -1
    for j in range(r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    q = i + 1
    A[q], A[r] = A[r], A[q]
    return q


def quick_sort(A, p, r, randomize=False):
    if p < r:
        q = partition(A, p, r, randomize)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


if __name__ == "__main__":
    arr = [2, 8, 7, 1, 3, 5, 6, 4, 1, 9] 
    quick_sort(arr, 0, len(arr) - 1, randomize=True) 
    print arr
