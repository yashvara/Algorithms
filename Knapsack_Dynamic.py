def knapsack(pr,wt,W,n):
    if(n==0 or W==0):
        return 0
    else:
        if(wt[n-1]>W):
            return knapsack(pr,wt,W,n-1)
        else:
           return (max(knapsack(pr,wt,W,n-1),pr[n-1]+knapsack(pr,wt,W-wt[n-1],n-1)))

pr=[5,7,8,10,3,6]
wt=[3,2,5,3,1,4]
W=10
n=len(pr)
print(knapsack(pr,wt,W,n))


