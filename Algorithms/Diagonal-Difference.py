
# Time Complexity -> O(n)

def diagonalDifference(arr):

    d1 = 0
    d2 = 0

    for i in range(0, len(arr)):
        d1 += arr[i][i] # Condition of Principal Diagonal is row = column
        d2 += arr[i][n-i-1] # Condition of Secondary Diagonal is row = numOfRow - columns - 1

    return abs(d2-d1)