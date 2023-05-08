
n=int(input())
a=list(map(int,input().split()))
ans=sum(a)
if ans%2==0:
    print("1")
else:
    print("0")