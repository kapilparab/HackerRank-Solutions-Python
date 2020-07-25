import string

def designerPdfViewer(h, word):

    wordLen = len(word)
    # Get index of character in the word and use it to index 
    # into h array to get the max height
    maxHeight = max([h[string.ascii_lowercase.index(i)] for i in word])

    return wordLen * maxHeight


# h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
# word = 'abc'
# designerPdfViewer(h, word)