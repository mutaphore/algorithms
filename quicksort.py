#!/usr/bin/python2


def partition(A, p, r):
    i = -1
    for j in range(r):
        if A[j] < A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    q = i + 1
    A[q], A[r] = A[r], A[q]
    return q


def quick_sort(A, p, r):
    if p <= r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


if __name__ == "__main__":
    arr = [2, 8, 7, 1, 3, 5, 6, 4] 
    quick_sort(arr, 0, len(arr) - 1) 
    print arr
