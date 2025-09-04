f=input("Enter the file name: ")
with open(f, "a") as file:
    a=input("Enter text: ")
    file.write(a+"\n")
    print("added to the csv file.")  

