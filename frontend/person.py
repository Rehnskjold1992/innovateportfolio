
class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age
        
    def talk(self):
        print(
            f"Hello, my name is {self.name}, I am {self.age} years old, and {self.height} tall.")

will = Person("Will", "31", "6ft0")

print(will.name)
print(will.age)
print(will.height)
will.talk()

# class Person():
#     def __init__(self, name, age, height):
#         self.name = name
#         self.height = height
#         self.age = age

#     def talk(self):
#         print(
#             f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.height} tall!")


# will = Person("Will", 31, "6'0''")

# print(will.name)
# print(will.age)
# print(will.height)
# will.talk()