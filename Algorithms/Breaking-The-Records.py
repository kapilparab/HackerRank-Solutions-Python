def breakingRecords(scores):

    minRecords = scores[0]
    maxRecords = scores[0]

    minCount = 0
    maxCount = 0

    for i in scores:
        
        if i > maxRecords:
            maxRecords = i
            maxCount += 1

        elif i < minRecords:
            minRecords = i
            minCount += 1

    return [maxCount, minCount]