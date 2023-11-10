"""Creates function that lets me switch possition of elements in periotic table list
to account for the five exceptions to the trend (increase in mr = increase in p+ #)"""
import float_input


def guess_the_mass_test():
    while True:
        # Test: Guess the Mass
        random_position = random.choice(list(periodic_table.keys()))
        random_element = periodic_table.get(random_position)

        if random_element is not None:
            correct_mass = random_element[1]

            print(f"Guess the mass of the element {random_element[0]}:")

            attempt = 0
            while attempt < 3:
                user_input = input(f"Attempt {attempt + 1}: Your guess: ")

                try:
                    user_guess = float(user_input)
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
                    continue

                attempt += 1

                if user_guess == correct_mass:
                    print("Correct!")
                    return  # Exit the function if the guess is correct
                else:
                    print("Wrong! Try again.")

            print("Sorry, you've failed three times.")
            retry = input("Do you want to try again? (yes/no): ").lower()
            if retry != 'yes':
                return  # Exit the function if the user chooses not to retry
        else:
            print("Error: Unable to select a random element.")




import integer_input
import string_input
import sys
import random

# Step 1: Importing the Data
data = []

with open('/Users/axelschelander/Desktop/KTH/DATAP/csc.kth.se_~lk_P_avikt.txt', 'r') as file:
    for line in file:
        symbol, mass = line.strip().split()
        data.append((symbol, float(mass)))

# Step 2: Sorting by Atomic Mass
sorted_data = sorted(data, key=lambda x: x[1])

# Step 3: Organizing into a Periodic Table Dictionary
periodic_table = {}

# Assuming 9 rows (7 for the main blocks and 2 for the lanthanides) and 18 columns for simplicity
num_rows = 9
num_cols = 18

# Populating the main block elements
for idx, (symbol, mass) in enumerate(sorted_data):
    row_index = idx % num_rows
    col_index = idx // num_rows
    position = (row_index, col_index)
    periodic_table[position] = (symbol, mass)

# Function to swap two elements in the periodic table
def swap_elements(table, index1, index2):
    row1, col1 = divmod(index1, num_cols)
    row2, col2 = divmod(index2, num_cols)

    if (row1, col1) in table and (row2, col2) in table:
        table[(row1, col1)], table[(row2, col2)] = table[(row2, col2)], table[(row1, col1)]

# Example usage: swapping elements at index 0 and 1
swap_elements(periodic_table, 0, 1)

# Populating the main block elements
for row in range(num_rows):
    for col in range(num_cols):
        idx = row + col * num_rows  # Calculate the index based on row and column
        if idx < len(sorted_data):
            symbol, mass = sorted_data[idx]
            position = (row, col)
            periodic_table[position] = (symbol, mass)

swap_elements(periodic_table, 17, 18)
swap_elements(periodic_table, 26, 27)
swap_elements(periodic_table, 51, 52)
swap_elements(periodic_table, 89, 90)
swap_elements(periodic_table, 91, 92)

# ... (previous code)

# ... (previous code)

while True:
    print("Välj ett alternativ:")
    print("1. Print all elements")
    print("2. Practice atomic numbers")
    print("3. Practice abbreviations")
    print("4. End")
    print("")

    choice = int(input("What do you want to do? (1, 2, 3, 4): "))

    if choice == 1:
        # Assuming num_rows and num_cols are defined earlier in your code
        num_rows = 9
        num_cols = 18

        # Sorting the periodic table items based on keys
        sorted_elements = sorted(periodic_table.items(), key=lambda x: (x[0][0], x[0][1]))

        # Printing the updated Periodic Table
        for position, element in sorted_elements:
            print(f'{element[0]} {element[1]:.3f}', end=' ')
            if position[1] == num_cols - 1:
                print()  # Move to the next row

    elif choice == 2:
        while True:
            guess_the_mass_test()
            continue_playing = input("Do you want to continue practicing atomic numbers? (yes/no): ").lower()
            if continue_playing != 'yes':
                break

    elif choice == 4:
        sys.exit()
    else:
        print("Prova igen med ett tal mellan 1-4")