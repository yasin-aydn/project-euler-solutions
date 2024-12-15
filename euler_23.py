def proper_divisors_sum(n):
    total = 1
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def get_abundant_numbers(limit):
    return [i for i in range(12, limit + 1) if proper_divisors_sum(i) > i]

def mark_abundant_sums(limit, abundants):
    can_be_written = [False] * (limit + 1)
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            sum_abundant = abundants[i] + abundants[j]
            if sum_abundant <= limit:
                can_be_written[sum_abundant] = True
            else:
                break
    return can_be_written

def non_abundant_sum_total(limit):
    abundants = get_abundant_numbers(limit)
    can_be_written = mark_abundant_sums(limit, abundants)
    return sum(i for i in range(1, limit + 1) if not can_be_written[i])

print(f"Result: {non_abundant_sum_total(28123)}")