import math

def viralAdvertising(n):

    shared_with = 5
    total_likes = 0

    for i in range(n):

        shared_with = math.floor(shared_with/2) 
        total_likes += shared_with
        shared_with *= 3

    return total_likes
        


n = 3
viralAdvertising(n)