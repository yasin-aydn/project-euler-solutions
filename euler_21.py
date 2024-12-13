def sum_of_multiples(number):
    sum = 1
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            if i**2 == number:
                sum += i
            else:
                sum += i + number//i
    return sum

def amicable_sum(limit):
    sum = 0
    for i in range(1,limit):
        if i == sum_of_multiples(sum_of_multiples(i)):
            if sum_of_multiples(i) == i:
                continue
            else:
                sum += i

    print(sum)

amicable_sum(10000)

