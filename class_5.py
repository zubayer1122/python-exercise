class Person:
    def  _init_(self, name, age):  # double underscores here
        self.name = name
        self.age = age

p1 = Person()
print(p1.name)
print(p1.age)