def add(x:int,y:int):
    return x+y

try:
    value1 = int(input("Enter the first number "))
    value2 = int(input("Enter the second number "))
    print(f"The sum of {value1} and {value2} is {add(value1,value2)}")

except ValueError as e:
    print(f"Oops {e}\n That was not vaild input try again")

except:
    print("Try again and enter the proper value")
