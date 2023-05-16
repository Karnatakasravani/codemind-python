x,y=map(int,input().split())
val=x+2*y
if(val%2==0):
    if(x==0 and y%2!=0):
        print("NO")
    else:
        print("YES")
else:
    print("NO")