import math
P,R,T=map(int,input().split())
interest=P*pow((1+(R/100.0)),T);
print("%0.2f"%interest)