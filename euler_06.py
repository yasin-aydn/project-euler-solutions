#################### 1 ####################

def sum_square_difference(number):
    num1 = 0
    num2 = 0
    for i in range(1,number+1):
        num1 += i**2
        num2 += i
    print(abs(num1-num2**2))
    
sum_square_difference(100)


