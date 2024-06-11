def print_pattern():
    size = 5  # Define the size of the pattern
    for i in range(size):
        for j in range(size):
            # Check conditions to print *
            if (i == j) or (i + j == size - 1):
                print('*', end=" ")
            else:
                print(' ', end=" ")
        print()  # Move to the next line after each row

print_pattern()
