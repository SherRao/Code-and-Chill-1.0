#!/bin/python3

import os

def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range( len(arr) ):
        left += arr[i][i]
        right += arr[-(i+1)][i]
        
    return abs(left - right)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()