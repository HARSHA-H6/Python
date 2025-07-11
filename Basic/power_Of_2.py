import sys
def power_of_2(number:int):
    if number<0 or number>=31:
        print(f"N must betwen 0 and 30 ")
        return
    
    for i in range(number):
        print(f"2^{i}={2**i}")

if len(sys.argv)<1:
    print("Please enter the input value in the command line argument")
else:
    try:
        number = int(sys.argv[1])
        power_of_2(number)
    except ValueError as ex:
        print("Invalid input","Please enter the valid input",sep="\n")
    