# positional arguments ::
print("this is positional arguments")
def details(name, age):
    print(f"My name is {name}")
    print(f"my age is {age}")

details("Pranai", 22)
print()
# keyword arguments ::
print("this is keyword arguments")
def information(name, age):
    print(f"this is my {name}")
    print(f"this is my {age}")

information(age=23,name="divakar")
print()
# default argument ::
print("this is default argument")

def bio(name,age=22,salary=2000,):
    print(f"this is my {name}")
    print(f"this is my {age}")
    print(f"this is my {salary}")

bio("pranai",24)
    
print()

# variable length argument :: *args **kwargs
print("this is *args argument.") # in tuple format
def adding(*args):
    c = 0
    for i in args:
        c += i
    print(c)
    
adding(10,20,30,40)

print("this is **kwargs argument") # in dictionary format
def details(name, **information):
    print(name)
    for i, j in information.items():
        print(i,":", j)

details("Pranai", age=22, work="kali", income= "no")

def another(a, **b):
    print(a)
    print(b)
another("Pranai", age=22, work="kali", income= "no")