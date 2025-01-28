# yield will make u code that it is a ganerator

class Student:
    
    def passed(self):
        print("He passed all the subjects")
        yield
    def failed(self):
        print("he failed all the subjects")

s = Student()
s.passed()
print("end")
s.failed()