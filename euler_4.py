#################### 1 ####################


def largest_palindrome_product(product_digit,factor_digit):
    highest_number = 0
    for i in range(10**factor_digit,10**(factor_digit-1),-1):
        for y in range(10**factor_digit,10**(factor_digit-1),-1):
            number = str(i*y)
            if len(number) != product_digit:
                continue
            if number == number[::-1]:
                if int(number) > highest_number:
                    highest_number = int(number)
                    factor1 = i
                    factor2 = y

    if highest_number == 0:
        print("No results found.")
    else:
        print(f"Result:{highest_number}\nFactors:{factor1,factor2}")


largest_palindrome_product(6,3)

#################### 2 ####################

def make_palindromic(number,lenght):

    if len(str(number))*2 == lenght:
        number = str(number) + str(number)[::-1]
        return number
    elif len(str(number))*2-1 == lenght:
        number = str(number) + str(number)[1::-1]
        return number
    else:
        return False

def find_divisors(number,digit):
    for q in range(1,int(number**0.5)+1):
        if number % q == 0:
            if len(str(q)) == digit and len(str(number//q)) == digit:
                return True
            
def largest_palindrome(product_digit,factor_digit):
    highest_number = 0
    for i in range(10**product_digit//2,10**(product_digit//2-1),-1):
        palindromic_number = make_palindromic(i,product_digit)
        palindromic_number = int(palindromic_number)
        if find_divisors(palindromic_number,factor_digit):
            if highest_number < palindromic_number:
                highest_number = palindromic_number
                
    print(f"Result:{highest_number}")


largest_palindrome(6,3)    
