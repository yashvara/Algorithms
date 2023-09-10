def merge_sort(arr):
    if len(arr) > 1:  # Base Case: If the array has more than one element
        mid = len(arr) // 2  # Calculate the middle index
        left = arr[:mid]     # Divide the array into two halves
        right = arr[mid:]

        merge_sort(left)     # Recursively sort the left half
        merge_sort(right)    # Recursively sort the right half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Handle remaining elements in the left and right halves
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [67,56,99,10,105,56,67]
merge_sort(arr)
print(arr)
