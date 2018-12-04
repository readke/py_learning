class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

dog = Dog("kal",5)
dog.sit()
dog.roll_over()
print(dog.name)
print(dog.age)
dog2 = Dog("lili",6)
dog2.sit()
dog2.roll_over()
print(dog2.name)
print(dog2.age)