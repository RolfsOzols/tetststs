# Right-aligned steps
def right_steps(step):
    for i in range(1, step + 1):
        print(" " * (step - i) + "#" * i)

# Left-aligned steps
def left_steps(step):
    for i in range(1, step + 1):
        print("#" * i)

# Pyramid steps (with 2 spaces in between)
def pyramid_steps(step):
    for i in range(1, step + 1):
        print("#" * i + "  " + "#" * i)

# Core function to request step input and run the desired pattern
def main():
    while True:
        try:
            # Request user input for step count between 1 and 8
            step = int(input("Enter a number between 1 and 8: "))
            if 1 <= step <= 8:
                print("\nRight-aligned steps:")
                right_steps(step)

                print("\nLeft-aligned steps:")
                left_steps(step)

                print("\nPyramid steps:")
                pyramid_steps(step)
                break
            else:
                print("Please enter a valid number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 8.")

# Run the program
if __name__ == "__main__":
    main()

