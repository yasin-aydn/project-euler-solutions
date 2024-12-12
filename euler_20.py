from math import factorial

def calc(num):
    print(sum(int(digit) for digit in str(factorial(num))))

calc(100)