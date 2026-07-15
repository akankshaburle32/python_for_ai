### Ek 3x3 grid ke saare items nested loop se print karo. ###

grid = [
            [5, 6, 9],
            [3, 8, 3],
            [7, 6, 7],
        ]

for row in grid:
     for col in row:
        print(col, end =" ")

     print()
