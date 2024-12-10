name = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def get_number_name(number):
    result = ""
    if number < 21:
        result = name[number]
    elif number < 100:
        tens_remainder = number % 10
        result = name[number - tens_remainder]
        if tens_remainder:
            result += "-" + name[tens_remainder]
    elif number < 1000:
        two_digit = number % 100
        result = name[(number - two_digit) // 100] + " " + name[100]
        if two_digit:
            result += " and " + get_number_name(two_digit)
    else:
        result = name[1] + " " + name[1000]

    return result

def letter_count(limit):
    count = 0
    for number in range(1,limit):
        number_str = get_number_name(number)
        for letter in number_str:
            if letter == " ":
                continue
            else:
                count += 1
    print(count)

def reduced_number_name_len(number):
    return len(get_number_name(number).replace(" ", "").replace("-", ""))


def run(limit):
    print(
        f"Result:{sum(map(reduced_number_name_len, range(1, limit+1)))}: "
    )
 
run(1000)