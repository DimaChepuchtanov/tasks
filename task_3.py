matrix_numbers = [["0", 0, 0, 3, 0, 0, 1, 0, 0, 0],
[0, 4, 0, 0, 2, 0, 0, 0, "0", 0],
[0, 0, 1, 0, "1", 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, "4", 0, 0, 0, 0, 0, 0, 7],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, "0", 0, 0, 5, 0, "6", 0, 0, 0],
[5, 0, 0, 0, 0, 0, 3, 4, 0, 0],
[0, 0, 0, 3, "0", 0, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

num_coord={}

for i in range(len(matrix_numbers)):
  for j in range(len(matrix_numbers[i])):
    matrix_numbers[i][j] = int(matrix_numbers[i][j])

for i in range(len(matrix_numbers)):
  for j in range(len(matrix_numbers[i])):
    if matrix_numbers[i][j] !=0 and matrix_numbers[i][j] not in num_coord:
      num_coord[matrix_numbers[i][j]] = [1,[[j+1,i+1]]]
    elif matrix_numbers[i][j] in num_coord:
      count = num_coord[matrix_numbers[i][j]][0]
      koord = num_coord[matrix_numbers[i][j]][1]
      count+=1
      koord.append([j+1,i+1])
      num_coord[matrix_numbers[i][j]] = [count,koord]
print(num_coord)
