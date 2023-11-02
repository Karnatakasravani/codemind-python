n=input()
N=list(n)
l=[]
for i in N:
    if i not in l:
        l.append(i)
if N==l:
    print("Unique Number")
else:
    print("Not Unique Number")