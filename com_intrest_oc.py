import math
p,r,t=map(int,input().split())
amount=p*(math.pow((1+(r/100)),t))
#ci=amount-p
print("%.2f"%amount)
