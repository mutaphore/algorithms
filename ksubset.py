#!/usr/bin/python

# Compute all subsets of size k of the set 1...n

def subsets(n, k, start, ans, results):
    if len(ans) == k:
        results.append(ans)
        return
    i = start
    while i <= n and k - len(ans) <= n - i + 1:
        temp = list(ans)
        temp.append(i)
        subsets(n, k, i+1, temp, results)
        i += 1

if __name__ == "__main__":
    n = 5
    k = 2
    ans = []
    results = []
    subsets(n, k, 1, ans, results)
    print results




