def minmaxproblem(arr, l, r):
    if l == r:
        return (arr[l], arr[l])  # Base case: single element, return as min and max

    elif r == l + 1:
        if arr[l] < arr[r]:
            return (arr[l], arr[r])  # Compare two elements and return as min and max
        else:
            return (arr[r], arr[l])

    else:
        mid = (l + r) // 2  # Corrected the calculation of mid using integer division
        
        # Divide the array into two parts and find min/max for each part
        arr_min1, arr_max1 = minmaxproblem(arr, l, mid)  # for the left part
        arr_min2, arr_max2 = minmaxproblem(arr, mid + 1, r)  # for the right part

        # Return the overall min and max of both parts
        return (min(arr_min1, arr_min2), max(arr_max1, arr_max2))

arr = [1, 23, -5, 67, 56]
result_min, result_max = minmaxproblem(arr, 0, len(arr) - 1)
print("Minimum:", result_min)
print("Maximum:", result_max)
