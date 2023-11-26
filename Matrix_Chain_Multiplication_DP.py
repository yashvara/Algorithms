def matrixChain(arr, n):
    m = [[0 for i in range(n)] for i in range(n)]
    
    for d in range(2, n):
        for i in range(1, n - d + 1):
            j = i + d - 1
            m[i][j] = float('inf')
            
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + (arr[i - 1] * arr[k] * arr[j])
                if q < m[i][j]:
                    m[i][j] = q
    
    return m[1][n - 1]

arr = [5, 4, 6, 2, 7]
n = len(arr)
result = matrixChain(arr, n)
print(result)

