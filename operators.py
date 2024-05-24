'''name="bl"

if len(name) < 3:
 print("name must be at least 3 characters")
 
elif len(name) > 50:
 print("name can be a maximum of 50 characters")
else:
 print("name looks good")'''

weight=input ("enter your weight:  ")
unit=input(" (L)bs or  (k)g?  ")

if unit.upper() == 'L' :
 weight= int(weight) * 0.4 
 '''string cannot multipy with integer, so we have to convert weight to int(weight)'''
elif unit.upper() == 'K' :
 weight= int(weight) / 0.4
print(f" you have the weight : {weight}")
  
 
  

