from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements, return it
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    
    # Selecting a random element using randint function
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result will be a merge of the low, same, and high lists
    return quicksort(low) + same + quicksort(high)
