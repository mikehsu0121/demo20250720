def sum(a,b):
    return a+b

class Student:
    
    Total=100

    @staticmethod
    def advance():

        print("学生都进步了！")


    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    
    def introduceSelf(self):
        print(f"学生姓名为{self.name},学生年龄为{self.age},学生成绩为{self.score}")

if __name__=="__main__":
    mike=Student("Mike",12,100)
    mike.introduceSelf()

    # print(Student.Total)
    # Student.advance()

    mike.height=180
    mike.weight=80

    print(mike.height)
    print(mike.weight)

    mike.test=sum
    print(mike.test)

    print(mike.test(1,1))

    test=Student("test",12,100)
