import os
import sys

#
# Complete the equalStacks function below.
#

def sumArray(x):
    return [sum(x[: i+1]) for i in range(len(x))]

def equalStacks(h1, h2, h3):
    
    col1 = 0
    col2 = 0
    col3 = 0

    while(h1[col1] != h2[col2] or h2[col2] != h3[col3]):
        
        if h1[col1] > h2[col2] or h1[col1] > h3[col3]:

            col1 += 1
        
        elif h2[col2] > h1[col1] or h2[col2] > h3[col3]:

            col2 += 1

        elif h3[col3] > h2[col2] or h3[col3] > h1[col1]:

            col3 += 1

    print(h1[col1])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    # fptr.write(str(result) + '\n')

    # fptr.close()
