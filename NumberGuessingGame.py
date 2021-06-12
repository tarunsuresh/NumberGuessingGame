import random
data=int(input("Guess a number between 1-9 :"))
value=random.randrange(1,10)
chance=0
print(value)


while chance<5:
    if(data>value):
        print("guess a number lower than it")
        data=int(input("Guess a number enter Your Guess again :"))
        chance=chance+1
    if(data<value):
        print("guess a number more than it")
        data=int(input("Guess a number enter Your Guess again :"))
        chance=chance+1
    if(data==value):
        print("You won")
        break
if(chance==5 and value!=data):
    print("you lose")


