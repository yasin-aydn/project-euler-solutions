def is_prime(x):
    if x < 0:
        return False
    
    x_sqrt = int(x**0.5)+1

    for i in range(2,x_sqrt):
        if x % i == 0:
            return False
    
    return True

def find_quadratic_prime(limit):
    highest_count = 0
    for a in range(-limit-1,limit):
        for b in list(i for i in range(2,limit+1) if is_prime(i)):
            count = 0
            n = 0
            while True:
                if is_prime(n**2 + n*a + b):
                    count += 1
                    n += 1
                else:
                    if count > highest_count:
                        highest_count = count
                        result = a*b
                    break
                    
    print(f"Result:{result}")

find_quadratic_prime(1000)