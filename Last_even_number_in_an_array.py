n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    if a[i]%2==0:
        l.append(a[i])
print(l[-1])