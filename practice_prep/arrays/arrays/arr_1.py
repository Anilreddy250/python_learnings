import array as arr
from array import *

# array.array() # function of array()
# arr.array()
vals = array('i',[5,9,8,4,2])

newArr =array(vals.typecode, (a*a for a in vals))

# print(vals.buffer_info())
# print(vals.reverse())
# for i in range(5):
#     print(vals[i])
# for e in newArr:
#     print(e)

# for i in range(len(vals)):
#     print(vals[i])
i=0
while i<len(newArr):
    print(newArr[i]) 
    i+=1
