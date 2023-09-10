def counting_sort(arr):
    # Find the range of input elements
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1

    # Initialize count array and sorted array
    count_array = [0] * range_of_elements
    sorted_array = [0] * len(arr)

    # Count the occurrences of each element
    for num in arr:
        count_array[num - min_element] += 1

    # Modify the count array to store cumulative counts
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # Create the sorted array
    for num in reversed(arr):
        sorted_array[count_array[num - min_element] - 1] = num
        count_array[num - min_element] -= 1

    return sorted_array

# Example usage
input_array = [4,56,67,99,89]
sorted_array = counting_sort(input_array)
print(sorted_array)  
