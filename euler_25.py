def even_fibonacci_sum(digit):
    liste = [1] * 2
    index = 2
    while len(str(liste[-1])) < digit:
        new_number = liste[-1]+liste[-2]
        liste.append(new_number)
        index += 1
        liste.pop(0)

    print(f"Result:{index}")

even_fibonacci_sum(1000)