def cnt_primes(start,end):
    cnt=0
    for n in range(start,end+1):
        if is_prime(n):
            cnt+=1
    return cnt
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
start=int(input())
end=int(input())
prime_cnt=cnt_primes(start,end)
print(prime_cnt)