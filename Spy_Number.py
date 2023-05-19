def spynumber(n):
    su=0
    prod=1
    while n>0:
        rem=n%10
        su=su+rem
        prod=prod*rem
        n=n//10
    if su==prod:
        return 'Spy Number' 
    else:
        return 'Not Spy Number'
n=int(input())
print(spynumber(n))