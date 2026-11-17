def absolute_value(num):
    """Returns the absolute value of a number without using abs()."""
    if num < 0:
        return -num
    return num

num=int(input("Enter a number: "))
print(absolute_value(num))