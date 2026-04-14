#Generate the first n numbers in the Fibonacci sequence
n = 5
a ,b = 0,1
for _ in range(n):
    print(a, end=' ')
    a , b = b, a+b
    print(a, b)