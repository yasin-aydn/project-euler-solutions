#################### 1 ####################

def sieve(n):

    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    print(f"Result:{sum(prime)}")

sieve(2000000)

#################### 2 ####################

def is_prime(num):
    if num == 1:
        return False
    if num <= 3:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    sum = 2
    for i in range(3,limit,2):
        if is_prime(i):
            sum += i

    print(f"Result:{sum}")


sum_of_primes(2000000)