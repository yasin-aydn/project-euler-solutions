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

def find_by_number(number):
    n = 3
    num = 1

    while True:
        if is_prime(n):
            num += 1
        if num == number:
            break
        n += 2

    print(f"Result:{n}")

find_by_number(10001)

