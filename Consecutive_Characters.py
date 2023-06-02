a=input()
b=set(a)
c=0
maxx=0
p=[]
for i in b:
    maxx=0
    for j in range(0,len(a)):
        if i==a[j]:
            c+=1
            maxx=max(c,maxx)
        else:
            c=0
    p.append(maxx)
print(max(p))