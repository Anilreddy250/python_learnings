matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = len(matrix)
#step1 : transpose the matrix
for i in range(n):
    for j in range(i+1, n):
        #swap the elements aceoss the diagonal
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#step 2 reverse each row
for i in range(n):
    matrix[i].reverse()
# print the rotated matrix
print("matrix after 90-degree clockwise rotation:")
for row in matrix:
    print(row)
