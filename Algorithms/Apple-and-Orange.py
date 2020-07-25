def countApplesAndOranges(s, t, a, b, apples, oranges):

    appleCount = 0
    orangeCount = 0

    for x in apples:

        if s<= (x+a) <= t:
            appleCount+=1
        
    for x in oranges:

        if s<= (x+b) <= t:
            orangeCount+=1

    print(appleCount, orangeCount, sep = '\n') 


    ###### OR ######

def countApplesAndOranges(s, t, a, b, apples, oranges):

    print(sum([1 for x in apples if s<= (x+a) <= t]))
    print(sum([1 for x in oranges if s<= (x+b) <= t]))