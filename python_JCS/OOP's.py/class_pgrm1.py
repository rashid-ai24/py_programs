class Student:
    def __init__(self,name, rno,):
        self.name=name
        self.rno=rno

    def display(self):
        print("Name is: ", self.name)
        print("Roll No: ", self.rno)

r=int(input("Enter the roll no: "))
n=input("Enter the name: ")
obj=Student(n,r)
obj.display()

print("Name taken:", obj.name)
print('Roll No taken:',obj.rno)

