def print_m():
  height = 7
  width = 7

  for i in range(height):
    for j in range(width):
      # Conditions for printing '*'
      # 1. Left and right vertical borders: j == 0 or j == width - 1
      # 2. Left and right diagonals: i == j and i <= height // 2
      if (
          j == 0
          or j == width - 1
          or (i == j and i <= height // 2)
          or (i + j == width - 1 and i <= height // 2)
      ):
        print("*", end="")
      else:
        print(" ", end="")
    print()  # Move to the next line after each row


print_m()