#!/usr/bin/python2

import sys

def lcs(X, Y):
    "Finds the longest common subsequence of strings X and Y"
    m = len(X)
    n = len(Y)
    # Build the lcs table
    c = [[0] * (n + 1) for x in range(m + 1)]
    b = [["0"] * (n + 1) for x in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "D"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "U"
            else: 
                c[i][j] = c[i][j-1]
                b[i][j] = "L"
    # Traverse table backwards to get common symbols
    i = m
    j = n
    s = []
    while i != 0 and j != 0:
        if b[i][j] == "D":
            s.append(X[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == "L":
            j -= 1
        else:
            i -= 1
    print s[::-1]     
    for row in b:
        print row
    return c


if __name__ == "__main__":
    X = "10010101"
    Y = "010110110"
    c = lcs(X, Y)
    for row in c:
        print row
