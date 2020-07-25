def lcm(a,b):

    return int((a * b)/gcd(a,b))

def gcd(a,b):

    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def getTotalX(a, b):

    # Find LCM of list A
    # Find GCD of list B
    # Count the number of multiples of LCM that divides the GCD
    # O(n log (n))

    count = 0

    lcm_a = a[0]
    for c in a[1::]:
        lcm_a = lcm(lcm_a,c)

    gcd_b = b[0]
    for c in b[1::]:
        gcd_b = gcd(gcd_b, c)
    
    multiples_of_lcm = lcm_a
    while multiples_of_lcm <= gcd_b:
        if gcd_b % multiples_of_lcm == 0:
            count += 1
        multiples_of_lcm += lcm_a
    
    return(count)