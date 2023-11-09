n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in arr:
    b=str(i)
    if b==b[::-1]:
        cnt+=1
print(cnt)