import random
rn=random.randint(0,10)
jackpot=random.randint(0,10)
a=int(input("enter a number ="))
assert 0<=a<=10, "please enter number between 0 to 10"
print("random number was ",rn,"\n jackpot was on",jackpot)
if rn==a:
    print("you win")
    if a==jackpot:
        print("you got a jackpot")
elif (rn+1==a) or (rn-1==a):
    print("you were too close")
else:
    print("you lose")