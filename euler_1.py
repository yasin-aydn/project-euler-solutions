#################### 1 ####################

def sum_of_multiples(target_number,multiples=[]):
    sum = 0
    for i in range(target_number):
        for number in multiples:
            if i % number == 0:
                sum += i
                break
    print(f"Result:{sum}")

sum_of_multiples(1000,[3,5])

#################### 2 ####################

def sum_of_multiples(target_number,multiples=[]):
    summation = set()
    for number in multiples:
        static_number = number

        while target_number>number:
            summation.add(number)
            number += static_number
    
    print(f"Result:{sum(summation)}")

sum_of_multiples(1000,[3,5])

#################### 3 ####################

def sum_of_multiples(target_number):
    print(f"Result:{sum(i for i in range(target_number) if i % 3 == 0 or i % 5 == 0)}")

sum_of_multiples(1000)






