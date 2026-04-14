class Dog:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def bark(self):
  print("says woof!")
d1 = Dog("Buddy", 3)
d1.bark()