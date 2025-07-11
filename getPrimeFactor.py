prime_factors=[]

def get_prime_factors(number):
    if type(number) is not int or number<2:
        return prime_factors
    
    while number %2 ==0:
        prime_factors.append(2)
        number = number//2
    if number==1:
        return prime_factors
    
    start_range = 3
    stop_range = number**0.5<3 or number**0.5
    skip_range = 2

    for prime_number in range(start_range, int(stop_range)+1,skip_range):
        while number %prime_number==0:
            prime_factors.append(prime_number)
            number = number//prime_number

    
    if number>2:
        prime_factors.append(number)

    return prime_factors


number = int(input("Enter the number: "))
print(f"Prime factors of the number {number} is {get_prime_factors(number)}")



