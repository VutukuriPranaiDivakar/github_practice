# class variable = inside the class
# instance variable == inside the functions we called instance variable

# class computer:

#     def __init__(self, cpu, ram):
#         self.ram = ram
#         self.cpu = cpu
    
#     def config(self):
#         print(f"config is cpu : {self.cpu} and ram : {self.ram}")
    

# a = computer("i5", 12.00)
# b = computer("i7", 15.00)

# a.config()
# b.config()


    # class variable = inside the class
    # instance variable == inside the functions we called instance variable



# class student:
#     school = "youtube"
#     def __init__(self,m1, m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self):
#         return(self.m1 + self.m2 + self.m3/ 3)
    
#     @classmethod
#     def info(cls):
#         return cls.school

#     @staticmethod
#     def pass_fail():
#         print('This is the pass fail section and we can do what even we want')

# s1 = student(90,80,70)
# s2 = student(12,34,56)
# print(s1.avg())
# print(s2.avg())
# print(student.info())
# student.pass_fail()


class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(f"{self.name}, {self.rollno}")
        self.lap.show()
    
    class Laptop():
        def __init__(self):
            self.brand = "Asus"
            self.cpu = "i5"
            self.price = 10000
        
        def show(self):
            print(f"{self.brand}, {self.cpu}, {self.price}")

s1 = student("Pranai", 23)
print(s1.name, s1.rollno)

s1.show()