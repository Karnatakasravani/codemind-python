n=int(input())
a=list(map(int,input().split()))
l=[]
res = []
for i, ele in enumerate(a):
    if ele % 2 == 0:
        res.append(i)
#print(str(res))
print(res[-1])