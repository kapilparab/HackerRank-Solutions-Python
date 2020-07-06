def plusMinus(arr):

    posRatio = sum(x > 0 for x in arr)/len(arr)
    negRatio = sum(x < 0 for x in arr)/len(arr)
    zeroRatio = sum(x == 0 for x in arr)/len(arr)

    print('{:.6f}'.format(posRatio))
    print('{:.6f}'.format(negRatio))
    print('{:.6f}'.format(zeroRatio))