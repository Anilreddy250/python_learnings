from array import *

arr = array("i",[])
n = int(input("enter the length od the array"))
for i in range(5):
    x = int(input("Enter the lenth of the nest value"))
    arr.append(x)
# print(arr.index(1))
print(arr)

val = int(input("ENter the valie for search"))
k = 0
for e in arr:
    if e==val:
        print(k)
        break    
    k+=1

print(arr.index(val))
        

