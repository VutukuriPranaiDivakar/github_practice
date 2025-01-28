class A:
    
    def __init__(self):
        print("This is in a class")
    
    def feature1(self):
        print("this is a feature1")
    def feature2(self):
        print("this is a feature2")

class B:
    
    def __init__(self):
        super().__init__()
        print('This is in b class')
    
    def feature3(self):
        print("this is a feature3")
    
    def feature4(self):
        print("this is a feature4")

class c(A, B):
    def __init__(self):
        super().__init__()
        print("THis is in c class")

a1 = c()
a1.feature1()
print(c.mro())
