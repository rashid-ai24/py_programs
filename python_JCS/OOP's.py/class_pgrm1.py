class Student:
    def __init__(self,name, rno,):
        self.name=name
        self.rno=rno

    def display(self):
        print("Name is: ", self.name)
        print("Roll No: ", self.rno)

obj=Student('Rashid', 3064)
obj.display()

print("Name taken:", obj.name)
print('Roll No taken:',obj.rno)

