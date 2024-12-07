#################### 1 ####################

def is_prime(num):
    if num == 1:
        return False
    if num <= 3:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(x):
    while not is_prime(x):
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                x //= i
                break
    print(f"Result:{x}")

largest_prime_factor(600851475143)

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

def largest_prime_factor(number):
    highest_number = 0
    for i in range(2,int(number**0.5)+1):
        if is_prime(i) and number % i == 0:
            if is_prime(number/i):
                if max(number/i,i) > highest_number:
                    highest_number = max(number/i,i)
            else:
                if i > highest_number:
                    highest_number = i
    print(f"Result:{highest_number}")

largest_prime_factor(600851475143)

