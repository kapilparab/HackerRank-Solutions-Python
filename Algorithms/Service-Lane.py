def serviceLane(n, cases):

    res = []

    for case in range(len(cases)):
        
        i = cases[case][0]
        j = cases[case][1]

        minWidth = min(width[i:j+1])
        res.append(minWidth)

    return res


n = 8
t = 5
width = [2,3,1,2,3,2,3,3]
cases = [[0,3], [4,6], [6,7], [3,5], [0,7]]
serviceLane(n, cases)