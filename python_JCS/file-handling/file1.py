with open("file1.txt", 'a+') as f:
    f.write("\n Details: \n\n")
    
    n = input("Enter your name:\t")
    a = int(input("Enter your age:\t"))
    p = input("Enter your country name:\t")
    
    f.writelines([f"Name: {n}\n", f"Age: {a}\n", f"Place: {p}\n"])
    
    f.seek(0)
    r = f.read()
    print(r)
