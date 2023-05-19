n=int(input())
lst=list(map(int,input().split()))
cnt1=0
cnt2=0
for i in lst:
    if i%2==0:
        cnt1=cnt1+1
    elif i%2!=0: 
        cnt2=cnt2+1
print(cnt1,cnt2)