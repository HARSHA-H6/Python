# Step1: Taking in the input

def isleap(year:int):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    return False

year = int(input("Enter the year: "))
answer = isleap(year)
if(answer):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

