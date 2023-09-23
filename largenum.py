n=int(input())
s=str(n)
p=''.join(sorted(s))
l=" "
for i in p:
    ch=i
    l=ch+l
print(l)
