class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")


# Creating an instance of the Person class
person1 = Person("Angela", 21, "Female")

# Calling the introduce method
person1.introduce()
