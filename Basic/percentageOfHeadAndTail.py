import random
number = int(input("Enter how many times we have to flip the coin: "))

percent=0.0
head=0
tail=0

for i in range(number):
    coin = random.random()
    if(coin<=0.5):
        tail+=1
    else:
        head+=1

print(f"The number of times head occured {head}")
print(f"The number of times tail occured {tail}")
print(f"The pecentage of head is {(head/number)*100}%")
print(f"The pecentage of tail is {(tail/number)*100}%")