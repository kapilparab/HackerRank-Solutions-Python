def kangaroo(x1, v1, x2, v2):

    try:
        if x2 > x1 and v2 > v1:
            print('NO')
        elif v1!=v2 and abs((x1-x2) % (v1-v2)) == 0:
            print('YES')
        else:
            print('NO')
    except:
        print('NO')


x1 = 0
v1 = 3

x2 = 4
v2 = 2

kangaroo(x1, v1, x2, v2)