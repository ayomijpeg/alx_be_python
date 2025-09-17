# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns (print stars in one row)
    for col in range(size):
        print("*", end="")  # stay on the same line
    print()  # move to the next line after finishing a row
    row += 1
