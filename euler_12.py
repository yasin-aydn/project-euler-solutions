import math

def find_divisors(x):
    divisor_amount = 0
    if math.sqrt(x) == int(math.sqrt(x)):
        divisor_amount -= 1
    for i in range(1,int(math.sqrt(x))+1):
        if x % i == 0:
            divisor_amount += 2
    return divisor_amount

def highly_divisible_triangular_number(number):
    n = 1
    while True:
        if n % 2 == 0:
            divisors = find_divisors(n//2) * find_divisors(n+1)
        else:
            divisors = find_divisors(n) * find_divisors((n+1)//2)
        if divisors > number:
            break
        n = n+1
    print((n**2+n)//2),n,divisors

highly_divisible_triangular_number(500)
