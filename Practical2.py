def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print '*' characters
        for k in range(2 * i - 1):
            print("*", end="")
        print()

def print_reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print '*' characters
        for k in range(2 * i - 1):
            print("*", end="")
        print()

def main():
    rows = int(input("Enter the number of rows for the pyramid: "))

    print("\nPyramid:")
    print_pyramid(rows)

    print("\nReverse Pyramid:")
    print_reverse_pyramid(rows)

if __name__ == "__main__":
    main()
