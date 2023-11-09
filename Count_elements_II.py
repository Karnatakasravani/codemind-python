n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
a=set(arr1)
b=set(arr2)
cnt=0
for i in a:
    if i not in b:
        cnt+=1
for i in b:
    if i not in a:
        cnt+=1
print(cnt)