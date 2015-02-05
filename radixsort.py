#!/usr/bin/python2

import math

def counting_sort(A):
    """Assumes elements in array are positive integers"""
    C = [0] * (max(A) + 1)
    B = [None] * len(A)
    for e in A:
        C[e] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for e in reversed(A):
        B[C[e]-1] = e
        C[e] -= 1
    return B


def radix_sort(A, D):
    """Do counting sort for each digit"""    

    # Prepend 0 to get same number of digits
    max_digits = max([int(math.log10(e)) + 1 for e in A])
    
    for d in reversed(range(0, max_digits)):
        C = [0] * 10
        B = [None] * len(A)
        for e in A:
            digit = int(str(e)[d])
            C[digit] += 1
        for i in range(1, len(C)):
            C[i] += C[i-1] 
        for e in reversed(A):
            digit = int(str(e)[d])
            B[C[digit]-1] = e
            C[digit] -= 1
        A = B    
    return A


if __name__ == "__main__":
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    sorted_arr = counting_sort(arr) 
    print sorted_arr

    arr = [329, 457, 657, 839, 436, 720, 355]
    sorted_arr = radix_sort(arr, 3)
    print sorted_arr
