n=int(input())
arr=list(map(int,input().split()))
l=[]
L=set(l)
for i in arr:
    if i==arr.count(i):
        l.append(i)
print(len(set(l)))