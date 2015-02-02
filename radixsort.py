#!/usr/bin/python2

def counting_sort(A):
    """Assumes elements in array are positive integers"""
    C = [0] * (max(A) + 1)
    B = [None] * len(A)
    for e in A:
        C[e] += 1
    for i in range(1, len(C)):
        C[i] = C[i-1] + C[i]
    for e in reversed(A):
        B[C[e]-1] = e
        C[e] -= 1
    return B

if __name__ == "__main__":
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    sorted_arr = counting_sort(arr) 
    print sorted_arr
