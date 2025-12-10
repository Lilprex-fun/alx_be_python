# Pattern Drawing with Nested Loops
# This script draws a square pattern using a while loop and nested for loop

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using a while loop for rows
row = 0
while row < size:
    # Use a for loop to print asterisks for each column
    for col in range(size):
        print("*", end="")
    # Print newline after each row
    print()
    row += 1
