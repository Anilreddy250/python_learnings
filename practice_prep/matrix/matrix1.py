
# square = [
#     [5, 1, 0],
#     [0, 5, 1],
#     [1, 0, 5]
# ]
# total = 0
# r = range(len(square))
# print(r)
# for i in range(len(square)):
#     print(i)
#     total += square[i][i]
#     print(square[i][i])

# print("Sum of diagonal:", total) # Output should be 15

matrix_A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matric_B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
# results = [
#     [],
#     [],
#     []
# ]
results = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
#iterate through rows
for i in range(len(matrix_A)):
    #iterate through columns
    for j in range(len(matrix_A[0])):
        results[i][j] = matrix_A[i][j] + matric_B[i][j]
print(results)
print("Sum of the two matrices")
for row in results:
    print(row)
