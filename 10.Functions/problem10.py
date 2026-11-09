def print_pyramid(rows):
    for i in range(rows):
        spaces = " " * (rows - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

height = 5
print_pyramid(height)