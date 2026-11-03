rows = 7

for i in range(rows):
    for j in range(rows):
        if (
            (i == j and i <= rows // 2)
            or (i + j == rows - 1 and i <= rows // 2)
            or (j == rows // 2 and i >= rows // 2)
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()