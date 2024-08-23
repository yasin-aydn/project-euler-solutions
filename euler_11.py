from euler_11_grid import num_grid

def largest_product(adjacent_amount):
    global num_grid
    numbers = num_grid.split("\n")
    num_grid_list = list()

    for number in numbers:
        number = number.split(" ")
        num_grid_list.append(number)

    # vertical
    vertical_max = 0
    for row in range(len(num_grid_list)):
        for col in range(len(num_grid_list[0])-(adjacent_amount+1)):
            result = 1
            for adj in range(adjacent_amount):
                result *= int(num_grid_list[col+adj][row])
            if result > vertical_max:
                vertical_max = result

    # horizontal
    horizontal_max = 0
    for col in range(len(num_grid_list)):
        for row in range(len(num_grid_list[0])-(adjacent_amount+1)):
            result = 1
            for adj in range(adjacent_amount):
                result *= int(num_grid_list[col][row+adj])
            if result > horizontal_max:
                horizontal_max = result

    # left diagonal \
    left_diagonal_max = 0
    for col in range(len(num_grid_list)-(adjacent_amount+1)):
        for row in range(len(num_grid_list[0])-(adjacent_amount+1)):
            result = 1
            for adj in range(adjacent_amount):
                result *= int(num_grid_list[col+adj][row+adj])
            if result > left_diagonal_max:
                left_diagonal_max = result

    # right diagonal /
    right_diagonal_max = 0
    for col in range(len(num_grid_list)-(adjacent_amount+1)):
        for row in range(len(num_grid_list[0])-1,(adjacent_amount-1),-1):
            result = 1
            for adj in range(adjacent_amount):
                result *= int(num_grid_list[col+adj][row-adj])
            if result > right_diagonal_max:
                right_diagonal_max = result

    print(f"Result:{max(horizontal_max,left_diagonal_max,vertical_max,right_diagonal_max)}")

largest_product(4)