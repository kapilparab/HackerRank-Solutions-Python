import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):

    last_answer = 0
    ret_values = []

    #Creating sequence lists and storing them in a dictionary
    seqDict = {}
    for i in range(n):
        seqDict['seqList' + str(i)] = list()

    for query in queries:
        if query[0] == 1:
            curr_seq = seqDict['seqList' + str((query[1] ^ last_answer) % n)]
            curr_seq.append(query[2])
        elif query[0] == 2:
            curr_seq = seqDict['seqList' + str((query[1] ^ last_answer) % n)]
            element = query[2] % len(curr_seq)
            last_answer = curr_seq[element]
            ret_values.append(last_answer)
    
    return ret_values
        

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    # queries = [[1,0,5], [1,1,7], [1,0,3], [2,1,0], [2,1,1]]

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
