def lattice_path_finder(width,height):
    grid = list([0]*(width+1) for _ in range(height+1))


    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if row == 0 or col == 0:
                grid[col][row] = 1
            else:
                grid[col][row] = grid[col-1][row] + grid[col][row-1]
    print(grid)
    print(f"Result:{grid[-1][-1]}")

lattice_path_finder(20,20)