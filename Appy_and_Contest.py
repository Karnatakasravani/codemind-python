# cook your dish here
import math as np
for i in range(int(input())):
    n,a,b,k=map(int,input().split())
    j=np.lcm(a,b)
    l=((n//a)+(n//b)-(n//j)*2)
    if l>=k:
        print("Win")
    else:
        print("Lose")