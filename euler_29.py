#################### 1 ####################

def find_distinc_powers(limit):
    powers = set()
    for a in range(2,limit+1):
        for b in range(2,limit+1):
            powers.add(a**b)
            powers.add(b**a)

    print(len(powers))

find_distinc_powers(100)

#################### 2 ####################

print(len(set(i ** j for j in range(2, 101) for i in range(2, 101))))
