def divisibleSumPairs(n, k, ar):

    freq = [0] * k

    pairs = 0

    for i in lst:

        rem = i % k

        if rem != 0:
            pairs += freq[k-rem]
        else:
            pairs += freq[0]

        freq[rem] += 1

return pairs