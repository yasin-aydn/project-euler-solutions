def find_digit_range(number):
     n = 1
     while True:
        if len(str(9**number*n)) >= n:
             n += 1
        else:
            return n

def find_digit_sum(digit):
    total_sum = 0
    digit_range = find_digit_range(digit)
    for i in range(2,10**digit_range):
        sum = 0
        for q in str(i):
            sum += int(q)**digit
        if sum == i:
            total_sum += sum

    print(total_sum)

find_digit_sum(5)