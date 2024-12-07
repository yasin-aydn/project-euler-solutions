#################### 1 ####################

def find_pythogoras_triplet(number):
    triplet = None
    for a in range(1,number):
        for b in range(1,number-a):
            if a + b > number:
                break
            c = number - (a + b)
            if a**2 + b**2 == c**2 and a + b + c == number:
                triplet = a*b*c
                triplet_numbers = a,b,c
                break
    if triplet:
        print(f"Result:{triplet}\nTriplet number:{triplet_numbers}")
    else:
        print("No results found.")

find_pythogoras_triplet(1000)

