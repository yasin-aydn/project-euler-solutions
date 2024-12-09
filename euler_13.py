from euler_13_numbers import numbers

def large_sum(digit):
    global numbers
    number_list = numbers.split("\n")
    int_list = list(map(int,number_list))
    print(str(sum(int_list))[:digit])

large_sum(10)