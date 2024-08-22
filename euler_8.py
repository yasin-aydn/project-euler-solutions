#################### 1 ####################

from euler_8_text import number

def largest_product(series):
    global number
    number = number.split("\n")
    number = "".join(number)
    highest_number = 0
    i = 0
    for a in range(0,len(number)-14):
        result = 1
        num = number[a:a+series]
        for q in range(series):
            result *= int(num[q])
        if result > highest_number:
            highest_number = result
        i += 1

    print(f"Result:{highest_number}")

largest_product(13)

#################### 2 ####################

from euler_8_text import number

def largest_product(series):

    global number
    number = number.split("\n")
    number = "".join(number)
    highest_number = 0

    while len(number) > 12:
        result = 1
        k = number[0:series]
        for i in k:
            result *= int(i)
        if result > highest_number:
            highest_number = result

        number = number[1:len(number)+1]

    print(f"Result:{highest_number}")

largest_product(13)