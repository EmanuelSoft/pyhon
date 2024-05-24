'''numbers=[4,5,2,3,7,6,8]
for x in numbers:
    largest=x
    for y in numbers[1:]:
        if y > largest:
            largest=y
            
print(largest)
         
         '''
'''
remove dupplicate number exe....
numbers=[2,5,3,5,6,5,3,7]
unique=[]
for no in numbers:
     if no not in unique:
        unique.append(no)
print(unique)
'''
'''
phone= input("enter phone number")
digit_mapping={
    "1":"one",
    "2":"two",
    "3":"three"
}
ph=""
for ch in phone:
    ph+=digit_mapping.get(ch) + " "
print(ph)    
'''
class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f" hi, i am {self.name}")
amanu=Person("amanu")
bura=Person("bura")
amanu.talk()
bura.talk()