# Height of the upper half of the diamond (including the middle row)
n = 5

print("--- Diamond Pattern ---")

# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)