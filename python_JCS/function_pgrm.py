def calc(a):
    match a:
        case 1:
            print("Addition of two nunber:")
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number:"))
            c=a+b
            print(f"The addition of the two numbers is {c}")
        case 2:
            print("Subtraction of two numbers")
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number: "))
            c=a-b
            print(f"The subtraction of the two numbers is {c}")
        case 3:
            print("Multiplication of two numbers")
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number: "))
            c=a*b
            print(f"The multiplication of the two numbers is {c}")
        case 4:
            print("Division of two numbers")
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number: "))
            try: 
                c=a/b
                print(f"The division of the two numbers is {c}")
            except ZeroDivisionError:
                print("Can't divide by zero:")
        case _:
            print("invalid input")

while True:
    print("This is a calculation program")
    print("0.Exit, 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division")
    a=int(input("Enter your choice: "))
    if a==1 or a==2 or a==3 or a==4:
        calc(a)
    elif a==0:
        print("Exiting program:")
        break
    else:
        print("Invalid choice.")
