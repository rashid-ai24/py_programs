import numpy as np

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print("The data type of the array is: ",arr.dtype,'\n')
print(" The dimension of the array is: ",arr.ndim,'\n')

for i in arr:
    print(i,)

print(' ')

for a in arr:
    for b in a:
        print(b)

print(' ')
for x in arr:
    for y in x:
        for z in y:
            print(z)
    