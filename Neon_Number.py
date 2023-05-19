def neon_number(s):
    n=s*s
    su=0
    while n>0:
        rem=n%10
        su=su+rem
        n=n//10
    if su==s:
        return 'Neon Number' 
    else:
        return 'Not Neon Number'
s=int(input())
print(neon_number(s))