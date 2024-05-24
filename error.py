try:
    age=int(input("Age: "))
    income =200
    risk= income/age
except ZeroDivisionError:
    print("zero cannot be  age.")
except ValueError:
 print("invalid value")
 