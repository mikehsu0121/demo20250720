class CPU:
    def run(self):
        print("CPU开始运行!")
    
class Disk:
    def run(self):
        print("Disk开始运行!")

class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

    def run(self):
       self.cpu.run()
       self.disk.run()
       print("computer开始运行!")


if __name__=="__main__":
    test=12

    cpu=CPU()
    print(cpu)
    disk=Disk()
    print(disk)

    computer=Computer(cpu,disk)

    computer.run()
