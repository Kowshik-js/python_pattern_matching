def print_pattern():
    size = 5
    for i in range(size):
        for space in range(i):
            print(" ", end=" ")
        for num in range(size - i, 0, -1):
            print(num, end=" ")
        print()
print_pattern()
