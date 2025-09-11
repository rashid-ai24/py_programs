class student:
    def __init__(self, rno, name, fname, age, place):
        self.rno=rno
        self.name=name
        self.fname=fname
        self.age=age
        self.place=place

    def display1(self):
        print("Roll No.: ", self.rno)
        print("Name: ", self.name)
        print("Father Name: ", self.fname)
        print("Age: ", self.age)
        print("Place: ", self.place)

class dept(student):
    def __init__(self, dname, year):
        self.dname=dname
        self.year=year

    def display2(self):
        print("Department: ",self.dname)
        print("Year: ", self.year)
        
        

obj=student(28,'Rashid', 'abc', 18, 'nagercoil')
obj1=dept('AI&DS', 2)

obj.display1()
obj1.display2()
