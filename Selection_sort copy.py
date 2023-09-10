Arr = [5,56,67,88,22,3,4]
for i in range(len(Arr)):       # position index
    min_idx = i  
    for j in range(i+1,len(Arr)):    # finding the min value 
        if(Arr[min_idx]>Arr[j]):
            min_idx = j   # swapping
    Arr[min_idx],Arr[i] = Arr[i],Arr[min_idx]
print(Arr)