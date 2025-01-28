# # a = 3
# # b = 5

# # print(a + b)
# # print(int.__add__(a, b))

# class student:

#     def __init__(self,m1, m2):
#         self.m1 = m1
#         self.m2 = m2
    
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         m3 = student(m1, m2)
#         return m3
    
#     def __get__(self,other):
#         r1 =self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1 > r2:
#             return True
#         else:
#             return False

    
# s1 = student(120,34)
# s2= student(124,342)

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)