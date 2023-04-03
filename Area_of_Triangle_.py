import math
a,b,c=map(float,input().split())
s=(a+b+c)//2
area=((math.sqrt(s*(s-a)*(s-b)*(s-c))))
print('%0.2f' %area)