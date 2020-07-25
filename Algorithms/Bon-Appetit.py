def bonAppetit(bill, k, b):

    totalBill = sum(bill)
    annaBill = (totalBill - bill[k])/2

    annaChange = bill[k]/2

    if (annaBill == b):
        print('Bon Appetit')
    else:
        print(annaChange)

# Test code
k = 1
b = 7
lst = [3, 10, 2, 9]
bonAppetit(lst, k, b)