def find_spiral_sum(limit):
    total_sum = 1
    sum = 1
    q = 2
    while True:
        for _ in range(4):
            sum += q
            total_sum += sum

        if sum == limit**2:
            break

        q += 2
    print(total_sum)

find_spiral_sum(1001)
