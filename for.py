''''
for item in "python":
    print(item)

for item in range(2,20,2):
       / range (start,step,stop) index/
    print(item)
prices =[10,20,30]
total=0
for item in prices:
    total= total + item
print(f"total is:{total}")
 
 
for x in range(4):
   for y in range(4):
      print( f" ( {x},{y} )" ) 
      
numbers=[5,2,5,2,2]
for x in numbers:
    print("x" * x)

for x in numbers:
    y=""
    for z in range(x):
       y+= 'x'
    print(y)     
    '''
y=""
for x in range (5):
    y+="x"
    print(y)