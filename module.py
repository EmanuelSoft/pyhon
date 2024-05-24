import random

#for i in range(4):
    #print(random.random())
class Dice:
    
    def roll(self):
        first=random.randinet(1,6)
        second=random.randinet(1,6)
        return f"( {first} , {second} )"

prob=Dice()
print(prob.roll())

