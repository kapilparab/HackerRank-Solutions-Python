import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def find_sum(arr, i, j):
    max_val = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
    return max_val

def hourglassSum(arr):

    max_val = -100

    for i in range(0,4):
        for j in range(0,4):
            total = find_sum(arr, i, j)
        
            if total > max_val:
                max_val = total
    
    return max_val

if __name__ == '__main__':

    # arr = [[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0], [0,0,2,4,4,0], [0,0,0,2,0,0], [0,0,1,2,4,0]]

    # arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    # result = hourglassSum(arr)
    # print(result)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()