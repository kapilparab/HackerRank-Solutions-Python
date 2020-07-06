import os
import sys
from heapq import heappop, heappush, heapify

#
# Complete the cookies function below.
#
def cookies(k, A):

    heapify(A) # Heapify the list
    num_ops = 0 # Num of operations performed

    try:
        while A[0] < k: # While the root is less than K
            num_ops += 1
            c1 = heappop(A) # Pop the two smallest elements from the heap
            c2 = heappop(A)
            newCookie = (1 * c1) + (2 * c2) # Calculate new sweetness
            heappush(A, newCookie) # Push the new cookie into the heap

        return num_ops
    except:
        return -1

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
