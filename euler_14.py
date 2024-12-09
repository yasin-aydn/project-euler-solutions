def find_longest_collatz(limit):
    collatz = {1:1}
    for number in range(2,limit+1):
        count = 0
        start_number = number
        while True:
            if number in collatz:
                collatz[start_number] = collatz[number] + count
                break
            if number % 2 == 0:
                number //=2
            else:
                number = number*3+1
            count += 1

    max_key = max(collatz, key=collatz.get)
    max_value = collatz[max_key]
    print(max_key,max_value)

find_longest_collatz(1000000)
print(2**100)