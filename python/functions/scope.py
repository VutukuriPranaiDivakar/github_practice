# global scope or variable :: outside the function is called global 
# local scope or variable :: inside the function is called local
# x = globals()["a"] # will access all the variables
a = 10
b = 30
c =40

def add():
    global a
    a = 20
    print("inside fun :",a)
add()
print("outside :",a)

