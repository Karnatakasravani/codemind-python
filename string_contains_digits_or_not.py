t=int(input())
for i in range(1,t+1):
    n=input(str())
    cnt=0
    for i in n:
        if i.isdigit():
            cnt+=1
    if cnt>=1:
        print("Yes")
    else:
        print("No")