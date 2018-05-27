m = [[1,2,3],[4,5,6],[7,8,9]]
# Get column 3, index 2 of each list set/row in matrix
col2 = [row[2] for row in m]
print(col2)
#  adds 1 to each filtered column
colplus = [row[1] + 1 for row in m ]
print(colplus)
# filters out odd nums
colif = [row[1] for row in m if row[1] % 2 == 0]
print(colif)