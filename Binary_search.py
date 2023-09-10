# Binary Search
# Assume : Already Sorted Arrray
# Time Complexity = [log(n)] => Master's Theorem 1T(n/2)+1
# Space Complexity = 1
# In-Place Searching

def binary_search(arr, key, left, right):
    # Check if the left pointer is still less than or equal to the right pointer
    if left <= right:
        mid = (left + right) // 2  # Calculate the middle index using integer division

        if arr[mid] == key:
            return mid  # Key found at the middle index
        elif arr[mid] > key:
            # If the middle element is greater than the key, search in the left half
            return binary_search(arr, key, left, mid - 1)
        else:
            # If the middle element is smaller than the key, search in the right half
            return binary_search(arr, key, mid + 1, right)
    else:
        return -1  # Key not found in the array

arr = [56, 67, 89, 105, 199, 199]
key = 67

result = binary_search(arr, key, 0, len(arr) - 1)
if result == -1:
    print("Key Not Found!!!")
else:
    print("Key is Found at Index:", result)
