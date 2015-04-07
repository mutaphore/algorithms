#!/usr/bin/python2

def matrix_chain_order(p):
    n = len(p) - 1
    m = [n * [0] for i in range(n)]
    for l in range(2, n + 1): 
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i-1][j-1] = float("inf")
            for k in range(i, j):
                q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
    for row in m:
        print row

if __name__ == "__main__":
    p = [5, 10, 3, 12, 5, 50, 6]
    matrix_chain_order(p)
