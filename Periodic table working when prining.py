import random
import tkinter as tk

correct_answer = None
correct_mass_answer = None
answers = None

def read_periodic_table(file_path):
    periodic_table = []
    with open('/Users/axelschelander/Desktop/KTH/DATAP/csc.kth.se_~lk_P_avikt.txt', 'r') as f:
        for line in f:
            element_info = line.strip().split()
            if len(element_info) >= 2:
                mass = float(element_info[1])
                element_data = {'element': element_info[0], 'mass': mass, 'proton_number': None}
                periodic_table.append(element_data)

    sorted_table = sorted(periodic_table, key=lambda x: x['mass'])

    max_row, max_col = divmod(len(sorted_table), 28)

    for i, element_data in enumerate(sorted_table):
        element_data['proton_number'] = i + 1
        element_data['row'] = i // 28
        element_data['col'] = i % 28

    return sorted_table

def assign_periodic_table_positions(table):
    for i, element in enumerate(table):
        element['row'] = i // 28
        element['col'] = i % 18



def calculate_column_widths(periodic_table):
    col_widths = [0] * len(periodic_table[0])

    for row in periodic_table:
        for col, element in enumerate(row):
            element_name_len = len(f"{element['symbol']} ({element['name']})")
            col_widths[col] = max(col_widths[col], element_name_len)

    return col_widths




def swap_elements_by_index(table, index1, index2):
    if 0 <= index1 < len(table) and 0 <= index2 < len(table):
        temp_proton_number = table[index1]['proton_number']
        table[index1]['proton_number'] = table[index2]['proton_number']
        table[index2]['proton_number'] = temp_proton_number

        # Sort the table based on proton numbers
        table.sort(key=lambda x: x['proton_number'])

        # Update row and col values after sorting
        assign_periodic_table_positions(table)
    else:
        print(f"Invalid indices: ({index1}, {index2})")


def setup_periodic_table_cells(frame, table):
    # Determine the number of rows and columns needed based on the maximum row and column values in the table
    max_row = max(element['row'] for element in table)
    max_col = max(element['col'] for element in table)

    # Add extra rows and columns to accommodate all elements
    base_grid = [[None] * (max_col + 1) for _ in range(max_row + 1)]

    # Iterate through the table and fill in the base grid
    for element in table:
        row, col = element['row'], element['col']
        element_name_str = f"{element['element']}\n{element['proton_number']}"

        # Create a label for the element with name and proton number on separate lines
        label_name = tk.Label(frame, text=element_name_str, padx=10, pady=5, borderwidth=1, relief="solid")

        try:
            # Place the label in the appropriate cell
            base_grid[row][col] = label_name
            print(f"Placing {element['element']} in row {row}, column {col}")
        except IndexError as e:
            print(f"Error placing {element['element']} in row {row}, column {col}: {e}")

    # Add labels to the frame using the base grid
    for row, labels_in_row in enumerate(base_grid):
        for col, label in enumerate(labels_in_row):
            if label:
                # Place the label in the appropriate cell
                label.grid(row=row, column=col, padx=2, pady=2)




