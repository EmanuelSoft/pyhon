''' unpacking'''
numbers=(1,2,3)
x,y,z= numbers
'''dictionaries=storing keys'''
customer={
    "name":"emanuel bekele",
    
    "age":25,
    "is_verified":True,
}
customer["sex"]="male"
print(customer.get("age"))
print(customer.get("birth","feb 28 2000"))
print(customer["sex"])
print(customer.items())
# there are 3 method  to cacth infor from dictionary easily ... .key(),.value(),.item()