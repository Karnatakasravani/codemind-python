n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//len(l)
for i in l:
    if i==avg:
        print("True")
        break
else:
    print("False")