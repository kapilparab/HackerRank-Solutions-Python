def hurdleRace(k, height):

    return max(max(height) - k, 0)

k = 7
height = [2,5,4,5,2]
hurdleRace(k, height)