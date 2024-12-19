def cycle_length(d):
    kalanlar = {}
    kalan = 1
    pozisyon = 0
    
    while kalan != 0:
        if kalan in kalanlar:
            return pozisyon - kalanlar[kalan]
        
        kalanlar[kalan] = pozisyon
        kalan = (kalan * 10) % d
        pozisyon += 1
    
    return 0

def calc(limit):
    highest_cycle = 0
    cycle_number = 0
    for i in range(1,limit):
        if cycle_length(i) > highest_cycle:
            highest_cycle = cycle_length(i)
            cycle_number = i

    print(f"Result:{cycle_number}")

calc(1000)