n=int(input())
a=list(map(int,input().split()))
l=[]
for i,ele in enumerate(a):
    if ele%2!=0:
        l.append(i)
print(l[-1])