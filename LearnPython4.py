class Animal:
    def __init__(self,age):
        self.age=age
    
    def sound(self):
        print("我在发出声音！")

class Pet:
    def __init__(self,name):
        self.name=name
    
    def eat(self):
        print(f"{self.name}说我在吃东西!")

class Dog(Animal,Pet):
    def __init__(self, age, name):
        Animal.__init__(self,age)
        Pet.__init__(self,name)
    
    def sound(self):
        print("汪汪汪")
    
    def eat(self):
        print(f"{self.name}说我在吃骨头!")
    


if __name__=="__main__":
    myDog=Dog(12,"欢欢")
    myDog.sound()
    myDog.eat()