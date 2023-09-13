def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    smaller = []
    larger = []
    for i in range(1, len(array)):
        if array[i] < pivot:
            smaller.append(array[i])
        else:
            larger.append(array[i])
    return quicksort(smaller) + [pivot] + quicksort(larger)

array = [93, 71, 56, 67, 94]
print(quicksort(array))