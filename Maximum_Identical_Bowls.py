def bowl(a,n,s):
    for i in range(n,0,-1):
        if s%i==0:
            return i
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
s=sum(a)
print(bowl(a,n,s))
