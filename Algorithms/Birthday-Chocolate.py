def birthday(s, d, m):

    # https://www.hackerrank.com/challenges/the-birthday-bar/forum/comments/422367

    total = 0
    count = 0

    for i in range(len(s)):

        total += s[i]
        if (i > m - 1):
            total -= s[i-m]

        if (i >= m - 1 and total == d):
            count += 1 

    return count