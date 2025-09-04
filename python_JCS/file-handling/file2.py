import os

def add():
    note = input("Enter the Note: ")
    with open("note_1.txt", 'a') as f:
        f.write(note + "\n")
    print("Note added successfully!")

def view():
    if not os.path.exists("note_1.txt"):
        print("File didn't exist")
        return
    
    with open("note_1.txt", 'r') as f:
        lines = f.readlines()
        
    if len(lines) == 0:
        print("The note is empty.")
        return
    
    print("\nYour Notes:")
    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")

while True:
    print("\n====== NOTES ======")
    print("1. Add Notes")
    print("2. Read Notes")
    print("3. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number.")
        continue
    
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        print("\nExiting program. Bye!")
        break
    else:
        print("Invalid choice.")