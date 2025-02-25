#################### 1 ####################

total = 1
for hundred in range(0, 201, 100):
    for fifty in range(0, 201 - hundred, 50):
        for twenty in range(0, 201 - (hundred + fifty), 20):
            for ten in range(0, 201 - (hundred + fifty + twenty), 10):
                for five in range(0, 201 - (hundred + fifty + twenty + ten), 5):
                    a = 200 - (hundred + fifty + twenty + ten + five)
                    total += 1 + a//2

print(total)

#################### 2 ####################

def nos(a,l):
    if a<0:
        return 0
    elif len(l)==1:
        if a%l[0]==0:
            return 1
        else:
            return 0
    else:
        return nos(a-l[0],l)+nos(a,l[1:])
    
print(nos(200,[200,100,50,20,10,5,2,1]))

def fact(x):
    if x == 1:
        return x
    else:
        return fact(x-1)*x
    
print(fact(5))