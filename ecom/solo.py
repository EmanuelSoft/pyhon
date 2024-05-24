''''contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
name=input()
for x in contacts:
    if name in x:
     print(str(x[0]) + " is " + str(x[1]))
     break
else:
       print("Not Found")
skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
print(skills&job_skills)
nums = [i*2 for i in range(10)]
print(nums)
word=input(">")
word=list(word)
reg=['a','e','i','o','u','A','E','I','O','U']
out=[i for i in word if  not i in reg ]
print(list(out))
def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2)) 
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
    for i in range(a,b):
     if isPrime(i)==True:
      yield i
    
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))'''
def my_min(*args):
    return min(args)  
      
print(my_min(8, 13, 4, 42, 120, 7))