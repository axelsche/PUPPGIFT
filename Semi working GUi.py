import random
import tkinter as tk

correct_answer = None

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

    max_row, max_col = divmod(len(sorted_table), 18)

    for i, element_data in enumerate(sorted_table):
        element_data['proton_number'] = i + 1
        element_data['row'] = i // 18
        element_data['col'] = i % 18

    return sorted_table

def assign_periodic_table_positions(table):
    for i, element in enumerate(table):
        element['row'] = i // 18
        element['col'] = i % 18


def print_periodic_table_to_text(text_widget, table):
    max_row = max(element['row'] for element in table)
    max_col = max(element['col'] for element in table)

    col_widths = [max(len(f"{element['element']} ({element['proton_number']})") for element in table if
                      element['col'] == col) for col in range(max_col + 1)]

    for row in range(max_row + 1):
        for col in range(max_col + 1):
            element = next((element for element in table if element['row'] == row and element['col'] == col), None)
            if element:
                element_str = f"{element['element']} ({element['proton_number']})"
                text_widget.insert(tk.END, element_str.ljust(col_widths[col] + 2) + ' | ')
            else:
                text_widget.insert(tk.END, ' ' * (col_widths[col] + 2) + ' | ')

            if col < max_col:
                next_element = next((element for element in table if element['row'] == row and element['col'] == col + 1),
                                    None)
                if element and next_element and element['element'] in ('H', 'He', 'Li', 'Be') and next_element[
                    'element'] not in ('H', 'He', 'Li', 'Be'):
                    text_widget.insert(tk.END, '   | ')

        text_widget.insert(tk.END, '\n')

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
    max_row = max(element['row'] for element in table)
    max_col = max(element['col'] for element in table)

    for row in range(max_row + 1):
        for col in range(max_col + 1):
            element = next((element for element in table if element['row'] == row and element['col'] == col), None)
            if element:
                element_str = f"{element['element']} ({element['proton_number']})"
                label = tk.Label(frame, text=element_str, padx=10, pady=5, borderwidth=1, relief="solid")
                label.grid(row=row, column=col, padx=2, pady=2)


def get_correct_answer(periodic_table):
    return random.choice(periodic_table)
"""error might be that this isn't sotoring the random variable correctly for later answer, as in 
it cant be called on by the function"""

def test_proton_number(sorted_periodic_table, text_widget, entry_widget, attempts_label, current_element=None):
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
    print(f"Answer: {answer}")
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


def main():
    file_path = 'periodic_table.txt'
    periodic_table = read_periodic_table(file_path)
    original_periodic_table = periodic_table.copy()  # Create a copy of the original data

    swap_elements_by_index(original_periodic_table, 17, 18)
    swap_elements_by_index(original_periodic_table, 26, 27)
    swap_elements_by_index(original_periodic_table, 51, 52)
    swap_elements_by_index(original_periodic_table, 89, 90)
    swap_elements_by_index(original_periodic_table, 91, 92)

    root = tk.Tk()
    root.title("Periodic Table App")

    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)

    btn_show_table = tk.Button(root, text="Show Periodic Table",
                               command=lambda: setup_periodic_table_cells(table_frame, original_periodic_table))
    btn_show_table.pack(pady=10)

    global btn_test_proton, btn_test_abbreviation, btn_submit_answer  # Added global declarations
    btn_test_proton = tk.Button(root, text="Test Proton Number", state=tk.NORMAL,
                                command=lambda: test_proton_number(original_periodic_table, text_widget, entry_widget,
                                                                     attempts_label))
    btn_test_proton.pack(pady=10)

    global btn_test_abbreviation  # Added global declaration
    btn_test_abbreviation = tk.Button(root, text="Test Abbreviation", state=tk.NORMAL,
                                      command=lambda: test_abbreviation(original_periodic_table, text_widget,
                                                                       entry_widget, attempts_label))
    btn_test_abbreviation.pack(pady=10)

    global btn_submit_answer  # Added global declaration
    btn_submit_answer = tk.Button(root, text="Submit Answer", state=tk.DISABLED,
                                  command=lambda: submit_answer(original_periodic_table, text_widget, entry_widget,
                                                               attempts_label))
    btn_submit_answer.pack(pady=10)

    btn_answer_again = tk.Button(root, text="Answer Again", state=tk.DISABLED, command=lambda: main())
    btn_answer_again.pack(pady=10)

    btn_exit = tk.Button(root, text="Exit", command=root.destroy)
    btn_exit.pack(pady=10)

    text_widget = tk.Text(root, height=20, width=100)  # Adjust the height as needed
    text_widget.pack(pady=10)

    entry_widget = tk.Entry(root, width=30)
    entry_widget.pack(pady=10)

    attempts_label = tk.Label(root, text="Attempts left: 3")
    attempts_label.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()