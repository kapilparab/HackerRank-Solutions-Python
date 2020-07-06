def birthdayCakeCandles(ar):

    maxVal = max(arr)  # Get the maximum value from the list

    # Store the indices / count of how many times maximum value appears
    indices = [index for index, val in enumerate(arr) if val == maxVal]

    # Return the length of the indices list
    print(len(indices))