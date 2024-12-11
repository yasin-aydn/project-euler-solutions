from euler_18_triangle import triangle

def find_max_path(triangle):
    triangle_grid = []
    
    for i in triangle.split("\n"):
        grid_list = i.split(" ")
        grid_list = list(map(int, grid_list))
        triangle_grid.append(grid_list)

    for i in triangle_grid:
        print(i)
    
    for row in range(len(triangle_grid) - 2, -1, -1):
        for col in range(len(triangle_grid[row])):
            triangle_grid[row][col] += max(triangle_grid[row + 1][col], triangle_grid[row + 1][col + 1])
    
    print("Result:", triangle_grid[0][0])

    for i in triangle_grid:
        print(i)

find_max_path(triangle)