def map_to_mendeleev_layout(periodic_table):
    # Create a dictionary to map proton numbers to row and column positions
    mandeleev_layout = {
        1: (1, 1), 2: (1, 18),
        3: (2, 1), 4: (2, 2), 5: (2, 13), 6: (2, 14), 7: (2, 15), 8: (2, 16), 9: (2, 17), 10: (2, 18),
        11: (3, 1), 12: (3, 2), 13: (3, 13), 14: (3, 14), 15: (3, 15), 16: (3, 16), 17: (3, 17), 18: (3, 18),
        19: (4, 1), 20: (4, 2),21: (4, 3), 22: (4, 4),23: (4,5), 24: (4, 6),25: (4, 7), 26: (4, 8),27: (4, 9), 28: (4, 10), 29: (4, 11), 30: (4, 12), 31: (4, 13), 32: (4, 14),33: (4, 15), 34: (4, 16), 35: (4, 17), 36: (4, 18),
        37: (5, 1), 38: (5, 2),39: (5, 3), 40: (5, 4),41: (5, 5), 42: (5, 6),43: (5, 7), 44: (5, 8),45: (5, 9), 46: (5, 10),47: (5, 11), 48: (5, 12),49: (5, 13), 50: (5, 14),51: (5, 15), 52: (5, 16), 53: (5, 17), 54: (5, 18),
        55: (6, 1), 56: (6, 2),57: (8, 3), 58: (8, 4), 59: (8, 5), 60: (8, 6), 61: (8, 7), 62: (8, 8),63: (8, 9), 64: (8, 10), 65: (8, 11), 66: (8, 12), 67: (8, 13), 68: (8, 14),69: (8, 15), 70: (8, 16), 71: (6, 3), 72: (6, 4), 73: (6, 5), 74: (6, 6),75: (6, 7), 76: (6, 8), 77: (6, 9), 78: (6, 10), 79: (6, 11), 80: (6, 12),81: (6, 13), 82: (6, 14), 83: (6, 15), 84: (6, 16), 85: (6, 17), 86: (6, 18),
        87: (7, 1), 88: (7, 2), 89: (9, 3), 90: (9, 4), 91: (9, 5), 92: (9, 6),93: (9, 7), 94: (9, 8), 95: (9, 9), 96: (9, 10), 97: (9, 11), 98: (9, 12),99: (9, 13), 100: (9, 14), 101: (9, 15), 102: (9, 16), 103: (7, 3),
    }

    # Add information about empty cells
    empty_cells = [(1, 3), (1, 4), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
                   (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                   (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                   (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                   (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
                   (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
                   (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
                   (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8),
                   (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8)]

    for cell in empty_cells:
        mandeleev_layout[cell] = None

    for element in periodic_table:
        proton_number = element['proton_number']
        if proton_number in mandeleev_layout:
            row, col = mandeleev_layout[proton_number]
            element['row'] = row
            element['col'] = col

    return periodic_table

def print_periodic_table_to_text(periodic_table, text_widget):
    text_widget.delete("1.0", tk.END)  # Clear the text widget
    col_widths = calculate_column_widths(periodic_table)

    for row in range(1, len(periodic_table) + 1):
        for col in range(1, len(periodic_table[row - 1]) + 1):
            element = periodic_table[row - 1][col - 1]
            element_name_str = f"{element['symbol']} ({element['name']})"
            proton_number_str = str(element['number'])

            insert_index = f"{row}.{col * (max(col_widths) + 3) - 2}"  # Adjust the multiplier based on your font and layout
            text_widget.insert(insert_index, element_name_str.center(col_widths[col - 1]) + ' | ')

            insert_index_proton = f"{row}.{col * (max(col_widths) + 3) + 1}"  # Adjust the multiplier based on your font and layout
            text_widget.insert(insert_index_proton, proton_number_str.center(col_widths[col - 1]) + ' | ')

    text_widget.config(state=tk.DISABLED)  # Disable the text widget for read-only


def get_correct_answer(periodic_table):
    non_empty_elements = [element for element in periodic_table if element['row'] is not None and element['col'] is not None]
    return random.choice(non_empty_elements)

def test_proton_number(sorted_periodic_table, text_widget, entry_widget, attempts_label, btn_test_proton,
                       btn_test_abbreviation, btn_submit_answer, current_element=None):
    global correct_answer  # Declares the global variable

    btn_test_proton.config(state=tk.DISABLED)
    btn_test_abbreviation.config(state=tk.DISABLED)
    btn_submit_answer.config(state=tk.NORMAL)


    if current_element is None:
        random_element = random.choice(sorted_periodic_table)
        current_element = random_element['element']
        proton_number = random_element['proton_number']
        mass = random_element['mass']

        text_widget.insert(tk.END,
                           f"\nEnter the proton number for the randomly selected element ({current_element}), with mass {mass}: ")

        # Store the correct answer in the global variable
        correct_answer = str(proton_number)
    else:
        text_widget.insert(tk.END,
                           f"\nEnter the proton number for the randomly selected element ({current_element}): ")

    entry_widget.delete(0, tk.END)  # Clear the entry box
    attempts_label.config(text="0")  # Reset the attempts label
    return current_element

def test_abbreviation(sorted_periodic_table, text_widget, entry_widget, attempts_label, current_element=None):
    global correct_answer  # Declare the global variable

    btn_test_proton.config(state=tk.DISABLED)
    btn_test_abbreviation.config(state=tk.DISABLED)
    btn_submit_answer.config(state=tk.NORMAL)

    if current_element is None:
        random_element = random.choice(sorted_periodic_table)
        current_element = random_element['element']
        abbreviation = current_element[:2]  # Use the first two characters as the abbreviation
        proton_number = random_element['proton_number']

        text_widget.insert(tk.END,
                           f"\nEnter the abbreviation for a randomly selected element with proton number {proton_number}: ")

        # Store the correct answer in the global variable
        correct_answer = abbreviation
    else:
        abbreviation = current_element[:2]
        proton_number = [element['proton_number'] for element in sorted_periodic_table if
                         element['element'] == current_element][0]

        text_widget.insert(tk.END,
                           f"\nEnter the abbreviation for a randomly selected element with proton number {proton_number}: ")

        # Store the correct answer in the global variable
        correct_answer = abbreviation

    entry_widget.delete(0, tk.END)  # Clear the entry box
    attempts_label.config(text="0")  # Reset the attempts label

    # Debugging prints
    print(f"Answer: {correct_answer}")
    print(f"Correct Answer: {correct_answer}")

    return abbreviation

def submit_answer(periodic_table, text_widget, entry_widget, attempts_label):
    global correct_answer  # Declare the global variable

    answer = entry_widget.get().lower()
    #test = answer[0]
    #if ord(test) >= 48 and ord(test) <= 57:
     #   answer = str(answer)

    # Get the correct answer for comparison
    if answer == correct_answer.lower():
        text_widget.insert(tk.END, "\nCorrect!")
    else:
        attempts = int(attempts_label.cget("text")) + 1
        if attempts < 3:
            text_widget.insert(tk.END, f"\nIncorrect. Try again. ({attempts}/3 attempts)")
            entry_widget.delete(0, tk.END)  # Clear the entry box
            attempts_label.config(text=str(attempts))
            return  # Add this line to prevent further execution if attempts are less than 3
        else:
            text_widget.insert(tk.END,
                                f"\nSorry, you've reached the maximum number of attempts. The correct answer is {correct_answer}. {answer}")

    # Clear the entry box
    entry_widget.delete(0, tk.END)
    btn_test_proton.config(state=tk.NORMAL)
    btn_test_abbreviation.config(state=tk.NORMAL)
    btn_submit_answer.config(state=tk.DISABLED)



def generate_incorrect_masses(correct_mass, sorted_periodic_table):
    # Get two random elements different from the correct one
    incorrect_elements = random.sample(sorted_periodic_table, 2)
    incorrect_masses = [element['mass'] for element in incorrect_elements]

    # Ensure that the correct mass is not among the incorrect masses
    while correct_mass in incorrect_masses:
        incorrect_elements = random.sample(sorted_periodic_table, 2)
        incorrect_masses = [element['mass'] for element in incorrect_elements]

    return incorrect_masses

# Function to test element masses

def submit_mass_answer(correct_mass, selected_index, attempts_label, text_widget):
    global correct_mass_answer  # Declare the global variable

    if selected_index is not None and 0 <= selected_index < 3:
        selected_mass = float(incorrect_masses[selected_index])
        if str(selected_mass) == str(correct_mass):  # Convert both to strings for comparison
            text_widget.insert(tk.END, "\nCorrect!")
        else:
            attempts = int(attempts_label.cget("text")) + 1
            if attempts < 3:
                text_widget.insert(tk.END, f"\nIncorrect. Try again. ({attempts}/3 attempts)")
                attempts_label.config(text=str(attempts))
                return  # Add this line to prevent further execution if attempts are less than 3
            else:
                text_widget.insert(tk.END, f"\nSorry, you've reached the maximum number of attempts. The correct answer is {correct_mass}.")
    else:
        text_widget.insert(tk.END, "Invalid selection. Please choose a number between 1 and 3.")

    # Clear the entry box
    entry_widget.delete(0, tk.END)
    btn_test_proton.config(state=tk.NORMAL)
    btn_test_abbreviation.config(state=tk.NORMAL)
    btn_test_masses.config(state=tk.NORMAL)  # Enable the mass testing button
    btn_submit_answer.config(state=tk.DISABLED)

def test_masses(sorted_periodic_table, text_widget, entry_widget, attempts_label):
    global correct_mass_answer, answers  # Declare the global variables

    random_element = random.choice(sorted_periodic_table)
    current_element = random_element['element']
    correct_mass = random_element['mass']

    text_widget.insert(tk.END, f"\nEnter the mass for the randomly selected element ({current_element}): ")

    incorrect_masses = generate_incorrect_masses(correct_mass, sorted_periodic_table)

    # Shuffle the answers so that the correct one is not always in the same position
    answers = [correct_mass] + incorrect_masses
    random.shuffle(answers)

    # Store the correct answer in the global variable
    correct_mass_answer = correct_mass

    for idx, mass in enumerate(answers, start=1):
        text_widget.insert(tk.END, f"\n{idx}. {mass}")

    entry_widget.delete(0, tk.END)  # Clear the entry box
    attempts_label.config(text="0")  # Reset the attempts label

    btn_test_masses.config(state=tk.DISABLED)  # Disable the "Test Masses" button




def main():
    global root, btn_test_proton, btn_test_abbreviation, btn_test_masses, btn_submit_answer, text_widget, entry_widget, attempts_label, original_periodic_table

    root = tk.Tk()

    original_periodic_table = read_periodic_table('/Users/axelschelander/Desktop/KTH/DATAP/csc.kth.se_~lk_P_avikt.txt')

    # Modify the table if needed
    swap_elements_by_index(original_periodic_table, 17, 18)
    swap_elements_by_index(original_periodic_table, 26, 27)
    swap_elements_by_index(original_periodic_table, 51, 52)
    swap_elements_by_index(original_periodic_table, 89, 90)
    swap_elements_by_index(original_periodic_table, 91, 92)

    # Map to Mandeleev layout
    original_periodic_table = map_to_mendeleev_layout(original_periodic_table)

    # Continue with the rest of your code
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=10)

    btn_show_table = tk.Button(button_frame, text="Show Periodic Table",
                               command=lambda: setup_periodic_table_cells(table_frame, original_periodic_table))
    btn_show_table.pack(pady=10, side=tk.TOP)

    btn_test_proton = tk.Button(button_frame, text="Test Proton Number", state=tk.NORMAL,
                                command=lambda: test_proton_number(original_periodic_table, text_widget, entry_widget,
                                                                   attempts_label, btn_test_proton, btn_test_abbreviation,
                                                                   btn_submit_answer))
    btn_test_proton.pack(pady=10, side=tk.TOP)

    btn_test_abbreviation = tk.Button(button_frame, text="Test Abbreviation", state=tk.NORMAL,
                                      command=lambda: test_abbreviation(original_periodic_table, text_widget,
                                                                        entry_widget, attempts_label))

    btn_test_abbreviation.pack(pady=10, side=tk.TOP)

    btn_test_masses = tk.Button(button_frame, text="Test Masses", state=tk.NORMAL,
                                command=lambda: test_masses(original_periodic_table, text_widget, entry_widget,
                                                            attempts_label))

    btn_test_masses.pack(pady=10, side=tk.TOP)

    btn_submit_answer = tk.Button(button_frame, text="Submit Answer", state=tk.DISABLED,
                                  command=lambda: submit_answer(original_periodic_table, text_widget, entry_widget, attempts_label))

    btn_submit_answer.pack(pady=10, side=tk.TOP)

    btn_answer_again = tk.Button(button_frame, text="Answer Again", state=tk.DISABLED, command=lambda: main())
    btn_answer_again.pack(pady=10, side=tk.TOP)

    btn_exit = tk.Button(button_frame, text="Exit", command=root.destroy)
    btn_exit.pack(pady=10, side=tk.TOP)

    text_widget = tk.Text(root, height=20, width=100)  # Adjust the height as needed
    text_widget.pack(pady=10)

    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)

    entry_widget = tk.Entry(root, width=30)
    entry_widget.pack(pady=10)

    attempts_label = tk.Label(root, text="Attempts left: 3")
    attempts_label.pack(pady=10)

    root.mainloop()

# Run the main function to start the application
if __name__ == '__main__':
    main()
