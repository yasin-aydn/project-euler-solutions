#################### 1 ####################

def even_fibonacci_sum(limit):
    liste = [1] * 2
    sum = 0

    while liste[-1]+liste[-2] < limit:
        new_number = liste[-1]+liste[-2]
        liste.append(new_number)
        if new_number % 2 == 0:
            sum += new_number
        liste.pop(0)

    print(f"Result:{sum}")

even_fibonacci_sum(4000000)

#################### 2 ####################

def even_fibonacci_sum(limit):
    sum = 0
    a,b,c = 1,1,0
    while c < limit:
        c = a+b
        if c % 2 == 0:
            sum += c
        b = c
        a = c - a
    print(f"Result:{sum}")

even_fibonacci_sum(4000000)


