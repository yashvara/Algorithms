def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while(key<arr[j] and j>0):
            arr[j-1] = arr[j]
            j=j-1
        arr[j+1] = key

Arr = [56,67,44,55,84,11,1]
insertion(Arr)
print(Arr)

# Bubble sort