#################### 1 ####################

def prime_factors(num):
    liste = []
    while num != 1:
        for i in range(2,num+1):
            if num % i == 0:
                liste.append(i)
                num //= i
                break

    return liste

def smallest_multiple(number):
    result = 1
    for i in range(1,number+1):
        factors = prime_factors(i)
        last_number = result
        for z in factors:
            if last_number/z == int(last_number/z):
                last_number /= z
            else:
                result *= z

    print(f"Result:{result}")

smallest_multiple(20)

#################### 2 ####################

def prime_factors_dict(num):
    prime_dict = {}
    while num != 1:
        for i in range(2,num+1):
            if num % i == 0:
                if i in prime_dict:
                    prime_dict[i] += 1
                else:
                    prime_dict[i] = 1
                num //= i
                break

    return prime_dict

def find_smallest_multiple(number):
    result = 1
    primes = dict()
    for i in range(1,number+1):
        prime = prime_factors_dict(i)
        for q in prime:
            if not q in primes or primes[q] < prime[q]:
                primes[q] = prime[q]

    for i in primes:
        result *= i**(primes[i])

    print(f"Result:{result}")

find_smallest_multiple(20)
