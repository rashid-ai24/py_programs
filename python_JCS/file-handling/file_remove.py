import os

d=input("Enter the file to delete: ")
if os.path.exists(d):
    os.remove(d)
    print("File successfully removed:")

else:
    print("File dosen't exist:")
