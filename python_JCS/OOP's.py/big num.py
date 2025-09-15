class big:
    def __init__(self, n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3

    def big1(self):
        if self.n1>self.n2 and self.n1>self.n3:
            print("The big num is:", self.n1)
        elif self.n2>self.n1 and self.n2>self.n3:
            print("The big num is: ", self.n2)
        else:
            print("The big num is: ", self.n3)
    
    def big1(self):
        if self.n1>self.n2:
            print("The big num is:", self.n1)
        else:
            print("The big num is: ", self.n2)



n1=input("Enter the number:")
n2=input("Enter the number:")
n3=input("Enter the number:")
obj=big(n1,n2,n3)
obj.big1()