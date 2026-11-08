def print_triangle(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "* " * i
        print(spaces + stars)

n = 5
print_triangle(n)