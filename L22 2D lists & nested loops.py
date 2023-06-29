number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# first we will type row's index position then we will type element's index position to get its value as output

print(number_grid[0][2])  # this will print element at index position 2 of the row which is at index position 0
print(number_grid[2][2])  # this will print element at index position 2 of the row which is at index position 2

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)
