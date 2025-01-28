#  polymorphism refers to a function or method taking different forms in different contexts
# one thing which behaves in differnt way
# Duck Typing
# Operator Overloading
# Method Overriding
# Method Overloading

# 1) duck typing
class Duck:

   def sound(self):
      return "Quack, quack!"

class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"

def makeSound(duck):
   print(duck.sound())

# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)   
makeSound(anotherBird) 


    