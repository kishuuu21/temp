def find_missing_2(arr,x1):
    n=len(arr)
    z = 0
    for i in range(1,n):
        if (arr[i-1]< arr[i]):
            pass
        else:
            if (i+1 < n) and arr[i+1]> arr[i]:
                z = i
            # arr.remove(arr[i-1])
    for j in range(z):
        if (arr[j+1] - arr[j] > 1):
           return arr[j]+1
    for k in range(z,n-1):
        if (arr[k+1] - arr[k] > 1):
           return arr[k]+1
arr = [5,7,1,2,3,4]
ans = find_missing_2(arr,[])
print(ans)
