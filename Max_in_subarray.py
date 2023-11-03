def max_of_subarr(n,k,arr):
    max_vales=[]
    max_value=max(arr[:k])
    max_vales.append(max_value)
    for i in range(k,n):
        if arr[i-k]==max_value:
            max_value=max(arr[i-k+1:i+1])
        else:
            max_value=max(max_value,arr[i])
        max_vales.append(max_value)
    return max_vales
        
n=int(input())
k=int(input())
arr=list(map(int,input().split()))
result=max_of_subarr(n,k,arr)
print(' '.join(map(str,result)))
