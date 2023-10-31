n=input()
l=[]
for i in n:
    if i.isdigit():
        l.append(int(i))
print(sum(l))
        