import math
n=int(input())
sq_n=n*n
N=str(n)
rev_n=N[::-1]
R=int(rev_n)
sq_rev_n=R*R
#print(n,sq_n,rev_n,sq_rev_n)
if str(sq_n)==(str(sq_rev_n))[::-1]:
    print("True")
else:
    print("False")