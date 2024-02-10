# էս նույն խնդիրը  lab ի ժամանկ ենք գրել, լուծումը հիշում էի (ու հասկանում)

def count_objects(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
               
                count += 1
                
                mark(matrix, i, j)

    return count


def mark(matrix, i, j):
    rows = len(matrix)
    cols = len(matrix[0])
   
    matrix[i][j] = -1

    
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_i, new_j = i + dr, j + dc
        if 0 <= new_i < rows and 0 <= new_j < cols and matrix[new_i][new_j] == 1:
            mark(matrix, new_i, new_j)


matrix = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0]
]



print(count_objects(matrix))
