# method overloading ::

def add(*nums):
   return sum(nums)

result1 = add(10, 25)
result2 = add(10, 25, 35)

print(result1)  
print(result2) 

# Method Overriding ::

class A:
   def show(self):
      print("this is a show")

class B(A):
   def show(self):
      print("this is b show")

z = B()
z.show()