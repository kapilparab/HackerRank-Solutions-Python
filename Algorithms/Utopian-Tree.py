def utopianTree(n):

    init_height = 1

    if n == 0:
        return init_height
    else:
        for i in range(1,n+1):

            if i%2==0:
                init_height += 1
            else:
                init_height *= 2
                
    return init_height

cycles = [0,1,4]
for i in cycles:
    utopianTree(i)