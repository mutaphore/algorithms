#!/usr/bin/python

# Find the longest increasing subarray

# Return the count of lis
def lis_count(arr):
    n = len(arr)
    dp = n * [0]
    dp[0] = 1
    prev = n * [0]
    prev[0] = -1
    max_len = 0
    best_end = 0
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
            j -= 1
        if dp[i] > max_len:
            max_len = dp[i]
            best_end = i
    # Create the sequence
    index = n - 1
    result = []
    result.append(arr[best_end])
    print prev
    print best_end
    for i in reversed(prev):
        if i == -1:
            break
        if best_end != i:
            best_end = i
            result.append(arr[best_end])
    return result[::-1], dp[n-1]

# Return the actual lis sequence

if __name__ == "__main__":
    #arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    #arr = [1, 5, 4, 2, 6, 3, 9]
    arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    print lis_count(arr)
    
