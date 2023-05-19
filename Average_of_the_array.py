n=int(input())
lst = list(map(int,input().split()))
avg=sum(lst) / len(lst)
print("%0.2f"%avg)