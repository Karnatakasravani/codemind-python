n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
a=((arr1))
b=((arr2))
l=[]
for i in a:
    if i not in b and a.count(i)==1:
        l.append(i)
for i in b:
    if i not in a and b.count(i)==1:
        l.append(i)
print(*l)
