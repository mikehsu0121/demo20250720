class Animal:
    def __init__(self,age):
        self.age=age
    
    def sound(self):
        print("我在发出声音！")


if __name__=="__main__":
    myAnimal=Animal(12)
    myAnimal.sound()
